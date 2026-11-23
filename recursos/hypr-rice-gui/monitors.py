#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · monitors.py — detección automática de monitores
# -----------------------------------------------------------------------------
# Sólo LEE `hyprctl monitors -j`. La única escritura es opcional y explícita:
# write_variables() sustituye MONITOR1..3 en config/variables.lua con los
# conectores detectados (por defecto MONITOR1="" → autodetección).
# No se modifica ninguna resolución/modo automáticamente.
# =============================================================================
"""Detección automática de monitores y sus propiedades (hyprctl monitors -j)."""
from __future__ import annotations

import json
import math
import re
import subprocess
from pathlib import Path
from typing import Any

VARIABLES = Path.home() / ".config/hypr/config/variables.lua"
CONFIG_DIR = Path.home() / ".config/hypr"
HGUI_MARKER = "-- [HGUI] "
MON_REF = re.compile(r"MONITOR([1-9])")


def list_monitors() -> list[dict[str, Any]]:
    try:
        out = subprocess.run(["hyprctl", "monitors", "-j"], capture_output=True,
                             text=True, timeout=6).stdout.strip()
        data = json.loads(out)
    except (OSError, subprocess.SubprocessError, ValueError):
        return []
    if not isinstance(data, list):
        return []

    def _num(value: Any, cast, default):
        try:
            n = cast(value)
            return n if math.isfinite(float(n)) else default
        except (TypeError, ValueError, OverflowError):
            return default

    result = []
    for m in data:
        if not isinstance(m, dict):
            continue
        ws = m.get("activeWorkspace")
        ws = ws if isinstance(ws, dict) else {}
        pos = m.get("position")
        pos = pos if isinstance(pos, list) else [0, 0]
        result.append({
            "id": _num(m.get("id"), int, 0),
            "name": str(m.get("name") or ""),
            "description": str(m.get("description") or ""),
            "make": str(m.get("make") or ""),
            "model": str(m.get("model") or ""),
            "serial": str(m.get("serial") or ""),
            "width": _num(m.get("width"), int, 0),
            "height": _num(m.get("height"), int, 0),
            "refresh": round(_num(m.get("refreshRate"), float, 0.0), 2),
            "scale": _num(m.get("scale"), float, 1.0),
            "position": pos,
            "vrr": bool(m.get("vrr", False)),
            "hdr": m.get("hdr"),
            "format": str(m.get("currentFormat") or ""),
            "workspace": str(ws.get("name") or ""),
        })
    return result


def sync_monitor_config(count: int | None = None) -> dict[str, Any]:
    """Comenta (o restaura) líneas que referencian monitores no conectados.

    AUDITORÍA:
      - Sólo se tocan archivos Lua dentro de ~/.config/hypr/config.
      - Las líneas que desactiva llevan la marca `-- [HGUI] `; nunca se
        descomenta un comentario del usuario que no tenga esa marca.
      - Antes de escribir se crea un backup completo con backup_manager.
    """
    if count is None:
        count = len(list_monitors())
    try:
        count = max(0, int(count))
    except (TypeError, ValueError):
        count = 0
    report: dict[str, Any] = {"detectados": count, "archivos": {}, "cambios": 0}

    files = sorted({p for p in CONFIG_DIR.rglob("*.lua") if p.is_file()})
    staged: list[tuple[Path, str]] = []
    for path in files:
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        lines = original.splitlines(keepends=True)
        changed = False
        commented = uncommented = 0
        for i, line in enumerate(lines):
            # AUDITORÍA: MONITOR1..3 son DEFINICIONES en variables.lua; con
            # count=0 se comentaban y el rice dejaba de arrancar. Nunca se
            # tocan las definiciones, sólo las referencias en binds/reglas.
            if re.match(r"^\s*MONITOR[1-9]\s*=", line):
                continue
            refs = [int(n) for n in MON_REF.findall(line)]
            if not refs:
                continue
            stripped = line.lstrip()
            indent = line[: len(line) - len(stripped)]
            over = any(n > count for n in refs)
            # Un comentario del usuario ya está inactivo: no hace falta marcarlo.
            if over and not stripped.startswith("--"):
                lines[i] = f"{indent}{HGUI_MARKER}{stripped}"
                commented += 1
                changed = True
            elif not over and stripped.startswith(HGUI_MARKER):
                lines[i] = indent + stripped[len(HGUI_MARKER):]
                uncommented += 1
                changed = True
        if changed:
            staged.append((path, "".join(lines)))
            report["archivos"][path.name] = {"comentadas": commented, "restauradas": uncommented}

    if staged:
        try:
            import backup_manager as bm  # import local: evita acoplamiento circular
            bm.create_backup(reason="monitor-sync")
        except (ImportError, OSError):
            pass
        for path, content in staged:
            path.write_text(content, encoding="utf-8")
        report["cambios"] = sum(sum(v.values()) for v in report["archivos"].values())
    return report


def write_variables(monitors: list[dict[str, Any]]) -> tuple[bool, str]:
    """Actualiza MONITOR1..3 en variables.lua con los conectores detectados.

    AUDITORÍA: el nombre de conector viene de `hyprctl monitors -j`; un valor
    con comillas podía inyectar código Lua en variables.lua. Se valida el
    formato de conector y se escapa la cadena antes de escribir.
    """
    if not VARIABLES.exists() or not isinstance(monitors, list) or not monitors:
        return False, "sin archivo o sin monitores"
    names = []
    for m in monitors[:3]:
        name = str(m.get("name") or "") if isinstance(m, dict) else ""
        if not re.fullmatch(r"[A-Za-z0-9._-]+", name):
            return False, f"nombre de monitor no válido: {name[:40]!r}"
        names.append(name)
    text = VARIABLES.read_text(encoding="utf-8")
    for i in range(1, 4):
        value = names[i - 1] if i <= len(names) else ""
        esc = value.replace("\\", "\\\\").replace('"', '\\"')
        line = f'MONITOR{i} = "{esc}"'
        text, n = re.subn(rf'(?m)^MONITOR{i}\s*=\s*".*"', lambda m, l=line: l, text)
        if n == 0:
            text += "\n" + line + "\n"
    VARIABLES.write_text(text, encoding="utf-8")
    return True, ", ".join(names)
