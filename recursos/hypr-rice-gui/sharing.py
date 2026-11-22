#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · sharing.py — integración web para compartir/descubrir rices
# -----------------------------------------------------------------------------
# Red: GitHub REST API (pública), raw.githubusercontent.com y dotfyle.com.
# Nunca se envían dotfiles automáticamente: publicar requiere un token que el
# usuario escribe en la GUI y que NO se guarda en disco.
# Efectos externos: crea un ZIP en ~/ricing/compartir/ y puede abrir el navegador
# con xdg-open. clonar repos los deja en ~/ricing/repositorios/importados/.
# =============================================================================
"""Descubrir, importar y compartir rices mediante GitHub, Gists y Dotfyle."""
from __future__ import annotations

import json
import re
import subprocess
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Any

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/125 Safari/537.36"
API = "https://api.github.com"
OUT = Path.home() / "ricing/compartir"
IMPORTADOS = Path.home() / "ricing/repositorios/importados"

# Rutas que se incluyen en el paquete compartible (sin secretos).
BUNDLE_PATHS = [
    Path.home() / ".config/hypr",
    Path.home() / ".config/noctalia/config.toml",
    Path.home() / ".config/kitty",
    Path.home() / ".config/alacritty",
    Path.home() / ".config/gtk-3.0/noctalia.css",
    Path.home() / ".config/fish/config.fish",
    Path.home() / ".local/share/color-schemes",
]
EXCLUDED = {"fish_variables", "keyrings", "opencode", "cache", ".git"}


def _curl(url: str, timeout: int = 25, headers: list[str] | None = None) -> str:
    cmd = ["curl", "-sS", "-L", "--compressed", "--max-time", str(timeout), "-A", UA]
    for h in headers or []:
        cmd += ["-H", h]
    cmd.append(url)
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5).stdout
    except (OSError, subprocess.SubprocessError):
        return ""


def search_repos(query: str, limit: int = 15) -> list[dict[str, Any]]:
    """Busca dotfiles/rices en GitHub (topic hyprland si el usuario no especifica)."""
    q = query.strip() or "topic:hyprland dotfiles"
    if "topic:" not in q:
        q = f"{q} hyprland"
    from urllib.parse import quote
    raw = _curl(f"{API}/search/repositories?q={quote(q)}&sort=stars&per_page={limit}",
                headers=["Accept: application/vnd.github+json"])
    try:
        items = json.loads(raw).get("items", [])
    except (ValueError, AttributeError):
        return []
    return [{"name": i["full_name"], "stars": i["stargazers_count"],
             "description": i.get("description") or "", "url": i["html_url"]}
            for i in items]


def search_gists(query: str, limit: int = 10) -> list[dict[str, Any]]:
    """Busca Gists públicos (configs sueltas)."""
    from urllib.parse import quote
    raw = _curl(f"{API}/search/gists?q={quote(query or 'hyprland')}&per_page={limit}",
                headers=["Accept: application/vnd.github+json"])
    try:
        items = json.loads(raw).get("items", [])
    except (ValueError, AttributeError):
        return []
    return [{"name": (i.get("description") or i["id"])[:60], "stars": 0,
             "description": ", ".join(i.get("files", {}).keys())[:80], "url": i["html_url"]}
            for i in items]


def dotfyle_featured() -> list[dict[str, Any]]:
    """Extrae enlaces a repos de la portada de Dotfyle (sin API pública)."""
    html = _curl("https://dotfyle.com/")
    urls = sorted(set(re.findall(r"https://github\.com/[\w.-]+/[\w.-]+", html)))
    return [{"name": u.rsplit("/", 2)[-2] + "/" + u.rsplit("/", 1)[-1],
             "stars": 0, "description": "Destacado en Dotfyle", "url": u} for u in urls[:15]]


