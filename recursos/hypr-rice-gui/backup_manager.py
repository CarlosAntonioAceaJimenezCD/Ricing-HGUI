#!/usr/bin/env python3
"""Gestor de backups automáticos para Ricing HGUI.

Características:
  - Copia de seguridad de los dotfiles del rice antes de cada cambio.
  - Backups programados (intervalo configurable) mientras la app está abierta.
  - Retención automática: conserva sólo los N más recientes.
  - Manifiesto con SHA-256 por archivo para verificar integridad.
  - Restauración segura: hace un backup "pre-restore" antes de sobrescribir.

No requiere privilegios de root. Nunca incluye secretos (fish_variables, keyrings…).
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import tarfile
from datetime import datetime, timedelta
from pathlib import Path
from typing import Iterable

APP_DIR = Path.home() / ".local/share/hypr-rice-gui"
BACKUP_DIR = APP_DIR / "backups"
SETTINGS_FILE = APP_DIR / "settings.json"
MANIFEST = "manifest.json"

DEFAULT_TARGETS: tuple[Path, ...] = (
    Path.home() / ".config/hypr",
    Path.home() / ".config/noctalia/config.toml",
    Path.home() / ".config/kitty",
    Path.home() / ".config/alacritty",
    Path.home() / ".config/gtk-3.0",
    Path.home() / ".config/fish/config.fish",
    Path.home() / ".local/share/color-schemes",
)

EXCLUDED_NAMES = {"fish_variables", "keyrings", "opencode", "cache", ".git", "__pycache__"}
EXCLUDED_PARTS = {"keyrings", "opencode"}

DEFAULT_SETTINGS = {
    "auto_backup": True,
    "interval_minutes": 15,
    "keep_last": 10,
}


# --------------------------------------------------------------------------- settings
def get_settings() -> dict:
    settings = dict(DEFAULT_SETTINGS)
    if SETTINGS_FILE.exists():
        try:
            settings.update(json.loads(SETTINGS_FILE.read_text(encoding="utf-8")))
        except (OSError, ValueError):
            pass
    return settings


def save_settings(settings: dict) -> None:
    APP_DIR.mkdir(parents=True, exist_ok=True)
    SETTINGS_FILE.write_text(json.dumps(settings, indent=2), encoding="utf-8")


# --------------------------------------------------------------------------- helpers
def _excluded(path: Path) -> bool:
    return any(p in EXCLUDED_PARTS for p in path.parts) or path.name in EXCLUDED_NAMES


def _iter_files(targets: Iterable[Path]) -> list[Path]:
    found: list[Path] = []
    for target in targets:
        if not target.exists():
            continue
        if target.is_file():
            if not _excluded(target):
                found.append(target)
        else:
            for p in target.rglob("*"):
                if p.is_file() and not _excluded(p):
                    found.append(p)
    return sorted(set(found))


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _relative(path: Path) -> str:
    return str(path).lstrip("/")


def _enforce_retention(keep_last: int) -> None:
    backups = sorted(BACKUP_DIR.glob("backup-*.tar.gz"), key=lambda p: p.stat().st_mtime, reverse=True)
    for old in backups[max(1, keep_last):]:
        old.unlink(missing_ok=True)


# --------------------------------------------------------------------------- create
def create_backup(reason: str = "manual", targets: Iterable[Path] | None = None) -> dict | None:
    """Crea un backup tar.gz y devuelve su manifiesto, o None si no hay nada que copiar."""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    files = _iter_files(tuple(targets) if targets is not None else DEFAULT_TARGETS)
    if not files:
        return None

    now = datetime.now().astimezone()
    stamp = now.strftime("%Y%m%d-%H%M%S")
    name = f"backup-{stamp}-{reason}"
    tmp = BACKUP_DIR / f".tmp-{name}"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)

    records = []
    for src in files:
        rel = _relative(src)
        dest = tmp / "data" / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy2(src, dest)
        except OSError:
            continue
        records.append({
            "path": rel,
            "sha256": _sha256(dest),
            "size": dest.stat().st_size,
        })

    manifest = {
        "created_at": now.isoformat(),
        "reason": reason,
        "app": "Ricing HGUI",
        "file_count": len(records),
        "files": records,
    }
    (tmp / MANIFEST).write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    archive = BACKUP_DIR / f"{name}.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        tar.add(tmp / MANIFEST, arcname=MANIFEST)
        tar.add(tmp / "data", arcname="data")

    shutil.rmtree(tmp, ignore_errors=True)
    _enforce_retention(get_settings().get("keep_last", 10))
    manifest["archive"] = archive.name
    manifest["archive_size"] = archive.stat().st_size
    return manifest


# --------------------------------------------------------------------------- list / inspect
def list_backups() -> list[dict]:
    items = []
    for archive in sorted(BACKUP_DIR.glob("backup-*.tar.gz"), key=lambda p: p.stat().st_mtime, reverse=True):
        try:
            with tarfile.open(archive, "r:gz") as tar:
                f = tar.extractfile(MANIFEST)
                if f is None:
                    continue
                m = json.loads(f.read())
        except (OSError, tarfile.TarError, ValueError):
            continue
        items.append({
            "name": archive.name,
            "created_at": m.get("created_at", ""),
            "reason": m.get("reason", ""),
            "file_count": m.get("file_count", 0),
            "size": archive.stat().st_size,
        })
    return items


def verify_backup(name: str) -> tuple[bool, str]:
    archive = BACKUP_DIR / name
    if not archive.exists():
        return False, "no existe"
    try:
        with tarfile.open(archive, "r:gz") as tar:
            f = tar.extractfile(MANIFEST)
            if f is None:
                return False, "sin manifiesto"
            m = json.loads(f.read())
            for rec in m.get("files", []):
                member = tar.extractfile(f"data/{rec['path']}")
                if member is None:
                    return False, f"falta {rec['path']}"
                if hashlib.sha256(member.read()).hexdigest() != rec["sha256"]:
                    return False, f"hash distinto: {rec['path']}"
    except (OSError, tarfile.TarError, ValueError) as e:
        return False, str(e)[:120]
    return True, f"{m.get('file_count', 0)} archivos íntegros"


# --------------------------------------------------------------------------- history / inspect
def get_backup_details(name: str) -> dict | None:
    """Devuelve el manifiesto completo de un backup (para inspeccionarlo)."""
    archive = BACKUP_DIR / name
    if not archive.exists():
        return None
    try:
        with tarfile.open(archive, "r:gz") as tar:
            f = tar.extractfile(MANIFEST)
            if f is None:
                return None
            return json.loads(f.read())
    except (OSError, tarfile.TarError, ValueError):
        return None


def read_file_from_backup(name: str, rel_path: str) -> str | None:
    """Lee un archivo de texto dentro de un backup sin extraerlo."""
    archive = BACKUP_DIR / name
    try:
        with tarfile.open(archive, "r:gz") as tar:
            member = tar.extractfile(f"data/{rel_path.lstrip('/')}")
            if member is None:
                return None
            return member.read().decode("utf-8", errors="replace")
    except (OSError, tarfile.TarError, KeyError):
        return None


def compare_with_current(name: str) -> dict:
    """Compara un backup con el estado actual: devuelve Changed/Missing/Same."""
    manifest = get_backup_details(name) or {}
    changed: list[str] = []
    missing: list[str] = []
    same: list[str] = []
    for rec in manifest.get("files", []):
        path = Path("/") / rec["path"]
        if not path.exists():
            missing.append(rec["path"])
        elif _sha256(path) != rec["sha256"]:
            changed.append(rec["path"])
        else:
            same.append(rec["path"])
    return {"changed": changed, "missing": missing, "same": same}


def delete_backup(name: str) -> tuple[bool, str]:
    archive = BACKUP_DIR / name
    if not archive.exists():
        return False, "no existe"
    try:
        archive.unlink()
        return True, "eliminado"
    except OSError as e:
        return False, str(e)[:120]


# --------------------------------------------------------------------------- restore
def restore_backup(name: str) -> tuple[bool, str]:
    """Restaura un backup. Antes hace un backup de seguridad del estado actual."""
    archive = BACKUP_DIR / name
    ok, msg = verify_backup(name)
    if not ok:
        return False, f"backup inválido: {msg}"

    create_backup(reason="pre-restore")
    tmp = BACKUP_DIR / f".restore-{Path(name).stem}"
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir(parents=True)

    try:
        with tarfile.open(archive, "r:gz") as tar:
            for member in tar.getmembers():
                target = (tmp / member.name).resolve()
                if not str(target).startswith(str(tmp.resolve())):
                    return False, "ruta insegura en el archivo"
            tar.extractall(tmp)

        data = tmp / "data"
        restored = 0
        for src in data.rglob("*"):
            if not src.is_file():
                continue
            rel = src.relative_to(data)
            dest = Path("/") / rel
            if _excluded(dest):
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            restored += 1
        return True, f"restaurados {restored} archivos"
    except (OSError, tarfile.TarError) as e:
        return False, str(e)[:160]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# --------------------------------------------------------------------------- scheduling
def next_due() -> datetime | None:
    """Devuelve cuándo toca el próximo backup automático, o None si está desactivado."""
    s = get_settings()
    if not s.get("auto_backup", True):
        return None
    backups = list_backups()
    auto = [b for b in backups if b["reason"] in {"auto", "inicio"}]
    if not auto:
        return datetime.now().astimezone()
    last = datetime.fromisoformat(auto[0]["created_at"])
    return last + timedelta(minutes=int(s.get("interval_minutes", 15)))
