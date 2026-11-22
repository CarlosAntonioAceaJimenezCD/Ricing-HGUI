#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · wallpaper_engine.py — integración con Wallpaper Engine (Steam)
# -----------------------------------------------------------------------------
# Steam está instalado pero Wallpaper Engine NO en esta máquina. El módulo:
#   1. detecta la instalación en las rutas habituales;
#   2. si existe, lista proyectos locales y del Workshop (app id 431960);
#   3. permite usar la imagen de vista previa como fondo estático vía Noctalia;
#   4. abre la ficha de Steam si no está instalado.
# No modifica archivos de Wallpaper Engine ni de Steam.
# =============================================================================
"""Detectar y usar fondos de Wallpaper Engine desde la GUI."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

ENGINE_ID = "431960"
SEARCH_ROOTS = [
    Path.home() / ".steam/steam/steamapps",
    Path.home() / ".local/share/Steam/steamapps",
]
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp"}


def _roots() -> list[Path]:
    found = []
    for base in SEARCH_ROOTS:
        if base.exists():
            found.append(base)
    return found


def detect() -> dict[str, Any]:
    for base in _roots():
        common = base / "common/wallpaper_engine"
        workshop = base / "workshop/content" / ENGINE_ID
        if common.exists():
            return {"installed": True, "common": str(common),
                    "workshop": str(workshop) if workshop.exists() else ""}
    return {"installed": False, "common": "", "workshop": "",
            "note": "Wallpaper Engine no está instalado (Steam sí). App id 431960."}


def list_wallpapers(limit: int = 40) -> list[dict[str, Any]]:
    """Lista proyectos con imagen de vista previa utilizable como fondo estático."""
    info = detect()
    if not info["installed"]:
        return []
    dirs: list[Path] = []
    for key in ("common", "workshop"):
        root = Path(info[key]) if info[key] else None
        if root and root.exists():
            dirs += [p for p in root.rglob("*") if p.is_dir() and (p / "project.json").exists()]
    out = []
    for project in dirs[:limit]:
        images = [p for p in project.iterdir() if p.suffix.lower() in IMAGE_EXT]
        if not images:
            continue
        title = project.name
        cfg = project / "project.json"
        try:
            data = json.loads(cfg.read_text(encoding="utf-8", errors="replace"))
            title = data.get("title", title)
        except (OSError, ValueError):
            pass
        out.append({"id": project.name, "title": str(title)[:60],
                    "resolution": "Wallpaper Engine", "path": str(images[0]),
                    "provider": "Wallpaper Engine"})
    return out


def preview_image(item: dict[str, Any]) -> str:
    return item.get("path", "")


def open_store() -> tuple[bool, str]:
    """Abre la ficha de Wallpaper Engine en Steam (o la web)."""
    for target in (f"steam://store/{ENGINE_ID}",
                   "https://store.steampowered.com/app/431960/Wallpaper_Engine/"):
        try:
            proc = subprocess.run(["xdg-open", target], capture_output=True, text=True, timeout=8)
            if proc.returncode == 0:
                return True, target
        except (OSError, subprocess.SubprocessError):
            continue
    return False, "no se pudo abrir"
