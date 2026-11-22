# 17 · Inventario exhaustivo de opciones configurables

> Objetivo: servir de **especificación de campos** para una GUI genérica de ricing.
> Se inventarían todas las opciones *presentes* (activas o comentadas) en los dotfiles
> del usuario, con su valor real, tipo, rango oficial cuando existe y la ruta para
> modificarla en vivo. No se propone diseño de GUI salvo en las columnas de control
> sugerido y en las secciones 3-5.

## 0. Convenciones, fuentes y ámbito

- **[HECHO]**: valor o rango extraído directamente de un archivo de configuración o
  de la wiki oficial. **[OPINIÓN]**: sugerencia de control GUI o de modelado.
- Las rutas de configuración se dan **relativas a `../configuracion-actual/`**:
  `hypr/config/decorations.lua` = `../configuracion-actual/hypr/config/decorations.lua`.
  La ruta real en la máquina es `~/.config/hypr/config/decorations.lua`, etc.
- Fuentes citadas (todas en `../sources/`):
  [Config Options](../sources/2026-11-21-hyprland-config-options.md) ·
  [Animations](../sources/2026-11-21-hyprland-animations.md) ·
  [Window Rules](../sources/2026-11-21-hyprland-window-rules.md) ·
  [Noctalia Bar](../sources/2026-11-21-noctalia-bar.md) ·
  [Noctalia Theming](../sources/2026-11-21-noctalia-theming-index.md) ·
  [Noctalia App Theming](../sources/2026-11-21-noctalia-app-theming.md) ·
  [Perfil del sistema](../00-perfil-del-sistema.md).
- **[HECHO] Runtime:** `hl.config()` actualiza opciones en vivo; **los cambios por
  `hyprctl eval` se pierden al recargar/reiniciar** y deben persistirse en el `.lua`
  [Fuente](../sources/2026-11-21-hyprland-config-options.md). Por eso la columna
  "Ruta en vivo" es para previsualizar y la columna "Archivo/sección" es la fuente
  de verdad que la GUI debe escribir.
- **[HECHO] Sintaxis alternativa:** `hl.config({ ["category.option"] = value })` es
  equivalente a la tabla anidada [Fuente](../sources/2026-11-21-hyprland-config-options.md).
  Útil para una GUI que guarde un dict plano.
- En la columna Tipo: `bool` → Toggle; numéricos → Intensidad; colores/gradientes →
  Color; cadenas/arrays/reglas → Enum/acción. **`[HECHO]` se omite en celdas obvias
  de valor** para no saturar: la tabla entera es [HECHO] salvo la columna
  "Control GUI sugerido", que es [OPINIÓN].

---

## 1. Tabla maestra de opciones (una fila por opción)

### 1.1 Hyprland — `hl.config`, `hl.animation`, `hl.curve`, `hl.monitor` y variables

