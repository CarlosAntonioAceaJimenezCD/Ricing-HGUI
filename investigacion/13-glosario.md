# 13 · Glosario: términos de ricing, Wayland y Hyprland

> Referencia rápida. Los térmidos marcados **[HECHO]** están documentados en las
> fuentes archivadas; los demás son definiciones de uso común en la comunidad.

## A

**Aquamarine** · Biblioteca de abstraction de backend gráfico (DRM, libinput, sesión)
usada por Hyprland; asume parte de las responsabilidades de wlroots. **[HECHO]**
Ver [hyprland-releases.md](../sources/2026-11-21-hyprland-releases.md).

**Autostart** · Programas que se lanzan al iniciar la sesión. En tu sistema,
`config/autostart.lua` lanza `dbus-update-activation-environment`, `noctalia` y
`xhost`; el resto va por XDG autostart al usar UWSM.

## B

**Bezier (curva)** · Curva de interpolación definida por puntos de control. En
Hyprland: `hl.curve("quick", { type = "bezier", points = {...} })`. Se usa para
workspaces y animaciones globales.

**Blur** · Desenfoque del fondo detrás de ventanas/capas. En 0.57 admite
variantes intercambiables y `decoration:blur:proportional`. Costoso en GPU.

**Bordes activos/inactivos** · Color del marco de la ventana con/sin foco. Tu
config usa un gradiente de 45°.

## C

**Capsule group** · En Noctalia, agrupación de widgets dentro de una "cápsula"
visual con `fill`, `padding` y `opacity` propios (tu `g1`: temp + gpu + ram).

**Catppuccin** · Paleta oscura comunitaria muy popular con cuatro variantes
(Latte, Frappe, Macchiato, Mocha). La tienes instalada para `micro`. **[HECHO]**

**Code (keycode)** · Identificador físico de tecla (`code:10`…`code:19`). Tu fix
AZERTY lo usa porque los caracteres de la fila de números cambian con Shift.

**Color semilla** · Color representativo extraído de una imagen a partir del
 cual se genera una paleta completa (Material You, matugen, pywal).

## D

**Dampening / Damping** · Parámetro de amortiguación de una curva spring. La
forma correcta en Hyprland 0.57 es `damping`; 0.57.0 corrigió el typo
`dampening`. **[HECHO]**

**Dwindle** · Layout por defecto de Hyprland: cada nueva ventana divide a la
mitad el espacio de la ventana activa. Configurable con `dwindle:preserve_split`.

**Dotfiles** · Archivos de configuración ocultos (punto inicial) versionados
normalmente en Git. Ver [10-dotfiles-y-gestion.md](10-dotfiles-y-gestion.md).

## E

**Evento** · Señal del compositor a la config (`hyprland.start`, `window.open`,
`workspace`). En Lua: `hl.on("hyprland.start", function() ... end)`. **[HECHO]**

## F

**Fish** · Shell de usuario (4.9.3) con sintaxis propia, no POSIX. Muchos
scripts de dotfiles asumen bash: revisa el shebang.

## G

**Gaps** · Espacio entre ventanas (`gaps_in`) y entre ventanas y borde de
pantalla (`gaps_out`). Tienes 3 y 8.

**Glyph** · Glifo: carácter gráfico de una fuente (p. ej. un icono de Nerd Font).
No confundir con un icono SVG de un theme XDG.

## H

**hl.\*** · API de configuración Lua de Hyprland 0.56+: `hl.config`, `hl.bind`,
`hl.window_rule`, `hl.curve`, `hl.animation`, `hl.on`, `hl.exec_cmd`, etc. **[HECHO]**

**Hyprctl** · CLI para consultar y modificar el estado del compositor en caliente:
`hyprctl monitors`, `hyprctl getoption`, `hyprctl keyword …`.

**Hyprland** · Compositor Wayland dinámico, independiente, con blur, animaciones
y plugins. Versión actual: 0.57.2. **[HECHO]**

**Hyprlang** · Lenguaje/parser de configuración de Hyprland (0.6.8).

## I

**IPC** · Comunicación entre procesos. `noctalia msg …` es el IPC que usan tus
atajos para controlar el shell desde Hyprland.

**iGPU** · GPU integrada. La tuya: Intel 2ª generación (Sandy Bridge), sin VRR/HDR.

## K

**Keybind** · Atajo de teclado. En Lua: `hl.bind("SUPER + Q", hl.dsp.window.close())`.
Tu `digitCode()` genera binds por keycode para AZERTY.

## L

**Layer rule** · Regla aplicable a capas del compositor (barra, overlays, shells).
Tu regla `noctalia` aplica `no_anim`, `blur` y `blur_popups`. **[HECHO]**

**Leaf** · Categoría de animación en Hyprland (`windows`, `workspaces`,
`specialWorkspaceIn/Out`, `global`).

**Lua config** · Configuración en Lua (`hyprland.lua`), nueva forma oficial desde
0.56/0.57; sustituye al clásico `hyprland.conf` (en deprecación). **[HECHO]**

## M

