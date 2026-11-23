#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · compact_rules.py — una fila por familia, 10 binds por debajo
# -----------------------------------------------------------------------------
# El módulo Lua generado es AUTOCONTENIDO: no usa mainMod, digitCode ni
# NUM_WPM externos (son locales de binds.lua y no existen en un require).
# Orden: primero hl.unbind de todas las teclas objetivo, luego los bucles.
# Fuentes: ~/.local/share/hypr-rice-gui/compact-rules.json
# Salida:  ~/.config/hypr/config/ui-workspace-rules.lua
# Requiere: require("config.ui-workspace-rules") en hyprland.lua tras binds.lua.
# =============================================================================
"""Reglas compactas de workspaces: <N> se expande a 1..NUM_WPM."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

DATA = Path.home() / ".local/share/hypr-rice-gui/compact-rules.json"
LUA = Path.home() / ".config/hypr/config/ui-workspace-rules.lua"
SOURCE_BINDS = Path.home() / ".config/hypr/config/binds.lua"
MARK = "-- [HGUI-COMPACT] "

FAMILIES = {
    "focus_same": ("Workspace de este monitor", "SUPER", 'hl.dsp.focus({workspace="m~"..i})'),
    "focus_abs": ("Workspace absoluto", "SUPER + CTRL", "hl.dsp.focus({workspace=i})"),
    "focus_mon": ("Monitor", "SUPER + ALT", "hl.dsp.focus({monitor=ms[i]})"),
    # Intercambio respecto al esquema anterior:
    #   SUPER + SHIFT + N        -> mover la ventana al workspace N (antes SHIFT+CTRL)
    #   SUPER + SHIFT + CTRL + N -> mover la ventana al monitor N   (antes SHIFT)
    "move_follow": ("Mover ventana al workspace (seguir)", "SUPER + SHIFT", 'hl.dsp.window.move({workspace="m~"..i})'),
    "move_nofollow": ("Mover ventana al workspace (sin seguir)", "SUPER + SHIFT + ALT", 'hl.dsp.window.move({workspace="m~"..i, follow=false})'),
    "move_mon": ("Mover ventana al monitor", "SUPER + SHIFT + CTRL", "hl.dsp.window.move({monitor=ms[i]})"),
}

# Mods del esquema anterior, para migrar JSON ya guardados sin perder start/end/enabled.
OLD_MOVE_MODS = "SUPER + SHIFT + CTRL"


def num_wpm() -> int:
    try:
        import re
        text = SOURCE_BINDS.parent.joinpath("variables.lua").read_text(encoding="utf-8")
        m = re.search(r"(?m)^NUM_WPM\s*=\s*(\d+)", text)
        return min(int(m.group(1)), 10) if m else 10
    except (OSError, ValueError):
        return 10


def defaults(monitors: list[str] | None = None) -> list[dict[str, Any]]:
    n = num_wpm()
    out = []
    for fid, (label, mods, action) in FAMILIES.items():
        end = len(monitors) if fid in ("focus_mon", "move_mon") and monitors else n
        out.append({"id": fid, "label": label, "mods": mods, "family": fid,
                    "action": action, "start": 1, "end": end, "enabled": True})
    return out


def _migrate(rules: list[dict[str, Any]], monitors: list[str] | None = None) -> list[dict[str, Any]]:
    """Adapta JSON del esquema anterior (mover a workspace en SHIFT+CTRL)."""
    for rule in rules:
        if rule.get("id") == "move_follow" and rule.get("mods") == OLD_MOVE_MODS:
            rule["mods"] = FAMILIES["move_follow"][1]
    if not any(rule.get("id") == "move_mon" for rule in rules):
        label, mods, action = FAMILIES["move_mon"]
        rules.append({"id": "move_mon", "label": label, "mods": mods,
                      "family": "move_mon", "action": action,
                      "start": 1, "end": len(monitors) if monitors else 1,
                      "enabled": True})
    return rules


def load(monitors: list[str] | None = None) -> list[dict[str, Any]]:
    if DATA.exists():
        try:
            data = json.loads(DATA.read_text(encoding="utf-8"))
            if isinstance(data, list) and all(isinstance(r, dict) for r in data):
                return _migrate(data, monitors)
        except (OSError, ValueError):
            pass
    return defaults(monitors)


def _code_lua() -> str:
    """Expresión Lua que convierte i (1..10) en code:10..19."""
    return "(d==0 and 19 or (9+d))"


# ------------------------------------------------------------------- saneamiento
def _lua_str(value: Any) -> str:
    """Cadena Lua de una sola línea (nombres de monitor/mods vienen del JSON)."""
    return (str(value if value is not None else "").replace("\\", "\\\\")
            .replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r"))


def _safe_int(value: Any, default: int, low: int = 1, high: int = 10) -> int:
    try:
        return max(low, min(int(value), high))
    except (TypeError, ValueError):
        return default


def _safe_mods(value: Any) -> str:
    """Sólo modificadores conocidos, en orden canónico y sin caracteres Lua."""
    found = []
    for token in str(value or "").upper().replace("+", " ").split():
        canonical = "CTRL" if token == "CONTROL" else token
        if canonical in {"SUPER", "CTRL", "ALT", "SHIFT", "HYPER", "MEGA"} and canonical not in found:
            found.append(canonical)
    order = ["CTRL", "ALT", "SHIFT", "SUPER", "HYPER", "MEGA"]
    return " + ".join(m for m in order if m in found)


def _bounds(rule: dict[str, Any]) -> tuple[int, int]:
    start = _safe_int(rule.get("start"), 1)
    end = _safe_int(rule.get("end"), start)
    return start, max(start, end)


def _rule_targets(rule: dict[str, Any], monitors: list[str] | None,
                  variants: bool = False) -> list[str]:
    mods = _safe_mods(rule.get("mods"))
    if not mods:
        return []
    names = set()
    base = [mods]
    if variants and "CTRL" in mods:
        base.append(mods.replace("CTRL", "CONTROL"))  # binds.lua usa CONTROL
    start, end = _bounds(rule)
    family = rule.get("family")
    if family in ("focus_mon", "move_mon"):
        count = max(1, min(len(monitors or ["VGA-1"]), 10)) if monitors else 1
        end = min(end, count)
        start = min(start, count)
    for v in base:
        for i in range(start, end + 1):
            names.add(f"{v} + code:{19 if i % 10 == 0 else 9 + i % 10}")
    return sorted(names)


def rule_lua(rule: dict[str, Any], monitors: list[str] | None = None) -> str:
    """Devuelve una línea Lua válida, autocontenida, para la familia."""
    rule = rule if isinstance(rule, dict) else {}
    mods = _safe_mods(rule.get("mods"))
    action = str(rule.get("action") or "").strip().replace("\n", " ").replace("\r", " ")
    if not mods or not action:
        return "-- regla compacta ignorada: mods o acción vacíos"
    start, end = _bounds(rule)
    if rule.get("family") in ("focus_mon", "move_mon"):
        names = (monitors or ["VGA-1"])[:end]
        names = [str(m) for m in names]
        if not names:
            return "-- regla compacta ignorada: sin monitores"
        joined = ", ".join(f'"{_lua_str(m)}"' for m in names)
        return (f"local ms={{{joined}}}; for i=1,#ms do hl.bind(\"{_lua_str(mods)} + \".."
                f"(i%10==0 and 'code:19' or ('code:'..(9+i%10))), {action}) end")
    return (f"for i={start},{end} do local d=i%10; hl.bind(\"{_lua_str(mods)} + \".."
            f"(\"code:\"..{_code_lua()}), {action}) end")


def all_target_keys(rules: list[dict[str, Any]], monitors: list[str] | None = None) -> list[str]:
    keys: set[str] = set()
    for r in (rules if isinstance(rules, list) else []):
        keys.update(_rule_targets(r, monitors))
    return sorted(keys)


def build_script(rules: list[dict[str, Any]], monitors: list[str] | None = None) -> str:
    lines = ["-- Generado por Ricing HGUI · reglas compactas (NO EDITAR A MANO)",
             "-- Añadir require(\"config.ui-workspace-rules\") en hyprland.lua tras binds.lua."]
    for r in (rules if isinstance(rules, list) else []):
        if not isinstance(r, dict):
            continue
        for k in _rule_targets(r, monitors, variants=True):
            lines.append(f'hl.unbind("{_lua_str(k)}")' +
                         ("  -- regla desactivada" if not r.get("enabled", True) else ""))
        if r.get("enabled", True):
            lines.append(rule_lua(r, monitors))
    return "\n".join(lines) + "\n"


def save_rules(rules: list[dict[str, Any]], monitors: list[str] | None = None) -> tuple[bool, str]:
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(rules, indent=2, ensure_ascii=False), encoding="utf-8")
    script = build_script(rules, monitors)
    LUA.parent.mkdir(parents=True, exist_ok=True)
    LUA.write_text(script, encoding="utf-8")
    return True, str(LUA)


def apply_rules(rules: list[dict[str, Any]], monitors: list[str] | None = None) -> tuple[bool, str]:
    # hyprctl eval interpreta las líneas que empiezan por "--" como sus
    # propias flags: se eliminan los comentarios para el envío en vivo.
    script = "\n".join(l for l in build_script(rules, monitors).splitlines()
                       if not l.lstrip().startswith("--"))
    try:
        proc = subprocess.run(["hyprctl", "eval", script], capture_output=True,
                              text=True, timeout=20)
        return proc.returncode == 0 and "error" not in proc.stdout.lower(), (
            proc.stdout or proc.stderr).strip()[:160]
    except (OSError, subprocess.SubprocessError) as e:
        return False, str(e)[:160]


def neutralize_source_loops() -> tuple[bool, str]:
    """Comenta los bucles de workspaces en binds.lua para que la regla sea la única fuente."""
    if not SOURCE_BINDS.exists():
        return False, "sin binds.lua"
    lines = SOURCE_BINDS.read_text(encoding="utf-8").splitlines()
    out, n = [], 0
    for line in lines:
        s = line.lstrip()
        if ("for i = 1, NUM_WPM do" in s and not s.startswith(MARK)):
            out.append(line.replace(s, MARK + s))
            n += 1
        elif s.startswith(MARK + "for i ="):
            out.append(line)  # ya neutralizado
        else:
            out.append(line)
    SOURCE_BINDS.write_text("\n".join(out) + "\n", encoding="utf-8")
    return True, f"{n} bucle(s) comentado(s)"
