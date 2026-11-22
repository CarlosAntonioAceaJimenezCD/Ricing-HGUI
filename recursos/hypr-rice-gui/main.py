#!/usr/bin/env python3
"""Prototipo de GUI de ricing para Hyprland 0.57 + Noctalia.

Incluye:
  - Aplicación en vivo de rounding/blur mediante hyprctl.
  - Persistencia en ~/.config/hypr/config/ui-settings.lua con backup previo.
  - BACKUPS AUTOMÁTICOS: programados, con retención, SHA-256 y restauración.

Requisitos (ya instalados en CachyOS): python3, python-gobject, gtk4, libadwaita.
Ejecutar: python3 main.py
"""
import gettext
import os
import shutil
import subprocess
from datetime import datetime
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
    """Escribe ui-settings.lua. El backup lo hace el llamador (apply)."""
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


# --------------------------------------------------------------------------- backups
def refresh_backups(combo: Gtk.ComboBoxText, status: Gtk.Label) -> None:
    combo.remove_all()
    items = bm.list_backups()
    for b in items:
        when = b["created_at"].replace("T", " ")[:19]
        combo.append_text(f"{when} · {b['reason']} · {b['file_count']} archivos")
    if items:
        combo.set_active(0)
        status.set_label(_(f"{len(items)} backup(s) disponible(s)"))
    else:
        status.set_label(_("Sin backups todavía"))


def install_timer(interval_minutes: int, callback) -> None:
    global _timer_id
    if _timer_id is not None:
        GLib.source_remove(_timer_id)
        _timer_id = None
    if interval_minutes > 0:
        _timer_id = GLib.timeout_add_seconds(interval_minutes * 60, callback)


def on_activate(app: Adw.Application) -> None:
    win = Adw.ApplicationWindow(application=app, title=_("Ricing HGUI"))
    win.set_default_size(480, 560)
    settings = bm.get_settings()

    # ---------------- Apariencia ----------------
    page = Adw.PreferencesPage()
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

    def apply(_btn: Gtk.Button) -> None:
        bm.create_backup(reason="antes-de-aplicar")
        r = int(scale.get_value())
        b = switch.get_active()
        hyprctl("keyword", "decoration:rounding", str(r))
        hyprctl("keyword", "decoration:blur:enabled", str(b).lower())
        save_state(r, b, 5, 4)
        status.set_label(_("Aplicado y guardado ✓"))
        refresh_backups(combo, backup_status)

    btn_apply = Gtk.Button(label=_("Aplicar y guardar"))
    btn_apply.connect("clicked", apply)
    group.add(btn_apply)

    # ---------------- Backups automáticos ----------------
    bg = Adw.PreferencesGroup(
        title=_("Backups automáticos"),
        description=_("Copias de los dotfiles del rice antes de cada cambio y de forma periódica."),
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

    combo = Gtk.ComboBoxText()

    def on_timer() -> bool:
        m = bm.create_backup(reason="auto")
        if m:
            backup_status.set_label(_("Backup automático creado ✓"))
            refresh_backups(combo, backup_status)
        return True  # seguir programado

    row_list = Adw.ActionRow(title=_("Historial"), subtitle=_("Backups guardados"))
    row_list.add_suffix(combo)
    bg.add(row_list)

    backup_status = Gtk.Label(label="", margin_top=6)

    def create_now(_btn: Gtk.Button) -> None:
        m = bm.create_backup(reason="manual")
        backup_status.set_label(_("Backup manual creado ✓") if m else _("Nada que respaldar"))
        refresh_backups(combo, backup_status)

    def restore(_btn: Gtk.Button) -> None:
        items = bm.list_backups()
        idx = combo.get_active()
        if idx < 0 or idx >= len(items):
            backup_status.set_label(_("Selecciona un backup"))
            return
        ok, msg = bm.restore_backup(items[idx]["name"])
        backup_status.set_label(_("Restaurado: ") + msg if ok else _("Error: ") + msg)

    box_btns = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8, margin_top=8)
    b_new = Gtk.Button(label=_("Crear ahora"))
    b_new.connect("clicked", create_now)
    b_restore = Gtk.Button(label=_("Restaurar seleccionado"))
    b_restore.connect("clicked", restore)
    box_btns.append(b_new)
    box_btns.append(b_restore)
    bg.add(box_btns)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, margin=18)
    box.append(page)
    box.append(status)
    box.append(backup_status)
    win.set_content(box)

    refresh_backups(combo, backup_status)
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


def main() -> int:
    app = Adw.Application(application_id="com.tu.hypr-rice-gui")
    app.connect("activate", on_activate)
    return app.run(None)


if __name__ == "__main__":
    raise SystemExit(main())