**m3-tonal-spot** · Esquema de color dinámico de Material 3 usado por tu Noctalia:
genera la paleta desde un acento local del wallpaper. **[HECHO]**

**Material You / Material 3** · Sistema de diseño de Google con color dinámico,
roles semánticos y tonos perceptuales.

**Monitor** · Salida de vídeo. Tu único monitor es `VGA-1` a 1440×900@60.

## N

**Noctalia** · Shell Wayland (QML) con barra, panel, launcher, notificaciones,
clipboard y motor de temas. Versión 5.6.0. **[HECHO]**

**Nerd Fonts** · Colección de fuentes parcheadas con miles de iconos en el
Private Use Area. Tienes FantasqueSansM y MesloLGM (3.5.1). **[HECHO]**

## O

**OKLCH** · Espacio de color perceptual (luminosidad, croma, tono) usado para
construir escalas uniformes. Ver [05-sistema-de-colores.md](05-sistema-de-colores.md).

**Opacity** · Opacidad. Tienes `active_opacity=0.95`, `inactive_opacity=0.85`;
algunas apps la fuerzan a `1.0 override`.

## P

**Portal (xdg-desktop-portal)** · API para que apps sandboxadas accedan a
archivos, capturas, etc. En Wayland: `xdg-desktop-portal-hyprland`.

**PiP** · Picture-in-Picture. Tu config lo hace flotante, con aspecto fijado y
`pin = true`.

## Q

**QML** · Lenguaje declarativo de Qt usado por Noctalia para su interfaz. Si
quieres hacer una barra, es la opción natural en tu sistema.

## R

**Ricing** · Personalización estética avanzada del escritorio: colores, fuentes,
iconos, animaciones y herramientas. Ver [01-que-es-ricing.md](01-que-es-ricing.md).

**Rounding** · Radio de las esquinas de las ventanas (10 px en tu config).

**Rule (window/workspace/layer)** · Regla declarativa que aplica propiedades a
ventanas o espacios según `class`, `title`, `content`, `xdg_tag`, etc.

## S

**Scale** · Factor de escalado de píxeles. Tu monitor usa `scale=1`; `force_zero_scaling`
en XWayland evita doble escalado en apps X11.

**Scratchpad / special workspace** · Workspace especial oculto. Tu atajo
`SUPER+S` lo alterna.

**Shader** · Programa de GPU para efectos (blur, color management). 0.57 añade
blur variants intercambiables. **[HECHO]**

**Spring** · Curva de animación física definida por `mass`, `stiffness` y
`damping`. Tu `easy` y `rubber` son springs.

**Swallow** · Comportamiento por el que un terminal lanza una app TUI y ésta
"se traga" la ventana del terminal (tu `enable_swallow=true`).

## T

**Tiling** · Disposición automática de ventanas en mosaico (dwindle, master,
scrolling). Hyprland es un tiling compositor.

**Token semántico** · Nombre de rol (`accent`, `danger`, `surface`) que desacopla
el color de su apariencia. Ver [05-sistema-de-colores.md](05-sistema-de-colores.md).

## U

**UWSM** · Universal Wayland Session Manager. Lanza apps como servicios systemd
de usuario (`uwsm app -- …`) y lee variables de `~/.config/uwsm/env`. **[HECHO]**

## V

**VRR** · Variable Refresh Rate. Tu monitor/GPU no lo soportan (`vrr: false`).

**ViewBox** · Atributo SVG (`viewBox="0 0 24 24"`) que define el sistema de
coordenadas; sin él un icono no escala. Ver [07-iconos-y-cursores.md](07-iconos-y-cursores.md).

## W

**Wallpaper** · Fondo de pantalla; en tu rice es la semilla del tema generativo.
Ver [09-wallpapers-y-generative-theming.md](09-wallpapers-y-generative-theming.md).

**Wayland** · Protocolo de composición que sustituye a X11. Tu sesión es
`XDG_SESSION_TYPE=wayland`.

**Window rule** · Ver **Rule**.

**wlroots** · Biblioteca base para compositors Wayland. Hyprland usa su propia
evolución (Aquamarine). **[HECHO]**

## X

**XDG autostart** · Estándar de arranque de apps mediante archivos `.desktop` en
`~/.config/autostart`. En tu sistema sólo está `cachyos-hello.desktop`.

**XWayland** · Servidor X11 compatibilidad sobre Wayland. Tienes
`xorg-xwayland 24.1.15` y `force_zero_scaling=true`.

## Z

**ζ (zeta)** · Ratio de amortiguación de un spring: ζ=1 es crítico, <1 rebota,
>1 es sobre-amortiguado. Ver [08-animaciones-y-efectos.md](08-animaciones-y-efectos.md).

---

## Abreviaturas frecuentes

| Sigla | Significado |
|---|---|
| GTK / Qt | Toolkits de interfaz |
| DE | Desktop Environment |
| WM / WM | Window Manager / Compositor |
| iGPU / dGPU | GPU integrada / dedicada |
| IPC | Inter-Process Communication |
| PUA | Private Use Area (Unicode, usado por Nerd Fonts) |
| WCAG | Web Content Accessibility Guidelines |
| WIP | Work In Progress |