| Opción | Archivo/sección | Valor actual | Tipo | ¿Toggle o Intensidad? | Rango/valores permitidos | Ruta para set en vivo | Control GUI sugerido | Notas |
|---|---|---|---|---|---|---|---|---|
| `general.gaps_in` | hypr/config/decorations.lua | 3 | int (css_gaps) | Intensidad | ≥0, sin límite superior [HECHO] | `hyprctl eval "hl.config({general={gaps_in=3}})"` | spin | Separación entre ventanas |
| `general.gaps_out` | hypr/config/decorations.lua | 8 | int (css_gaps) | Intensidad | ≥0 | `hyprctl eval "hl.config({general={gaps_out=8}})"` | spin | Separación respecto al borde del monitor |
| `general.border_size` | hypr/config/decorations.lua | 2 | int | Intensidad | 0-20 [HECHO] | `hyprctl eval "hl.config({general={border_size=2}})"` | spin | Default wiki: 1 |
| `general.extend_border_grab_area` | hypr/config/decorations.lua | 10 | int | Intensidad | 0-100 [HECHO] | `hyprctl eval "hl.config({general={extend_border_grab_area=10}})"` | spin | Solo activo si `resize_on_border` |
| `general.resize_on_border` | hypr/config/decorations.lua | true | bool | Toggle | true/false | `hyprctl eval "hl.config({general={resize_on_border=true}})"` | switch | Redimensionar arrastrando bordes/gaps |
| `general.col.active_border.colors` | hypr/config/decorations.lua | `{CACHYLGREEN, CACHYDGREEN}` | array de color | Color | 1..N colores + `angle` [HECHO] | `hyprctl eval "hl.config({general={col={active_border={colors={'rgba(82dcccff)','rgba(007d6fff)'}}}}})"` | color (gradiente) | Gradiente activo; ver paleta en colors.lua |
| `general.col.active_border.angle` | hypr/config/decorations.lua | 45 | int | Intensidad | grados, sin rango documentado | `hyprctl eval "hl.config({general={col={active_border={angle=45}}}})"` | spin | Ángulo del gradiente |
| `general.col.inactive_border` | hypr/config/decorations.lua | `CACHYGRAY` = `rgba(798bb2ff)` | color/gradiente | Color | color/gradiente [HECHO] | `hyprctl eval "hl.config({general={col={inactive_border='rgba(798bb2ff)'}}})"` | color | Borde inactivo |
| `group.col.border_active` | hypr/config/decorations.lua | `CACHYLBLUE` | gradiente | Color | gradiente (+`whole_monitor`) [HECHO] | `hl.config({group={col={border_active=...}}})` | color | Borde de grupo activo |
| `group.col.border_inactive` | hypr/config/decorations.lua | `CACHYGRAY` | gradiente | Color | gradiente | `hl.config({group={col={border_inactive=...}}})` | color | Borde de grupo inactivo |
| `group.col.border_locked_active` | hypr/config/decorations.lua | `CACHYDBLUE` | gradiente | Color | gradiente | `hl.config({group={col={border_locked_active=...}}})` | color | Grupo bloqueado activo |
| `group.col.border_locked_inactive` | hypr/config/decorations.lua | `CACHYGRAY` | gradiente | Color | gradiente | `hl.config({group={col={border_locked_inactive=...}}})` | color | Grupo bloqueado inactivo |
| `group.groupbar.col.active` | hypr/config/decorations.lua | `CACHYLGREEN` | gradiente | Color | gradiente | `hl.config({group={groupbar={col={active=...}}}})` | color | Fondo groupbar activo |
| `group.groupbar.col.inactive` | hypr/config/decorations.lua | `CACHYGRAY` | gradiente | Color | gradiente | `hl.config({group={groupbar={col={inactive=...}}}})` | color | Fondo groupbar inactivo |
| `group.groupbar.col.locked_active` | hypr/config/decorations.lua | `CACHYDBLUE` | gradiente | Color | gradiente | `hl.config({group={groupbar={col={locked_active=...}}}})` | color | Groupbar bloqueado activo |
| `group.groupbar.col.locked_inactive` | hypr/config/decorations.lua | `CACHYGRAY` | gradiente | Color | gradiente | `hl.config({group={groupbar={col={locked_inactive=...}}}})` | color | Groupbar bloqueado inactivo |
| `decoration.dim_special` | hypr/config/decorations.lua | 0.3 | float | Intensidad | 0.0-1.0 [HECHO] | `hyprctl eval "hl.config({decoration={dim_special=0.3}})"` | slider | Default wiki: 0.2 |
| `decoration.rounding` | hypr/config/decorations.lua | 10 | int | Intensidad | 0-100 [HECHO] | `hyprctl eval "hl.config({decoration={rounding=10}})"` | spin | Radio de esquinas en px lógicos |
| `decoration.active_opacity` | hypr/config/decorations.lua | 0.95 | float | Intensidad | 0.0-1.0 (>1 permitido pero causa glitches) [HECHO] | `hyprctl eval "hl.config({decoration={active_opacity=0.95}})"` | slider | Se multiplica con reglas de opacidad |
| `decoration.inactive_opacity` | hypr/config/decorations.lua | 0.85 | float | Intensidad | 0.0-1.0 | `hyprctl eval "hl.config({decoration={inactive_opacity=0.85}})"` | slider | ídem |
| `decoration.fullscreen_opacity` | hypr/config/decorations.lua | 1 | float | Intensidad | 0.0-1.0 | `hyprctl eval "hl.config({decoration={fullscreen_opacity=1}})"` | slider | ídem |
| `decoration.blur.size` | hypr/config/decorations.lua | 5 | int | Intensidad | ≥1 para aplicar; default 8; sin máx. documentado [HECHO] | `hyprctl eval "hl.config({decoration={blur={size=5}}})"` | spin | Coste alto en iGPU Sandy Bridge |
| `decoration.blur.passes` | hypr/config/decorations.lua | 4 | int | Intensidad | 0-10 (≥1 para aplicar) [HECHO] | `hyprctl eval "hl.config({decoration={blur={passes=4}}})"` | spin | Más passes = más carga GPU |
| `decoration.blur.special` | hypr/config/decorations.lua | true | bool | Toggle | true/false | `hyprctl eval "hl.config({decoration={blur={special=true}}})"` | switch | La wiki advierte: "expensive" |
| `curve.easeOutQuint` | hypr/config/animations.lua | bezier `{{0.23,1},{0.32,1}}` | array de float | Intensidad | 4 coords X/Y [HECHO] | editar `hypr/config/animations.lua` / `hl.curve(...)` | gráfico bezier | Curva con nombre |
| `curve.easeInOutCubic` | hypr/config/animations.lua | bezier `{{0.65,0.05},{0.36,1}}` | array de float | Intensidad | ídem | editar `hypr/config/animations.lua` | gráfico bezier | Curva con nombre |
| `curve.linear` | hypr/config/animations.lua | bezier `{{0,0},{1,1}}` | array de float | Intensidad | ídem | editar `hypr/config/animations.lua` | gráfico bezier | Curva con nombre |
| `curve.almostLinear` | hypr/config/animations.lua | bezier `{{0.5,0.5},{0.75,1}}` | array de float | Intensidad | ídem | editar `hypr/config/animations.lua` | gráfico bezier | Curva con nombre |
| `curve.quick` | hypr/config/animations.lua | bezier `{{0.15,0},{0.1,1}}` | array de float | Intensidad | ídem | editar `hypr/config/animations.lua` | gráfico bezier | Usada por global/workspaces |
| `curve.overshoot` | hypr/config/animations.lua | bezier `{{0.5,0.9},{0.1,1.1}}` | array de float | Intensidad | ídem | editar `hypr/config/animations.lua` | gráfico bezier | Permite Y>1 |
| `curve.easy` | hypr/config/animations.lua | spring `mass=1, stiffness=500, dampening=35` | float×3 | Intensidad | mass~1 recomendado; stiffness/damping libres [HECHO] | editar `hypr/config/animations.lua` | 3 spin | **Ojo:** el archivo dice `dampening`, la wiki documenta `damping` [Fuente](../sources/2026-11-21-hyprland-animations.md) — verificar |
| `curve.rubber` | hypr/config/animations.lua | spring `mass=1, stiffness=200, dampening=15` | float×3 | Intensidad | ídem | editar `hypr/config/animations.lua` | 3 spin | Misma discrepancia `dampening`/`damping` |
| `animation.global` | hypr/config/animations.lua | enabled=true, speed=3, bezier=quick | struct | Intensidad+Toggle | speed en decisegundos (1=100 ms) [HECHO] | editar `hypr/config/animations.lua` | switch+spin+combo | Nodo raíz del árbol de animaciones |
| `animation.windows` | hypr/config/animations.lua | enabled=true, speed=3, spring=easy, style=slide | struct | Intensidad+Toggle | style: slide/popin/gnomed [HECHO] | editar `hypr/config/animations.lua` | switch+spin+combo | Hereda de global |
| `animation.workspaces` | hypr/config/animations.lua | enabled=true, speed=5, bezier=quick, style=slide | struct | Intensidad+Toggle | style: slide/slidevert/fade/slidefade/slidefadevert [HECHO] | editar `hypr/config/animations.lua` | switch+spin+combo | Hereda de global |
| `animation.specialWorkspaceIn` | hypr/config/animations.lua | enabled=true, speed=2, bezier=quick, style="slide top" | struct | Intensidad+Toggle | slide + lado top/bottom/left/right [HECHO] | editar `hypr/config/animations.lua` | switch+spin+combo | Entrada de scratchpad |
| `animation.specialWorkspaceOut` | hypr/config/animations.lua | enabled=true, speed=2, bezier=quick, style="slide bottom" | struct | Intensidad+Toggle | ídem | editar `hypr/config/animations.lua` | switch+spin+combo | Salida de scratchpad |
| `input.sensitivity` | hypr/config/inputs.lua | *comentada* (-0.25) | float | Intensidad | -1.0 a 1.0 [HECHO] | `hyprctl eval "hl.config({input={sensitivity=-0.25}})"` | slider | Inactiva; default wiki 0.0 |
| `input.accel_profile` | hypr/config/inputs.lua | `"flat"` | enum/string | Enum | `""`, `adaptive`, `flat`, `custom` [HECHO] | `hyprctl eval "hl.config({input={accel_profile='flat'}})"` | combo | Perfil de aceleración |
| `input.kb_layout` | hypr/config/inputs.lua | `"es"` | string | Enum/acción | códigos XKB (`/usr/share/X11/xkb/rules/evdev.lst`) [HECHO] | `hyprctl eval "hl.config({input={kb_layout='es'}})"` | combo | Fix AZERTY en binds con `code:` |
| `cursor.no_hardware_cursors` | hypr/config/inputs.lua | *comentada* (1) | int | Intensidad (0-2) | 0-2 [HECHO] | `hyprctl eval "hl.config({cursor={no_hardware_cursors=1}})"` | combo | 2 = auto (default) |
| `cursor.zoom_factor` | hypr/config/binds.lua (zoomfunction) | dinámico; default 1.0 al arrancar | float | Intensidad | 1-10 wiki; **el bind limita a 1.0-3.0** [HECHO] | `hyprctl eval "hl.config({cursor={zoom_factor=1.5}})"` | slider | `get_config("cursor:zoom_factor")` usa `:` [HECHO] |
| `dwindle.preserve_split` | hypr/config/misc.lua | true | bool | Toggle | true/false | `hyprctl eval "hl.config({dwindle={preserve_split=true}})"` | switch | Conserva el split al enfocar |
| `ecosystem.no_update_news` | hypr/config/misc.lua | true | bool | Toggle | true/false | `hyprctl eval "hl.config({ecosystem={no_update_news=true}})"` | switch | Suprime popup de novedades |
| `ecosystem.no_donation_nag` | hypr/config/misc.lua | true | bool | Toggle | true/false | `hyprctl eval "hl.config({ecosystem={no_donation_nag=true}})"` | switch | Suprime popup de donaciones |
| `misc.col.splash` | hypr/config/misc.lua | `CACHYLGREEN` | color | Color | color [HECHO] | `hyprctl eval "hl.config({misc={col={splash='rgba(82dcccff)'}}})"` | color | Requiere recarga de monitor |
| `misc.middle_click_paste` | hypr/config/misc.lua | false | bool | Toggle | true/false (default wiki true) | `hyprctl eval "hl.config({misc={middle_click_paste=false}})"` | switch | Desactivado a propósito |
| `misc.enable_swallow` | hypr/config/misc.lua | true | bool | Toggle | true/false | `hyprctl eval "hl.config({misc={enable_swallow=true}})"` | switch | Terminal "absorbe" al proceso hijo |
| `misc.swallow_regex` | hypr/config/misc.lua | regex de clases de terminales | string | Enum/acción | regex de clase [HECHO] | `hyprctl eval "hl.config({misc={swallow_regex='...'}})"` | text | Ver valor literal en el archivo |
| `misc.vrr` | hypr/config/misc.lua | 3 | int | Intensidad (modo) | 0 off, 1 on, 2 fullscreen, 3 fullscreen+game/video [HECHO] | `hyprctl eval "hl.config({misc={vrr=3}})"` | combo | Hardware sin VRR (ver perfil) |
| `render.direct_scanout` | hypr/config/misc.lua | 2 | int | Intensidad (modo) | 0 off, 1 on, 2 auto [HECHO] | `hyprctl eval "hl.config({render={direct_scanout=2}})"` | combo | Auto = solo con content type "game" |
| `render.non_shader_cm` | hypr/config/misc.lua | *comentada* (0) | int | Intensidad (modo) | 0-3 [HECHO] | `hyprctl eval "hl.config({render={non_shader_cm=0}})"` | combo | Workaround para juegos con DS |
| `xwayland.force_zero_scaling` | hypr/config/misc.lua | true | bool | Toggle | true/false | `hyprctl eval "hl.config({xwayland={force_zero_scaling=true}})"` | switch | Fuerza escala 1 en X11 |
| `monitor.output` | hypr/config/monitors.lua | `MONITOR1` (= `""`, autodetectar) | string | Enum/acción | nombre de salida o vacío [HECHO] | editar `hypr/config/monitors.lua` + `hyprctl reload` | combo (de `hyprctl monitors`) | Variable en variables.lua |
| `monitor.mode` | hypr/config/monitors.lua | `"preferred"` | string | Enum/acción | `preferred`, `WxH@Hz`, `auto` [HECHO] | editar `hypr/config/monitors.lua` | combo | 1440×900@59.89 real |
| `monitor.position` | hypr/config/monitors.lua | `"auto"` | string | Enum/acción | `auto` o `XxY` [HECHO] | editar `hypr/config/monitors.lua` | text | Un único monitor |
| `monitor.scale` | hypr/config/monitors.lua | `"auto"` | string | Enum/acción | `auto` o float [HECHO] | editar `hypr/config/monitors.lua` | spin | Escala real: 1 |
| `TERMINAL` | hypr/config/variables.lua | `"kitty"` | string | Enum/acción | comando arbitrario | editar `hypr/config/variables.lua` | text | Usada por binds de lanzamiento |
| `FILE_MANAGER` | hypr/config/variables.lua | `"dolphin"` | string | Enum/acción | comando | editar `hypr/config/variables.lua` | text | — |
| `BROWSER` | hypr/config/variables.lua | `"firefox"` | string | Enum/acción | comando | editar `hypr/config/variables.lua` | text | — |
| `EDITOR` | hypr/config/variables.lua | `"gnome-text-editor --new-window"` | string | Enum/acción | comando con args | editar `hypr/config/variables.lua` | text | — |
| `CALCULATOR` | hypr/config/variables.lua | `"gnome-calculator"` | string | Enum/acción | comando | editar `hypr/config/variables.lua` | text | — |
| `MONITOR1` / `MONITOR2` / `MONITOR3` | hypr/config/variables.lua | `""` / `""` / `""` | string | Enum/acción | nombres de salida | editar `hypr/config/variables.lua` | combo | Vacío = autodetección |
| `PRIMARY_MONITOR` | hypr/config/variables.lua | `MONITOR1` | string | Enum/acción | alias de monitor | editar `hypr/config/variables.lua` | combo | Usado en reglas y workspace rules |
| `NUM_WPM` | hypr/config/variables.lua | 3 | int | Intensidad | 1-10 [HECHO: comentario "Max 10"] | editar `hypr/config/variables.lua` | spin | Genera binds en bucles `for` |
| `screencopy.allow_token_by_default` | hypr/xdph.conf | true | bool | Toggle | true/false | editar `hypr/xdph.conf` | switch | Portal hyprland (xdg-desktop-portal) |

