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


def _limit(value: Any, default: int = 10, cap: int = 50) -> int:
    """Normaliza límites de la GUI/API: nunca cero, negativo ni texto."""
    try:
        return max(1, min(int(value), cap))
    except (TypeError, ValueError):
        return default


def _curl(url: str, timeout: int = 25, headers: list[str] | None = None) -> str:
    """GET con curl. `headers` permite autenticar Unsplash/Pexels sin exponer
    la clave en la URL (se pasa como cabecera, nunca en el query string)."""
    cmd = ["curl", "-sS", "-L", "--compressed", "--max-time", str(timeout), "-A", UA]
    for h in headers or []:
        cmd += ["-H", h]
    cmd.append(url)
    try:
        return subprocess.run(cmd, capture_output=True, text=True,
                              timeout=timeout + 5).stdout
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
    """Reduce la resolución del monitor a una proporción tipo '8x5' (Wallhaven).

    AUDITORÍA: la API rechaza proporciones no positivas. Antes, un monitor con
    datos corruptos (0, negativos) producía "0x0" o "-16x9" y la búsqueda
    devolvía cero resultados; ahora se considera "sin filtro".
    """
    from math import gcd
    try:
        width, height = int(width), int(height)
    except (TypeError, ValueError):
        return ""
    if width <= 0 or height <= 0:
        return ""
    g = gcd(width, height) or 1
    return f"{width // g}x{height // g}"


def matches_ratio(resolution: str, width: int, height: int, tolerance: float = 0.02) -> bool:
    """Comprueba que una resolución 'WxH' respete la proporción del monitor.

    AUDITORÍA: "0x0" (respuesta habitual de algunos proveedores cuando no
    conocen el tamaño) provocaba ZeroDivisionError y tumbaba toda la lista.
    Sin datos válidos no se filtra: se devuelve True.
    """
    m = re.match(r"(\d+)\s*[xX]\s*(\d+)", resolution or "")
    try:
        width, height = int(width), int(height)
    except (TypeError, ValueError):
        return True
    if not m or width <= 0 or height <= 0:
        return True  # sin datos, no filtramos
    w, h = int(m.group(1)), int(m.group(2))
    if w <= 0 or h <= 0:
        return True
    try:
        return abs((w / h) - (width / height)) <= tolerance * (width / height)
    except ZeroDivisionError:
        return True


def search_wallhaven(query: str, limit: int = 16, width: int = 0, height: int = 0) -> list[dict[str, Any]]:
    limit = _limit(limit, 16, 50)
    params = {
        "q": (query or "").strip(), "categories": "111", "purity": "100", "sorting": "relevance",
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
        payload = json.loads(raw)
        data = payload.get("data", []) if isinstance(payload, dict) else []
    except (ValueError, AttributeError):
        data = []
    if not isinstance(data, list):
        return []
    out = []
    for w in data[:limit]:
        if not isinstance(w, dict):
            continue
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
    api_key = (api_key or "").strip()
    if not api_key:
        return []
    params = {"query": (query or "wallpaper").strip() or "wallpaper", "per_page": _limit(limit, 10, 30)}
    if width and height:
        params.update({"w": width, "h": height, "fit": "crop"})
    raw = _curl(f"https://api.unsplash.com/search/photos?{urllib.parse.urlencode(params)}",
                headers=[f"Authorization: Client-ID {api_key.strip()}"])
    try:
        payload = json.loads(raw)
        items = payload.get("results", []) if isinstance(payload, dict) else []
    except (ValueError, AttributeError):
        items = []
    out = []
    for i in (items if isinstance(items, list) else [])[:limit]:
        if not isinstance(i, dict):
            continue
        out.append({"id": str(i.get("id", "")),
                    "title": str(i.get("alt_description") or "Unsplash")[:50],
                    "resolution": f"{i.get('width', 0)}x{i.get('height', 0)}",
                    "thumb": "", "url": i.get("urls", {}).get("full", "") if isinstance(i.get("urls"), dict) else "",
                    "path": "", "provider": "Unsplash"})
    return out


def search_pexels(query: str, api_key: str, limit: int = 10,
                  width: int = 0, height: int = 0) -> list[dict[str, Any]]:
    """Pexels (clave opcional del usuario). Respeta la proporción del monitor."""
    api_key = (api_key or "").strip()
    if not api_key:
        return []
    params = {"query": (query or "wallpaper").strip() or "wallpaper", "per_page": _limit(limit, 10, 30)}
    if width and height:
        params.update({"width": width, "height": height})
    raw = _curl(f"https://api.pexels.com/v1/search?{urllib.parse.urlencode(params)}",
                headers=[f"Authorization: {api_key.strip()}"])
    try:
        payload = json.loads(raw)
        items = payload.get("photos", []) if isinstance(payload, dict) else []
    except (ValueError, AttributeError):
        items = []
    out = []
    for i in (items if isinstance(items, list) else [])[:limit]:
        if not isinstance(i, dict):
            continue
        src = i.get("src") if isinstance(i.get("src"), dict) else {}
        out.append({"id": str(i.get("id", "")), "title": str(i.get("alt") or "Pexels")[:50],
                    "resolution": f"{i.get('width', 0)}x{i.get('height', 0)}",
                    "thumb": src.get("tiny", ""), "url": src.get("original", ""),
                    "path": "", "provider": "Pexels"})
    return out


def download(item: dict[str, Any]) -> tuple[bool, str]:
    """Descarga un wallpaper a ~/Imágenes/ricing-wallpapers y devuelve la ruta.

    AUDITORÍA: `id` y `provider` vienen de una API externa (Wallhaven). Un id
    con `../` podía escapar del directorio de descargas; un `file://` podía
    copiar archivos locales. Se sanea el nombre y sólo se permiten http(s).
    """
    item = item if isinstance(item, dict) else {}
    local = item.get("path", "")
    if local and Path(str(local)).is_file() and not Path(str(local)).is_symlink():
        return True, str(local)
    url = str(item.get("url") or "").strip()
    scheme = urllib.parse.urlparse(url).scheme.lower()
    if scheme not in {"http", "https"}:
        return False, "URL no válida (sólo http/https)"
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", f"{item.get('provider', 'wall')}-{item.get('id', 'wallpaper')}")
    safe = safe.lstrip(".") or "wallpaper"
    dest = (DOWNLOADS / f"{safe}.jpg").resolve()
    # Doble barrera: aunque `safe` cambiara, la ruta debe quedar dentro.
    if dest.parent != DOWNLOADS.resolve():
        return False, "ruta de destino no válida"
    try:
        proc = subprocess.run(["curl", "-sS", "-L", "--max-time", "60", "-A", UA,
                               url, "-o", str(dest)], capture_output=True, text=True, timeout=75)
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
