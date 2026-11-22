#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · apps.py — editor de aplicaciones por defecto
# -----------------------------------------------------------------------------
# Fuente canónica: ~/.config/hypr/config/variables.lua (los binds ya apuntan
# a estas variables, así que NO se reescribe binds.lua salvo una línea extra
# para el navegador secundario).
# Antes de escribir siempre se crea un backup parcial (backup_manager).
# El valor se valida (sin comillas/newlines) y se escapa para Lua.
# uwsm-env se sincroniza con TERMINAL/BROWSER/EDITOR para que Noctalia y UWSM
# vean las mismas apps (hoy sólo estaba TERM → desincronización detectada).
# =============================================================================
"""Gestión de aplicaciones por defecto (principal y secundaria)."""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

VARS = Path.home() / ".config/hypr/config/variables.lua"
BINDS = Path.home() / ".config/hypr/config/binds.lua"
UWSM_ENV = Path.home() / ".config/uwsm/env"

ROLES = ("TERMINAL", "FILE_MANAGER", "BROWSER", "BROWSER_SECONDARY", "EDITOR", "CALCULATOR")
SECONDARY_KEY = "SUPER + SHIFT + W"
SECONDARY_LINE = 'hl.bind(mainMod .. " + SHIFT + W", hl.dsp.exec_cmd(launchPrefix .. BROWSER_SECONDARY))'


def _escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def read_apps() -> dict[str, str]:
    result = {r: "" for r in ROLES}
    if not VARS.exists():
        return result
    for line in VARS.read_text(encoding="utf-8").splitlines():
        m = re.match(r'^(TERMINAL|FILE_MANAGER|BROWSER|BROWSER_SECONDARY|EDITOR|CALCULATOR)\s*=\s*"(.*)"\s*$', line)
        if m:
            result[m.group(1)] = m.group(2).replace('\\"', '"')
    return result


def validate(values: dict[str, str]) -> list[str]:
    problems = []
    for role in ROLES:
        v = (values.get(role) or "").strip()
        if role != "BROWSER_SECONDARY" and not v:
            problems.append(f"{role} no puede estar vacío")
        if "\n" in v or "\r" in v:
            problems.append(f"{role} contiene saltos de línea")
        if '"' in v or "\\" in v:
            problems.append(f"{role} contiene comillas o barras (se escaparán)")
        if v and not shutil.which(v.split()[0]):
            problems.append(f"{role}: «{v.split()[0]}» no está en PATH (advertencia)")
    return problems


def write_apps(values: dict[str, str]) -> tuple[bool, str]:
    import backup_manager as bm
    bm.create_backup(reason="editar-apps-variables")
    if not VARS.exists():
        return False, "no existe variables.lua"
    text = VARS.read_text(encoding="utf-8")
    for role in ROLES:
        value = (values.get(role) or "").strip()
        line = f'{role} = "{_escape(value)}"'
        text, n = re.subn(rf'(?m)^{role}\s*=\s*".*"', line, text)
        if n == 0 and role == "BROWSER_SECONDARY":
            # insertar junto a BROWSER si no existe (lambda evita interpretar \\ en el reemplazo)
            text = re.sub(r'(?m)^(BROWSER\s*=.*)$',
                          lambda m: m.group(1) + "\n" + line, text, count=1)
    VARS.write_text(text, encoding="utf-8")
    return sync_env(values)


def sync_env(values: dict[str, str]) -> tuple[bool, str]:
    """Añade/actualiza exports para Noctalia y UWSM."""
    if not UWSM_ENV.exists():
        return True, "variables guardadas (sin uwsm-env)"
    text = UWSM_ENV.read_text(encoding="utf-8")
    for env_name, role in (("TERMINAL", "TERMINAL"), ("BROWSER", "BROWSER"), ("EDITOR", "EDITOR")):
        value = (values.get(role) or "").split()[0] if values.get(role) else ""
        if not value:
            continue
        text, n = re.subn(rf'(?m)^export {env_name}=.*$', f'export {env_name}={value}', text)
        if n == 0:
            text += f'\nexport {env_name}={value}\n'
    UWSM_ENV.write_text(text, encoding="utf-8")
    return True, "variables y entorno guardados (el entorno se aplica al reiniciar sesión)"


def ensure_secondary_bind(values: dict[str, str] | None = None) -> tuple[bool, str]:
    """Añade una sola línea a binds.lua para el navegador secundario."""
    if values is not None and not (values.get("BROWSER_SECONDARY") or "").strip():
        return True, "sin navegador secundario: no se añade bind"
    if not BINDS.exists():
        return False, "no existe binds.lua"
    text = BINDS.read_text(encoding="utf-8")
    if "BROWSER_SECONDARY" in text and "hl.bind" in text:
        return True, "bind secundario ya presente"
    text = text.rstrip() + "\n\n-- Navegador secundario (gestionado por Ricing HGUI)\n" + SECONDARY_LINE + "\n"
    BINDS.write_text(text, encoding="utf-8")
    return True, "bind secundario añadido"


def apply_live(values: dict[str, str]) -> tuple[bool, str]:
    """Rebindea los launchers con los valores resueltos (sin reload)."""
    launch = "uwsm app -- "
    code = ['hl.unbind("SUPER + W")', f'hl.unbind("{SECONDARY_KEY}")']
    if values.get("BROWSER"):
        code.append(f'hl.bind("SUPER + W", hl.dsp.exec_cmd("{_escape(launch + values["BROWSER"])}"))')
    if values.get("BROWSER_SECONDARY"):
        code.append(f'hl.bind("{SECONDARY_KEY}", hl.dsp.exec_cmd("{_escape(launch + values["BROWSER_SECONDARY"])}"))')
    try:
        p = subprocess.run(["hyprctl", "eval", "\n".join(code)], capture_output=True,
                           text=True, timeout=15)
        return p.returncode == 0, (p.stdout or p.stderr).strip()[:160]
    except (OSError, subprocess.SubprocessError) as e:
        return False, str(e)[:160]


def reload_hyprland() -> tuple[bool, str]:
    try:
        p = subprocess.run(["hyprctl", "reload"], capture_output=True, text=True, timeout=20)
        return p.returncode == 0, (p.stdout or p.stderr).strip()[:160]
    except (OSError, subprocess.SubprocessError) as e:
        return False, str(e)[:160]
