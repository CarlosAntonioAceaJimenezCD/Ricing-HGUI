#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · config_model.py — única fuente de verdad de las opciones
# -----------------------------------------------------------------------------
# Cada Option declara su ruta REAL (path), tipo, rango y origen. La GUI genera
# los widgets desde esta lista; no hay controles escritos a mano.
# Efectos externos:
#   - lectura: `hyprctl getoption` y ~/.config/noctalia/config.toml (tomllib);
#   - aplicación en vivo: `hyprctl eval "hl.config({...})"` (API Lua de 0.57;
#     `hyprctl keyword` está obsoleto y devuelve "unknown request");
#   - persistencia: ~/.config/hypr/config/ui-settings.lua y config.toml.
# Invariantes: los IDs son únicos; `by_id` devuelve None si no existe (nunca
# lanza excepciones que puedan romper el bucle de eventos de GTK).
# =============================================================================
"""Modelo declarativo de opciones de configuración para Ricing HGUI.

Cada opción define: ruta real, tipo, rango/valores, si es toggle o intensidad,
cómo se aplica en vivo y dónde se persiste. La GUI se genera desde este modelo,
así añadir una opción nueva no requiere reescribir widgets.
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

HOME = Path.home()
STATE_FILE = HOME / ".config/hypr/config/ui-settings.lua"
NOCTALIA_FILE = HOME / ".config/noctalia/config.toml"


@dataclass(frozen=True)
class Option:
    id: str
    label: str
    path: str                      # ruta real: decoration.blur.size
    kind: str                      # bool | int | float | enum | color
    category: str                  #Apariencia, Blur, Entrada, …
    source: str = "hyprland"       # hyprland | noctalia
    minimum: float | None = None
    maximum: float | None = None
    step: float = 1
    choices: tuple[str, ...] = ()
    live: bool = True
    note: str = ""

    @property
    def is_intensity(self) -> bool:
        return self.kind in {"int", "float", "color"}

    @property
    def control(self) -> str:
        if self.kind == "bool":
            return "switch"
        if self.kind == "enum":
            return "combo"
        if self.kind == "color":
            return "color"
        return "slider"


# --------------------------------------------------------------------------- catálogo
OPTIONS: list[Option] = [
    # --- General ---
    Option("gaps_in", "Gaps internos", "general.gaps_in", "int", "General", minimum=0, maximum=100, note="Espacio entre ventanas"),
    Option("gaps_out", "Gaps externos", "general.gaps_out", "int", "General", minimum=0, maximum=100, note="Espacio hasta el borde de pantalla"),
    Option("border_size", "Grosor del borde", "general.border_size", "int", "General", minimum=0, maximum=20),
    Option("extend_border_grab_area", "Área de agarre extendida", "general.extend_border_grab_area", "int", "General", minimum=0, maximum=50, note="0 desactiva el resize por borde"),
    Option("resize_on_border", "Redimensionar por borde", "general.resize_on_border", "bool", "General"),

    # --- Decoración ---
    Option("rounding", "Redondeo", "decoration.rounding", "int", "Decoración", minimum=0, maximum=100),
    Option("dim_special", "Atenuar workspace especial", "decoration.dim_special", "float", "Decoración", minimum=0, maximum=1, step=0.05),
    Option("active_opacity", "Opacidad activa", "decoration.active_opacity", "float", "Decoración", minimum=0, maximum=1, step=0.05),
    Option("inactive_opacity", "Opacidad inactiva", "decoration.inactive_opacity", "float", "Decoración", minimum=0, maximum=1, step=0.05),
    Option("fullscreen_opacity", "Opacidad en pantalla completa", "decoration.fullscreen_opacity", "float", "Decoración", minimum=0, maximum=1, step=0.05),

    # --- Blur (intensidad) ---
    Option("blur_enabled", "Blur activado", "decoration.blur.enabled", "bool", "Blur"),
    Option("blur_size", "Tamaño del blur", "decoration.blur.size", "int", "Blur", minimum=1, maximum=50, note="Requiere al menos 1"),
    Option("blur_passes", "Pasadas del blur", "decoration.blur.passes", "int", "Blur", minimum=1, maximum=10, note="Más pasadas = más GPU"),
    Option("blur_brightness", "Brillo del blur", "decoration.blur.brightness", "float", "Blur", minimum=0, maximum=2, step=0.05),
    Option("blur_contrast", "Contraste del blur", "decoration.blur.contrast", "float", "Blur", minimum=0, maximum=2, step=0.05),
    Option("blur_vibrancy", "Vibrancia del blur", "decoration.blur.vibrancy", "float", "Blur", minimum=0, maximum=1, step=0.05),
    Option("blur_special", "Blur en workspace especial", "decoration.blur.special", "bool", "Blur", note="Costoso"),
    Option("blur_xray", "Blur xray", "decoration.blur.xray", "bool", "Blur", note="Reduce coste en flotantes"),
    Option("blur_popups", "Blur en popups", "decoration.blur.popups", "bool", "Blur"),
    Option("blur_proportional", "Blur proporcional", "decoration.blur.proportional", "bool", "Blur", note="0.57: requiere render:use_shader_blur_blend"),
    Option("blur_new_optimizations", "Optimizaciones del blur", "decoration.blur.new_optimizations", "bool", "Blur", note="Recomendado dejar activado"),
    Option("blur_ignore_opacity", "Blur ignora opacidad", "decoration.blur.ignore_opacity", "bool", "Blur"),
    Option("blur_input_methods", "Blur en métodos de entrada", "decoration.blur.input_methods", "bool", "Blur"),
    Option("blur_variant", "Variante del blur", "decoration.blur.variant", "int", "Blur", minimum=0, maximum=3, note="0 kawase · 1 acrylic · 2 aurora (según versión)"),
    Option("use_shader_blur_blend", "Shader blur blend", "render.use_shader_blur_blend", "bool", "Blur", note="Requerido por blur proporcional en 0.57"),
    Option("no_hardware_cursors", "Cursores por software", "cursor.no_hardware_cursors", "int", "Entrada", minimum=0, maximum=2),

    # --- Entrada / cursor ---
    Option("sensitivity", "Sensibilidad del ratón", "input.sensitivity", "float", "Entrada", minimum=-1, maximum=1, step=0.05),
    Option("accel_profile", "Perfil de aceleración", "input.accel_profile", "enum", "Entrada", choices=("flat", "adaptive", "none")),
    Option("zoom_factor", "Zoom del cursor", "cursor.zoom_factor", "float", "Entrada", minimum=1, maximum=3, step=0.1),

    # --- Comportamiento ---
    Option("vrr", "Modo VRR", "misc.vrr", "enum", "Comportamiento", choices=("0", "1", "2", "3"), note="0 off · 1 on · 2 fullscreen · 3 fullscreen+video/game"),
    Option("middle_click_paste", "Pegar con botón medio", "misc.middle_click_paste", "bool", "Comportamiento"),
    Option("enable_swallow", "Swallow de terminal", "misc.enable_swallow", "bool", "Comportamiento"),
    Option("direct_scanout", "Direct scanout", "render.direct_scanout", "enum", "Comportamiento", choices=("0", "1", "2")),
    Option("force_zero_scaling", "Force zero scaling (XWayland)", "xwayland.force_zero_scaling", "bool", "Comportamiento"),
    Option("preserve_split", "Preservar split (dwindle)", "dwindle.preserve_split", "bool", "Comportamiento"),
    Option("no_update_news", "Sin noticias de actualización", "ecosystem.no_update_news", "bool", "Comportamiento"),
    Option("no_donation_nag", "Sin aviso de donaciones", "ecosystem.no_donation_nag", "bool", "Comportamiento"),

    # --- Noctalia (se escriben en config.toml; no se aplican en vivo) ---
    Option("n_ui_scale", "Escala de UI", "accessibility.ui_scale", "float", "Noctalia", source="noctalia", minimum=0.5, maximum=2, step=0.05, live=False),
    Option("n_bar_thickness", "Grosor de barra", "bar.default.thickness", "int", "Noctalia", source="noctalia", minimum=20, maximum=80, live=False),
    Option("n_bar_scale", "Escala de barra", "bar.default.scale", "float", "Noctalia", source="noctalia", minimum=0.5, maximum=2, step=0.05, live=False),
    Option("n_bar_radius", "Radio inferior de barra", "bar.default.radius_bottom_left", "int", "Noctalia", source="noctalia", minimum=0, maximum=40, live=False),
    Option("n_bar_concave", "Esquinas cóncavas", "bar.default.concave_edge_corners", "bool", "Noctalia", source="noctalia", live=False),
    Option("n_theme_mode", "Modo del tema", "theme.mode", "enum", "Noctalia", source="noctalia", choices=("dark", "light"), live=False),
    Option("n_theme_scheme", "Esquema de color", "theme.wallpaper_scheme", "enum", "Noctalia", source="noctalia",
           choices=("m3-tonal-spot", "m3-vibrant", "m3-expressive", "m3-neutral", "m3-monochrome"), live=False,
           note="Los esquemas disponibles dependen de la versión de Noctalia"),
    Option("n_pill_scale", "Escala de pills de workspace", "widget.workspaces.pill_scale", "float", "Noctalia", source="noctalia", minimum=0.5, maximum=2, step=0.05, live=False),
    Option("n_show_labels", "Etiquetas de workspace", "widget.workspaces.show_labels", "bool", "Noctalia", source="noctalia", live=False),
]


# --------------------------------------------------------------------------- utilidades
def by_id(option_id: str) -> Option | None:
    """Devuelve la opción o None si el ID no existe (nunca lanza StopIteration)."""
    return next((o for o in OPTIONS if o.id == option_id), None)


def categories() -> dict[str, list[Option]]:
    out: dict[str, list[Option]] = {}
    for o in OPTIONS:
        out.setdefault(o.category, []).append(o)
    return out


def _hypr_path(path: str) -> str:
    return path.replace(".", ":")


def get_value(opt: Option) -> Any:
    if opt.source == "noctalia":
        try:
            data = tomllib.loads(NOCTALIA_FILE.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            return None
        node: Any = data
        for part in opt.path.split("."):
            if not isinstance(node, dict) or part not in node:
                return None
            node = node[part]
        return node

    try:
        out = subprocess.run(["hyprctl", "getoption", _hypr_path(opt.path)],
                             capture_output=True, text=True, timeout=5).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None
    first = out.splitlines()[0] if out else ""
    m = re.search(r"^(?:int|float|bool|str):\s*(.+)$", first)
    if m:
        raw = m.group(1).strip()
    else:
        m = re.search(r"css gap data:\s*(\d+)", first)
        if not m:
            return None
        raw = m.group(1)
    try:
        if opt.kind == "bool":
            return raw.lower() == "true"
        if opt.kind in {"int", "enum"}:
            return int(float(raw))
        if opt.kind == "float":
            return float(raw)
        return raw
    except ValueError:
        return None


def _nest(path: str, value: Any) -> dict:
    node: Any = value
    for part in reversed(path.split(".")):
        node = {part: node}
    return node


def _deep_merge(a: dict, b: dict) -> dict:
    out = dict(a)
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def _lua_value(v: Any) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        # AUDITORÍA: NaN/Infinity no existen en Lua: `active_opacity = nan`
        # rompía hl.config y, con él, la sesión completa al recargar.
        return str(v) if math.isfinite(v) else "0"
    s = str(v if v is not None else "")
    return ('"' + s.replace("\\", "\\\\").replace('"', '\\"')
            .replace("\r", "\\r").replace("\n", "\\n").replace("\t", "\\t") + '"')


def clean_value(opt: Option | None, value: Any) -> Any:
    """Sanea un valor según la declaración de la opción (rango/tipo/enum).

    AUDITORÍA: la GUI usa sliders/combos, pero un JSON editado a mano, un
    valor NaN o un enum inesperado podían generar Lua inválido. Se recorta al
    rango declarado y se descartan los enums desconocidos (None = omitir).
    """
    if opt is None or value is None:
        return None
    try:
        if opt.kind == "bool":
            if isinstance(value, str):
                return value.strip().lower() in {"1", "true", "yes", "on"}
            return bool(value)
        if opt.kind in {"int", "float"}:
            n = float(value)
            if not math.isfinite(n):
                n = float(opt.minimum if opt.minimum is not None else 0)
            if opt.minimum is not None:
                n = max(n, float(opt.minimum))
            if opt.maximum is not None:
                n = min(n, float(opt.maximum))
            return int(n) if opt.kind == "int" else n
        if opt.kind == "enum":
            s = str(value)
            return s if (not opt.choices or s in opt.choices) else None
        s = str(value)
        return s.replace("\n", " ").replace("\r", " ").replace("\0", "")
    except (TypeError, ValueError, OverflowError):
        return None


def _lua_table(d: dict, indent: int = 0) -> str:
    lines = []
    pad = "  " * indent
    for k, v in d.items():
        if isinstance(v, dict):
            lines.append(f"{pad}{k} = {{\n{_lua_table(v, indent + 1)}{pad}}},")
        else:
            lines.append(f"{pad}{k} = {_lua_value(v)},")
    return "\n".join(lines)


def build_hypr_config(values: dict[str, Any]) -> str:
    """Devuelve el código Lua hl.config({...}) para las opciones Hyprland dadas."""
    tree: dict = {}
    for oid, value in values.items():
        opt = by_id(oid)
        if opt is None or opt.source != "hyprland":
            continue
        clean = clean_value(opt, value)
        if clean is None:
            continue
        tree = _deep_merge(tree, _nest(opt.path, clean))
    return "hl.config({\n" + _lua_table(tree, 1) + "\n})"


def apply_live(values: dict[str, Any]) -> str:
    code = build_hypr_config(values)
    if code.strip() == "hl.config({\n\n})":
        return ""
    try:
        return subprocess.run(["hyprctl", "eval", code], capture_output=True,
                              text=True, timeout=5).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return ""


def persist(values: dict[str, Any]) -> None:
    """Guarda TODAS las opciones en sus archivos (ui-settings.lua, config.toml)."""
    hypr_values = {}
    noct_values = {}
    for oid, value in values.items():
        opt = by_id(oid)
        clean = clean_value(opt, value)
        if opt is None or clean is None:
            continue
        (noct_values if opt.source == "noctalia" else hypr_values)[oid] = clean

    if hypr_values:
        tree: dict = {}
        for oid, value in hypr_values.items():
            tree = _deep_merge(tree, _nest(by_id(oid).path, value))
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        STATE_FILE.write_text(
            "-- Generado por Ricing HGUI. NO EDITAR A MANO.\n"
            "return {\n" + _lua_table(tree, 1) + "\n}\n",
            encoding="utf-8",
        )
    if noct_values:
        _persist_noctalia(noct_values)


def _persist_noctalia(values: dict[str, Any]) -> None:
    """Actualiza config.toml sin borrar secciones ajenas.

    AUDITORÍA: antes fallaba con FileNotFoundError si Noctalia no estaba
    instalado y sólo reemplazaba claves ya existentes. Ahora crea la sección
    y/o la clave cuando faltan y nunca lanza excepciones a la GUI.
    """
    try:
        lines = NOCTALIA_FILE.read_text(encoding="utf-8").splitlines() if NOCTALIA_FILE.exists() else []
    except OSError:
        return
    for oid, value in values.items():
        opt = by_id(oid)
        if opt is None:
            continue
        section, _, key = opt.path.rpartition(".")
        if not section or not key:
            continue
        header = f"[{section}]"
        try:
            start = lines.index(header)
        except ValueError:
            lines += ["", header]
            start = len(lines) - 1
        end = next((i for i in range(start + 1, len(lines))
                    if lines[i].lstrip().startswith("[")), len(lines))
        for i in range(start + 1, end):
            if re.match(rf"^\s*{re.escape(key)}\s*=", lines[i]):
                lines[i] = f"{key} = {_toml_value(value)}"
                break
        else:
            lines.insert(end, f"{key} = {_toml_value(value)}")
    try:
        NOCTALIA_FILE.parent.mkdir(parents=True, exist_ok=True)
        NOCTALIA_FILE.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    except OSError:
        pass


def _toml_value(v: Any) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, str):
        esc = (v.replace("\\", "\\\\").replace('"', '\\"')
               .replace("\n", "\\n").replace("\r", "\\r"))
        return f'"{esc}"'
    return str(v)


def snapshot() -> dict[str, Any]:
    """Lee TODAS las opciones de una vez.

    AUDITORÍA / OPTIMIZACIÓN: antes se hacía un `hyprctl getoption` por opción
    (46 subprocesses, ~280 ms medidos). Ahora se usa un único `hyprctl -j
    --batch` y se lee el TOML de Noctalia una sola vez (~10 ms medidos).
    El formato devuelto por --batch es un objeto JSON por línea con clave
    "option" y el valor tipado ("int", "float", "bool", "str", "css"...).
    """
    hypr_opts = [o for o in OPTIONS if o.source == "hyprland"]
    cmd = ";".join(f"getoption {_hypr_path(o.path)}" for o in hypr_opts)
    try:
        raw = subprocess.run(["hyprctl", "-j", "--batch", cmd], capture_output=True,
                             text=True, timeout=12).stdout
    except (OSError, subprocess.SubprocessError):
        raw = ""

    by_path: dict[str, Any] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        path = obj.get("option")
        if not path:
            continue
        # normalizar ':' del path devuelto al formato con puntos del modelo
        key = path.replace(":", ".")
        try:
            if "int" in obj:
                by_path[key] = int(obj["int"])
            elif "float" in obj:
                by_path[key] = float(obj["float"])
            elif "bool" in obj:
                by_path[key] = bool(obj["bool"])
            elif "str" in obj:
                by_path[key] = obj["str"]
            elif "css" in obj:
                nums = re.findall(r"-?\d+", str(obj["css"]))
                by_path[key] = int(nums[0]) if nums else 0
        except (TypeError, ValueError, OverflowError):
            continue

    # Noctalia: una sola lectura/escritura del TOML para todas sus opciones.
    noct_data: dict[str, Any] = {}
    noct_opts = [o for o in OPTIONS if o.source == "noctalia"]
    if noct_opts:
        try:
            noct_data = tomllib.loads(NOCTALIA_FILE.read_text(encoding="utf-8"))
        except (OSError, tomllib.TOMLDecodeError):
            noct_data = {}

    result: dict[str, Any] = {}
    for o in OPTIONS:
        if o.source == "hyprland":
            result[o.id] = by_path.get(o.path)
        else:
            node: Any = noct_data
            for part in o.path.split("."):
                if not isinstance(node, dict) or part not in node:
                    node = None
                    break
                node = node[part]
            result[o.id] = node
    return result