**Colores de la paleta CachyOS** (`hypr/config/colors.lua`): `CACHYLGREEN=rgba(82dcccff)`,
`CACHYMGREEN=rgba(00aa84ff)`, `CACHYDGREEN=rgba(007d6fff)`, `CACHYLBLUE=rgba(01ccffff)`,
`CACHYMBLUE=rgba(182545ff)`, `CACHYDBLUE=rgba(111826ff)`, `CACHYWHITE=ffffffff`,
`CACHYGREY=ddddddff`, `CACHYGRAY=798bb2ff` [HECHO]. [OPINIÓN]: la GUI debe tratarlos
como un *token* reutilizable, no como 9 color-pickers independientes.

### 1.2 Noctalia — `noctalia/config.toml`

| Opción | Archivo/sección | Valor actual | Tipo | ¿Toggle o Intensidad? | Rango/valores permitidos | Ruta para set en vivo | Control GUI sugerido | Notas |
|---|---|---|---|---|---|---|---|---|
| `accessibility.ui_scale` | noctalia/config.toml | 1.20 | float | Intensidad | no documentado en las fuentes consultadas | editar `noctalia/config.toml` (GUI Ajustes → Accesibilidad) | slider | [OPINIÓN] 0.8-2.0 |
| `bar.default.thickness` | noctalia/config.toml | 35 | int (px) | Intensidad | ≥0 px [HECHO] | editar `noctalia/config.toml` | spin | Default documentado 34 [Fuente](../sources/2026-11-21-noctalia-bar.md) |
| `bar.default.scale` | noctalia/config.toml | 1.10 | float | Intensidad | widgets 0.2-2.5 [HECHO] | editar `noctalia/config.toml` | slider | Multiplica iconos, espaciado y texto |
| `bar.default.concave_edge_corners` | noctalia/config.toml | true | bool | Toggle | true/false [HECHO] | editar `noctalia/config.toml` | switch | Requiere `margin_edge = 0` |
| `bar.default.margin_edge` | noctalia/config.toml | 0 | int (px) | Intensidad | ≥0 [HECHO] | editar `noctalia/config.toml` | spin | 0 = barra pegada al borde |
| `bar.default.margin_ends` | noctalia/config.toml | 0 | int o `"N%"` | Intensidad | px o porcentaje 0-49 [HECHO] | editar `noctalia/config.toml` | spin | 0 = barra a lo largo de toda la pantalla |
| `bar.default.radius_top_left` | noctalia/config.toml | 0 | int (px) | Intensidad | ≥0 [HECHO] | editar `noctalia/config.toml` | spin | Esquina superior izquierda |
| `bar.default.radius_top_right` | noctalia/config.toml | 0 | int (px) | Intensidad | ≥0 | editar `noctalia/config.toml` | spin | ídem derecha |
| `bar.default.radius_bottom_left` | noctalia/config.toml | 12 | int (px) | Intensidad | ≥0 | editar `noctalia/config.toml` | spin | Cóncava activa (barra arriba) |
| `bar.default.radius_bottom_right` | noctalia/config.toml | 12 | int (px) | Intensidad | ≥0 | editar `noctalia/config.toml` | spin | Cóncava activa |
| `bar.default.start` | noctalia/config.toml | `launcher, clock, spacer_1, group:g1` | array de string | Enum/acción | ids de widget [HECHO] | editar `noctalia/config.toml` | reorder list | Sección izquierda |
| `bar.default.center` | noctalia/config.toml | `workspaces, spacer_1, active_window` | array de string | Enum/acción | ids de widget | editar `noctalia/config.toml` | reorder list | Sección central |
| `bar.default.end` | noctalia/config.toml | `media, spacer_1, tray, notifications, network, volume, session` | array de string | Enum/acción | ids de widget | editar `noctalia/config.toml` | reorder list | Sección derecha |
| `bar.default.capsule_group[].id` | noctalia/config.toml | `g1` | string | Enum/acción | identificador único [HECHO] | editar `noctalia/config.toml` | text | Referenciado como `group:g1` |
| `bar.default.capsule_group[].members` | noctalia/config.toml | `temp, sysmon_2, sysmon_3` | array de string | Enum/acción | ids de widget [HECHO] | editar `noctalia/config.toml` | reorder list | Cápsula de 3 widgets |
| `bar.default.capsule_group[].fill` | noctalia/config.toml | `"on_secondary"` | string/color | Color | rol de color o hex [HECHO] | editar `noctalia/config.toml` | color | Fondo de cápsula |
| `bar.default.capsule_group[].border` | noctalia/config.toml | `""` (sin borde) | string/color | Color | rol de color, `""` = none [HECHO] | editar `noctalia/config.toml` | color | — |
| `bar.default.capsule_group[].opacity` | noctalia/config.toml | 1.0 | float | Intensidad | 0.0-1.0 [HECHO] | editar `noctalia/config.toml` | slider | — |
| `bar.default.capsule_group[].padding` | noctalia/config.toml | 6.0 | float | Intensidad | 0-48 (widget capsule_padding) [HECHO] | editar `noctalia/config.toml` | spin | Default documentado 6 |
| `shell.clipboard_image_action_command` | noctalia/config.toml | `swash --stdin --name ...` | string | Enum/acción | comando | editar `noctalia/config.toml` | text | Integración con swash |
| `shell.launch_apps_as_systemd_services` | noctalia/config.toml | true | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | Coincide con UWSM |
| `shell.polkit_agent` | noctalia/config.toml | true | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | Agente PolKit interno |
| `shell.settings_show_advanced` | noctalia/config.toml | true | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | Muestra opciones avanzadas |
| `shell.greeter_sync.auto_sync` | noctalia/config.toml | false | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | Sincronización con greeter |
| `shell.panel.open_near_click_control_center` | noctalia/config.toml | true | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | — |
| `shell.panel.session_placement` | noctalia/config.toml | `"floating"` | enum | Enum | floating/otras [HECHO: valor presente] | editar `noctalia/config.toml` | combo | Panel de sesión |
| `shell.panel.session_position` | noctalia/config.toml | `"center"` | enum | Enum | center/otras | editar `noctalia/config.toml` | combo | — |
| `shell.screenshot.copy_to_clipboard` | noctalia/config.toml | false | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | — |
| `shell.screenshot.pipe_command` | noctalia/config.toml | `swash --stdin --name ...` | string | Enum/acción | comando | editar `noctalia/config.toml` | text | — |
| `shell.screenshot.pipe_to_command` | noctalia/config.toml | true | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | Envía captura a swash |
| `shell.screenshot.save_to_file` | noctalia/config.toml | false | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | — |
| `shell.session.actions[]` | noctalia/config.toml | 5 acciones (lock, logout, lock_and_suspend, reboot, shutdown) | array de struct | Enum/acción | `action`, `countdown_seconds`, `enabled`, `shortcut`, `variant` [HECHO] | editar `noctalia/config.toml` | editor de lista | `countdown_seconds`: 0.0/3.0; `variant`: default/destructive |
| `system.monitor.gpu_poll_seconds` | noctalia/config.toml | 2 | int | Intensidad | >0 s [HECHO: semántica] | editar `noctalia/config.toml` | spin | Frecuencia de sondeo GPU |
| `theme.mode` | noctalia/config.toml | `"dark"` | enum | Enum | `dark`, `light`, `auto` [HECHO] | editar `noctalia/config.toml` / GUI Theme | combo | Fuente: [Theming](../sources/2026-11-21-noctalia-theming-index.md) |
| `theme.source` | noctalia/config.toml | `"wallpaper"` | enum | Enum | `wallpaper`, `builtin`, `community`, `custom` [HECHO] | editar `noctalia/config.toml` | combo | Motor generativo Material You |
| `theme.wallpaper_scheme` | noctalia/config.toml | `"m3-tonal-spot"` | enum | Enum | m3-tonal-spot, m3-content, m3-fruit-salad, m3-rainbow, m3-monochrome, vibrant, faithful, soft, dysfunctional, muted [HECHO] | editar `noctalia/config.toml` | combo | 10 valores documentados |
| `theme.templates.builtin_ids` | noctalia/config.toml | `btop, gtk3, gtk4, kcolorscheme, kitty, qt, alacritty` | array de string | Enum/acción | ids de plantillas [HECHO] | editar `noctalia/config.toml` (o `noctalia theme --list-templates`) | multi-select check | 7 destinos; ver [App Theming](../sources/2026-11-21-noctalia-app-theming.md) |
| `widget.clock.color` | noctalia/config.toml | `"secondary"` | string/color | Color | rol de color [HECHO] | editar `noctalia/config.toml` | color | — |
| `widget.clock.format` | noctalia/config.toml | `"{:%H:%M %A %m/%d/%y}"` | string | Enum/acción | formato chrono/strftime [HECHO] | editar `noctalia/config.toml` | text | — |
| `widget.launcher.color` | noctalia/config.toml | `"secondary"` | string/color | Color | rol de color | editar `noctalia/config.toml` | color | — |
| `widget.media.hide_when_no_media` | noctalia/config.toml | true | bool | Toggle | true/false [HECHO] | editar `noctalia/config.toml` | switch | — |
| `widget.media.title_scroll` | noctalia/config.toml | `"on_hover"` | enum | Enum | on_hover/otras [HECHO: valor presente] | editar `noctalia/config.toml` | combo | — |
| `widget.network.color` | noctalia/config.toml | `"secondary"` | string/color | Color | rol de color | editar `noctalia/config.toml` | color | — |
| `widget.notifications.color` | noctalia/config.toml | `"secondary"` | string/color | Color | rol de color | editar `noctalia/config.toml` | color | — |
| `widget.session.color` | noctalia/config.toml | `"error"` | string/color | Color | rol de color | editar `noctalia/config.toml` | color | Peligro/rojo |
| `widget.spacer_1.type` | noctalia/config.toml | `"spacer"` | enum | Enum | spacer [HECHO] | editar `noctalia/config.toml` | combo | Separador |
| `widget.temp.show_value` | noctalia/config.toml | false | bool | Toggle | true/false [HECHO] | editar `noctalia/config.toml` | switch | Solo icono |
| `widget.sysmon_2.glyph` | noctalia/config.toml | `"gpu-usage"` | string | Enum/acción | id de glifo [HECHO] | editar `noctalia/config.toml` | combo | — |
| `widget.sysmon_2.show_value` | noctalia/config.toml | false | bool | Toggle | true/false | editar `noctalia/config.toml` | switch | — |
| `widget.sysmon_2.stat` | noctalia/config.toml | `"gpu_temp"` | string | Enum/acción | syscall de sysmon [HECHO] | editar `noctalia/config.toml` | combo | Cápsula g1 |
| `widget.sysmon_2.type` | noctalia/config.toml | `"sysmon"` | enum | Enum | sysmon [HECHO] | editar `noctalia/config.toml` | combo | — |
| `widget.sysmon_3.stat` | noctalia/config.toml | `"ram_used"` | string | Enum/acción | syscall de sysmon | editar `noctalia/config.toml` | combo | Cápsula g1 |
| `widget.sysmon_3.type` | noctalia/config.toml | `"sysmon"` | enum | Enum | sysmon | editar `noctalia/config.toml` | combo | — |
| `widget.tray.capsule` | noctalia/config.toml | true | bool | Toggle | true/false [HECHO] | editar `noctalia/config.toml` | switch | Ver [Bar](../sources/2026-11-21-noctalia-bar.md) |
| `widget.tray.capsule_fill` | noctalia/config.toml | `"on_secondary"` | string/color | Color | rol o hex [HECHO] | editar `noctalia/config.toml` | color | — |
| `widget.volume.color` | noctalia/config.toml | `"secondary"` | string/color | Color | rol de color | editar `noctalia/config.toml` | color | — |
| `widget.workspaces.active_pill_size` | noctalia/config.toml | 2.5 | float | Intensidad | ≥0 [HECHO: semántica] | editar `noctalia/config.toml` | slider | Tamaño de píldora activa |
| `widget.workspaces.inactive_pill_size` | noctalia/config.toml | 1.0 | float | Intensidad | ≥0 | editar `noctalia/config.toml` | slider | Tamaño de píldora inactiva |
| `widget.workspaces.pill_scale` | noctalia/config.toml | 0.80 | float | Intensidad | 0.2-2.5 (escala de widget) [HECHO] | editar `noctalia/config.toml` | slider | — |
| `widget.workspaces.capsule` | noctalia/config.toml | true | bool | Toggle | true/false [HECHO] | editar `noctalia/config.toml` | switch | — |
| `widget.workspaces.capsule_fill` | noctalia/config.toml | `"on_primary"` | string/color | Color | rol o hex [HECHO] | editar `noctalia/config.toml` | color | — |
| `widget.workspaces.show_labels` | noctalia/config.toml | false | bool | Toggle | true/false [HECHO] | editar `noctalia/config.toml` | switch | Solo píldoras, sin números |

