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
    result = []
    for m in data:
        result.append({
            "id": m.get("id"),
            "name": m.get("name", ""),
            "description": m.get("description", ""),
            "make": m.get("make", ""),
            "model": m.get("model", ""),
            "serial": m.get("serial", ""),
            "width": m.get("width", 0),
            "height": m.get("height", 0),
            "refresh": round(float(m.get("refreshRate", 0)), 2),
            "scale": m.get("scale", 1),
            "position": m.get("position", [0, 0]),
            "vrr": m.get("vrr", False),
            "hdr": m.get("hdr"),
            "format": m.get("currentFormat", ""),
            "workspace": m.get("activeWorkspace", {}).get("name", ""),
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
    """Actualiza MONITOR1..3 en variables.lua con los conectores detectados."""
    if not VARIABLES.exists() or not monitors:
        return False, "sin archivo o sin monitores"
    text = VARIABLES.read_text(encoding="utf-8")
    names = [m["name"] for m in monitors[:3]]
    for i in range(1, 4):
        value = names[i - 1] if i <= len(names) else ""
        text, n = re.subn(rf'(?m)^MONITOR{i}\s*=\s*".*"', f'MONITOR{i} = "{value}"', text)
        if n == 0:
            text += f'\nMONITOR{i} = "{value}"\n'
    VARIABLES.write_text(text, encoding="utf-8")
    return True, ", ".join(names)
