# 08 · Animaciones y efectos: teoría, práctica y coste en Sandy Bridge

> Investigación 2026-11-21/22. Contexto real: Hyprland 0.57.2, CachyOS, **un** monitor
> 1440×900 @ 59.89 Hz, iGPU Intel 2.ª generación (Sandy Bridge), sin VRR ni HDR. La config
> viva está en `../configuracion-actual/hypr/config/animations.lua` y `decorations.lua`.
> Convención: **Hecho** = verificable en fuentes/config; **Opinión** = recomendación
> incentivada por el hardware. El doc 02 cubre la arquitectura y la migración Lua.

---

## 1. Modelo mental: el árbol de animaciones

**Hecho.** Las animaciones se declaran con `hl.animation({ leaf, enabled, speed, bezier|spring, style? })`.
`leaf` es el ámbito; `speed` son **decisegundos** (100 ms cada uno), de modo que
`speed = 3` ≈ 300 ms; si `enabled = false` se pueden omitir el resto de argumentos
([Animations](sources/2026-11-21-hyprland-animations.md),
https://wiki.hypr.land/configuring/core/animations/).

**Hecho.** Las animaciones forman un **árbol**: si un leaf no está definido, hereda los
valores de su padre:

```
global
 ├─ windows  (slide, popin, gnomed)
 │   ├─ windowsIn     · apertura
 │   ├─ windowsOut    · cierre
 │   └─ windowsMove   · mover/arrastrar/redimensionar
 ├─ layers   (slide, popin, fade) ── layersIn / layersOut
 ├─ fade ── fadeIn, fadeOut, fadeSwitch, fadeShadow, fadeGlow, fadeDim,
 │          fadeLayers(In/Out), fadePopups(In/Out), fadeDpms
 ├─ border          · velocidad del cambio de color del borde
 ├─ borderangle     · estilos once (default) / loop
 ├─ shadowangle     · estilos once / loop
 ├─ glowangle       · estilos once / loop
 ├─ workspaces (slide, slidevert, fade, slidefade, slidefadevert)
 │   ├─ workspacesIn / workspacesOut
 │   └─ specialWorkspace ── specialWorkspaceIn / specialWorkspaceOut
 ├─ zoomFactor
 └─ monitorAdded
```

### Estado real del usuario

```lua
-- animations.lua (copia literal)
hl.curve("easeOutQuint",   { type = "bezier", points = { {0.23, 1},   {0.32, 1}   } })
hl.curve("easeInOutCubic", { type = "bezier", points = { {0.65, 0.05}, {0.36, 1}  } })
hl.curve("linear",         { type = "bezier", points = { {0, 0},      {1, 1}      } })
hl.curve("almostLinear",   { type = "bezier", points = { {0.5, 0.5},  {0.75, 1}   } })
hl.curve("quick",          { type = "bezier", points = { {0.15, 0},   {0.1, 1}    } })
hl.curve("overshoot",      { type = "bezier", points = { {0.5, 0.9},  {0.1, 1.1}  } })
hl.curve("easy",           { type = "spring", mass = 1, stiffness = 500, dampening = 35 })
hl.curve("rubber",         { type = "spring", mass = 1, stiffness = 200,  dampening = 15 })

hl.animation({ leaf = "global",              enabled = true, speed = 3, bezier = "quick" })
hl.animation({ leaf = "windows",             enabled = true, speed = 3, spring = "easy", style = "slide" })
hl.animation({ leaf = "workspaces",          enabled = true, speed = 5, bezier = "quick", style = "slide" })
hl.animation({ leaf = "specialWorkspaceIn",  enabled = true, speed = 2, bezier = "quick", style = "slide top" })
hl.animation({ leaf = "specialWorkspaceOut", enabled = true, speed = 2, bezier = "quick", style = "slide bottom" })
```

| Leaf | Valor efectivo | Duración aprox. | Herencia |
|---|---|---|---|
| `global` | bezier `quick`, speed 3 | ~300 ms | base del resto |
| `windows` | spring `easy`, `slide` | gobernada por física | no hereda `quick` |
| `windowsIn/Out/Move` | — | — | heredan `windows` |
| `workspaces` | bezier `quick`, `slide`, speed 5 | ~500 ms | propio |
| `specialWorkspaceIn` | `quick`, `slide top`, speed 2 | ~200 ms | propio |
| `specialWorkspaceOut` | `quick`, `slide bottom`, speed 2 | ~200 ms | propio |
| `fade*`, `border*`, `layers*` | — | — | heredan `global` (`quick`) |

**Opinión.** La combinación es coherente: el `global` rápido da respuesta inmediata a
fades y bordes, `windows` usa un muelle casi crítico para una entrada «con peso», y el
special workspace entra/sale desde arriba/abajo en 200 ms. Es una base sólida; el único
problema detectable es la clave `dampening` (§2.2).

---

## 2. Bézier vs springs

### 2.1 Curvas Bézier

**Hecho.** Una Bézier cúbica tiene 4 puntos; se configuran los dos intermedios:

```lua
hl.curve("overshoot", { type = "bezier", points = { {0.5, 0.9}, {0.1, 1.1} } })
```

**Hecho.** Las curvas del usuario, con su carácter según los puntos de control:

| Curva | P1 / P2 | Carácter | Uso recomendado |
|---|---|---|---|
| `easeOutQuint` | (0.23,1) (0.32,1) | arranca muy rápido y se asienta de golpe | workspaces largos, overlays |
| `easeInOutCubic` | (0.65,0.05) (0.36,1) | acelera y frena simétrico | transiciones «pesadas» |
| `linear` | (0,0) (1,1) | sin easing | animaciones mecánicas/depuración |
| `almostLinear` | (0.5,0.5) (0.75,1) | casi lineal, cola suave | barridos sutiles |
| `quick` | (0.15,0) (0.1,1) | salida inmediata, frenada corta | **global/workspaces actuales** |
| `overshoot` | (0.5,0.9) (0.1,1.1) | sobrepasa 1 (Y=1.1) → rebote visual | pop-in, acentos; no abusar |

**Opinión.** Para un iGPU, las Bézier son «baratas»: el coste está en el número de frames
que la animación fuerza, no en la curva en sí. `quick` es la elección correcta para no
multiplicar frames; `overshoot` debe reservarse a un leaf pequeño (`windowsIn`), porque sus
oscilaciones percibidas invitan a subir la duración.

### 2.2 Springs y el coeficiente de amortiguación

**Hecho.** Un spring se define con `mass`, `stiffness` y `damping`; la wiki recomienda
mantener `mass = 1` y ajustar los otros dos: más *stiffness* = más velocidad, más *damping*
= menos rebote ([Animations](sources/2026-11-21-hyprland-animations.md)). Define
ζ = c / (2·√(k·m)):

| Régimen | ζ | Sensación |
|---|---|---|
| Crítico | = 1 | asienta rápido sin sobrepasar |
| Subamortiguado | < 1 | oscila; amplitud decae exponencialmente |
| Sobreamortiguado | > 1 | vuelve despacio, sin rebote |

**Hecho.** La wiki sugiere «damping around 0.6 to 0.8» en términos de ζ para una respuesta
viva. Traducido a los valores del usuario (k=500, m=1 → c_crítica = 2√500 ≈ 44.7;
k=200 → c_crítica ≈ 28.3):

| Spring del usuario | k | c | ζ calculado | Interpretación |
|---|---|---|---|---|
| `easy` | 500 | 35 | ≈ 0.78 | casi crítico, sin apenas rebote — ideal para ventanas |
| `rubber` | 200 | 15 | ≈ 0.53 | subamortiguado, rebote elástico notable |

**Hecho — hallazgo importante.** `animations.lua` escribe `dampening` en ambos springs,
pero la release 0.57.0 corrigió el typo `dampening` → `damping` (#15993) y la wiki actual
documenta `damping`. **Opinión**: en 0.57.2 la clave antigua podría no aplicarse, en cuyo
caso `easy`/`rubber` estarían usando el damping por defecto y el análisis ζ anterior no
sería efectivo. Corrección:

```lua
-- ✅ correcto en 0.57.x
hl.curve("easy",   { type = "spring", mass = 1, stiffness = 500, damping = 35 })
hl.curve("rubber", { type = "spring", mass = 1, stiffness = 200, damping = 15 })
```

Verificar siempre el valor efectivo con `hyprctl` / el REPL Lua antes de dar por buena
cualquier curva (§6).

---

## 3. Leafs, estilos y duración

**Hecho.** Estilos por leaf: `windows` → `slide`, `popin`, `gnomed`; `layers` → `slide`,
`popin`, `fade`; `workspaces` → `slide`, `slidevert`, `fade`, `slidefade`,
`slidefadevert`; `*angle` → `once` (default) o `loop`. Modificadores: `popin 80%`,
`slidefade 20%` y `slide left|right|top|bottom`. Ejemplo:
`hl.animation({ leaf="workspaces", enabled=true, speed=8, curve="default", style="slidefade 20%" })`.

| leaf | Estilo actual | Alternativa útil | Coste relativo |
|---|---|---|---|
| `windows` | `slide` | `popin 90%` (scale), `gnomed` | slide bajo; popin medio |
| `fadeSwitch` | hereda `quick` | `enabled = false` | muy bajo |
| `workspaces` | `slide` | `slidefade 20%`, `fade` | slide bajo; fade medio |
| `specialWorkspaceIn/Out` | `slide top/bottom` | `fade` | bajo |
| `borderangle` | no definido (`once`) | **`loop` ✗** | **muy alto** |
| `shadowangle` / `glowangle` | no definido | **`loop` ✗** | **muy alto** |

**Hecho — advertencia literal:** `loop` en `*angle` obliga a renderizar **constantemente**
a la frecuencia de refresco, estresando CPU/GPU incluso con animaciones desactivadas
([Animations](sources/2026-11-21-hyprland-animations.md)). El borde del usuario es un
gradiente **estático** a 45°, así que no hay coste de `loop`. **Opinión.** Gradientes sí,
gradientes en bucle no. **Hecho.** `misc.animate_manual_resizes` y
`misc.animate_mouse_windowdragging` son `false` por defecto
([Config options](sources/2026-11-21-hyprland-config-options.md)); **Opinión**: mantenerlos.

---

## 4. Blur: el efecto dominante en el presupuesto de frames

### 4.1 Parámetros

**Hecho.** Categoría `decoration.blur` (valores por defecto entre paréntesis):

| Opción | Default | Effecto | Coste en iGPU |
|---|---|---|---|
| `enabled` | `true` | activa blur Kawase | base |
| `size` | `8` | distancia de desenfoque | ↑ con tamaño |
| `passes` | `1` | número de pasadas | **↑↑ lineal** (0-10) |
| `special` | `false` | difumina tras special workspace | **«expensive»** según la wiki |
| `new_optimizations` | `true` | «massively improve performance» | **↓** mantener |
| `xray` | `false` | flotantes ignoran ventanas tileadas en su blur | **↓↓** muy recomendable |
| `variant` | `kawase` | patrón de blur | ver §4.2 |
| `proportional` | `false` | fuerza ∝ opacidad del píxel; requiere `render.use_shader_blur_blend` | ↑ |
| `popups`, `popups_ignorealpha` | `false`, `0.2` | blur de menús | ↑ |
| `input_methods` | `false` | blur de IME | ↑ |
| `noise` / `vibrancy` / `contrast` / `brightness` | `0.0117` / `0.1696` / `0.8916` / `1` | modulación estética | bajo |

**Hecho.** `size` y `passes` deben ser ≥ 1 para que el blur se aplique; aumentar `passes`
es necesario para que un `size` alto no se vea mal, pero «más passes = más carga para la
GPU» ([Config options](sources/2026-11-21-hyprland-config-options.md)).
**Hecho.** El usuario tiene `size=5`, `passes=4`, `special=true` y **no** ha tocado
`new_optimizations` (queda `true`) ni `xray` (queda `false`).

**Opinión.** `passes=4` con `special=true` es la configuración más exigente de todo el
rice. No es catastrófica a 1440×900, pero es el primer candidato a recortar si aparecen
tirones: `passes=2` + `xray=true` mantiene el aspecto «cristal» de Noctalia con bastante
menos trabajo. La propia documentación de Noctalia recomienda
`blur = { enabled=true, xray=true, size=3, passes=2, vibrancy=0.1696 }`
([integración](sources/2026-11-21-noctalia-hyprland-integration.md)).

### 4.2 Variantes intercambiables (0.57.0)

**Hecho.** Desde 0.57.0 el blur tiene variantes seleccionables (#15661):
`kawase` (default), `acrylic`, `aurora`, `drops`, `fluid_jar`, `frost`, `haze`,
`heat_shimmer`, `prism`, `ripple`, `water`. La wiki advierte que la variante «may
significantly increase GPU and CPU usage». Algunas son **animadas**: `aurora.speed`
(default 1), `drops.speed` (3), `heat_shimmer.speed` (1), `water.duration` (12 s),
`ripple.duration` (0.45 s). `fluid_jar.precision` indica explícitamente que 2× es un buen
compromiso, 4× caro y 8× «extreme and unnecessary».

| Variante | Coste típico | Veredicto para Sandy Bridge |
|---|---|---|
| `kawase` | bajo | **mantener** |
| `acrylic`, `haze`, `prism`, `frost` | medio-alto | solo si se mide y sobra margen |
| `aurora`, `drops`, `heat_shimmer`, `water`, `ripple` | alto + frames continuos | **evitar**: mismo problema del `loop` |
| `fluid_jar` | muy alto (simulación 2D) | **evitar** |

**Hecho.** `decoration.blur.proportional` llegó en 0.57.0 (#16643) y hace que la fuerza del
blur sea proporcional a la opacidad del píxel; requiere `render.use_shader_blur_blend =
true`, que la wiki marca como experimental y «glitched on rotated screens» (irrelevante con
un solo monitor sin rotación). **Opinión.** Es un efecto elegante para ventanas con
opacidad parcial —justo el caso del usuario (0.95/0.85)— pero hay que medirlo: añade un
blend de shader por píxel.

### 4.3 Blur en capas (Noctalia)

```lua
hl.layer_rule({
  name = "noctalia",
  match = { namespace = "^noctalia-(bar-.+|notification|dock|panel|attached-panel|osd|window-switcher)$" },
  no_anim = true,          -- evita el "panel tearing" documentado por Noctalia
  ignore_alpha = 0.5,
  blur = true,
  blur_popups = true,
})
```

**Hecho.** Es literalmente la regla que recomienda Noctalia y la que ya tiene el usuario.
**Opinión.** El área de una barra de 35 px es pequeña, así que su blur es barato; el coste
está en las ventanas, no en la capa. Si se activa `no_blur` por regla en juegos o terminales
se reduce bastante la carga cuando hay contenido en movimiento debajo.

---

## 5. El resto de decoraciones

| Efecto | Valor real | Coste | Recomendación (opinión) |
|---|---|---|---|
| `rounding = 10` (+ `rounding_power = 2` default) | esquinas redondeadas | bajo (máscara en shader) | mantener; `rounding_power=4` (squircle) es gratis también |
| Borde activo | gradiente `rgba(82dcccff)`→`rgba(007d6fff)` @45° | bajo si es estático | mantener; **no** usar `borderangle loop` |
| Borde inactivo | `rgba(798bb2ff)` | bajo | mantener |
| `active_opacity = 0.95` / `inactive_opacity = 0.85` | transparencia | **medio**: obliga a blending | mantener, pero compensar con `1.0 override` (ya hecho para firefox/terminales/mpv) |
| `fullscreen_opacity = 1` | opaco a pantalla completa | nulo | correcto; ayuda a `direct_scanout` |
| `dim_special = 0.3` | atenúa el resto al abrir special | bajo | mantener; default 0.2 |
| `shadow` | default `enabled=true`, `range=4`, `render_power=3` | medio-bajo | Noctalia recomienda `range=4, render_power=3` → ya equivalente |
| `glow` | default `enabled=false` | medio-alto si se activa | **dejar apagado**; además existe regla `no_glow` (0.57) |
| `motion_blur` | default `enabled=false` | **alto** (7 samples) | **no activar** |
| `wobble` | default `enabled=false` | medio (mesh 12×4) | opcional; usar `no_wobble` en juegos/terminales |
| `dim_inactive` / `dim_strength` | default `false` / `0.5` | medio | no activar |

**Hecho.** La opacidad es **un producto**: `active_opacity=0.5` más una regla `opacity=0.5` da
0.25; `override` fija un valor absoluto en vez de multiplicar; se admiten hasta tres valores
(activo/inactivo/fullscreen) y cualquier producto > 1.0 produce glitches
([Config options](sources/2026-11-21-hyprland-config-options.md)).

```lua
-- windowrules.lua del usuario: estas reglas REDUCEN coste, no lo aumentan
hl.window_rule({ match = { class = "^(firefox|zen)$" },      opacity = "1.0 override" })
hl.window_rule({ match = { class = terminals },              opacity = "1.0 override" })
hl.window_rule({ match = { class = "^(mpv|...|.*vlc.*)$" },  opacity = "1.0 override" })
```

**Hecho.** Window wobble se introdujo en 0.57.0 (#14920) junto con la regla `no_wobble`
(#15735) y `no_glow` (#15863); sus parámetros son `mesh` (12, rango 2-32), `stiffness`
(200), `damping` (12), `mass` (1), `intensity` (0.2) y los epsilons de estabilidad
([releases](sources/2026-11-21-hyprland-releases.md),
[Config options](sources/2026-11-21-hyprland-config-options.md)). **Opinión.** Si se activa,
que sea con `no_wobble = true` en `steam_app*`, `gamescope` y terminales: son las ventanas
donde una deformación elástica distrae y donde cada frame extra cuenta.

---

## 6. Coste de render y cómo medirlo en este iGPU

### 6.1 Qué fuerza un frame

**Hecho.** `debug.vfr` (variable frame rate) está activado por defecto y la wiki lo
considera «heavily recommended to leave enabled to conserve resources»; `debug.overlay`
imprime un overlay de rendimiento y, para que sea preciso, hay que **desactivar VFR**
temporalmente. `debug.damage_tracking = 2` (full) es el default y no debe cambiarse;
`debug.damage_blink` tiene advertencia epiléptica.
([Config options](sources/2026-11-21-hyprland-config-options.md)).

En la práctica, un marco se renderiza por: daño (damage) en pantalla, animaciones activas,
efectos animados (`loop`, variantes de blur animadas) y movimiento del cursor si la
configuración lo fuerza. Cada píxel dañado puede pasar por: blending de opacidad → blur
(N pasadas) → máscara de rounding → sombra → borde. Por eso blur y loops dominan el coste.

### 6.2 Protocolo de medición (recomendación)

1. **Línea base:** `hyprctl version`, `hyprctl monitors` y
   `hyprctl getoption decoration.blur.passes`.
2. **Telemetría:** `sudo intel_gpu_top` al abrir/cerrar ventanas y cambiar de workspace;
   comparar `% busy` de Render/Blitter. Lo sugiere el [perfil](../00-perfil-del-sistema.md).
3. **Overlay:** activar `debug.overlay=true` y `debug.vfr=false` vía `hyprctl eval`,
   observar frames y **devolver VFR a `true`** al terminar.
4. **A/B de una sola variable:** `passes` 4→2, `special` true→false o `xray` false→true;
   `hyprctl reload` y repetir 2-3 veces. Nunca tres cambios a la vez.
5. **Peor caso:** panel/launcher de Noctalia (blur de capa) + ventana flotante sobre vídeo.
6. **Reglas:** `hyprctl clients` (Xwayland, `no_blur`, `opacity override`) y
   `hyprctl workspaces` (special).
7. **Si hay TLP:** subir `INTEL_GPU_MIN_FREQ_ON_AC` de 300 a ~500 en `/etc/tlp.conf`
   ([Performance](sources/2026-11-21-hyprland-performance.md)).

**Opinión.** Una señal de alarma clara en Sandy Bridge es que el simple hecho de mover una
ventana flotante con blur haga subir `intel_gpu_top` de forma sostenida. Eso indica que el
coste está en el blur y no en las curvas.

---

## 7. Recomendaciones concretas para no degradar el rendimiento

### 7.1 Perfil conservador (mantener)

1. `blur.new_optimizations=true`, `rounding=10`, `debug.vfr=true`, `render.use_fp16=2`.
2. **Desactivados**: `motion_blur`, `glow`, estilos `loop` en `*angle`.
3. `animations.enabled=true` con `quick` en `global` (300 ms barato); `no_anim` en Noctalia y
   `1.0 override` en navegador/terminales/reproductor (ya presentes).
4. Evitar blur animado y `fluid_jar`; no subir `passes` de 4.
5. Probar `render.new_render_scheduling=true` (wiki: «improves FPS on underpowered devices»).

### 7.2 Perfil rifado-seguro (cambios propuestos)

```lua
-- En decorations.lua: mismo aspecto, menos pasadas
hl.config({
  decoration = {
    blur = {
      size = 5,
      passes = 2,      -- antes 4
      special = false, -- antes true; se puede volver a activar si sobra margen
      xray = true,     -- flotantes ignoran tiled en el blur
      new_optimizations = true,
    },
  },
  render = { new_render_scheduling = true },
})
```

**Hecho.** El patrón para alternar en caliente está documentado: `hl.get_config()` lee el
valor y `hl.config()` lo cambia; `hl.bind` puede envolver la lógica en una función
([Lua utilities](sources/2026-11-21-hyprland-lua-utilities.md)).

```lua
-- Atajo "modo rendimiento" (ejemplo; usa digitCode del propio binds.lua)
local fullFx = true
hl.bind("SUPER + " .. digitCode(0), function()
  fullFx = not fullFx
  hl.config({
    ["decoration.blur.size"]    = fullFx and 5 or 3,
    ["decoration.blur.passes"]  = fullFx and 4 or 2,
    ["decoration.blur.special"] = fullFx,
    ["animations.enabled"]      = fullFx,
  })
end)
```

**Hecho.** `animations` es una categoría con opción `enabled` (default `true`), así que la
clave plana `["animations.enabled"]` es válida
([Config options](sources/2026-11-21-hyprland-config-options.md)).

### 7.3 Opt-in deliberado (solo si la medición lo permite)

```lua
-- Blur proporcional: más limpio con 0.95/0.85, pero añade blend de shader
hl.config({
  ["decoration.blur.proportional"]    = true,
  ["render.use_shader_blur_blend"]    = true,
})

-- Wobble elástico suave + exenciones
hl.config({
  decoration = { wobble = {
    enabled = true, mesh = 12, stiffness = 200,
    damping = 12, mass = 1, intensity = 0.2,
  }},
})
hl.window_rule({ match = { class = "^(steam_app.*|gamescope|kitty)$" }, no_wobble = true })
```

---

## 8. Hechos vs opiniones (resumen)

| Afirmación | Clasificación | Base |
|---|---|---|
| `speed` son decisegundos; `dampening`→`damping` en 0.57 | **Hecho** | [Animations](sources/2026-11-21-hyprland-animations.md), [releases](sources/2026-11-21-hyprland-releases.md) |
| `blur.special` es caro; `new_optimizations` mejora el rendimiento | **Hecho** | [Config options](sources/2026-11-21-hyprland-config-options.md) |
| `loop` en `*angle` renderiza a 60 fps aunque todo esté off | **Hecho (literal)** | [Animations](sources/2026-11-21-hyprland-animations.md) |
| Variantes de blur aumentan mucho CPU/GPU | **Hecho** | [Config options](sources/2026-11-21-hyprland-config-options.md) |
| Curvas actuales y borde estático: adecuados | **Opinión** | perfil de hardware |
| `passes=4`+`special=true`: primer recorte | **Opinión** | recomendación Noctalia (3/2/xray) |
| `1.0 override` reduce blending | **Opinión fundada** | opacidad es producto + `windowrules.lua` |
| `new_render_scheduling=true` conviene | **Opinión fundada** | «improves FPS on underpowered devices» ([Config options](sources/2026-11-21-hyprland-config-options.md)) |

**Cierre.** En este equipo el problema no es la elegancia de las curvas sino el número de
frames y de pasadas de shader. Bezier rápidos, springs casi críticos con la clave bien
escrita, blur Kawase con pocas pasadas y `xray`, gradientes estáticos, glow/motion-blur/loop
apagados y medición con `intel_gpu_top` antes de cualquier subida: esa es la receta para
mantener el rice intacto sin pagarlo en fluidez.
