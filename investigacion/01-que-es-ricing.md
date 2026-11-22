# 01 · ¿Qué es el *ricing*?

> Documento de investigación · Proyecto de ricing para CachyOS + Hyprland 0.57.2 (Lua) + Noctalia 5.6.0
> Fecha de consulta de las fuentes: 2026-11-21/22. Todas las fuentes citadas están archivadas en `sources/`.

## Convención de este documento

Para no mezclar lo que está demostrado con lo que se comenta en la comunidad, se usan tres marcas:

| Marca | Significado |
|---|---|
| **HECHO** | Afirmación respaldada por una fuente archivada en `sources/` o por la auditoría local (`00-perfil-del-sistema.md`). |
| **OPINIÓN** | Interpretación, juicio estético o recomendación del autor de este documento. |
| **INCIERTO** | Creencia extendida, dato no documentado en el corpus o fuentes que se contradicen entre sí. |

Las citas usan el formato `[Fuente](sources/2026-11-21-xxx.md)`; cuando aporta, se añade la URL original entre paréntesis.

---

## 1. Definición de *ricing*

**HECHO (delimitación operativa).** En esta investigación entendemos el *ricing* como **la personalización deliberada y detallista de la apariencia y la experiencia de uso de un escritorio Linux**, normalmente combinando: gestor de ventanas o compositor, temas, iconos, cursores, tipografías, paleta de colores, barra de estado, wallpaper, animaciones y atajos de teclado. El objeto de estudio no es solo "poner bonito": incluye la capa funcional (binds, reglas de ventanas, autostart, scripts) porque en la cultura Unix la estética y la configuración comparten el mismo archivo de texto.

