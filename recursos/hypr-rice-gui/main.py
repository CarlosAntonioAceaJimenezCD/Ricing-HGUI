#!/usr/bin/env python3
"""Prototipo de GUI de ricing para Hyprland 0.57 + Noctalia.

Incluye:
  - Aplicación en vivo de rounding/blur mediante hyprctl.
  - Persistencia en ~/.config/hypr/config/ui-settings.lua con backup previo.
  - BACKUPS AUTOMÁTICOS: programados, con retención, SHA-256 y restauración.
  - HISTORIAL: explorar cualquier punto en el pasado, ver archivos, comparar
    con el estado actual, restaurar o borrar backups.

Requisitos: python3, python-gobject, gtk4, libadwaita (ya en CachyOS).
Ejecutar: python3 main.py
"""
import gettext
import os
import subprocess
from pathlib import Path

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("GLib", "2.0")
from gi.repository import Adw, GLib, Gtk  # noqa: E402

import backup_manager as bm  # noqa: E402

gettext.bindtextdomain("hypr-rice-gui", os.path.expanduser("~/.local/share/locale"))
gettext.textdomain("hypr-rice-gui")
_ = gettext.gettext

STATE = Path.home() / ".config/hypr/config/ui-settings.lua"
_timer_id: int | None = None


# --------------------------------------------------------------------------- Hyprland
def hyprctl(*args: str) -> str:
    try:
        return subprocess.run(["hyprctl", *args], capture_output=True,
                              text=True, timeout=5).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def current_rounding() -> int:
    out = hyprctl("getoption", "decoration:rounding")
    try:
        return int(out.split("=", 1)[1].strip().split(" ")[0])
    except (IndexError, ValueError):
        return 10


def save_state(rounding: int, blur: bool, size: int, passes: int) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(
        "-- Generado por hypr-rice-gui. NO EDITAR A MANO.\n"
        "return {\n"
        f"  rounding = {rounding},\n"
        f"  blur = {str(blur).lower()},\n"
        f"  blur_size = {size},\n"
        f"  blur_passes = {passes},\n"
        "}\n",
        encoding="utf-8",
    )


# --------------------------------------------------------------------------- widgets
def make_button(label: str, callback, *args) -> Gtk.Button:
    b = Gtk.Button(label=label)
    b.connect("clicked", callback, *args)
    return b


def show_text_window(parent: Gtk.Window, title: str, text: str) -> None:
    win = Gtk.Window(title=title, transient_for=parent, default_width=760, default_height=520)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6, margin=10)
    view = Gtk.TextView()
    view.set_editable(False)
    view.set_monospace(True)
    view.get_buffer().set_text(text)
    scroll = Gtk.ScrolledWindow()
    scroll.set_child(view)
    scroll.set_vexpand(True)
    box.append(scroll)
    close = make_button(_("Cerrar"), lambda _b: win.close())
    box.append(close)
    win.set_child(box)
    win.present()


