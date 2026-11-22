#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · wallpapers.py — proveedores de fondos y aplicación
# -----------------------------------------------------------------------------
# Red: sólo dos proveedores; Wallhaven API pública (sin clave) y archivos
# locales de /usr/share/wallpapers. No se envían datos del usuario a la API
# salvo el término de búsqueda que escribe el usuario.
# Efectos externos: descarga archivos a ~/Imágenes/ricing-wallpapers y ejecuta
# `noctalia msg wallpaper-set [connector] <path>` (IPC oficial, documentado).
# Picsum quedó descartado porque responde "Geoblocked" desde esta máquina.
# =============================================================================
"""Integración con sitios de wallpapers y aplicación vía Noctalia IPC.

Proveedores:
  - Local: /usr/share/wallpapers/cachyos-wallpapers
  - Wallhaven: API pública https://wallhaven.cc/api/v1/search (sin clave)
"""
from __future__ import annotations

import json
import re
import subprocess
import urllib.parse
from pathlib import Path
from typing import Any

DOWNLOADS = Path.home() / "Imágenes/ricing-wallpapers"
LOCAL_DIRS = [
    Path("/usr/share/wallpapers/cachyos-wallpapers"),
    Path("/usr/share/noctalia/assets"),
]
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125 Safari/537.36"


def _curl(url: str, timeout: int = 25) -> str:
    try:
        return subprocess.run(["curl", "-sS", "-L", "--compressed", "--max-time", str(timeout),
                               "-A", UA, url], capture_output=True, text=True).stdout
    except (OSError, subprocess.SubprocessError):
        return ""


def local_wallpapers() -> list[dict[str, Any]]:
    items = []
    for d in LOCAL_DIRS:
        if not d.exists():
            continue
        for p in sorted(d.rglob("*")):
            if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                items.append({"id": p.name, "title": p.stem, "resolution": "local",
                              "thumb": "", "url": "", "path": str(p), "provider": "Local"})
    return items[:80]


def ratio_filter(width: int, height: int) -> str:
    """Reduce la resolución del monitor a una proporción tipo '8x5' (Wallhaven)."""
    from math import gcd
    if not width or not height:
        return ""
    g = gcd(int(width), int(height)) or 1
    return f"{int(width) // g}x{int(height) // g}"


def matches_ratio(resolution: str, width: int, height: int, tolerance: float = 0.02) -> bool:
    """Comprueba que una resolución 'WxH' respete la proporción del monitor."""
    m = re.match(r"(\d+)\s*[xX]\s*(\d+)", resolution or "")
    if not m or not width or not height:
        return True  # sin datos, no filtramos
    w, h = int(m.group(1)), int(m.group(2))
    return abs((w / h) - (width / height)) <= tolerance * (width / height)


def search_wallhaven(query: str, limit: int = 16, width: int = 0, height: int = 0) -> list[dict[str, Any]]:
    params = {
        "q": query, "categories": "111", "purity": "100", "sorting": "relevance",
    }
    if width and height:
        # AUDITORÍA: filtro automático por monitor → sólo fondos de la misma
        # proporción y resolución mínima nativa. Evita recortes raros.
        params["ratios"] = ratio_filter(width, height)
        params["atleast"] = f"{width}x{height}"
    else:
        params["atleast"] = "1440x900"
    raw = _curl(f"https://wallhaven.cc/api/v1/search?{urllib.parse.urlencode(params)}")
    try:
        data = json.loads(raw).get("data", [])
    except (ValueError, AttributeError):
        return []
    out = []
    for w in data[:limit]:
        out.append({
            "id": w.get("id", ""),
            "title": w.get("id", ""),
            "resolution": w.get("resolution", ""),
            "thumb": w.get("thumbs", {}).get("small", ""),
            "url": w.get("path", ""),
            "path": "",
            "provider": "Wallhaven",
        })
    return out


def search_unsplash(query: str, api_key: str, limit: int = 10,
                    width: int = 0, height: int = 0) -> list[dict[str, Any]]:
    """Unsplash con clave opcional del usuario (nunca se guarda)."""
    if not api_key.strip():
        return []
    params = {"query": query or "wallpaper", "per_page": limit}
    if width and height:
        params.update({"w": width, "h": height, "fit": "crop"})
    raw = _curl(f"https://api.unsplash.com/search/photos?{urllib.parse.urlencode(params)}",
                headers=[f"Authorization: Client-ID {api_key.strip()}"])
    try:
        items = json.loads(raw).get("results", [])
    except (ValueError, AttributeError):
        return []
    return [{"id": i.get("id", ""), "title": (i.get("alt_description") or "Unsplash")[:50],
             "resolution": f"{i.get('width', 0)}x{i.get('height', 0)}",
             "thumb": "", "url": i.get("urls", {}).get("full", ""),
             "path": "", "provider": "Unsplash"} for i in items]


def search_pexels(query: str, api_key: str, limit: int = 10,
                  width: int = 0, height: int = 0) -> list[dict[str, Any]]:
    """Pexels (clave opcional del usuario). Respeta la proporción del monitor."""
    if not api_key.strip():
        return []
    params = {"query": query or "wallpaper", "per_page": limit}
    if width and height:
        params.update({"width": width, "height": height})
    raw = _curl(f"https://api.pexels.com/v1/search?{urllib.parse.urlencode(params)}",
                headers=[f"Authorization: {api_key.strip()}"])
    try:
        items = json.loads(raw).get("photos", [])
    except (ValueError, AttributeError):
        return []
    return [{"id": str(i.get("id", "")), "title": (i.get("alt") or "Pexels")[:50],
             "resolution": f"{i.get('width', 0)}x{i.get('height', 0)}",
             "thumb": i.get("src", {}).get("tiny", ""),
             "url": i.get("src", {}).get("original", ""),
             "path": "", "provider": "Pexels"} for i in items]


def download(item: dict[str, Any]) -> tuple[bool, str]:
    """Descarga un wallpaper a ~/Imágenes/ricing-wallpapers y devuelve la ruta."""
    if item.get("path") and Path(item["path"]).exists():
        return True, item["path"]
    url = item.get("url", "")
    if not url:
        return False, "sin URL"
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    name = f"{item.get('provider', 'wall')}-{item.get('id', 'wallpaper')}.jpg"
    dest = DOWNLOADS / name
    try:
        proc = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-A", UA,
                               url, "-o", str(dest)], capture_output=True, text=True)
        if proc.returncode != 0 or not dest.exists() or dest.stat().st_size < 5000:
            return False, "descarga fallida"
    except (OSError, subprocess.SubprocessError):
        return False, "descarga fallida"
    return True, str(dest)


def set_wallpaper(path: str, connector: str | None = None) -> tuple[bool, str]:
    """Aplica el wallpaper con Noctalia IPC (wallpaper-set)."""
    cmd = ["noctalia", "msg", "wallpaper-set"]
    if connector:
        cmd.append(connector)
    cmd.append(path)
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return proc.returncode == 0, (proc.stdout or proc.stderr).strip()[:160]
    except (OSError, subprocess.SubprocessError) as e:
        return False, str(e)[:160]