### 1.3 Terminales, GTK, btop y esquema Qt

| Opción | Archivo/sección | Valor actual | Tipo | ¿Toggle o Intensidad? | Rango/valores permitidos | Ruta para set en vivo | Control GUI sugerido | Notas |
|---|---|---|---|---|---|---|---|---|
| `background_opacity` | kitty/kitty.conf | 0.6 | float | Intensidad | 0.0-1.0 [HECHO: semántica] | editar `kitty/kitty.conf` | slider | Transparencia de kitty |
| `window_padding_width` | kitty/kitty.conf | 25 | int (px) | Intensidad | ≥0 [HECHO: semántica] | editar `kitty/kitty.conf` | spin | Padding de ventana |
| `cursor_trail` | kitty/kitty.conf | 1 | int | Intensidad | ≥0 [HECHO: semántica] | editar `kitty/kitty.conf` | spin | Longitud de estela |
| `include` | kitty/kitty.conf | `themes/noctalia.conf` | string | Enum/acción | ruta de archivo [HECHO] | editar `kitty/kitty.conf` | text | Puente al tema generado |
| `color0-color15` | kitty/themes/noctalia.conf | 16 hex (negro…blanco) | array de color | Color | `#RRGGBB` [HECHO] | editar `kitty/themes/noctalia.conf` | paleta 16 | Generada por Noctalia |
| `cursor`, `cursor_text_color` | kitty/themes/noctalia.conf | `#f3f3f2`, `#292414` | color×2 | Color | hex | editar `kitty/themes/noctalia.conf` | color×2 | — |
| `background`, `foreground` | kitty/themes/noctalia.conf | `#292414`, `#f3f3f2` | color×2 | Color | hex | editar `kitty/themes/noctalia.conf` | color×2 | — |
| `selection_foreground`, `selection_background` | kitty/themes/noctalia.conf | `#b6b5af`, `#37311b` | color×2 | Color | hex | editar `kitty/themes/noctalia.conf` | color×2 | — |
| `active_border_color`, `inactive_border_color`, `url_color` | kitty/themes/noctalia.conf | `#e4c867`, `#37311b`, `#e4c867` | color×3 | Color | hex | editar `kitty/themes/noctalia.conf` | color×3 | — |
| `active/inactive_tab_*`, `cursor_trail_color` | kitty/themes/noctalia.conf | 5 hex | array de color | Color | hex | editar `kitty/themes/noctalia.conf` | paleta | — |
| `general.import` | alacritty/alacritty.toml | `["~/.config/alacritty/themes/noctalia.toml"]` | array de string | Enum/acción | rutas [HECHO] | editar `alacritty/alacritty.toml` | text | Tema generado por Noctalia |
| `general.live_config_reload` | alacritty/alacritty.toml | true | bool | Toggle | true/false [HECHO] | editar `alacritty/alacritty.toml` | switch | Recarga en vivo |
| `general.working_directory` | alacritty/alacritty.toml | `"None"` | string | Enum/acción | ruta o None | editar `alacritty/alacritty.toml` | text | — |
| `env.TERM`, `env.WINIT_X11_SCALE_FACTOR` | alacritty/alacritty.toml | `xterm-256color`, `1.0` | string×2 | Enum/acción | variables de entorno | editar `alacritty/alacritty.toml` | text×2 | — |
| `window.opacity` | alacritty/alacritty.toml | 0.8 | float | Intensidad | 0.0-1.0 [HECHO: semántica] | editar `alacritty/alacritty.toml` | slider |terminal principal usa 0.6 |
| `window.dynamic_padding` | alacritty/alacritty.toml | true | bool | Toggle | true/false [HECHO] | editar `alacritty/alacritty.toml` | switch | Padding dinámico |
| `window.dimensions` | alacritty/alacritty.toml | columns=100, lines=30 | struct int×2 | Intensidad | >0 [HECHO: semántica] | editar `alacritty/alacritty.toml` | spin×2 | — |
| `window.decorations`, `decorations_theme_variant` | alacritty/alacritty.toml | `"Full"`, `"Dark"` | enum×2 | Enum | Full/None; Dark/Light [HECHO] | editar `alacritty/alacritty.toml` | combo×2 | — |
| `window.title`, `window.class` | alacritty/alacritty.toml | `Alacritty@CachyOS`, instance/general `Alacritty` | string/struct | Enum/acción | cadenas [HECHO] | editar `alacritty/alacritty.toml` | text | Clase usada por window rules |
| `scrolling.history`, `scrolling.multiplier` | alacritty/alacritty.toml | 10000, 3 | int, float | Intensidad | ≥0 [HECHO: semántica] | editar `alacritty/alacritty.toml` | spin, slider | — |
| `font.family` (normal/bold/italic/bold_italic) | alacritty/alacritty.toml | `monospace` en los 4 | string×4 | Enum/acción | familias instaladas [HECHO] | editar `alacritty/alacritty.toml` | combo×4 | Fuentes Nerd disponibles |
| `font.size` | alacritty/alacritty.toml | 12.0 | float | Intensidad | >0 [HECHO: semántica] | editar `alacritty/alacritty.toml` | spin | Tamaño de fuente |
| `colors.draw_bold_text_with_bright_colors` | alacritty/alacritty.toml | true | bool | Toggle | true/false [HECHO] | editar `alacritty/alacritty.toml` | switch | — |
| `colors.primary`, `colors.normal`, `colors.bright` | alacritty/alacritty.toml | Nord (base) — 18 colores | array de color | Color | `0xRRGGBB` [HECHO] | editar `alacritty/alacritty.toml` | paleta | **Conflicto:** el theme importado sobrescribe con paleta Noctalia |
| `colors.*` (theme importado) | alacritty/themes/noctalia.toml | primary/cursor/vi/search/footer/hints/selection + normal/bright/dim (8+8+8) | array de color | Color | `#RRGGBB` [HECHO] | editar `alacritty/themes/noctalia.toml` | paleta | Generado por Noctalia |
| `selection.semantic_escape_chars`, `save_to_clipboard` | alacritty/alacritty.toml | `,│…`, true | string+bool | Enum/acción+Toggle | cadena / bool [HECHO] | editar `alacritty/alacritty.toml` | text+switch | — |
| `cursor.style.shape`, `blinking` | alacritty/alacritty.toml | `Underline`, `Off` | enum×2 | Enum | shape/blinking [HECHO] | editar `alacritty/alacritty.toml` | combo×2 | — |
| `cursor.unfocused_hollow`, `cursor.thickness` | alacritty/alacritty.toml | true, 0.15 | bool, float | Toggle+Intensidad | bool; >0 [HECHO: semántica] | editar `alacritty/alacritty.toml` | switch+slider | Grosor de cursor |
| `mouse.hide_when_typing`, `mouse.bindings` | alacritty/alacritty.toml | true; Middle→PasteSelection | bool+array | Toggle+Enum/acción | modelo de bindings [HECHO] | editar `alacritty/alacritty.toml` | switch+editor de lista | — |
| `keyboard.bindings` | alacritty/alacritty.toml | 16 entradas (Copy/Paste/Search/…) | array de struct | Enum/acción | key+mods+action [HECHO] | editar `alacritty/alacritty.toml` | editor de lista | Ver sección 4 |
| `gtk-theme-name` | gtk/settings.ini | `adw-gtk3` | string | Enum/acción | temas GTK instalados [HECHO] | editar `gtk/settings.ini` / `nwg-look` | combo | Tema GTK3 |
| `gtk-cursor-theme-name` | gtk/settings.ini | `Bibata-Modern-Ice` | string | Enum/acción | temas de cursor [HECHO] | editar `gtk/settings.ini` | combo | — |
| `gtk-cursor-theme-size` | gtk/settings.ini | 24 | int (px) | Intensidad | >0 [HECHO: semántica] | editar `gtk/settings.ini` | spin | **Tamaño de cursor** |
| `gtk-toolbar-style`, `gtk-toolbar-icon-size` | gtk/settings.ini | `GTK_TOOLBAR_ICONS`, `GTK_ICON_SIZE_LARGE_TOOLBAR` | enum×2 | Enum | constantes GTK [HECHO] | editar `gtk/settings.ini` | combo×2 | — |
| `gtk-button-images`, `gtk-menu-images` | gtk/settings.ini | 0, 0 | bool (0/1) | Toggle | 0/1 [HECHO] | editar `gtk/settings.ini` | switch×2 | — |
| `gtk-enable-event-sounds`, `gtk-enable-input-feedback-sounds` | gtk/settings.ini | 1, 0 | bool (0/1) | Toggle | 0/1 [HECHO] | editar `gtk/settings.ini` | switch×2 | — |
| `gtk-xft-antialias`, `gtk-xft-hinting` | gtk/settings.ini | 1, 1 | bool (0/1) | Toggle | 0/1 [HECHO] | editar `gtk/settings.ini` | switch×2 | — |
| `gtk-xft-hintstyle` | gtk/settings.ini | `hintslight` | enum | Enum | hintnone/hintslight/hintmedium/hintfull [HECHO] | editar `gtk/settings.ini` | combo | — |
| `gtk-xft-rgba` | gtk/settings.ini | `rgb` | enum | Enum | rgb/bgr/vrgb/vbgr/none [HECHO] | editar `gtk/settings.ini` | combo | Subpixel |
| `gtk-application-prefer-dark-theme` | gtk/settings.ini | 1 | bool (0/1) | Toggle | 0/1 [HECHO] | editar `gtk/settings.ini` | switch | Coincide con `theme.mode=dark` |
| `@define-color` GTK4 (≈30 tokens) | gtk/noctalia.css | accent/destructive/error/window/view/headerbar/popover/card/dialog/overview/sidebar/selected/unfocused | color×≈30 | Color | hex o `@otro-color` [HECHO] | editar `gtk/noctalia.css` (lo regenera Noctalia) | paleta | No editar a mano: plantilla `gtk4` |
| `theme[main_bg]`…`theme[upload_end]` | terminales/btop-noctalia.theme | 39 claves, paleta Noctalia | array de color | Color | `#RRGGBB` [HECHO] | editar `terminales/btop-noctalia.theme` (lo regenera Noctalia) | paleta | Plantilla `btop` |
| `color_theme`, `theme_background`, `truecolor` | terminales/btop.conf | `noctalia`, true, true | string+bool×2 | Enum/acción+Toggle×2 | ver comentarios del archivo [HECHO] | editar `terminales/btop.conf` | combo+switch×2 | Tema + fondo + 24 bit |
| `rounded_corners`, `terminal_sync`, `background_update` | terminales/btop.conf | true, true, true | bool×3 | Toggle×3 | true/false [HECHO] | editar `terminales/btop.conf` | switch×3 | — |
| `graph_symbol` (+5 variantes por caja) | terminales/btop.conf | `braille` (cpu/gpu/mem/net/proc=`default`) | enum×6 | Enum | braille/block/tty/default [HECHO] | editar `terminales/btop.conf` | combo×6 | — |
| `shown_boxes`, `update_ms`, `presets` | terminales/btop.conf | `proc mem net cpu`; 2000; 3 presets | string+int+string | Enum/acción+Intensidad | cajas cpu/mem/net/proc/gpu0-5; ms [HECHO] | editar `terminales/btop.conf` | multi-select+spin+text | — |
| `proc_sorting`, `proc_reversed`, `proc_tree`, `proc_colors`, `proc_gradient` | terminales/btop.conf | `memory`; false; false; true; true | enum+bool×4 | Enum+Toggle×4 | valores en comentarios [HECHO] | editar `terminales/btop.conf` | combo+switch×4 | — |
| `temp_scale`, `clock_format`, `show_uptime`, `show_battery` | terminales/btop.conf | `celsius`, `%X`, true, true | enum+string+bool×2 | Enum+Intensidad+Toggle×2 | celsius/fahrenheit/kelvin/rankine [HECHO] | editar `terminales/btop.conf` | combo+text+switch×2 | — |
| `net_download`, `net_upload`, `net_auto`, `net_sync` | terminales/btop.conf | 100, 100, true, true | int×2+bool×2 | Intensidad+Toggle | MiB; bool [HECHO] | editar `terminales/btop.conf` | spin×2+switch×2 | Escalado de red |
| `shown_gpus`, `gpu_mirror_graph` | terminales/btop.conf | `nvidia amd intel`, true | string+bool | Enum+Toggle | nvidia/amd/intel/apple [HECHO] | editar `terminales/btop.conf` | multi-select+switch | — |
| `log_level`, `save_config_on_exit` | terminales/btop.conf | `WARNING`, true | enum+bool | Enum+Toggle | ERROR/WARNING/INFO/DEBUG [HECHO] | editar `terminales/btop.conf` | combo+switch | ~80 opciones más comentadas en el archivo |
| `[KDE].contrast` | temas/noctalia.colors | 4 | int | Intensidad | 0-7 aprox. [HECHO: semántica Qt] | editar `temas/noctalia.colors` | spin | Esquema Qt/KDE |
| `[General].ColorScheme`, `.Name` | temas/noctalia.colors | `noctalia`, `noctalia` | string×2 | Enum/acción | nombre de esquema [HECHO] | editar `temas/noctalia.colors` | text×2 | Instalado en `~/.local/share/color-schemes/` |
| `ColorEffects:Disabled` / `:Inactive` | temas/noctalia.colors | Color, ColorAmount, ColorEffect, ContrastAmount, ContrastEffect, IntensityAmount, IntensityEffect | array de float/int | Intensidad | 0-1 / enum [HECHO] | editar `temas/noctalia.colors` | sliders+combos | Efectos de accesibilidad Qt |
| `Colors:Button/Complementary/Header/Selection/Tooltip/View/Window` | temas/noctalia.colors | 7 secciones × ~9 roles RGB | array de color | Color | `R,G,B` [HECHO] | editar `temas/noctalia.colors` | paleta | Generado por plantilla `qt`/`kcolorscheme` |
| `[WM]` | temas/noctalia.colors | active/inactive Background/Blend/Foreground | color×6 | Color | `R,G,B` [HECHO] | editar `temas/noctalia.colors` | paleta | Colores de barra de título KDE |

