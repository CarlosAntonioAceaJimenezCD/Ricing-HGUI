#!/usr/bin/env python3
"""Prototipo de GUI de ricing: rounding + blur para Hyprland 0.57.

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
from gi.repository import Adw, Gtk  # noqa: E402

# --- i18n: español como idioma base, pero externalizado desde el inicio ---
gettext.bindtextdomain("hypr-rice-gui", os.path.expanduser("~/.local/share/locale"))
gettext.textdomain("hypr-rice-gui")
_ = gettext.gettext

STATE = Path.home() / ".config/hypr/config/ui-settings.lua"


def hyprctl(*args: str) -> str:
    """Ejecuta hyprctl y devuelve stdout (o '' si falla)."""
    try:
        return subprocess.run(["hyprctl", *args], capture_output=True,
                              text=True, timeout=5).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def current_rounding() -> int:
    out = hyprctl("getoption", "decoration:rounding")
    # p. ej. 'decoration:rounding = 10'
    try:
        return int(out.split("=", 1)[1].strip().split(" ")[0])
    except (IndexError, ValueError):
        return 10


def save_state(rounding: int, blur: bool, size: int, passes: int) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    if STATE.exists():
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(STATE, STATE.with_suffix(f".lua.bak-{stamp}"))
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


def on_activate(app: Adw.Application) -> None:
    win = Adw.ApplicationWindow(application=app, title=_("Ricing GUI"))
    win.set_default_size(420, 360)

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

    status = Gtk.Label(label=_("Sin aplicar"), margin_top=12)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12, margin=18)
    box.append(page)
    box.append(status)
    win.set_content(box)

    def apply(_btn: Gtk.Button) -> None:
        r = int(scale.get_value())
        b = switch.get_active()
        hyprctl("keyword", "decoration:rounding", str(r))
        hyprctl("keyword", "decoration:blur:enabled", str(b).lower())
        save_state(r, b, 5, 4)
        status.set_label(_("Aplicado y guardado ✓"))

    btn = Gtk.Button(label=_("Aplicar y guardar"))
    btn.connect("clicked", apply)
    box.append(btn)
    win.present()


def main() -> int:
    app = Adw.Application(application_id="com.tu.hypr-rice-gui")
    app.connect("activate", on_activate)
    return app.run(None)


if __name__ == "__main__":
    raise SystemExit(main())
