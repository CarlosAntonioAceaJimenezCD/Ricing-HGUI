#!/usr/bin/env python3
"""Detección automática de monitores y sus propiedades (hyprctl monitors -j)."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any

VARIABLES = Path.home() / ".config/hypr/config/variables.lua"


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
