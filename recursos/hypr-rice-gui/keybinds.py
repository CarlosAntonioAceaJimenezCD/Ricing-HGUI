#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · keybinds.py — atajos existentes, edición, desactivado y borrado
# -----------------------------------------------------------------------------
# Fuentes:
#   - en vivo: `hyprctl binds -j` (84+ atajos; la acción aparece como closure
#     opaca HL.Dispatcher(...), por eso también se lee binds.lua para texto);
#   - texto: binds.lua se parsea con regex para mostrar la acción legible.
# Efectos externos: ejecuta `hl.bind` / `hl.unbind` vía `hyprctl eval`; escribe
# ~/.config/hypr/config/ui-bindings.lua y ~/.local/share/.../keybinds.json.
# Invariantes:
#   1. "Desactivar" conserva la entrada y genera un `hl.unbind` persistente.
#   2. "Eliminar" añade una entrada de supresión para que no reaparezca al
#      recargar el config (los atajos de binds.lua no se pueden borrar del todo).
#   3. Para editar un atajo existente se desvincula la tecla antigua primero.
# =============================================================================
"""Gestión de keybindings para Ricing HGUI.

- Lista los atajos actuales desde `hyprctl binds -j` (fuente oficial en vivo).
- Permite añadir, editar y eliminar atajos usando la API Lua de Hyprland 0.57.
- Persiste los atajos propios en JSON y genera un módulo Lua autocontenido
  (~/.config/hypr/config/ui-bindings.lua) que se carga desde hyprland.lua.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any

DATA = Path.home() / ".local/share/hypr-rice-gui/keybinds.json"
LUA_MODULE = Path.home() / ".config/hypr/config/ui-bindings.lua"
SOURCE_BINDS = Path.home() / ".config/hypr/config/binds.lua"
SOURCE_VARS = Path.home() / ".config/hypr/config/variables.lua"

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


def parse_source_binds() -> list[dict[str, str]]:
    """Lee binds.lua y devuelve atajos legibles (clave + acción en texto).

    AUDITORÍA: es un parser de líneas con regex, no un intérprete Lua. Resuelve
    los casos presentes en esta config (mainMod, noctCall, digitCode, variables
    de variables.lua). Bucles y funciones complejas pueden no aparecer: para eso
    está la lista en vivo de `hyprctl binds -j`.
    """
    if not SOURCE_BINDS.exists():
        return []
    variables = {"mainMod": "SUPER", "noctCall": "noctalia msg ", "launchPrefix": "uwsm app -- "}
    if SOURCE_VARS.exists():
        for name, value in re.findall(r'(?m)^(\w+)\s*=\s*"([^"]*)"', SOURCE_VARS.read_text(encoding="utf-8")):
            variables[name] = value

    def resolve(expr: str) -> str:
        if "digitCode(" in expr:
            expr = re.sub(r"digitCode\((\d+)\)",
                          lambda m: f"code:{9 + int(m.group(1)) if int(m.group(1)) else 19}", expr)
        for name, value in variables.items():
            expr = re.sub(rf"\b{re.escape(name)}\b", f'"{value}"', expr)
        parts = re.findall(r'"([^"]*)"', expr)
        return "".join(parts) if len(parts) > 1 else expr.strip()

    out = []
    for line in SOURCE_BINDS.read_text(encoding="utf-8").splitlines():
        m = re.search(r"hl\.bind\(\s*(.+?)\s*,\s*(.+?)\s*(?:,\s*\{[^}]*\})?\s*\)\s*$", line)
        if not m:
            continue
        key = resolve(m.group(1)).strip()
        action = resolve(m.group(2)).strip()
        if key:
            out.append({"key": key, "action": action, "source": "binds.lua"})
    return out


def enriched_binds() -> list[dict[str, Any]]:
    """Atajos en runtime enriquecidos con la acción legible de binds.lua cuando existe."""
    source = {b["key"].lower(): b for b in parse_source_binds()}
    result = list_binds()
    for b in result:
        match = source.get(b["key"].lower())
        if match:
            b["source_action"] = match["action"]
            # Clave EXACTA del config (p. ej. "SUPER + Q"), mejor que la
            # reconstruida desde modmask, que puede decodificar mal los bits.
            b["source_key"] = match["key"]
        else:
            b["source_action"] = b["dispatcher"] + (" " + str(b["arg"]) if b["arg"] else "")
    return result


def action_from_ui(choice: int, param: str) -> tuple[str, str]:
    """Traduce una opción legible de la GUI a (kind, acción Lua).

    AUDITORÍA: el usuario nunca escribe Lua para las acciones habituales;
    sólo la opción "avanzada" permite una expresión cruda.
    """
    p = param.strip().replace('"', '\\"')
    options = {
        0: ("exec", f'hl.dsp.exec_cmd("{p}")'),
        1: ("lua", "hl.dsp.window.close()"),
        2: ("lua", 'hl.dsp.window.float({ action = "toggle" })'),
        3: ("lua", "hl.dsp.window.fullscreen()"),
        4: ("exec", f'hl.dsp.exec_cmd("noctalia msg {p}")'),
        5: ("lua", param.strip()),
    }
    return options.get(choice, options[0])


def action_to_ui(action: str) -> tuple[int, str]:
    """Convierte una acción existente en (índice de opción, parámetro)."""
    a = action.strip()
    m = re.search(r'hl\.dsp\.exec_cmd\("?noctalia msg ([^")]+)"?\)', a)
    if m:
        return 4, m.group(1).strip()
    m = re.search(r'hl\.dsp\.exec_cmd\("([^"]*)"\)', a)
    if m:
        return 0, m.group(1)
    if "window.close" in a:
        return 1, ""
    if "window.float" in a:
        return 2, ""
    if "fullscreen" in a:
        return 3, ""
    return 5, a


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


def set_disabled(key: str, disabled: bool) -> tuple[bool, str]:
    """Desactiva un atajo sin borrarlo (o lo reactiva)."""
    entries = stored()
    entry = next((e for e in entries if e.get("key") == key), None)
    if disabled:
        # Quitar el bind en vivo; conservar el entry para poder reactivarlo.
        esc = key.replace("\\", "\\\\").replace('"', '\\"')
        res = hyprctl("eval", f'hl.unbind("{esc}")')
        if entry:
            entry["disabled"] = True
        else:
            entry = {"key": key, "kind": "exec", "action": "", "description": "desactivado",
                     "repeat": False, "locked": False, "disabled": True}
            entries.append(entry)
        _write_stored(entries)
        return True, "atajo desactivado (conservado)"
    # Reactivar: necesita una acción guardada.
    if not entry or not entry.get("action"):
        return False, "no hay acción guardada para reactivar; vuelve a crear el atajo"
    entry["disabled"] = False
    _write_stored(entries)
    return apply_bind(entry)


def delete(key: str) -> tuple[bool, str]:
    """Elimina el atajo en vivo y guarda una supresión para que no reaparezca al reiniciar."""
    esc = key.replace("\\", "\\\\").replace('"', '\\"')
    res = hyprctl("eval", f'hl.unbind("{esc}")')
    entries = [e for e in stored() if e.get("key") != key]
    # Si el atajo venía de binds.lua, necesitamos un hl.unbind persistente.
    entries.append({"key": key, "kind": "exec", "action": "", "description": "eliminado",
                    "repeat": False, "locked": False, "disabled": True,
                    "old_key": key, "suppression": True})
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
        # Un atajo desactivado/eliminado se representa sólo con hl.unbind.
        if e.get("disabled") or not e.get("action"):
            target = old or e["key"]
            lines.append(f'hl.unbind("{target}")  -- desactivado/eliminado')
            lines.append("")
            continue
        if old:
            lines.append(f'hl.unbind("{old}")')
        lines.append(f'hl.bind("{e["key"]}", {_lua_action(e.get("kind", "exec"), e.get("action", ""))})')
        lines.append("")
    LUA_MODULE.parent.mkdir(parents=True, exist_ok=True)
    LUA_MODULE.write_text("\n".join(lines) + "\n", encoding="utf-8")
