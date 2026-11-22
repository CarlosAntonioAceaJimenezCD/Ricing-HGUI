# 02 · Hyprland 0.57.2: el compositor y la migración a Lua

> Documento de investigación, 2026-11-21/22. Contexto: CachyOS, Hyprland **0.57.2** (commit
> `11cbc6c5`, ABI `..._aq_0.16_hu_0.14_hg_0.6_hc_0.1_hlg_0.6`), un monitor VGA-1 1440×900
> @ 59.89 Hz e iGPU Intel Sandy Bridge. Toda la configuración viva está en Lua.
> Convención: **Hecho** = verificable en las fuentes citadas; **Opinión** = recomendación
> derivada del perfil de hardware.

---

## 1. Qué es Hyprland (y por qué es el eje del ricing)

**Hecho.** Hyprland es un *compositor Wayland independiente*, no un desktop environment.
La ArchWiki lo describe como «an independent tiling Wayland compositor» y destaca como
características el tiling dinámico, ventanas tabuladas, una base de código C++ legible y
**un renderizador propio** que proporciona animaciones de ventanas, esquinas redondeadas y
*Dual-Kawase Blur* en ventanas transparentes ([ArchWiki](sources/2026-11-21-archwiki-hyprland.md),
URL original: https://wiki.archlinux.org/title/Hyprland).

**Hecho.** El stack instalado en la máquina se lee literalmente en `hyprctl version`:

| Capa | Versión instalada | Papel |
|---|---|---|
| Hyprland | 0.57.2 (8015 commits, tag `v0.57.2`) | compositor + renderizador + intérprete de config |
| **Aquamarine** | 0.16.0 (built = system) | abstracción DRM/KMS/outputs del ecosistema Hypr |
| Hyprlang | 0.6.8 | parser del lenguaje de configuración |
| Hyprutils / Hyprgraphics / Hyprcursor | 0.14.4 / 0.6.0 / 0.1.14 | utilidades, gráficos y cursores |
| `wlroots0.20` | 0.20.2-1 | presente en el sistema como paquete (compatibilidad/ecosistema) |

Fuente: [apéndice de versión](../apendices/hyprland-version.txt) y
[perfil del sistema](../00-perfil-del-sistema.md). La propia cadena ABI incluye `aq_0.16`,
lo que confirma que Aquamarine es la capa de salida con la que se compiló este binario.

**Hecho.** Aquamarine figure como biblioteca del ecosistema en la navegación de la wiki
oficial (`Hypr Ecosystem → Developer libs and toolkits → aquamarine`), junto a hyprgraphics,
hyprlang, hyprutils y hyprwayland-scanner
([Lua utilities](sources/2026-11-21-hyprland-lua-utilities.md), https://wiki.hypr.land/configuring/core/advanced-configuration/lua-utilities/).

**Opinión.** En un DE el usuario elige entre opciones predefinidas; aquí el compositor
**define cada píxel**: qué se difumina, cuánto tarda una ventana en aparecer o el ángulo de
un borde. El rice pasa a ser **programar declarativamente el compositor**, lo que explica
por qué la migración a `hyprland.lua` (§3) es el cambio clave: config con funciones,
eventos y tipos. La wiki agrupa bajo `Configuring → Core` justo esas áreas (monitors,
config options, devices, dispatchers, binds, rules, animations, autostart) y bajo
`Advanced configuration` los eventos, utilidades Lua, hyprctl y permisos
([Config options](sources/2026-11-21-hyprland-config-options.md)).

---

## 2. Cronología 0.56 → 0.57.2 (features leídas de las notas de release)

Fuente primaria: [Hyprland releases](sources/2026-11-21-hyprland-releases.md),
https://github.com/hyprwm/Hyprland/releases. Las fechas son las de publicación del tag.

| Versión | Fecha | Features/fixes concretos relevantes para ricing |
|---|---|---|
| **0.56.0** | 2026-07-20 | «No breaking changes :)». Gestos Lua *custom live* (#15393); API `change_id` de workspaces; `get_loaded_plugins`; `is_key_down` + evento de tecla; `physicalWidth`/`physicalHeight` en `Monitor`; prop-refresh inmediato + evento; stubs Lua; animación de gradiente y ángulo en **glow** (#15208) y **shadow** (#14809); regla `no_auto_hdr`; selector `stableid:`; **motion blur** de ventanas (#14911); ajustes de tonemap; **REPL Lua interactivo en hyprctl** (#15043); `config full-reload` (#14748); evento `specialActive`; refactor del gestor de animaciones (#15302). |
| **0.56.1** | 2026-07-27 | **Aviso de deprecación para configs `.conf`** (#15538); no destrozar `package.path` (arregla `require()` en configs modulares, #15622); `openLate` para eventos `window.open`; se actualizan los springs por defecto del ejemplo (#15499). |
| **0.56.2** | 2026-08-05 | Solo fixes (scrolling/fullscreen, stubs Lua, strings de hyprctl, ICCCM, entre otros). |
| **0.57.0** | 2026-10-28 | Gran release: evento `config.unload`; API `reload_config()`; `hl.get_devices()`; evento `window.minimize`; `window.update_state`; `cursor:warp_on_monitor_change`; nueva categoría `layers`; avisos de deprecación; reglas `no_xdg_drags`, `active_border`/`inactive_border`, `no_glow`, `no_wobble`; **pointer transforms** (#16143); **scene composition** (#16340); **window wobble** (#14920); **variantes de blur intercambiables** (#15661); **`decoration.blur.proportional`** (#16643); `workspace presentable`; fix de eventos `created` → `created_early`; **fix del typo `dampening` → `damping` en springs** (#15993); límites de shadow y `CONFIG_VALUES`. |
| **0.57.1** | 2026-11-03 | Fixes: validador de accel profiles custom; keybinds (chords, shadowing de mouse events); session-lock; `max_bpc`; feedback dmabuf; renderer dibuja superficies pequeñas a tamaño lógico; conservar fullscreen ante maximize del cliente. |
| **0.57.2** | 2026-11-09 | Parches backporteados: **referencia de ventana expirada desde Lua** (#16853); fullscreen `client_requested_fs_uses_layout_handler`; resolución de modificadores remapeados; artefactos de invalidación con dos ventanas flotantes solapadas; capas bottom/background bajo fullscreen; **dejar de adquirir scheduling en tiempo real** (arregla crashes bajo carga); desanclar ventana al workspace special. **Esta es la versión instalada.** |

### 2.1 Tabla de features y su impacto visual

| Feature (release) | Qué cambia | Impacto visual en este equipo |
|---|---|---|
| API `hl.*` consolidada (0.56→0.57) | Config como código: tablas, callbacks, eventos | Alto: permite temas dinámicos y toggles en vivo (§3.2) |
| Deprecación `.conf` (0.56.1) | El parser avisa; el futuro es `hyprland.lua` | Medio: obliga a traducir tutoriales antiguos |
| Config Lua modular (0.56.1, fix `package.path`) | `require("config.x")` funciona | Alto: es la estructura real del usuario (§4) |
| **Scene composition** (0.57.0, #16340) | Composición de escena en el renderizador | Potencial alto; las notas solo dan el título, sin detalle de interfaz |
| **Blur variants intercambiables** (0.57.0, #15661) | `kawase`, `acrylic`, `aurora`, `drops`, `fluid_jar`, `frost`, `haze`, `heat_shimmer`, `prism`, `ripple`, `water` | Alto y **peligroso** en iGPU: la wiki avisa que «may significantly increase GPU and CPU usage» |
| **Blur proporcional** (0.57.0, #16643) | Fuerza de blur ∝ opacidad del píxel; requiere `render.use_shader_blur_blend` | Medio: transiciones más limpias, coste extra de shader |
| **Window wobble** (0.57.0, #14920) | Deformación elástica al mover/redimensionar; regla `no_wobble` | Medio; desactivado por defecto (ver doc 08) |
| **Pointer transforms** (0.57.0, #16143) | Transformaciones de puntero en el compositor | Bajo/medio; útil con tablets/rotación, no crítico aquí |
| Gradiente/ángulo animado en shadow y glow (0.56.0) | `*angle` con estilo `once`/`loop` | **Alto coste** si se usa `loop` (frames constantes) |
| Motion blur (0.56.0) | Samples sobre ventanas en movimiento | Alto coste; desactivado por defecto |
| Eventos (`config.unload`, `minimize`, `specialActive`, key) | Scripts reactivos | Medio: autocleanup, integraciones con Noctalia |
| `active_border`/`inactive_border` por regla (0.57.0) | Color de borde por aplicación/foco | Medio: permite unificar paletas sin tocar el global |
| Fix `dampening` → `damping` (0.57.0) | Nombre correcto de la clave de springs | **Crítico**: el config actual usa la forma antigua (§8) |
| Stop RT scheduling (0.57.2) | Estabilidad bajo carga | Indirecto: menos crashes en iGPU cargada |

---

## 3. De `hyprland.conf` a `hyprland.lua`

### 3.1 Correspondencia sintáctica

**Hecho.** La wiki documenta dos formas de `hl.config()`: agrupada por categorías o con
clave plana `["category.option"]`, y advierte que **la última línea que asigna una opción
gana** ([Config options](sources/2026-11-21-hyprland-config-options.md),
https://wiki.hypr.land/configuring/core/config-options/).

| Sintaxis antigua (`.conf`) | API actual (`.lua`) |
|---|---|
| `general { gaps_in = 5 }` | `hl.config({ general = { gaps_in = 5 } })` o `hl.config({ ["general.gaps_in"] = 5 })` |
| `bind = SUPER, Q, exec, firefox` | `hl.bind("SUPER + Q", hl.dsp.exec_cmd("firefox"))` |
| `windowrule = float, class:kitty` | `hl.window_rule({ match = { class = "kitty" }, float = true })` |
| `layerrule = blur, noctalia` | `hl.layer_rule({ name = "...", match = { namespace = "..." }, blur = true })` |
| `workspace = 1, monitor:DP-1, persistent:true` | `hl.workspace_rule({ workspace = "1", monitor = "DP-1", persistent = true })` |
| `bezier = quick, 0.15, 0, 0.1, 1` | `hl.curve("quick", { type = "bezier", points = { {0.15, 0}, {0.1, 1} } })` |
| `spring = easy, 1, 500, 35` | `hl.curve("easy", { type = "spring", mass = 1, stiffness = 500, damping = 35 })` |
| `animation = windows, 1, 3, easy, slide` | `hl.animation({ leaf = "windows", enabled = true, speed = 3, spring = "easy", style = "slide" })` |
| `exec-once = noctalia` | `hl.on("hyprland.start", function() hl.exec_cmd("noctalia") end)` |
| `exec = ...` (con `&`) | `hl.exec_cmd(...)` (ya es asíncrono; no hace falta `& disown`) |
| `monitor = DP-1, preferred, auto, 1` | `hl.monitor({ output = "DP-1", mode = "preferred", position = "auto", scale = 1 })` |
| `env = QT_QPA_PLATFORM, wayland` | `hl.env("QT_QPA_PLATFORM", "wayland")` (o `~/.config/uwsm/env`, ver §7) |
| `plugin = ...` / `exec` de script | `hl.get_loaded_plugins()`, `hl.permission(...)`, eventos |

Fuentes: [Lua utilities](sources/2026-11-21-hyprland-lua-utilities.md),
[Animations](sources/2026-11-21-hyprland-animations.md),
[Window rules](sources/2026-11-21-hyprland-window-rules.md),
[Master tutorial](sources/2026-11-21-hyprland-master-tutorial.md),
[ArchWiki](sources/2026-11-21-archwiki-hyprland.md).

### 3.2 La API `hl.*` en la práctica (ejemplos reales del usuario)

El usuario ya usa prácticamente toda la superficie citada en el encargo. Ejemplos copiados
de `../configuracion-actual/hypr/config/`:

```lua
-- hl.config: categorías anidadas (decorations.lua)
hl.config({
    general   = { gaps_in = 3, gaps_out = 8, border_size = 2,
                  col = { active_border = { colors = { CACHYLGREEN, CACHYDGREEN }, angle = 45 } } },
    decoration = { rounding = 10, active_opacity = 0.95, inactive_opacity = 0.85,
                   blur = { size = 5, passes = 4, special = true } },
})

-- hl.curve / hl.animation (animations.lua)
hl.curve("quick", { type = "bezier", points = { {0.15, 0}, {0.1, 1} } })
hl.animation({ leaf = "global", enabled = true, speed = 3, bezier = "quick" })
hl.animation({ leaf = "windows", enabled = true, speed = 3, spring = "easy", style = "slide" })

-- hl.bind + hl.get_config + hl.config en vivo (binds.lua, función de zoom)
local function zoomfunction(value)
    local zoomvalue = hl.get_config("cursor:zoom_factor")
    if (zoomvalue + value) > 3.0 then hl.config({ cursor = { zoom_factor = 3.0 } })
    else hl.config({ cursor = { zoom_factor = zoomvalue + value } }) end
end

-- hl.window_rule / hl.layer_rule / hl.workspace_rule
hl.window_rule({ match = { class = "firefox" }, opacity = "1.0 override" })
hl.layer_rule({ name = "noctalia", match = { namespace = "^noctalia-(bar-.+|...)$" },
                no_anim = true, ignore_alpha = 0.5, blur = true, blur_popups = true })
hl.workspace_rule({ workspace = "1", monitor = MONITOR1, default = true, persistent = true })

-- hl.on + hl.exec_cmd (autostart.lua)
hl.on("hyprland.start", function()
    hl.exec_cmd("dbus-update-activation-environment --systemd --all")
    hl.exec_cmd("noctalia")
end)

-- hl.monitor (monitors.lua) y hl.gesture (inputs.lua)
hl.monitor({ output = MONITOR1, mode = "preferred", position = "auto", scale = "auto" })
hl.gesture({ fingers = 4, direction = "horizontal", action = "workspace" })
```

**Hecho.** `hl.exec_cmd()` es asíncrono (no necesita `& disown`) y `hl.get_config()` devuelve
el tipo subyacente (para `gaps_in`, una tabla `{top,left,right,bottom}`)
([Lua utilities](sources/2026-11-21-hyprland-lua-utilities.md)). El usuario usa `"cursor:
zoom_factor"` con dos puntos mientras la wiki documenta puntos: **Opinión**, verificar con
`hyprctl eval` cada clave nueva. Otras utilidades: `hl.get_windows()`,
`hl.get_active_workspace()`, `hl.get_layers()`, `hl.version()`, `hl.timer()`,
`hl.get_loaded_plugins()`, `hl.is_key_down()`, `hl.dispatch()`, `reload_config()` (0.57.0) y
el evento `config.unload` para limpiar estado Lua
([Events](sources/2026-11-21-hyprland-events.md),
[releases](sources/2026-11-21-hyprland-releases.md)).

### 3.3 Trampas del modelo de eventos

**Hecho.** Los callbacks de binds corren en el event loop: `io.popen`, red,
`wl-paste`/`xclip` o sleeps **congelan la entrada y el escritorio**; usar
`hl.dsp.exec_cmd(...)` y acotar con `timeout`
([Binds](sources/2026-11-21-hyprland-binds.md),
https://wiki.hypr.land/configuring/core/binds/). Una condición escrita como argumento
directo de `hl.bind` se resuelve al cargar la config: hay que envolverla en `function()`
para evaluarla en cada pulsación. `hl.unbind` es sensible a mayúsculas, y el prefijo
`code:` permite enlazar por código físico (el usuario lo usa en `digitCode(d)` para su
AZERTY). **Hecho.** Hyprland programa **un único** prop-refresh al final del evento: crear
una workspace rule no cambia `gaps_in` hasta que termina la función, y abusar de
`hl.exec_scheduled_prop_refresh_immediately()` ralentiza; `config.props_refreshed` cuenta
los disparos ([Lua utilities](sources/2026-11-21-hyprland-lua-utilities.md)).

---

## 4. Estructura modular del usuario

`~/.config/hypr/hyprland.lua` es solo un cargador de 13 módulos:

```lua
require("config.animations")   require("config.autostart")  require("config.colors")
require("config.decorations")  require("config.variables")  require("config.environment")
require("config.inputs")       require("config.binds")      require("config.misc")
require("config.monitors")     require("config.windowrules") require("config.workspaces")
```

Fuente: [hyprland.lua](../configuracion-actual/hypr/hyprland.lua).

| Módulo | Contenido | API principal |
|---|---|---|
| `animations.lua` | 6 beziers + 2 springs + 5 leafs | `hl.curve`, `hl.animation` |
| `autostart.lua` | dbus, Noctalia, xhost | `hl.on`, `hl.exec_cmd` |
| `colors.lua` | globals `CACHYLGREEN`…`CACHYGRAY` | variables Lua globales |
| `decorations.lua` | gaps, bordes, gradiente 45°, blur, opacidad | `hl.config` |
| `variables.lua` | apps, `MONITOR1..3`, `NUM_WPM=3` | variables globales |
| `environment.lua` | plantilla de variables (UWSM) | `hl.env` (comentado) |
| `inputs.lua` | `kb_layout="es"`, `accel_profile="flat"`, 4 gestures | `hl.config`, `hl.gesture` |
| `binds.lua` | atajos, fix AZERTY, delega a `noctalia msg` | `hl.bind`, `hl.dsp`, `hl.get_config` |
| `misc.lua` | dwindle, splash, swallow, `vrr=3`, `direct_scanout=2` | `hl.config` |
| `monitors.lua` | VGA-1 `preferred/auto/auto` | `hl.monitor` |
| `windowrules.lua` | PiP, gaming, flotantes, opacidad, capa Noctalia | `hl.window_rule`, `hl.layer_rule` |
| `workspaces.lua` | gaming + workspaces 1-3 persistentes | `hl.workspace_rule` |
| `xdph.conf` | configuración del portal (archivo `.conf` ajeno al parser de Hyprland) | — |

**Hecho.** El orden de `require` importa para las globales: `colors.lua` se carga antes que
`decorations.lua`, que usa `CACHYLGREEN`/`CACHYDGREEN`/`CACHYGRAY`. Desde 0.56.1 Hyprland ya
no destruye `package.path`, lo que hace viable este patrón
([releases](sources/2026-11-21-hyprland-releases.md)). **Opinión.** El aviso de deprecación
es para `hyprland.conf`, no para `xdph.conf` del portal.

---

## 5. `hyprctl`: la interfaz de observación y cambio en caliente

**Hecho.** `hyprctl` es la utilidad que se comunica con el display server; permite
dispatchers, keywords, consultas e información; existen además dos sockets UNIX que emiten
eventos de foco, creación de ventanas/workspaces, etc.
([ArchWiki](sources/2026-11-21-archwiki-hyprland.md),
https://wiki.archlinux.org/title/Hyprland).

| Comando | Uso concreto aquí |
|---|---|
| `hyprctl version` | confirmar 0.57.2, commit y ABI |
| `hyprctl monitors` | VGA-1, 1440×900@59.89, `scale=1` |
| `hyprctl clients` | apps en Xwayland, reglas/tags aplicadas |
| `hyprctl workspaces` | workspaces persistentes y `name:gaming` |
| `hyprctl getoption decoration.blur.size` | valor efectivo tras `reload` |
| `hyprctl reload` | recargar `hyprland.lua` (también al guardar) |
| `hyprctl eval 'hl.config({ ["decoration.blur.size"] = 3 })'` | cambio en caliente, **no persistente** |
| `hyprctl dispatch <dispatcher>` | ejecutar dispatchers desde scripts |
| `hyprctl hyprpaper listloaded` | subcomando de ecosistema (ArchWiki) |

**Hecho.** `hyprctl eval` para modificar opciones y el carácter no persistente de esos
cambios están documentados en [Config options](sources/2026-11-21-hyprland-config-options.md).
**Hecho.** Desde 0.56.0 existe un **REPL Lua interactivo** en `hyprctl`
([releases](sources/2026-11-21-hyprland-releases.md)), muy útil para probar `hl.curve()` o
`hl.animation()` sin editar archivos.

---

## 6. Integración con Noctalia 5.6.0

**Hecho.** La documentación oficial de Noctalia prescribe: arrancar con
`hl.on("hyprland.start", function() hl.exec_cmd("noctalia") end)`, workspaces persistentes,
atajos IPC `noctalia msg ...`, desactivar las animaciones de capa de Hyprland para
`noctalia-*` (si no, «panel tearing») y aplicar `ignore_alpha=0.5`, `blur=true`,
`blur_popups=true`
([integración](sources/2026-11-21-noctalia-hyprland-integration.md),
https://github.com/noctalia-dev/noctalia/blob/main/docs/user/compositor-settings/hyprland.mdx).

**Hecho.** El usuario ya cumple todo eso: `autostart.lua`, `workspaces.lua`, `binds.lua` y la
regla de capa de `windowrules.lua` reproducen **exactamente** el regex oficial. El tamaño
recomendado para la ventana de ajustes es `monitor_w*0.5625 monitor_h*0.85`; el usuario usa
`0.70/0.70` — **Opinión**: diferencia cosmética legítima en 1440×900.

**Hecho.** Noctalia genera una plantilla `hyprland.lua` con colores M3 que devuelve
`{ colors = ..., apply_theme = apply_theme }`; `apply_theme()` llama a `hl.config()` para
bordes y colores de grupo/groupbar
([plantilla](sources/2026-11-21-noctalia-hyprland-template.md),
https://github.com/noctalia-dev/noctalia/blob/main/assets/templates/hyprland/hyprland.lua).

```lua
-- Patrón sugerido por la integración oficial (permisos)
hl.config({ ecosystem = { enforce_permissions = true } })
hl.permission("^/usr/bin/noctalia$", "screencopy", "allow")
hl.permission("^hl-virtual-keyboard-noctalia$", "keyboard", "allow")
```

**Hecho.** Las reglas de permisos **no se recargan** con `hyprctl reload`: hay que
reiniciar Hyprland. **Hecho.** En la config actual `ecosystem` solo tiene
`no_update_news`/`no_donation_nag`, por lo que `enforce_permissions` queda en `false` (default).
**Opinión.** Si se activa, hay que añadir las dos reglas anteriores o el screenshot y el
autopaste del launcher de Noctalia fallarán.

**Opinión.** La plantilla de Noctalia es la vía natural para resolver el hallazgo del
perfil: hoy conviven el verde CachyOS de los bordes de Hyprland y el azul/violeta M3 del
resto del escritorio. `require()` de la plantilla y llamar a `apply_theme()` desde un
evento `config.reloaded`/`window.active` unificaría la paleta sin editar `decorations.lua`.

---

## 7. Consideraciones para hardware antiguo (Sandy Bridge)

**Hecho.** El perfil reporta un único monitor 1440×900 @ 59.89 Hz, sin VRR ni HDR, con
`directScanoutBlockedBy` y `tearingBlockedBy: … hw cursor`. La wiki de rendimiento
recomienda escalado entero si hay tirones, subir `INTEL_GPU_MIN_FREQ_ON_AC/BAT` con TLP,
desactivar blur con `hl.config({ ["decoration.blur.enabled"] = false })` y usar `gamescope`
para Proton ([Performance](sources/2026-11-21-hyprland-performance.md),
https://wiki.hypr.land/configuring/extra/performance/). El usuario ya usa `scale="auto"`
(=1) y `xwayland.force_zero_scaling=true`.

Opciones de la wiki con impacto directo en equipos débiles
([Config options](sources/2026-11-21-hyprland-config-options.md)):

| Opción | Default | Recomendación (opinión) |
|---|---|---|
| `render.new_render_scheduling` | `false` | «improves FPS on underpowered devices» → probar `true` |
| `debug.vfr` | `true` | «Heavily recommended to leave enabled to conserve resources» → no tocar |
| `misc.disable_autoreload` | `false` | «Might save on battery» → opcional |
| `misc.render_unfocused_fps` | `15` | tope para ventanas `render_unfocused`; dejar |
| `render.use_fp16` | `2` (solo HDR) | en SDR no activa → bien |
| `render.direct_scanout` | `0` | el usuario usa `2` (auto con contenido `game`); útil con gaming |
| `misc.vrr` | `0` | el usuario usa `3`; **sin hardware VRR es inerte** |
| `decoration.blur.new_optimizations` | `true` | «massively improve performance» → mantener |
| `decoration.blur.xray` | `false` | reduce mucho el coste de blur en flotantes → valorar `true` |

**Opinión.** En 1440×900 y 60 Hz el presupuesto es ajustado: el coste de cada frame se
multiplica por las pasadas de blur y por cualquier estilo `loop`. La estrategia correcta es
**medir antes de subir** (doc 08) y mantener `render.new_render_scheduling=true` como
único cambio «gratis» de rendimiento.

---

## 8. Errores de migración detectados / frecuentes

| # | Error | Evidencia | Consecuencia / corrección |
|---|---|---|---|
| 1 | Seguir usando `hyprland.conf` | Deprecación 0.56.1 (#15538); ArchWiki «since 0.55…» | Migrar a `hl.config()` |
| 2 | **`dampening` en springs** | El config usa `dampening`; 0.57.0 corrigió el typo (#15993); wiki dice `damping` | **Hecho**: discrepancia real. **Opinión**: la clave podría ignorarse; renombrar y verificar |
| 3 | Eventos `created` antiguos | 0.57.0: `created` → `created_early` (#16221) | Reglas mal disparadas |
| 4 | Duplicar una opción | «the latest line will always shadow…» | El valor esperado no se aplica |
| 5 | Condición fuera de `function()` en `hl.bind` | [Binds](sources/2026-11-21-hyprland-binds.md) | Se resuelve al cargar |
| 6 | Llamadas bloqueantes | [Binds](sources/2026-11-21-hyprland-binds.md) | Congela input y escritorio |
| 7 | `hl.unbind` mal capitalizado | [Binds](sources/2026-11-21-hyprland-binds.md) | No desenlaza |
| 8 | Esperar prop-refresh inmediato | [Lua utilities](sources/2026-11-21-hyprland-lua-utilities.md) | Cambios visibles al terminar el evento |
| 9 | Animaciones de capa con Noctalia | [Integración](sources/2026-11-21-noctalia-hyprland-integration.md) | Panel «tearing» (ya mitigado) |
| 10 | Permisos + solo `reload` | [Integración](sources/2026-11-21-noctalia-hyprland-integration.md) | Requiere reinicio |
| 11 | `hl.get_config()` como escalar | [Lua utilities](sources/2026-11-21-hyprland-lua-utilities.md) | `gaps_in` es tabla |
| 12 | `speed` como segundos | [Animations](sources/2026-11-21-hyprland-animations.md) | Son decisegundos: `3`≈300 ms |

---

## 9. Resumen ejecutivo

**Hecho.** Hyprland 0.57.2 combina un compositor Wayland con renderizador propio
(Aquamarine 0.16) y configuración íntegramente Lua. Lo que más afecta al rice en 0.56→0.57
es la API `hl.*`, la deprecación de `.conf`, scene composition, blur intercambiable y
proporcional, window wobble, pointer transforms y el fix `dampening`→`damping`.

**Opinión.** El usuario ya está bien modularizado; tres acciones de mayor retorno:
corregir `damping`, unificar la paleta CachyOS/M3 con la plantilla de Noctalia y tratar
`passes=4` y cualquier estilo `loop` como sospechosos antes de añadir efectos (doc 08).
