#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · keybinds.py — atajos existentes, edición, desactivado y borrado
# -----------------------------------------------------------------------------
# Fuentes:
#   - en vivo: `hyprctl binds -j` (84+ atajos; la acción aparece como closure
#     opaca HL.Dispatcher(...), por eso también se lee binds.lua para texto);
#   - texto: binds.lua se parsea con regex para mostrar la acción legible.
# Efectos externos: ejecuta `hl.bind` / `hl.unbind` vía `hyprctl eval`; escribe
# ~/.config/hypr/config/ui-bindings.lua y ~/.local/share/.../keybinds.json.
# Invariantes:
#   1. "Desactivar" conserva la entrada y genera un `hl.unbind` persistente.
#   2. "Eliminar" añade una entrada de supresión para que no reaparezca al
#      recargar el config (los atajos de binds.lua no se pueden borrar del todo).
#   3. Para editar un atajo existente se desvincula la tecla antigua primero.
# =============================================================================
"""Gestión de keybindings para Ricing HGUI.

- Lista los atajos actuales desde `hyprctl binds -j` (fuente oficial en vivo).
- Permite añadir, editar y eliminar atajos usando la API Lua de Hyprland 0.57.
- Persiste los atajos propios en JSON y genera un módulo Lua autocontenido
  (~/.config/hypr/config/ui-bindings.lua) que se carga desde hyprland.lua.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any

DATA = Path.home() / ".local/share/hypr-rice-gui/keybinds.json"
LUA_MODULE = Path.home() / ".config/hypr/config/ui-bindings.lua"
SOURCE_BINDS = Path.home() / ".config/hypr/config/binds.lua"
SOURCE_VARS = Path.home() / ".config/hypr/config/variables.lua"

# AUDITORÍA: máscara real de Hyprland (hyprland/src/config/...):
# SHIFT=1, CAPS=2, CTRL=4, ALT=8, SUPER=64, HYPER=128, MEGA=256.
# El mapping anterior (0x40->CTRL) hacía que TODOS los atajos salieran
# como "CTRL + ..." y no emparejaran con binds.lua.
MODS = [
    (0x01, "SHIFT"), (0x04, "CTRL"), (0x08, "ALT"), (0x40, "SUPER"),
]


def hyprctl(*args: str) -> str:
    try:
        return subprocess.run(["hyprctl", *args], capture_output=True,
                              text=True, timeout=6).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def list_binds() -> list[dict[str, Any]]:
    out = hyprctl("binds", "-j")
    try:
        data = json.loads(out)
    except (ValueError, TypeError):
        return []
    result = []
    for b in data:
        mods = [name for bit, name in MODS if b.get("modmask", 0) & bit]
        # AUDITORÍA: Hyprland 0.57 reporta key="" y un `keycode` para los binds
        # creados con code:N (el fix AZERTY del usuario). Sin esto, 44 atajos
        # aparecían como "SUPER + SHIFT + " repetidos.
        key = b.get("key", "")
        if not key and b.get("keycode"):
            key = f"code:{b['keycode']}"
        result.append({
            "key": key,
            "mods": " + ".join(mods) if mods else "(sin modifier)",
            "dispatcher": b.get("dispatcher", ""),
            "arg": b.get("arg", ""),
            "description": b.get("description", ""),
            "repeat": b.get("repeat", False),
            "locked": b.get("locked", False),
            "raw": b,
        })
    return result


def parse_source_binds() -> list[dict[str, str]]:
    """Lee binds.lua y devuelve atajos legibles (clave + acción en texto).

    AUDITORÍA: es un parser de líneas con regex, no un intérprete Lua. Resuelve
    los casos presentes en esta config (mainMod, noctCall, digitCode, variables
    de variables.lua). Bucles y funciones complejas pueden no aparecer: para eso
    está la lista en vivo de `hyprctl binds -j`.
    """
    if not SOURCE_BINDS.exists():
        return []
    variables = {"mainMod": "SUPER", "noctCall": "noctalia msg ", "launchPrefix": "uwsm app -- "}
    if SOURCE_VARS.exists():
        for name, value in re.findall(r'(?m)^(\w+)\s*=\s*"([^"]*)"', SOURCE_VARS.read_text(encoding="utf-8")):
            variables[name] = value

    def resolve(expr: str) -> str:
        # AUDITORÍA: los binds por código usan digitCode(d) -> code:(9+d),
        # con 0 -> code:19. Se inserta COMO LITERAL ENTRE COMILLAS para que
        # la concatenación Lua no lo pierda (antes daba "SUPER + SHIFT + ").
        if "digitCode(" in expr:
            expr = re.sub(
                r"digitCode\((\d+)\)",
                lambda m: '"code:' + str(9 + int(m.group(1)) if int(m.group(1)) else 19) + '"',
                expr,
            )
        # digitCode(key) dentro de bucles no es resoluble estáticamente:
        # se marca para descartar en vez de generar una clave engañosa.
        if re.search(r"digitCode\(", expr):
            return ""
        for name, value in variables.items():
            expr = re.sub(rf"\b{re.escape(name)}\b", f'"{value}"', expr)
        if ".." in expr:
            return "".join(re.findall(r'"([^"]*)"', expr))
        clean = expr.strip()
        if clean.startswith('"') and clean.endswith('"') and clean.count('"') == 2:
            clean = clean[1:-1]
        return clean

    out = []
    for line in SOURCE_BINDS.read_text(encoding="utf-8").splitlines():
        m = re.search(r"hl\.bind\(\s*(.+?)\s*,\s*(.+?)\s*(?:,\s*\{[^}]*\})?\s*\)\s*$", line)
        if not m:
            continue
        key = resolve(m.group(1)).strip()
        action = resolve(m.group(2)).strip()
        # Descartar claves truncadas ("SUPER + SHIFT + ") o sin resolver.
        if key and not key.rstrip().endswith("+") and "digitCode(" not in key:
            out.append({"key": key, "action": action, "source": "binds.lua"})
    return out


def expand_workspace_loops() -> dict[tuple[frozenset, str], str]:
    """Expande los `for i=1,NUM_WPM` de binds.lua que crean binds de workspace.

    AUDITORÍA: son 4 bucles (mover a workspace, mover sin follow, enfocar
    workspace, enfocar relativo). El parser estático no puede resolver
    `digitCode(key)`; aquí se acota a esos patrones conocidos y se genera
    una entrada por i con su code:N y su acción ya resuelta.
    """
    if not SOURCE_BINDS.exists():
        return {}
    text = SOURCE_BINDS.read_text(encoding="utf-8")
    num_wpm = 3
    if SOURCE_VARS.exists():
        m = re.search(r"(?m)^NUM_WPM\s*=\s*(\d+)", SOURCE_VARS.read_text(encoding="utf-8"))
        if m:
            num_wpm = min(int(m.group(1)), 10)

    result: dict[tuple[frozenset, str], str] = {}
    for line in text.splitlines():
        if "digitCode(key)" not in line or "workspace" not in line:
            continue
        m = re.match(r"\s*hl\.bind\(\s*(.+?)\s*,\s*(.+?)\s*\)", line)
        if not m:
            continue
        key_expr, action_expr = m.group(1), m.group(2)
        mods = set()
        if "mainMod" in key_expr or "SUPER" in key_expr:
            mods.add("SUPER")
        if "CONTROL" in key_expr or "CTRL" in key_expr:
            mods.add("CTRL")
        for name in ("SHIFT", "ALT"):
            if name in key_expr:
                mods.add(name)
        for i in range(1, num_wpm + 1):
            d = i % 10
            code = f"code:{19 if d == 0 else 9 + d}"
            action = re.sub(r"\bi\b", str(i), action_expr)
            action = action.replace('"m~" .. ' + str(i), f'"m~{i}"')
            parts = re.findall(r'"([^"]*)"', action)
            readable = "".join(parts) if parts else action
            result[(frozenset(mods), code)] = readable
    return result


def enriched_binds() -> list[dict[str, Any]]:
    """Atajos en runtime enriquecidos con la acción legible de binds.lua cuando existe."""
    # AUDITORÍA: emparejar por el último token causaba 44 falsos positivos
    # (todos los binds por código terminaban en la misma clave truncada).
    # Ahora se indexa por la CLAVE COMPLETA normalizada y se deduplican los
    # atajos idénticos que hyprctl puede repetir.
    source: dict[str, dict[str, str]] = {}
    for sb in parse_source_binds():
        k = normalize_key(sb["key"])
        old = source.get(k)
        # Si la misma tecla tiene varios binds, preferir el de workspace:
        # en esta config hay binds de monitor y de workspace con la misma
        # combinación y el primero ocultaba al otro.
        if old is None or ("workspace" in sb["action"].lower()
                           and "workspace" not in old["action"].lower()):
            source[k] = sb
    loops = expand_workspace_loops()

    seen: set[tuple] = set()
    result = []
    for b in list_binds():
        label = f"{b['mods']} + {b['key']}" if b["mods"] and b["mods"] != "(sin modifier)" else b["key"]
        signature = (label, b["dispatcher"], b["arg"])
        if signature in seen:
            continue
        seen.add(signature)

        b["dispatcher_name"] = re.sub(r"^HL\.Dispatcher\(([^)]+)\).*$", r"\1", b["dispatcher"])
        match = source.get(normalize_key(label))
        b["source_action"] = match["action"] if match else ""
        b["source_key"] = match["key"] if match else label

        # Los binds de workspace de los bucles se resolvían contra la primera
        # clave code:N (monitor=VGA-1). La expansión acotada corrige eso.
        if b["key"].startswith("code:") and b["dispatcher_name"] in {"focus", "move"}:
            mods_set = frozenset(t for t in b["mods"].split(" + ") if t)
            override = loops.get((mods_set, b["key"]))
            if override:
                b["source_action"] = override
        b["label"] = label
        result.append(b)
    return result


def action_from_ui(choice: int, param: str) -> tuple[str, str]:
    """Traduce una opción legible de la GUI a (kind, acción Lua).

    AUDITORÍA: el usuario nunca escribe Lua para las acciones habituales;
    sólo la opción "avanzada" permite una expresión cruda.
    """
    p = param.strip().replace('"', '\\"')
    options = {
        0: ("exec", f'hl.dsp.exec_cmd("{p}")'),
        1: ("lua", "hl.dsp.window.close()"),
        2: ("lua", 'hl.dsp.window.float({ action = "toggle" })'),
        3: ("lua", "hl.dsp.window.fullscreen()"),
        4: ("exec", f'hl.dsp.exec_cmd("noctalia msg {p}")'),
        5: ("lua", param.strip()),
    }
    return options.get(choice, options[0])


def action_to_ui(action: str) -> tuple[int, str]:
    """Convierte una acción existente en (índice de opción, parámetro)."""
    a = action.strip()
    m = re.search(r'hl\.dsp\.exec_cmd\("?noctalia msg ([^")]+)"?\)', a)
    if m:
        return 4, m.group(1).strip()
    m = re.search(r'hl\.dsp\.exec_cmd\("([^"]*)"\)', a)
    if m:
        return 0, m.group(1)
    if "window.close" in a:
        return 1, ""
    if "window.float" in a:
        return 2, ""
    if "fullscreen" in a:
        return 3, ""
    return 5, a


def normalize_key(key: str) -> str:
    """Clave canónica para comparar solapes (ordena modificadores y baja a minúsculas)."""
    parts = [p.strip().lower() for p in (key or "").split("+") if p.strip()]
    return "+".join(sorted(parts))


def _workspace_label(expr: str) -> str:
    """Traduce el destino de un workspace a texto legible."""
    m = re.search(r'workspace\s*=\s*"([^"]+)"', expr) or re.search(r"workspace\s*=\s*(\d+)", expr)
    target = (m.group(1) if m else "") or "otro"
    table = {"m+1": "siguiente", "m-1": "anterior", "emptym": "vacío",
             "special": "especial", "e+1": "siguiente", "e-1": "anterior"}
    if target in table:
        return table[target]
    mm = re.match(r"m~(\d+)$", target)
    if mm:
        return f"{mm.group(1)} de este monitor"
    return f"{target}"


def describe(action: str, dispatcher: str = "") -> tuple[str, str]:
    """Devuelve (categoría, descripción legible) de una acción Lua/exec.

    Acepta tanto el texto de binds.lua como el dispatcher opaco de hyprctl
    ('HL.Dispatcher(close) 10'), para que NINGÚN atajo diga sólo "ejecutar".
    """
    a = (action or "").strip()
    low = a.lower()
    if not a and dispatcher:
        a = dispatcher
        low = a.lower()

    # Dispatchers de hyprctl (cuando no hay texto fuente disponible).
    disp_table = {
        "close": ("Ventanas", "Cerrar la ventana activa"),
        "float": ("Ventanas", "Alternar ventana flotante"),
        "fullscreen": ("Ventanas", "Alternar pantalla completa"),
        "focus": ("Ventanas", "Mover el foco de ventana"),
        "layout": ("Ventanas", "Cambiar la disposición (split)"),
        "cycle_next": ("Ventanas", "Pasar a la siguiente ventana"),
        "workspace": ("Workspaces", "Cambiar de workspace"),
        "movetoworkspace": ("Workspaces", "Mover ventana a otro workspace"),
        "exec_cmd": ("Otros", "Ejecutar una acción"),
        "kill": ("Sesión", "Cerrar Hyprland"),
    }
    m = re.match(r"HL\.Dispatcher\(([^)]+)\)", a)
    if m and m.group(1) in disp_table:
        return disp_table[m.group(1)]
    if "noctalia msg" in low:
        msg = low.split("noctalia msg", 1)[-1].strip().strip('"')
        table = {
            "window-switcher": ("Ventanas", "Cambiar de ventana"),
            "settings-toggle": ("Sistema", "Abrir ajustes del sistema"),
            "panel-toggle launcher": ("Launcher", "Abrir el launcher"),
            "panel-toggle clipboard": ("Utilidades", "Abrir portapapeles"),
            "panel-toggle control-center": ("Sistema", "Abrir centro de control"),
            "panel-toggle session": ("Sesión", "Menú de sesión"),
            "panel-toggle wallpaper": ("Wallpapers", "Selector de wallpaper"),
            "volume-up": ("Multimedia", "Subir volumen"),
            "volume-down": ("Multimedia", "Bajar volumen"),
            "volume-mute": ("Multimedia", "Silenciar"),
            "brightness-up": ("Sistema", "Subir brillo"),
            "brightness-down": ("Sistema", "Bajar brillo"),
            "screenshot-region": ("Capturas", "Capturar una región"),
            "screenshot-fullscreen": ("Capturas", "Capturar pantalla completa"),
            "session lock": ("Sesión", "Bloquear la sesión"),
            "media toggle": ("Multimedia", "Reproducir / pausar"),
        }
        for k, v in table.items():
            if msg.startswith(k):
                return v
        return ("Noctalia", f"Enviar a Noctalia: {msg[:40]}")

    # Comando en texto plano (p. ej. 'uwsm app -- firefox' desde binds.lua).
    if a and not a.startswith("hl.") and "HL.Dispatcher" not in a:
        cmd = a.replace("uwsm app -- ", "").strip()
        table = {
            "hyprctl kill": ("Sesión", "Cerrar Hyprland"),
            "kitty": ("Launcher", "Abrir terminal (kitty)"),
            "alacritty": ("Launcher", "Abrir terminal (Alacritty)"),
            "dolphin": ("Launcher", "Abrir gestor de archivos (Dolphin)"),
            "firefox": ("Launcher", "Abrir navegador (Firefox)"),
            "gnome-text-editor": ("Launcher", "Abrir editor de texto"),
            "gnome-calculator": ("Utilidades", "Abrir calculadora"),
            "btop": ("Utilidades", "Abrir monitor de recursos"),
            "swash": ("Capturas", "Capturar pantalla (Swash)"),
        }
        for k, v in table.items():
            if cmd.lower().startswith(k):
                return v
        return ("Launcher", "Ejecutar: " + cmd[:45])

    # Workspaces: los atajos del usuario usan focus({workspace=...}) y
    # window.move({workspace=...}), no un dispatcher llamado "workspace".
    if "workspace.toggle_special" in low:
        return ("Workspaces", "Alternar workspace especial (scratchpad)")
    if "focus" in low and "workspace" in low:
        return ("Workspaces", "Ir al workspace " + _workspace_label(a))
    if "window.move" in low and "workspace" in low:
        return ("Workspaces", "Mover ventana al workspace " + _workspace_label(a))

    # Movimiento de ventana por dirección (no es cambio de monitor).
    if "window.move" in low and "direction" in low:
        d = re.search(r'direction\s*=\s*"([^"]+)"', a)
        dirs = {"u": "arriba", "d": "abajo", "l": "a la izquierda", "r": "a la derecha"}
        return ("Ventanas", "Mover ventana hacia " + dirs.get(d.group(1) if d else "", "otro lado"))

    # Expresiones Lua crudas que aparecen en binds.lua.
    if "window.move" in low:
        mon = re.search(r'monitor\s*=\s*"([^"]+)"', a)
        target = mon.group(1) if mon else "otro monitor"
        pretty = {"-1": "anterior", "+1": "siguiente"}.get(target, target)
        return ("Workspaces", f"Mover ventana al monitor {pretty}")
    if "layout" in low:
        return ("Ventanas", "Alternar la disposición (split)")
    if "window.drag" in low:
        return ("Ventanas", "Arrastrar ventana con el ratón")
    if "window.resize" in low:
        return ("Ventanas", "Redimensionar ventana con el ratón")
    if "dsp.workspace" in low or "workspace.toggle" in low:
        return ("Workspaces", "Alternar workspace especial")
    if "window.close" in low:
        return ("Ventanas", "Cerrar la ventana activa")
    if "window.fullscreen" in low:
        return ("Ventanas", "Alternar pantalla completa")
    if "dsp.window.float" in low or "togglefloating" in low:
        return ("Ventanas", "Alternar ventana flotante")
    if "kill" in low and "hyprctl" in low:
        return ("Sesión", "Cerrar Hyprland")
    if "workspace" in low:
        return ("Workspaces", "Cambiar de workspace")
    if "focus" in low or "cyclenext" in low:
        return ("Ventanas", "Cambiar el foco de ventana")
    # Comando real dentro de hl.dsp.exec_cmd("..."): nunca dejarlo genérico.
    m = re.search(r'hl\.dsp\.exec_cmd\("([^"]*)"\)', a)
    if m:
        cmd = m.group(1).strip()
        if cmd.startswith("uwsm app -- "):
            cmd = cmd[len("uwsm app -- "):]
        pref = {
            "hyprctl kill": ("Sesión", "Cerrar Hyprland"),
            "kitty": ("Launcher", "Abrir terminal (kitty)"),
            "alacritty": ("Launcher", "Abrir terminal (Alacritty)"),
            "dolphin": ("Launcher", "Abrir gestor de archivos (Dolphin)"),
            "firefox": ("Launcher", "Abrir navegador (Firefox)"),
            "gnome-text-editor": ("Launcher", "Abrir editor de texto"),
            "gnome-calculator": ("Utilidades", "Abrir calculadora"),
            "btop": ("Utilidades", "Abrir monitor de recursos"),
            "swash": ("Capturas", "Capturar pantalla (Swash)"),
        }
        for k, v in pref.items():
            if cmd.lower().startswith(k):
                return v
        return ("Launcher", "Ejecutar: " + cmd[:45])
    if "exec_cmd" in low:
        return ("Otros", "Ejecutar una acción")
    return ("Otros", a[:50])


def check_conflict(key: str, exclude: str = "") -> list[dict[str, str]]:
    """Busca atajos que se solapan con `key` (excluyendo uno por su clave exacta)."""
    target = normalize_key(key)
    if not target:
        return []
    found: list[dict[str, str]] = []
    for b in enriched_binds():
        candidate = b.get("source_key") or f"{b['mods']} + {b['key']}"
        if exclude and normalize_key(exclude) == normalize_key(candidate):
            continue
        if normalize_key(candidate) == target:
            found.append({"key": candidate, "description": b.get("source_action", b["dispatcher"])[:60]})
    for e in stored():
        if e.get("disabled") or e.get("suppression"):
            continue
        if normalize_key(e.get("key", "")) == target:
            found.append({"key": e["key"], "description": e.get("description", "atajo guardado")})
    return found


def notify_info(title: str, text: str) -> None:
    """Notificación informativa de escritorio (notify-send con fallback)."""
    for cmd in (["notify-send", title, text], ["noctalia", "msg", "notify", text]):
        try:
            subprocess.run(cmd, capture_output=True, timeout=5)
            return
        except (OSError, subprocess.SubprocessError):
            continue


def notify_conflict(key: str, matches: list[dict[str, str]]) -> None:
    """Notificación de escritorio al detectar un solape."""
    desc = "; ".join(f"{m['key']} ({m['description']})" for m in matches[:2])
    text = f"El atajo {key} ya está asignado a: {desc}"
    for cmd in (["notify-send", "-u", "critical", "Ricing HGUI · Conflicto", text],
                ["noctalia", "msg", "notify", text]):
        try:
            subprocess.run(cmd, capture_output=True, timeout=5)
            return
        except (OSError, subprocess.SubprocessError):
            continue


def stored() -> list[dict[str, str]]:
    if DATA.exists():
        try:
            return json.loads(DATA.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return []
    return []


def _write_stored(entries: list[dict[str, str]]) -> None:
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
    _generate_lua(entries)


def _lua_action(kind: str, action: str) -> str:
    if kind == "exec":
        escaped = action.replace("\\", "\\\\").replace('"', '\\"')
        return f'hl.dsp.exec_cmd("{escaped}")'
    return action  # expresión Lua cruda, p. ej. hl.dsp.window.close()


def apply_bind(entry: dict[str, str]) -> tuple[bool, str]:
    """Aplica un atajo en vivo; si old_key existe, desvincula primero."""
    old = (entry.get("old_key") or "").strip()
    if old:
        esc = old.replace("\\", "\\\\").replace('"', '\\"')
        hyprctl("eval", f'hl.unbind("{esc}")')
    key = entry["key"].replace("\\", "\\\\").replace('"', '\\"')
    action = _lua_action(entry.get("kind", "exec"), entry.get("action", ""))
    flags = []
    if entry.get("repeat"):
        flags.append("repeat = true")
    if entry.get("locked"):
        flags.append("locked = true")
    opts = ", { " + ", ".join(flags) + " }" if flags else ""
    res = hyprctl("eval", f'hl.bind("{key}", {action}{opts})')
    return (res.strip().lower() == "ok"), res.strip() or "sin respuesta"


def add_or_update(entry: dict[str, str]) -> tuple[bool, str]:
    ok, msg = apply_bind(entry)
    if not ok:
        return False, msg
    entries = stored()
    key = entry["key"]
    entries = [e for e in entries if e.get("key") != key and e.get("old_key") != key]
    entries.append(entry)
    _write_stored(entries)
    return True, "atajo aplicado y guardado"


def set_disabled(key: str, disabled: bool) -> tuple[bool, str]:
    """Desactiva un atajo sin borrarlo (o lo reactiva)."""
    entries = stored()
    entry = next((e for e in entries if e.get("key") == key), None)
    if disabled:
        # Quitar el bind en vivo; conservar el entry para poder reactivarlo.
        esc = key.replace("\\", "\\\\").replace('"', '\\"')
        res = hyprctl("eval", f'hl.unbind("{esc}")')
        if entry:
            entry["disabled"] = True
        else:
            entry = {"key": key, "kind": "exec", "action": "", "description": "desactivado",
                     "repeat": False, "locked": False, "disabled": True}
            entries.append(entry)
        _write_stored(entries)
        return True, "atajo desactivado (conservado)"
    # Reactivar: necesita una acción guardada.
    if not entry or not entry.get("action"):
        return False, "no hay acción guardada para reactivar; vuelve a crear el atajo"
    entry["disabled"] = False
    _write_stored(entries)
    return apply_bind(entry)


def delete(key: str) -> tuple[bool, str]:
    """Elimina el atajo en vivo y guarda una supresión para que no reaparezca al reiniciar."""
    esc = key.replace("\\", "\\\\").replace('"', '\\"')
    res = hyprctl("eval", f'hl.unbind("{esc}")')
    entries = [e for e in stored() if e.get("key") != key]
    # Si el atajo venía de binds.lua, necesitamos un hl.unbind persistente.
    entries.append({"key": key, "kind": "exec", "action": "", "description": "eliminado",
                    "repeat": False, "locked": False, "disabled": True,
                    "old_key": key, "suppression": True})
    _write_stored(entries)
    return res.strip().lower() == "ok", res.strip() or "eliminado"


def _generate_lua(entries: list[dict[str, str]]) -> None:
    lines = [
        "-- Generado por Ricing HGUI. NO EDITAR A MANO.",
        "-- Añadir `require(\"config.ui-bindings\")` en hyprland.lua tras los binds habituales.",
        "",
    ]
    for i, e in enumerate(entries, 1):
        old = e.get("old_key", "")
        lines.append(f"-- [{i}] {e.get('description', '') or e['key']}")
        # Un atajo desactivado/eliminado se representa sólo con hl.unbind.
        if e.get("disabled") or not e.get("action"):
            target = old or e["key"]
            lines.append(f'hl.unbind("{target}")  -- desactivado/eliminado')
            lines.append("")
            continue
        if old:
            lines.append(f'hl.unbind("{old}")')
        lines.append(f'hl.bind("{e["key"]}", {_lua_action(e.get("kind", "exec"), e.get("action", ""))})')
        lines.append("")
    LUA_MODULE.parent.mkdir(parents=True, exist_ok=True)
    LUA_MODULE.write_text("\n".join(lines) + "\n", encoding="utf-8")
