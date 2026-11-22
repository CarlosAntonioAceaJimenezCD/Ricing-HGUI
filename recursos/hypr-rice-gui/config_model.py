#!/usr/bin/env python3
"""Modelo declarativo de opciones de configuración para Ricing HGUI.

Cada opción define: ruta real, tipo, rango/valores, si es toggle o intensidad,
cómo se aplica en vivo y dónde se persiste. La GUI se genera desde este modelo,
así añadir una opción nueva no requiere reescribir widgets.
"""
from __future__ import annotations

import json
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
def by_id(option_id: str) -> Option:
    return next(o for o in OPTIONS if o.id == option_id)


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
        return str(v)
    return '"' + str(v).replace('"', '\\"') + '"'


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
        if opt.source != "hyprland" or value is None:
            continue
        tree = _deep_merge(tree, _nest(opt.path, value))
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
        if value is None:
            continue
        (noct_values if opt.source == "noctalia" else hypr_values)[oid] = value

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
    text = NOCTALIA_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()
    for oid, value in values.items():
        opt = by_id(oid)
        section, _, key = opt.path.rpartition(".")
        header = f"[{section}]"
        try:
            start = lines.index(header)
        except ValueError:
            continue
        end = next((i for i in range(start + 1, len(lines))
                    if lines[i].startswith("[")), len(lines))
        for i in range(start + 1, end):
            if re.match(rf"^\s*{re.escape(key)}\s*=", lines[i]):
                lines[i] = f"{key} = {_toml_value(value)}"
                break
    NOCTALIA_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _toml_value(v: Any) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, str):
        return f'"{v}"'
    return str(v)


def snapshot() -> dict[str, Any]:
    return {o.id: get_value(o) for o in OPTIONS}
