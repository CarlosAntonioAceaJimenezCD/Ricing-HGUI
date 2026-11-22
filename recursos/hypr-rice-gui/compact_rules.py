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
    "move_follow": ("Mover ventana al workspace (seguir)", "SUPER + SHIFT + CTRL", 'hl.dsp.window.move({workspace="m~"..i})'),
    "move_nofollow": ("Mover ventana al workspace (sin seguir)", "SUPER + SHIFT + ALT", 'hl.dsp.window.move({workspace="m~"..i, follow=false})'),
}


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
        end = len(monitors) if fid == "focus_mon" and monitors else n
        out.append({"id": fid, "label": label, "mods": mods, "family": fid,
                    "action": action, "start": 1, "end": end, "enabled": True})
    return out


def load(monitors: list[str] | None = None) -> list[dict[str, Any]]:
    if DATA.exists():
        try:
            return json.loads(DATA.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
    return defaults(monitors)


def _code_lua() -> str:
    """Expresión Lua que convierte i (1..10) en code:10..19."""
    return "(d==0 and 19 or (9+d))"


def rule_lua(rule: dict[str, Any], monitors: list[str] | None = None) -> str:
    """Devuelve una línea Lua válida, autocontenida, para la familia."""
    mods = rule["mods"]
    action = rule["action"]
    start, end = int(rule["start"]), int(rule["end"])
    if rule["family"] == "focus_mon":
        names = ", ".join(f'"{m}"' for m in (monitors or ["VGA-1"])[:end])
        return (f"local ms={{{names}}}; for i=1,#ms do hl.bind(\"{mods} + \".."
                f"(i%10==0 and 'code:19' or ('code:'..(9+i%10))), {action}) end")
    return (f"for i={start},{end} do local d=i%10; hl.bind(\"{mods} + \".."
            f"(\"code:\"..{_code_lua()}), {action}) end")


def all_target_keys(rules: list[dict[str, Any]], monitors: list[str] | None = None) -> list[str]:
    keys = []
    for r in rules:
        end = int(r["end"])
        for i in range(int(r["start"]), end + 1):
            d = i % 10
            code = 19 if d == 0 else 9 + d
            keys.append(f"{r['mods']} + code:{code}")
    return sorted(set(keys))


def build_script(rules: list[dict[str, Any]], monitors: list[str] | None = None) -> str:
    lines = ["-- Generado por Ricing HGUI · reglas compactas (NO EDITAR A MANO)",
             "-- Añadir require(\"config.ui-workspace-rules\") en hyprland.lua tras binds.lua."]
    keys = all_target_keys(rules, monitors)
    for r in rules:
        mods = r["mods"]
        variants = {mods}
        if "CTRL" in mods:
            variants.add(mods.replace("CTRL", "CONTROL"))  # binds.lua usa CONTROL
        targets = sorted({
            f"{v} + code:{19 if i % 10 == 0 else 9 + i % 10}"
            for v in variants
            for i in range(int(r["start"]), int(r["end"]) + 1)
        })
        for k in targets:
            lines.append(f'hl.unbind("{k}")' + ("  -- regla desactivada" if not r.get("enabled", True) else ""))
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
