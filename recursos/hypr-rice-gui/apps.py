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
import shlex
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
    values = values if isinstance(values, dict) else {}
    for role in ROLES:
        v = str(values.get(role) or "").strip()
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
    """Escribe las apps en variables.lua. Nunca parta el archivo por un \n.

    AUDITORÍA: si un campo contenía un salto de línea, `re.subn` insertaba
    una línea Lua nueva y rompía la configuración. Además, un dict parcial
    borraba los roles no enviados: ahora se fusiona con los valores actuales.
    """
    values = values if isinstance(values, dict) else {}
    current = read_apps()
    for role in ROLES:
        if role in values:
            current[role] = str(values[role] or "").strip()
    hard = [p for p in validate(current) if "saltos de línea" in p or "NUL" in p]
    if hard:
        return False, "; ".join(hard)
    if any("\0" in v for v in current.values()):
        return False, "valor con carácter NUL"
    import backup_manager as bm
    bm.create_backup(reason="editar-apps-variables")
    if not VARS.exists():
        return False, "no existe variables.lua"
    text = VARS.read_text(encoding="utf-8")
    for role in ROLES:
        line = f'{role} = "{_escape(current[role])}"'
        text, n = re.subn(rf'(?m)^{role}\s*=\s*".*"', lambda m, l=line: l, text)
        if n == 0 and role == "BROWSER_SECONDARY":
            # insertar junto a BROWSER si no existe (lambda evita interpretar \\ en el reemplazo)
            text = re.sub(r'(?m)^(BROWSER\s*=.*)$',
                          lambda m: m.group(1) + "\n" + line, text, count=1)
    VARS.write_text(text, encoding="utf-8")
    return sync_env(current)


def sync_env(values: dict[str, str]) -> tuple[bool, str]:
    """Añade/actualiza exports para Noctalia y UWSM (comandos citados)."""
    if not UWSM_ENV.exists():
        return True, "variables guardadas (sin uwsm-env)"
    values = values if isinstance(values, dict) else {}
    try:
        text = UWSM_ENV.read_text(encoding="utf-8")
    except OSError:
        return False, "no se pudo leer uwsm-env"
    for env_name, role in (("TERMINAL", "TERMINAL"), ("BROWSER", "BROWSER"), ("EDITOR", "EDITOR")):
        value = str(values.get(role) or "").strip()
        if not value or "\n" in value or "\r" in value:
            continue
        # AUDITORÍA: antes se conservaba sólo la primera palabra (`sh -c ...`
        # se volvía `sh`) y los backslashes se interpretaban como grupos de
        # regex en re.subn. shlex.quote mantiene el comando completo y seguro.
        exported = f"export {env_name}={shlex.quote(value)}"
        text, n = re.subn(rf'(?m)^export {env_name}=.*$',
                          lambda m, e=exported: e, text)
        if n == 0:
            text += "\n" + exported + "\n"
    try:
        UWSM_ENV.write_text(text, encoding="utf-8")
    except OSError:
        return False, "no se pudo escribir uwsm-env"
    return True, "variables y entorno guardados (el entorno se aplica al reiniciar sesión)"


def ensure_secondary_bind(values: dict[str, str] | None = None) -> tuple[bool, str]:
    """Añade una sola línea a binds.lua para el navegador secundario."""
    if values is not None and not (values.get("BROWSER_SECONDARY") or "").strip():
        return True, "sin navegador secundario: no se añade bind"
    if not BINDS.exists():
        return False, "no existe binds.lua"
    text = BINDS.read_text(encoding="utf-8")
    # AUDITORÍA: un comentario que mencionaba BROWSER_SECONDARY daba falso
    # positivo y el bind nunca se añadía. Sólo cuenta una línea activa.
    if re.search(r"(?m)^\s*hl\.bind\([^\n]*BROWSER_SECONDARY", text):
        return True, "bind secundario ya presente"
    text = text.rstrip() + "\n\n-- Navegador secundario (gestionado por Ricing HGUI)\n" + SECONDARY_LINE + "\n"
    BINDS.write_text(text, encoding="utf-8")
    return True, "bind secundario añadido"


def apply_live(values: dict[str, str]) -> tuple[bool, str]:
    """Rebindea los launchers con los valores resueltos (sin reload)."""
    values = values if isinstance(values, dict) else {}
    if any("\n" in str(v or "") or "\r" in str(v or "") for v in values.values()):
        return False, "valor con salto de línea"
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