# --------------------------------------------------------------------------- app
def on_activate(app: Adw.Application) -> None:
    win = Adw.ApplicationWindow(application=app, title=_("Ricing HGUI"))
    win.set_default_size(560, 720)
    settings = bm.get_settings()

    page = Adw.PreferencesPage()

    # ---------------- Apariencia ----------------
    group = Adw.PreferencesGroup(title=_("Apariencia de ventanas"))
    page.add(group)

    row_r = Adw.ActionRow(title=_("Redondeo"), subtitle=_("Radio de esquinas (px)"))
    scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 30, 1)
    scale.set_value(current_rounding())
    scale.set_hexpand(True)
    row_r.add_suffix(scale)
    group.add(row_r)

    row_b = Adw.ActionRow(title=_("Blur"), subtitle=_("Desenfoque de ventanas"))
    switch = Gtk.Switch()
    switch.set_active(True)
    switch.set_valign(Gtk.Align.CENTER)
    row_b.add_suffix(switch)
    group.add(row_b)

    status = Gtk.Label(label=_("Sin aplicar"), margin_top=6)

    # ---------------- Backups automáticos ----------------
    bg = Adw.PreferencesGroup(
        title=_("Backups automáticos"),
        description=_("Copias de los dotfiles antes de cada cambio y de forma periódica."),
    )
    page.add(bg)

    row_auto = Adw.ActionRow(title=_("Activados"), subtitle=_("Copiar configs periódicamente"))
    auto_switch = Gtk.Switch()
    auto_switch.set_active(bool(settings.get("auto_backup", True)))
    auto_switch.set_valign(Gtk.Align.CENTER)
    row_auto.add_suffix(auto_switch)
    bg.add(row_auto)

    row_int = Adw.ActionRow(title=_("Intervalo (minutos)"), subtitle=_("Cada cuánto se crea un backup"))
    spin_int = Gtk.SpinButton.new_with_range(1, 1440, 1)
    spin_int.set_value(int(settings.get("interval_minutes", 15)))
    spin_int.set_valign(Gtk.Align.CENTER)
    row_int.add_suffix(spin_int)
    bg.add(row_int)

    row_keep = Adw.ActionRow(title=_("Conservar últimos N"), subtitle=_("Los demás se borran solos"))
    spin_keep = Gtk.SpinButton.new_with_range(1, 100, 1)
    spin_keep.set_value(int(settings.get("keep_last", 10)))
    spin_keep.set_valign(Gtk.Align.CENTER)
    row_keep.add_suffix(spin_keep)
    bg.add(row_keep)

    # ---------------- Historial (puntos en el pasado) ----------------
    hg = Adw.PreferencesGroup(
        title=_("Historial · puntos en el pasado"),
        description=_("Selecciona cualquier copia para inspeccionarla, compararla o restaurarla."),
    )
    page.add(hg)

    history_list = Gtk.ListBox()
    history_list.set_selection_mode(Gtk.SelectionMode.SINGLE)
    history_scroll = Gtk.ScrolledWindow()
    history_scroll.set_child(history_list)
    history_scroll.set_min_content_height(180)
    history_scroll.set_max_content_height(260)
    hg.add(history_scroll)

    detail = Gtk.Label(label=_("Selecciona un backup"), margin_top=6, wrap=True)
    files_combo = Gtk.ComboBoxText()
    row_files = Adw.ActionRow(title=_("Archivos del backup"), subtitle=_("Elige uno para verlo"))
    row_files.add_suffix(files_combo)
    hg.add(row_files)

    backup_status = Gtk.Label(label="", wrap=True)
    selected: dict[str, str] = {}

    def populate_files(name: str) -> None:
        files_combo.remove_all()
        m = bm.get_backup_details(name) or {}
        for rec in m.get("files", []):
            files_combo.append_text(rec["path"])
        if m.get("files"):
            files_combo.set_active(0)

    def on_row_selected(_list: Gtk.ListBox, row: Gtk.ListBoxRow | None) -> None:
        if row is None:
            return
        name = row.get_name()
        selected["name"] = name
        items = {b["name"]: b for b in bm.list_backups()}
        b = items.get(name, {})
        detail.set_label(
            f"{b.get('created_at', '').replace('T', ' ')[:19]} · "
            f"{b.get('reason', '')} · {b.get('file_count', 0)} archivos · "
            f"{b.get('size', 0)//1024} KB"
        )
        populate_files(name)

    def refresh_history() -> None:
        history_list.remove_all()
        for b in bm.list_backups():
            row = Adw.ActionRow(
                title=b["created_at"].replace("T", " ")[:19],
                subtitle=f"{b['reason']} · {b['file_count']} archivos · {b['size']//1024} KB",
            )
            row.set_name(b["name"])
            row.set_activatable(True)
            history_list.append(row)
        if len(bm.list_backups()) == 0:
            detail.set_label(_("Sin backups todavía"))

    history_list.connect("row-selected", on_row_selected)

    def apply(_btn: Gtk.Button) -> None:
        bm.create_backup(reason="antes-de-aplicar")
        r = int(scale.get_value())
        b = switch.get_active()
        hyprctl("keyword", "decoration:rounding", str(r))
        hyprctl("keyword", "decoration:blur:enabled", str(b).lower())
        save_state(r, b, 5, 4)
        status.set_label(_("Aplicado y guardado ✓"))
        refresh_history()

    def create_now(_btn: Gtk.Button) -> None:
        bm.create_backup(reason="manual")
        backup_status.set_label(_("Backup manual creado ✓"))
        refresh_history()

    def view_file(_btn: Gtk.Button) -> None:
        name = selected.get("name")
        idx = files_combo.get_active()
        if not name or idx < 0:
            backup_status.set_label(_("Selecciona un backup y un archivo"))
            return
        path = files_combo.get_active_text() or ""
        text = bm.read_file_from_backup(name, path)
        if text is None:
            backup_status.set_label(_("No se pudo leer el archivo"))
            return
        show_text_window(win, f"{name} · {path}", text)

    def compare(_btn: Gtk.Button) -> None:
        name = selected.get("name")
        if not name:
            backup_status.set_label(_("Selecciona un backup"))
            return
        d = bm.compare_with_current(name)
        backup_status.set_label(
            _("Cambios: {n} modificados, {m} ausentes, {s} iguales").format(
                n=len(d["changed"]), m=len(d["missing"]), s=len(d["same"]))
        )

    def restore(_btn: Gtk.Button) -> None:
        name = selected.get("name")
        if not name:
            backup_status.set_label(_("Selecciona un backup"))
            return
        ok, msg = bm.restore_backup(name)
        backup_status.set_label(_("Restaurado: ") + msg if ok else _("Error: ") + msg)
        refresh_history()

    def delete(_btn: Gtk.Button) -> None:
        name = selected.get("name")
        if not name:
            return
        ok, msg = bm.delete_backup(name)
        backup_status.set_label(_("Eliminado") if ok else _("Error: ") + msg)
        refresh_history()

    row_actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=8)
    for label, cb in [
        (_("Crear ahora"), create_now), (_("Ver archivo"), view_file),
        (_("Comparar"), compare), (_("Restaurar"), restore), (_("Borrar"), delete),
    ]:
        row_actions.append(make_button(label, cb))
    hg.add(row_actions)

    # Persistencia de ajustes y temporizador
    def persist_settings(*_args) -> None:
        s = bm.get_settings()
        s["auto_backup"] = auto_switch.get_active()
        s["interval_minutes"] = int(spin_int.get_value())
        s["keep_last"] = int(spin_keep.get_value())
        bm.save_settings(s)
        install_timer(s["interval_minutes"] if s["auto_backup"] else 0, on_timer)

    auto_switch.connect("notify::active", persist_settings)
    spin_int.connect("value-changed", persist_settings)
    spin_keep.connect("value-changed", persist_settings)

    def on_timer() -> bool:
        bm.create_backup(reason="auto")
        refresh_history()
        return True

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, margin=18)
    box.append(page)
    for lbl in (status, detail, backup_status):
        box.append(lbl)
    box.append(make_button(_("Aplicar y guardar"), apply))
    win.set_content(box)

    refresh_history()
    s = bm.get_settings()
    install_timer(s["interval_minutes"] if s.get("auto_backup", True) else 0, on_timer)

    def on_close(_win) -> bool:
        global _timer_id
        if _timer_id is not None:
            GLib.source_remove(_timer_id)
            _timer_id = None
        return False

    win.connect("close-request", on_close)
    win.present()


def install_timer(interval_minutes: int, callback) -> None:
    global _timer_id
    if _timer_id is not None:
        GLib.source_remove(_timer_id)
        _timer_id = None
    if interval_minutes > 0:
        _timer_id = GLib.timeout_add_seconds(interval_minutes * 60, callback)


def main() -> int:
    app = Adw.Application(application_id="com.tu.hypr-rice-gui")
    app.connect("activate", on_activate)
    return app.run(None)


if __name__ == "__main__":
    raise SystemExit(main())