> El resto de `btop.conf` (≈80 claves) son **defaults comentados** con descripción
> en el propio archivo; se inventarían con el mismo patrón si la GUI quiere exponerlos.

---

## 2. Opciones de intensidad (NO binarias)

**[HECHO]** Todo lo de abajo es numérico o enumerado con más de dos estados: un
`switch` sería incorrecto. **[OPINIÓN]** La columna de control es la recomendación
para la GUI. Rangos tomados de [Config Options](../sources/2026-11-21-hyprland-config-options.md)
salvo indicación contraria.

| Opción | Valor actual | Rango real [HECHO] | Control [OPINIÓN] | Notas |
|---|---|---|---|---|
| `general.gaps_in` / `gaps_out` | 3 / 8 | css_gaps, ≥0 (default 5/20) | spin | En px lógicos |
| `general.border_size` | 2 | **0-20** | spin | — |
| `general.extend_border_grab_area` | 10 | **0-100** | spin | — |
| `general.col.active_border.angle` | 45 | grados (sin límite oficial) | spin | 0-360 en la práctica |
| `decoration.rounding` | 10 | **0-100** | spin | `rounding_power` 1.0-10.0 no está configurado |
| `decoration.dim_special` | 0.3 | **0.0-1.0** | slider | — |
| `decoration.active_opacity` | 0.95 | **0.0-1.0** | slider | >1.0 da glitches |
| `decoration.inactive_opacity` | 0.85 | **0.0-1.0** | slider | — |
| `decoration.fullscreen_opacity` | 1 | **0.0-1.0** | slider | — |
| `decoration.blur.size` | 5 | ≥1 (default 8), sin máx. | spin | — |
| `decoration.blur.passes` | 4 | **0-10** | spin | Coste GPU |
| `animation.*.speed` | 3, 3, 5, 2, 2 | decisegundos (1 = 100 ms) | spin | Valores altos = más lentos |
| `curve.*` bezier points | 4 coords por curva | X/Y libres, Y puede >1 | editor 2D | 6 curvas |
| `curve.easy/rubber` mass | 1 / 1 | ~1 recomendado | spin | — |
| `curve.easy/rubber` stiffness | 500 / 200 | float libre | spin | Más = más rápido |
| `curve.easy/rubber` damping | 35 / 15 | ζ≈0.6-0.8 recomendado | spin | Ver aviso `dampening` arriba |
| `input.sensitivity` | -0.25 (comentada) | **-1.0 a 1.0** | slider | — |
| `cursor.zoom_factor` | 1.0 (bind 1.0-3.0) | **1-10** wiki | slider | El bind limita a 3.0 [HECHO] |
| `misc.vrr` | 3 | **0/1/2/3** | combo (no slider) | Sin hardware VRR |
| `render.direct_scanout` | 2 | **0/1/2** | combo | auto = juegos |
| `render.non_shader_cm` | 0 (comentada) | **0-3** | combo | — |
| `cursor.no_hardware_cursors` | 1 (comentada) | **0/1/2** | combo | — |
| `NUM_WPM` | 3 | **1-10** | spin | Regenera binds |
| `accessibility.ui_scale` (Noctalia) | 1.20 | sin rango documentado | slider | [OPINIÓN] 0.8-2.0 |
| `bar.default.thickness` | 35 | ≥0 px | spin | — |
| `bar.default.scale` | 1.10 | 0.2-2.5 (widgets) | slider | [HECHO parcial] |
| `bar.default.margin_edge` / `margin_ends` | 0 / 0 | px; `margin_ends` 0-49% | spin | — |
| `bar.default.radius_*` | 0/0/12/12 | ≥0 px | spin×4 | — |
| `capsule_group.opacity` / `.padding` | 1.0 / 6.0 | 0.0-1.0; 0-48 | slider+spin | [Bar](../sources/2026-11-21-noctalia-bar.md) |
| `widget.workspaces.*_pill_size`, `pill_scale` | 2.5 / 1.0 / 0.80 | ≥0; escala 0.2-2.5 | slider×3 | — |
| `system.monitor.gpu_poll_seconds` | 2 | >0 s | spin | — |
| kitty `background_opacity` / padding / trail | 0.6 / 25 / 1 | 0-1; ≥0; ≥0 | slider+spin×2 | — |
| alacritty `window.opacity` / `font.size` / `cursor.thickness` | 0.8 / 12.0 / 0.15 | 0-1; >0; >0 | slider+spin×2 | — |
| GTK `gtk-cursor-theme-size` | 24 | >0 px | spin | — |
| btop `update_ms` / `net_download` / `net_upload` | 2000 / 100 / 100 | ms; MiB | spin×3 | — |
| Qt `[KDE].contrast` | 4 | enum acotado | spin | — |

