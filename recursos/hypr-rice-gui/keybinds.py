#!/usr/bin/env python3
"""Gestión de keybindings para Ricing HGUI.

- Lista los atajos actuales desde `hyprctl binds -j` (fuente oficial en vivo).
- Permite añadir, editar y eliminar atajos usando la API Lua de Hyprland 0.57.
- Persiste los atajos propios en JSON y genera un módulo Lua autocontenido
  (~/.config/hypr/config/ui-bindings.lua) que se carga desde hyprland.lua.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

DATA = Path.home() / ".local/share/hypr-rice-gui/keybinds.json"
LUA_MODULE = Path.home() / ".config/hypr/config/ui-bindings.lua"

MODS = [
    (0x10, "SUPER"), (0x20, "ALT"), (0x40, "CTRL"), (0x80, "SHIFT"),
]


def hyprctl(*args: str) -> str:
    try:
        return subprocess.run(["hyprctl", *args], capture_output=True,
                              text=True, timeout=6).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def list_binds() -> list[dict[str, Any]]:
    out = hyprctl("binds", "-j")
    try:
        data = json.loads(out)
    except (ValueError, TypeError):
        return []
    result = []
    for b in data:
        mods = [name for bit, name in MODS if b.get("modmask", 0) & bit]
        result.append({
            "key": b.get("key", ""),
            "mods": " + ".join(mods) if mods else "(sin modifier)",
            "dispatcher": b.get("dispatcher", ""),
            "arg": b.get("arg", ""),
            "description": b.get("description", ""),
            "repeat": b.get("repeat", False),
            "locked": b.get("locked", False),
            "raw": b,
        })
    return result


def stored() -> list[dict[str, str]]:
    if DATA.exists():
        try:
            return json.loads(DATA.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return []
    return []


def _write_stored(entries: list[dict[str, str]]) -> None:
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
    _generate_lua(entries)


def _lua_action(kind: str, action: str) -> str:
    if kind == "exec":
        escaped = action.replace("\\", "\\\\").replace('"', '\\"')
        return f'hl.dsp.exec_cmd("{escaped}")'
    return action  # expresión Lua cruda, p. ej. hl.dsp.window.close()


def apply_bind(entry: dict[str, str]) -> tuple[bool, str]:
    """Aplica un atajo en vivo; si old_key existe, desvincula primero."""
    old = (entry.get("old_key") or "").strip()
    if old:
        esc = old.replace("\\", "\\\\").replace('"', '\\"')
        hyprctl("eval", f'hl.unbind("{esc}")')
    key = entry["key"].replace("\\", "\\\\").replace('"', '\\"')
    action = _lua_action(entry.get("kind", "exec"), entry.get("action", ""))
    flags = []
    if entry.get("repeat"):
        flags.append("repeat = true")
    if entry.get("locked"):
        flags.append("locked = true")
    opts = ", { " + ", ".join(flags) + " }" if flags else ""
    res = hyprctl("eval", f'hl.bind("{key}", {action}{opts})')
    return (res.strip().lower() == "ok"), res.strip() or "sin respuesta"


def add_or_update(entry: dict[str, str]) -> tuple[bool, str]:
    ok, msg = apply_bind(entry)
    if not ok:
        return False, msg
    entries = stored()
    key = entry["key"]
    entries = [e for e in entries if e.get("key") != key and e.get("old_key") != key]
    entries.append(entry)
    _write_stored(entries)
    return True, "atajo aplicado y guardado"


def delete(key: str) -> tuple[bool, str]:
    esc = key.replace("\\", "\\\\").replace('"', '\\"')
    res = hyprctl("eval", f'hl.unbind("{esc}")')
    entries = [e for e in stored() if e.get("key") != key]
    _write_stored(entries)
    return res.strip().lower() == "ok", res.strip() or "eliminado"


def _generate_lua(entries: list[dict[str, str]]) -> None:
    lines = [
        "-- Generado por Ricing HGUI. NO EDITAR A MANO.",
        "-- Añadir `require(\"config.ui-bindings\")` en hyprland.lua tras los binds habituales.",
        "",
    ]
    for i, e in enumerate(entries, 1):
        old = e.get("old_key", "")
        lines.append(f"-- [{i}] {e.get('description', '') or e['key']}")
        if old:
            lines.append(f'hl.unbind("{old}")')
        lines.append(f'hl.bind("{e["key"]}", {_lua_action(e.get("kind", "exec"), e.get("action", ""))})')
        lines.append("")
    LUA_MODULE.parent.mkdir(parents=True, exist_ok=True)
    LUA_MODULE.write_text("\n".join(lines) + "\n", encoding="utf-8")