La documentación oficial de Hyprland describe preciseamente ese terreno: el compositor configurado mediante un archivo que contiene "dispositivos y monitores, diseño, decoración y animaciones", además de "reglas de ventanas, atajos de teclado y comandos a ejecutar al inicio" ([ArchWiki · Hyprland](sources/2026-11-21-archwiki-hyprland.md), [URL original](https://wiki.archlinux.org/title/Hyprland)). La wiki de Hyprland separa además utilidades "imprescindibles" (daemon de notificaciones, PipeWire, portal XDG, agente polkit, fuentes) de la capa puramente visual ([Hyprland · Must-have](sources/2026-11-21-hyprland-must-have.md), [URL original](https://wiki.hypr.land/useful-utilities/must-have/)). Esa separación es útil: **ricing es la capa visible, pero depende de una capa invisible que debe funcionar**.

**OPINIÓN.** Definición corta: *ricing = diseño de interfaces aplicado a tu propio escritorio, con dotfiles como medio de expresión y como documento de configuración*. No es instalar un tema prefabricado ni programar un compositor: está en el punto medio.

### 1.1 *Ricing* frente a *overclocking* y frente a *rice*

| Concepto | Qué es | Se parece a *ricing* en… | Se diferencia en… |
|---|---|---|---|
| **Ricing** | Personalización estética + funcional del escritorio | — | — |
| **Overclocking** | Aumentar la frecuencia de reloj del hardware por encima de la especificación | Ambos son "tuning" y ambos pueden degradar la estabilidad si se excede | El overclocking actúa sobre **hardware** y busca **rendimiento**; el ricing actúa sobre **software** y busca **apariencia/experiencia**. **HECHO conceptual** |
| **Rice (arroz)** | Alimento; también *rice* / *ricer* como argot anglosajón con carga racial e histórica en la cultura automovilística | Solo el juego de palabras | No es un término técnico. **INCIERTO / CONTEXTUAL** (ver §8.1) |

**INCIERTO.** El corpus archivado **no contiene ningún estudio etimológico del término**. La explicación que suele circular en la comunidad deriva *ricing* de *rice/ricer* (argot despectivo ligado a coches importados y, en origen, a personas asiáticas), reapropiado de forma irónica por la comunidad Linux; también se oyen etimologías populares tipo *riot + icing* o *rice + -ing*. **Ninguna de ellas está confirmada por las fuentes de este proyecto**: deben tratarse como hipótesis, no como dato. Lo que sí es verificable es el uso actual del término como autodescripción de la personalización de escritorios, y su carga polémica (§8.1).

---

## 2. Historia y evolución (con lo que las fuentes sí documentan)

### 2.1 De los dotfiles al tiling WM

**HECHO parcial / INCIERTO en los detalles.** Guardar la configuración en archivos ocultos del `$HOME` (`.Xresources`, `.vimrc`, …) es anterior a la escena actual y se difundió con Unix y con los *tiling WMs* (dwm, i3, awesome, bspwm). **El corpus no archiva fuentes históricas sobre esa etapa**: la cronología concreta se marca como **INCIERTA**.

**HECHO.** Lo que sí se rastrea es la madurez del ecosistema: la wiki de Hyprland dedica páginas completas a *keybinds*, animaciones, reglas de ventanas y opciones ([Binds](sources/2026-11-21-hyprland-binds.md), [Animaciones](sources/2026-11-21-hyprland-animations.md), [Window Rules](sources/2026-11-21-hyprland-window-rules.md), [Config Options](sources/2026-11-21-hyprland-config-options.md); [URL base](https://wiki.hypr.land/)). Esa granularidad es la huella de años de cultura de dotfiles: el usuario afina un parámetro a la vez.

### 2.2 El giro Wayland

**HECHO.** ArchWiki describe Hyprland como "un compositor Wayland de mosaico independiente" con "mosaico dinámico, ventanas en pestañas, una base de código C++ limpia y legible, y un renderizador propio que ofrece animaciones de ventanas, esquinas redondeadas y Dual-Kawase Blur en ventanas transparentes" ([ArchWiki · Hyprland](sources/2026-11-21-archwiki-hyprland.md), [URL original](https://wiki.archlinux.org/title/Hyprland)). Es decir: lo que antes se lograba con parches y composición en X11 pasó a ser una prestación del compositor.

**HECHO.** Hyprland no viene solo: la wiki enumera utilidades que un entorno de escritorio (DE) proporcionaría automáticamente pero que un compositor no ([Hyprland · Must-have](sources/2026-11-21-hyprland-must-have.md), [URL original](https://wiki.hypr.land/useful-utilities/must-have/)); y una familia de aplicaciones propias —hyprpaper, hyprpicker, hypridle, hyprlock, hyprcursor, hyprsysteminfo, xdg-desktop-portal-hyprland— documentadas en [Hyprland · User ecosystem](sources/2026-11-21-hyprland-ecosystem-user.md) y en la [ArchWiki](sources/2026-11-21-archwiki-hyprland.md). El *ricing* moderno es, por tanto, **integración de piezas**.

### 2.3 De `hyprland.conf` a Lua (el cambio que afecta al usuario)

**HECHO.** ArchWiki afirma que "desde la versión 0.55, Hyprland ha transitado a Lua para su configuración, dejando obsoleta la sintaxis personalizada anterior", y que la configuración se hace en `~/.config/hypr/hyprland.lua`, que puede dividirse en varios archivos con `require()` ([ArchWiki · Hyprland](sources/2026-11-21-archwiki-hyprland.md), [URL original](https://wiki.archlinux.org/title/Hyprland)). Los releases lo confirman: la 0.56.1 añadió "un aviso de deprecación a los configs `.conf`" y la 0.57.0 añadió "notices de deprecación" junto a nuevas APIs Lua como `reload_config()`, `hl.get_devices()` y `hl.on` ([Hyprland · Releases](sources/2026-11-21-hyprland-releases.md), [URL original](https://github.com/hyprwm/Hyprland/releases)).

**HECHO (verificado localmente).** El equipo ya usa ese modelo: `hyprland.lua` hace `require()` de 13 módulos (`animations.lua`, `colors.lua`, `decorations.lua`, `binds.lua`, …), según la auditoría (`00-perfil-del-sistema.md`, §2.1). El plugin de Noctalia además genera una plantilla Lua (`assets/templates/hyprland/hyprland.lua`) con `hl.config({ general = { col = { active_border = primary, … } } })` ([Noctalia · Plantilla Lua](sources/2026-11-21-noctalia-hyprland-template.md), [URL original](https://github.com/noctalia-dev/noctalia/blob/main/assets/templates/hyprland/hyprland.lua)).

**OPINIÓN.** Este es el punto de inflexión más importante para investigar en 2026: los tutoriales y dotfiles escritos para `hyprland.conf` son ya documentación histórica. Copiarlos sin traducir a la API `hl.*` es la causa más probable de un rice roto.

---

## 3. Filosofía y estética

### 3.1 Las tres respuestas clásicas

| Corriente | Idea rectora | Cómo se ve | Riesgo |
|---|---|---|---|
| **Minimalismo** | Reducir elementos; que el escritorio desapareca | Sin barra o barra fina, pocos colores, gaps generosos, tipografía neutra | Puede volverse ilegible o esterilizante (**OPINIÓN**) |
| **Skeuomorphism / retro** | Imitar objetos físicos o interfaces antiguas | Sombras, texturas, botones con relieve, iconos "de siempre" | Consume espacio y puede envejecer mal (**OPINIÓN**) |
| **Cyberpunk / neon** | Alto contraste, luces, saturación | Bordes neón, glassmorphism, blur, glitch, fuentes técnicas | Coste de GPU y fatiga visual (**OPINIÓN**); el propio Hyprland ofrece blur y animaciones como prestaciones ([ArchWiki](sources/2026-11-21-archwiki-hyprland.md)) |

### 3.2 El caso Catppuccin: estética con principios explícitos

**HECHO.** Catppuccin se define como "un tema pastel impulsado por la comunidad que busca el término medio entre temas de contraste bajo y alto", con "4 sabores cálidos relajantes con 26 colores cada uno" ([Catppuccin · README](sources/2026-11-21-catppuccin-readme.md), [URL original](https://github.com/catppuccin/catppuccin/blob/main/README.md)). Su filosofía de diseño está escrita, algo poco habitual:

1. *"Colorful is better than colorless"* — el color ayuda a distinguir las partes de un todo.
2. *"There should be balance"* — ni demasiado apagado ni demasiado brillante; validez bajo distintas condiciones de luz.
3. *"Harmony is superior to dissonance"* — los colores vivos deben complementarse.

([Catppuccin · README](sources/2026-11-21-catppuccin-readme.md), [URL original](https://github.com/catppuccin/catppuccin/blob/main/README.md))

**HECHO.** Catppuccin se publica bajo licencia MIT ([Catppuccin · README](sources/2026-11-21-catppuccin-readme.md)) y cuenta con guía de estilo propia, señal de que una estética puede convertirse en un sistema documentado. En el equipo, `micro` ya incorpora cuatro sabores (latte, frappe, macchiato, mocha) según el perfil (`00-perfil-del-sistema.md`, §4) — una base estética disponible pero hoy desconectada del resto del escritorio (**OPINIÓN**).

### 3.3 *Rice* frente a productividad

**OPINIÓN.** La comunidad suele plantearlo como disyuntiva: "si ajustas el borde, no estás trabajando". Conviene distinguir **tres costes**:

- **Configuración** (una vez, amortizable si versionas dotfiles).
- **Mantenimiento** (cada actualización puede cambiar claves; §2.3).
- **Ejecución** (blur y transparencias en una iGPU antigua).

**HECHO.** El tercer coste está documentado: la wiki de Hyprland recomienda desactivar `decoration.blur.enabled` para consumir menos energía, usar escalado entero si hay tirones y subir la frecuencia mínima de la iGPU en TLP para reducir el *stutter* ([Hyprland · Performance](sources/2026-11-21-hyprland-performance.md), [URL original](https://wiki.hypr.land/configuring/extra/performance/)). Es decir, **la estética tiene un presupuesto de frames**, y eso es medible, no una opinión.

---

## 4. Taxonomía de estilos (elaboración propia)

> **OPINIÓN.** Tabla construida para este proyecto a partir de las herramientas documentadas en las fuentes; no es una clasificación oficial.

| Estilo | Paleta y forma | Stack típico documentado | Encaje con este usuario |
|---|---|---|---|
| **Minimal funcional** | 1 acento, monocromía, gaps grandes, sin blur | Hyprland + barra simple | **Alto**: reduce carga en Sandy Bridge |
| **Material You generativo** | Paleta derivada del wallpaper, roles semánticos | Noctalia `m3-tonal-spot`, matugen | **Ya activo**: `source="wallpaper"` ([Perfil](00-perfil-del-sistema.md) §3) |
| **Pastel estructurado** | 4 variantes claras/oscuras, 26 colores | Catppuccin | **Medio**: ya está en `micro`, falta propagarlo |
| **Neon / cyberpunk** | Saturación alta, bordes brillantes, glow | Gradientes de `decorations.lua` | **Parcial**: el borde actual es verde CachyOS, choca con el azul M3 |
| **Glassmorphism** | Transparencias + blur en capas | `blur size=5 passes=4`, `ignore_alpha`, `blur_popups` ([Status Bars](sources/2026-11-21-hyprland-status-bars.md)) | **Bajo-medio**: 4 pases de blur en iGPU antigua |
| **Maximalista / "rice de showroom"** | Máximo número de widgets y efectos | Shells completas + plugins | **Bajo**: fragilidad y coste de mantenimiento |
| **Utilitario gaming** | Reglas por aplicación, workspace dedicado, PiP | `windowrules.lua` del perfil | **Ya muy desarrollado** en la config actual |

---

## 5. Principios de diseño aplicables al rice

Aunque el *ricing* se hace en archivos de configuración, los principios son los del diseño de interfaces. **OPINIÓN fundamentada**: los cinco que más afectan a este equipo son:

1. **Jerarquía.** Lo que se usa más debe destacar más. En la barra actual, el grupo `capsule_group g1` reúne temperatura, GPU y RAM, y los workspaces son *pills* sin etiquetas ([Perfil](00-perfil-del-sistema.md) §3): la jerarquía está resuelta a favor de la densidad informativa. Con 1440×900 y un solo monitor, conviene no añadir módulos nuevos sin quitar otros.
2. **Consistencia.** Un mismo rol semántico debe tener un mismo color en todos los destinos. Noctalia expone **28 roles** (`primary`, `on_primary`, `surface`, `error`, …) precisamente para eso ([Noctalia · Palette](sources/2026-11-21-noctalia-theming-palette.md), [URL original](https://github.com/noctalia-dev/noctalia/blob/main/docs/user/theming/palette.mdx)). **HECHO:** hoy conviven el verde CachyOS de los bordes y el azul/violeta M3 del resto (auditoría §6); es la inconsistencia más visible del rice.
3. **Contraste.** Material Color Utilities incluye componentes explícitos de contraste, HCT y paletas tonales ([Material Color Utilities](sources/2026-11-21-material-you-color-system.md), [URL original](https://github.com/material-foundation/material-color-utilities/blob/main/README.md)). Un acento `#6791e4` sobre `#1e1e20` es legible; el mismo acento sobre una superficie clara puede no serlo. **OPINIÓN:** conviene validar el modo claro antes de activarlo.
4. **Espacio en blanco.** Los valores actuales —`gaps_in=3`, `gaps_out=8`, `border_size=2`, `rounding=10`, barra de 35 px— son el "aire" del escritorio (auditoría §2.2 y §3). Subir los gaps mejora la lectura pero resta espacio útil en 1440×900.
5. **Unidad de escala.** `ui_scale=1.20` y `scale=1.10` conviven con escalado de monitor 1 (auditoría §§1, 3). La wiki de Hyprland advierte que el escalado fraccionario puede causar tirones y recomienda valores enteros si hay problemas ([Performance](sources/2026-11-21-hyprland-performance.md)). **OPINIÓN:** aquí hay una decisión de diseño con impacto en rendimiento.

---

## 6. Tendencias 2025-2026

### 6.1 Teming generativo / Material You

**HECHO.** Material Color Utilities (Google) desplaza la elección manual de colores hacia *dynamic color*: componentes como `quantize` (extrae N colores de una imagen), `score` (prioriza colores adecuados para tematizar), `dynamiccolor` (ajusta a estado de UI, modo oscuro y requisitos de contraste) y `hct` (espacio de color basado en CAM16 × L*) ([Material Color Utilities](sources/2026-11-21-material-you-color-system.md), [URL original](https://github.com/material-foundation/material-color-utilities/blob/main/README.md)).

**HECHO.** Eso ya está dentro de Noctalia: el equipo usa `wallpaper_scheme = "m3-tonal-spot"`, y la documentación de Noctalia describe roles derivados del esquema Material cuando la paleta se genera desde un wallpaper ([Perfil](00-perfil-del-sistema.md) §3; [Noctalia · Palette](sources/2026-11-21-noctalia-theming-palette.md)). Existen además generadores independientes: **pywal** ("genera paletas a partir de los colores dominantes de una imagen", 5 backends y >250 temas), **wallust** (motor de plantillas Jinja2/sintaxis pywal, backends configurables) y **matugen** (Material You + base16, motor de plantillas propio) ([pywal](sources/2026-11-21-pywal-readme.md), [wallust](sources/2026-11-21-wallust-readme.md), [matugen](sources/2026-11-21-matugen-readme.md)).

### 6.2 Shells "todo en uno" y el caso QML/Quickshell

**HECHO.** La wiki de Hyprland separa tres niveles: barras simples (Waybar, ashell), *desktop shells* (Noctalia, DankMaterialShell: barra + launcher + notificaciones + lock screen en un paquete) y sistemas de widgets (AGS/Astal, Eww, Quickshell), con una tabla de lenguajes: JS(X)/TS, Yuck (Lisp) y **QML** respectivamente ([Hyprland · Status Bars](sources/2026-11-21-hyprland-status-bars.md), [URL original](https://wiki.hypr.land/useful-utilities/status-bars/)).

**INCIERTO / FUENTES EN CONFLICTO.** Esa misma wiki dice que Noctalia está "construida sobre Quickshell", mientras el README oficial de Noctalia afirma que está "construida directamente sobre Wayland y OpenGL ES, sin dependencia de Qt ni GTK" ([README de Noctalia](sources/2026-11-21-noctalia-readme.md), [URL original](https://github.com/noctalia-dev/noctalia/blob/main/README.md)). La explicación plausible —no verificada en el corpus— es una migración de QML/Quickshell a una implementación nativa. **Conclusión prudente:** Noctalia pertenece a la ola de *shells* QML/Quickshell por linaje, pero la documentación actual ya no la describe como tal. Los metadatos de GitHub la dan como proyecto C++ creado el 2025-07-11, con ~12 172 estrellas en noviembre de 2026 ([Noctalia · Metadatos](sources/2026-11-21-noctalia-repo-metadata.md), [URL original](https://api.github.com/repos/noctalia-dev/noctalia)): un ejemplo claro de tendencia 2025-2026.

### 6.3 Configuración como código

**HECHO.** Lua en Hyprland (§2.3), TOML con recarga en caliente en Noctalia ([README](sources/2026-11-21-noctalia-readme.md)), y plantillas que escriben la configuración de terminales, GTK, Qt y del propio compositor ([Noctalia · Plantillas](sources/2026-11-21-noctalia-builtin-templates.md)). La consecuencia es que el rice se parece cada vez más a un proyecto de software: versionable, modular y con APIs que cambian.

---

## 7. Errores comunes y críticas

| Error / crítica | Qué dice la evidencia | Mitigación |
|---|---|---|
| **Copiar dotfiles de terceros sin leerlos** | La wiki avisa: muchas configuraciones preconfiguradas "se inyectan agresivamente y modifican el sistema en profundidad"; incluso sus scripts de desinstalación pueden no limpiar todo ([Preconfigured setups](sources/2026-11-21-hyprland-preconfigured-setups.md), [URL original](https://wiki.hypr.land/getting-started/preconfigured-setups/)) | Leer `copy.sh`/`install.sh` antes de ejecutar; probar en usuario aparte; JaKooLit recomienda backups manuales además de los del script ([JaKooLit](sources/2026-11-21-jakoolit-hyprland-dots.md)) |
| **Tutoriales desactualizados (.conf)** | Deprecación documentada en 0.56.1/0.57 ([Releases](sources/2026-11-21-hyprland-releases.md); [ArchWiki](sources/2026-11-21-archwiki-hyprland.md)) | Traducir a `hl.*`; contrastar siempre con la wiki de la versión instalada |
| **Efectos caros en hardware modesto** | Desactivar blur reduce consumo; escalado fraccionario puede causar tirones ([Performance](sources/2026-11-21-hyprland-performance.md)) | Medir antes de subir `passes`; priorizar escalado entero |
| **Doble fuente de color** | Hallazgo de la auditoría local §6 | Elegir un único sistema (M3 o CachyOS) y propagarlo con plantillas |
| **Atajos que dependen del layout** | El perfil documenta el fix AZERTY con `digitCode(d)`/`code:10…19` (§2.3) | Usar `code:` para atajos nuevos |
| **Fragilidad de dependencias** | La wiki lista servicios que un DE arranca solo y Hyprland no ([Must-have](sources/2026-11-21-hyprland-must-have.md)) | Verificar notificaciones, portal, polkit tras cada cambio |
| **Pérdida de tiempo** | **OPINIÓN**: el riesgo es real cuando se rehace el rice completo en cada actualización | Cambios pequeños, medibles y versionados |
| **Uso del término "rice/ricing"** | **INCIERTO / CRÍTICA SOCIAL**: se le atribuye un origen en argot con carga racial y una apropiación estética de culturales asiáticas. El corpus **no** documenta esta debate; se registra como crítica reportada, no como hecho verificable | Usar el término con conciencia de su carga; preferir "personalización de escritorio" en contextos formales (**OPINIÓN**) |

**HECHO adicional sobre coste de mantenimiento:** el README de JaKooLit anuncia que en marzo de 2026 el proyecto se archivaría y pasaría a mantenerse en `LinuxBeginnings/Hyprland-Dots`, y advierte explícitamente a usuarios de **fish shell** de no usar cierta función de instalación (usar `install.sh` en su lugar) ([JaKooLit · README](sources/2026-11-21-jakoolit-hyprland-dots.md), [URL original](https://github.com/JaKooLit/Hyprland-Dots/blob/main/README.md)). Es un ejemplo concreto de por qué "bajar dots" no es gratis.

---

## 8. Qué significa ricing para ESTE usuario

> Sección de síntesis. **OPINIÓN fundamentada** a partir de la auditoría local (`00-perfil-del-sistema.md`) y de las fuentes citadas.

El perfil real es: **CachyOS** (Arch rolling), **Hyprland 0.57.2 con configuración Lua modular**, **Noctalia 5.6.0** con tema M3 derivado del wallpaper, **iGPU Intel Sandy Bridge**, un monitor **1440×900**, **fish 4.9.3**, **kitty/alacritty** con temas generados, Nerd Fonts y cursor **Bibata-Modern-Ice**.

Para este usuario, ricing significa tres cosas concretas:

1. **Unificación, no acumulación.** El problema estético principal no es que falten efectos, sino que hay dos sistemas de color peleando: verde CachyOS en bordes vs. azul M3 en el resto (auditoría §6). El mayor salto de calidad vendrá de convertir la paleta M3 en la única fuente —por ejemplo usando la plantilla Lua que Noctalia ya genera ([Plantilla Lua](sources/2026-11-21-noctalia-hyprland-template.md))—, no de añadir widgets.

2. **Ricing con presupuesto de GPU.** Con Sandy Bridge (2011), sin VRR ni HDR, cada capa de blur y cada transparencia cuenta. La wiki lo dice sin ambigüedad: desactivar blur reduce consumo ([Performance](sources/2026-11-21-hyprland-performance.md)). Aquí "buen rice" es el que se ve bien a 60 fps, no el que más brilla en una captura.

3. **Ricing como ingeniería de configuración.** El usuario ya tiene reglas de gaming muy elaboradas, manejo de AZERTY vía `code:`, UWSM, 13 módulos Lua y un shell que escribe 7 plantillas de tema. Eso es ricing en su sentido más moderno: **un sistema pequeño y reproducible**, no una carpeta de dotfiles opaca. El riesgo correspondiente es la fragilidad ante actualizaciones (§7), así que versionar y documentar es parte del rice.

**OPINIÓN final.** En este contexto, la meta no es "parecerse a una captura de r/unixporn", sino **que el escritorio se sienta como un solo objeto diseñado**: un acento, una escala, una familia tipográfica (Fantasque/Meslo Nerd + Bibata), una paleta y una sola fuente de verdad para el color. El resto —blur, animaciones, widgets— es negociable; la coherencia, no.

---

## 9. Límites de esta investigación

- No se archivó ninguna fuente histórica sobre el origen del término ni sobre la fundación de r/unixporn: esos apartados son **INCIERTO**.
- Las normas de publicación de r/unixporn se tratan en el documento 11 con la misma cautela.
- Las fuentes oficiales pueden cambiar (ya difieren sobre Quickshell, §6.2).
- Las clasificaciones de §3 y §4 son **OPINIÓN**, revisables en la hoja de ruta (`12-hoja-de-ruta-personalizada.md`).