**Regla de oro [OPINIÓN]:** los modos `vrr` (0-3), `direct_scanout` (0-2),
`non_shader_cm` (0-3), `no_hardware_cursors` (0-2) y `accel_profile` son
*enteros semánticos*: deben ser `combo`, nunca `slider`, porque cada número
significa un comportamiento distinto, no una cantidad.

---

## 3. Reglas y estructuras complejas

**[HECHO]** Ninguna de estas construcciones es un par clave/valor escalar: son
**listas de estructuras** con un bloque `match` (selector) y un bloque de efectos,
o una tabla de dispatch. La GUI no puede representarlas con un switch: necesita un
**editor de lista con campos**, idealmente con botones Añadir/Editar/Eliminar y
reordenación (el orden importa: *"effects are processed top to bottom, and the last
match takes precedence"* [Fuente](../sources/2026-11-21-hyprland-window-rules.md)).

### 3.1 Window rules (`windowrules.lua`, 25 llamadas → 37 reglas efectivas)

Campos del `match` disponibles [HECHO]:
`class`, `title`, `initial_class`, `initial_title` (RegEx), `content`
(none/photo/video/game), `focus`, `float`, `fullscreen`, `fullscreen_state_client`,
`fullscreen_state_internal`, `group`, `modal`, `pin`, `tag`, `xdg_tag`,
`workspace` (selector), `xwayland`. Soportan el prefijo `negative:` (usado en
PiP, steam y dolphin del archivo del usuario).

Efectos estáticos usados por el usuario: `float`, `fullscreen_state`, `size`,
`min_size`, `move`, `center`, `workspace`, `monitor`, `pin`, `keep_aspect_ratio`,
`persistent_size`, `suppress_event`, `decorate`, `content`, `sync_fullscreen`.
Efectos dinámicos relevantes: `opacity` (`"1.0 override"`), `no_focus`, `rounding`,
`no_anim`, `no_blur` [Fuente](../sources/2026-11-21-hyprland-window-rules.md).

[OPINIÓN] Modelo para la GUI:

```text
WindowRule {
  name?: Text,
  match: { class?: RegEx, title?: RegEx, initial_title?: RegEx,
           content?: Enum, xdg_tag?: RegEx, xwayland?: Bool, ... },
  effects: { float?: Bool, size?: [Expr, Expr], move?: [Expr, Expr],
             workspace?: Text, monitor?: Text, opacity?: Text,
             fullscreen_state?: Enum(0..3), ... }
}
Expr = número | "monitor_w*0.70" | "max(20, min(cursor_x-..., ...))"
```

Los `size`/`move` usan expresiones con `monitor_w`, `monitor_h`, `window_w`,
`window_h`, `cursor_x`, `cursor_y` [HECHO]. [OPINIÓN]: la GUI debe ofrecer un
selector de expresión con esas variables, no un simple par de números.

### 3.2 Layer rules (1 regla: `noctalia`)

`hl.layer_rule({ name="noctalia", match={ namespace=regex }, no_anim=true,
ignore_alpha=0.5, blur=true, blur_popups=true })` [HECHO]. `ignore_alpha` es una
**intensidad** (0.0-1.0). Modelo [OPINIÓN]: `LayerRule { name, namespace_regex,
no_anim:Switch, ignore_alpha:Slider, blur:Switch, blur_popups:Switch }`.

### 3.3 Workspace rules (4 activas: `name:gaming`, `1`, `2`, `3`)

Campos [HECHO]: `workspace` (selector o `name:`), `monitor`, `default`,
`persistent`, `layout` (`scrolling` en el ejemplo comentado). Modelo [OPINIÓN]:
tabla editable `WorkspaceRule { workspace:Text, monitor:Combo, default:Switch,
persistent:Switch, layout:Combo }`. Las reglas 4-6 están comentadas y preparadas
para `MONITOR2` (sin uso hoy, ver perfil).

### 3.4 Keybinds (`binds.lua`, 76 llamadas → ~84 atajos efectivos)

Estructura [HECHO]: `hl.bind(combination, dispatcher_or_function, flags?)`.
Los Flags usados: `repeating=true` (zoom, volumen, brillo) y `locked=true`
(medios/volumen/brightness). Hay tres familias:
(a) `hl.dsp.*` nativos (`window.close`, `window.float`, `focus`, `workspace`,
`exec_cmd`, `gesture`…), (b) `noctalia msg …` delegados al shell, y (c) una
función Lua `zoomfunction` con clamps 1.0-3.0 [HECHO]. El fix AZERTY genera
atajos con `digitCode(d)` → `code:10..19` [HECHO]: la GUI **debe** permitir
binding por `code:` además de por símbolo. Modelo [OPINIÓN]:
`Bind { keys:KeyComboField, action:Enum+Args, repeating:Bool, locked:Bool }`.

### 3.5 Gestos (4 `hl.gesture` en `inputs.lua`)

`hl.gesture({ fingers=3|4, direction=horizontal|down|up|left, action=workspace|close|fullscreen|float })`
[HECHO]. Los parámetros globales calibrables están en la categoría `gestures`
(`workspace_swipe_distance` 0-2000, `workspace_swipe_cancel_ratio` 0.0-1.0,
`workspace_swipe_direction_lock_threshold` 0-200, `workspace_swipe_create_new`,
etc. [HECHO,Fuente](../sources/2026-11-21-hyprland-config-options.md)): la GUI
puede ofrecer sliders para esos y un editor de lista para los 4 gestos.

### 3.6 Curvas y animaciones

`hl.curve(nombre, {type=bezier|spring, points={{x,y},{x,y}} | mass,stiffness,damping})`
y `hl.animation({leaf, enabled, speed, bezier|spring, style})` [HECHO]. Son
**definiciones nombradas reutilizables**: la GUI debe permitir crear curvas y
luego elegirlas por nombre desde cada nodo del árbol (`global → windows →
windowsIn/Out/Move`, `fade*`, `workspaces*`, `specialWorkspace*`, `border*`,
`zoomFactor`, …) [Fuente](../sources/2026-11-21-hyprland-animations.md). Advertencia
[HECHO]: el estilo `loop` en animaciones `*angle` fuerza render continuo a la
tasa de refresco.

---

## 4. Mapeo a `hl.config` (estructura anidada exacta, verificada)

**[HECHO]** Estructura equivalente a la configuración real del usuario, con la
forma anidada de la wiki [Fuente](../sources/2026-11-21-hyprland-config-options.md):

```lua
hl.config({
  general = {
    gaps_in = 3, gaps_out = 8, border_size = 2,
    extend_border_grab_area = 10, resize_on_border = true,
    col = {
      active_border = { colors = { CACHYLGREEN, CACHYDGREEN }, angle = 45 },
      inactive_border = CACHYGRAY,
    },
  },
  group = {
    col = {
      border_active = CACHYLBLUE, border_inactive = CACHYGRAY,
      border_locked_active = CACHYDBLUE, border_locked_inactive = CACHYGRAY,
    },
    groupbar = { col = {
      active = CACHYLGREEN, inactive = CACHYGRAY,
      locked_active = CACHYDBLUE, locked_inactive = CACHYGRAY,
    } },
  },
  decoration = {
    dim_special = 0.3, rounding = 10,
    active_opacity = 0.95, inactive_opacity = 0.85, fullscreen_opacity = 1,
    blur = { size = 5, passes = 4, special = true },
  },
  input  = { accel_profile = "flat", kb_layout = "es" },
  cursor = { zoom_factor = 1.5 },  -- el bind lo ajusta en vivo
  dwindle   = { preserve_split = true },
  ecosystem = { no_update_news = true, no_donation_nag = true },
  misc = {
    col = { splash = CACHYLGREEN },
    middle_click_paste = false, enable_swallow = true,
    swallow_regex = "(kitty|ghostty|[Kk]onsole|Alacritty|...)",
    vrr = 3,
  },
  render    = { direct_scanout = 2 },
  xwayland  = { force_zero_scaling = true },
})
```

Categorías adicionales que **no** están en `hl.config` (API distinta) [HECHO]:

```lua
-- Animaciones: hl.animation / hl.curve, NO hl.config.animaciones
hl.curve("quick", { type = "bezier", points = { {0.15, 0}, {0.1, 1} } })
hl.curve("easy",  { type = "spring", mass = 1, stiffness = 500, damping = 35 })
hl.animation({ leaf = "global", enabled = true, speed = 3, bezier = "quick" })
hl.animation({ leaf = "windows", enabled = true, speed = 3, spring = "easy", style = "slide" })

-- Monitores: hl.monitor
hl.monitor({ output = MONITOR1, mode = "preferred", position = "auto", scale = "auto" })

-- Reglas: hl.window_rule / hl.layer_rule / hl.workspace_rule
hl.window_rule({ match = { float = true }, persistent_size = true })
hl.layer_rule({ name = "noctalia", match = { namespace = "^noctalia-..." },
                no_anim = true, ignore_alpha = 0.5, blur = true, blur_popups = true })
hl.workspace_rule({ workspace = "1", monitor = MONITOR1, default = true, persistent = true })

-- En vivo (no persistente): forma de clave plana con punto
hyprctl eval "hl.config({ ['decoration.rounding'] = 12 })"
```

**[HECHO]** La categoría `animations` sí existe en `hl.config`, pero solo con
`enabled` y `workspace_wraparound`; los *leaf* de animación se definen con
`hl.animation()` [Fuente](../sources/2026-11-21-hyprland-config-options.md) y
[Fuente](../sources/2026-11-21-hyprland-animations.md). **[OPINIÓN]** la GUI debe
generar código con indentación y escribir el archivo fuente, no solo `hyprctl eval`,
para que el cambio sobreviva a un `hyprctl reload`.

---

## 5. Cierre

**[HECHO]** El inventario cubre la configuración real auditada: 12 módulos Lua,
`config.toml` de Noctalia (5.6.0), kitty 0.51.0, alacritty 0.17.0, GTK3/GTK4,
btop 1.4.8 y el esquema Qt/KDE. **[OPINIÓN]** El siguiente paso es convertir la
tabla maestra en un esquema de datos (JSON Schema o `dataclass`) con tres niveles:
`category → option → {tipo, rango, valor, ruta, persistencia}`, y un adaptador
que sepa si escribe Lua, TOML, INI o conf. Los hallazgos a resolver antes de
programar son: (1) `dampening` vs `damping` en las curvas spring; (2) doble fuente
de color (verde CachyOS en bordes vs. M3 azul en el resto, ver perfil); y
(3) `vrr=3`/`direct_scanout=2` en hardware sin VRR.