def get_readme(repo_full_name: str) -> str:
    """Devuelve el README de un repo para previsualizarlo en la GUI."""
    for branch in ("main", "master"):
        for name in ("README.md", "readme.md", "README.rst"):
            txt = _curl(f"https://raw.githubusercontent.com/{repo_full_name}/{branch}/{name}")
            if len(txt) > 200:
                return txt
    return "(sin README disponible)"


def open_browser(url: str) -> tuple[bool, str]:
    try:
        proc = subprocess.run(["xdg-open", url], capture_output=True, text=True, timeout=8)
        return proc.returncode == 0, proc.stderr.strip()[:120]
    except (OSError, subprocess.SubprocessError) as e:
        return False, str(e)[:120]


def import_repo(url: str) -> tuple[bool, str]:
    """Clona shallow un repo de referencia a ~/ricing/repositorios/importados."""
    name = url.rstrip("/").rsplit("/", 1)[-1].removesuffix(".git")
    if not re.fullmatch(r"[\w.-]+", name):
        return False, "nombre de repo inválido"
    IMPORTADOS.mkdir(parents=True, exist_ok=True)
    dest = IMPORTADOS / name
    if dest.exists():
        return True, str(dest)
    try:
        proc = subprocess.run(["git", "clone", "--depth", "1", url, str(dest)],
                              capture_output=True, text=True, timeout=180)
        return proc.returncode == 0, str(dest) if proc.returncode == 0 else proc.stderr.strip()[:160]
    except (OSError, subprocess.SubprocessError) as e:
        return False, str(e)[:160]


def create_bundle() -> tuple[bool, str]:
    """Genera un ZIP con la configuración del rice (excluyendo secretos)."""
    OUT.mkdir(parents=True, exist_ok=True)
    name = f"rice-{datetime.now().strftime('%Y%m%d-%H%M%S')}.zip"
    dest = OUT / name
    count = 0
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for base in BUNDLE_PATHS:
            if not base.exists():
                continue
            files = [base] if base.is_file() else [p for p in base.rglob("*") if p.is_file()]
            for p in files:
                if any(x in p.parts for x in EXCLUDED):
                    continue
                z.write(p, p.relative_to(Path.home()).as_posix())
                count += 1
        z.writestr("LEEME.txt",
                   "Rice exportado por Ricing HGUI\n"
                   "Hyprland 0.57 (config Lua) + Noctalia\n"
                   "No incluye secretos. Revisa los archivos antes de publicarlos.\n")
    return True, f"{dest} ({count} archivos)"


def publish_gist(token: str, description: str, public: bool) -> tuple[bool, str]:
    """Publica los archivos del bundle en un Gist. El token NO se persiste."""
    if not token.startswith(("ghp_", "github_pat_")):
        return False, "token no válido"
    bundle = sorted(OUT.glob("rice-*.zip"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not bundle:
        return False, "genera primero el ZIP"
    with zipfile.ZipFile(bundle[0]) as z:
        files = {}
        for n in z.namelist():
            if n.endswith("/") or len(files) >= 9:
                continue
            data = z.read(n)
            try:
                files[n.replace("/", "__")] = {"content": data.decode("utf-8")}
            except UnicodeDecodeError:
                continue
    payload = json.dumps({"description": description or "Rice Hyprland + Noctalia",
                          "public": bool(public), "files": files})
    # curl con POST requiere -X y --data; se construye aparte.
    try:
        proc = subprocess.run([
            "curl", "-sS", "-X", "POST", "--max-time", "40", "-A", UA,
            "-H", "Accept: application/vnd.github+json",
            "-H", f"Authorization: Bearer {token}",
            "-H", "Content-Type: application/json",
            "--data", payload, f"{API}/gists",
        ], capture_output=True, text=True, timeout=50)
        data = json.loads(proc.stdout)
        if data.get("html_url"):
            return True, data["html_url"]
        return False, data.get("message", "error al publicar")[:160]
    except (OSError, subprocess.SubprocessError, ValueError) as e:
        return False, str(e)[:160]
