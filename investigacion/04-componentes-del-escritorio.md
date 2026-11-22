# 04 · Componentes del escritorio Wayland: catálogo y estado real

> Elaborado el 2026-11-21/22 a partir de la auditoría de `00-perfil-del-sistema.md`, los
> paquetes de `apendices/paquetes-instalados.txt` (1232 entradas), las copias de
> `configuracion-actual/` y las fuentes archivadas en `sources/`.
> **Leyenda de estado:** ✅ instalado y en uso · ⚠️ parcial (lo cubre otra capa, está
> descargado pero sin binario, o es incompleto) · ❌ no instalado.
> **Convención:** los datos de estado son **hechos** verificables; las recomendaciones del
> §16 están marcadas expresamente como **opinión**.

---

## 0. Cómo leer este catálogo

En Wayland no existe un "desktop environment" monolítico: el compositor dibuja, pero
**todo lo demás** (barra, launcher, notificaciones, bloqueo, wallpaper, portales) son
procesos independientes o un *shell* que aglutina varios de ellos. La wiki de Hyprland lo
dice explícitamente: los DE como Plasma o GNOME se encargan de eso automáticamente,
Hyprland no, "porque quizá quieras usar otra cosa" ([Must-have](sources/2026-11-21-hyprland-must-have.md)
— https://wiki.hypr.land/useful-utilities/must-have/).

Aquí la decisión está tomada: **Noctalia 5.6.0 es el shell** y absorbe barra, launcher,
notificaciones, clipboard, wallpaper, screenshot, sesión/bloqueo y polkit. De ahí los
⚠️: la *función* existe, pero no como paquete separado. **[Opinión]** No conviene añadir
el equivalente suelto (waybar + mako + wofi + swaylock…): se duplican superficies de
layer-shell y servicios D-Bus.

---

## 1. Mapa de capas

Catorce capas, de abajo arriba: compositor → shell/barra → launcher → wallpaper →
bloqueo → inactividad → notificaciones → clipboard → capturas → salidas → audio →
tematizado → terminal/editor → portales. El detalle con estados y paquetes está en la
[tabla-resumen del §15](#15-tabla-resumen-de-estados); en síntesis, todo lo que no es el
compositor, el shell Noctalia, grim/slurp/swash, PipeWire o los portales está ausente o
cubierto de forma indirecta.

---

## 2. Capa 1 · Compositor

**Qué hace.** Es el servidor de pantalla Wayland: gestiona buffers, entrada, workspaces,
reglas de ventanas y el protocolo `wlroots`. En este equipo es **Hyprland 0.57.2-1**
(commit `11cbc6c`, ABI `…_aq_0.16_hu_0.14_hg_0.6_hc_0.1_hlg_0.6`). La config no es la
clásica `hyprland.conf` sino `~/.config/hypr/hyprland.lua`, que hace `require()` de 13
módulos (`animations`, `autostart`, `colors`, `decorations`, `environment`, `inputs`,
`binds`, `misc`, `monitors`, `variables`, `windowrules`, `workspaces`, `xdph.conf`).
La API moderna expone `hl.config`,
`hl.bind`, `hl.window_rule`, `hl.animation`, `hl.on`, `hl.exec_cmd`, etc.
([Releases](sources/2026-11-21-hyprland-releases.md) — https://github.com/hyprwm/Hyprland/releases;
[ArchWiki](sources/2026-11-21-archwiki-hyprland.md) — https://wiki.archlinux.org/title/Hyprland;
[Config options](sources/2026-11-21-hyprland-config-options.md) — https://wiki.hypr.land/configuring/core/config-options/).

**Alternativas.** sway (estable, i3-like), niri (scrollable tiles), labwc (ligero,
Openbox-like), river, wayfire. Ninguna aporta ventajas aquí: el usuario ya tiene reglas
Lua muy específicas (gaming, PiP, AZERTY con `digitCode`) que tendría que reescribir.

**Comandos y configs reales.**

```fish
hyprctl version                 # verificar build/ABI
hyprctl monitors                # VGA-1 1440x900@59.89, scale 1
hyprctl configerrors            # errores de parseo del config cargado
hyprctl reload config-only      # recargar sin tocar monitores
hyprland --verify-config        # validar sintaxis SIN iniciar sesión → "config ok"
```

```lua
-- ~/.config/hypr/config/autostart.lua (copia real)
hl.on("hyprland.start", function ()
    hl.exec_cmd("dbus-update-activation-environment --systemd --all")
    hl.exec_cmd("noctalia")
    hl.exec_cmd("xhost +SI:localuser:root")
end)
```

**Estado: ✅.** Con matiz de rendimiento: blur `size=5, passes=4`, opacidades 0.95/0.85,
springs y `dim_special` sobre una **Intel Sandy Bridge de 2.ª generación**. El wiki de
rendimiento recomienda medir antes de subir efectos
([Performance](sources/2026-11-21-hyprland-performance.md) —
https://wiki.hypr.land/configuring/extra/performance/). No hay VRR/HDR expuesto, aunque
`vrr: 3` aparece configurado.

---

## 3. Capa 2 · Shell, barra y widgets

**Qué hace.** Un *shell* reúne varias superficies de escritorio en un solo proceso con un
modelo de configuración coherente. La wiki distingue tres familias
([Status bars](sources/2026-11-21-hyprland-status-bars.md) —
https://wiki.hypr.land/useful-utilities/status-bars/):

| Familia | Herramienta | Lenguaje / base | Ventaja | Coste |
|---|---|---|---|---|
| Barra simple | **waybar** | GTK/C++ | módulos Hyprland nativos, JSON+CSS | solo barra; hay que añadir el resto |
| Barra simple | **ashell** | Rust/iced | lista para usar | configuración muy limitada |
| Desktop shell | **Noctalia** | (ver nota) | barra+launcher+notif+lock+clipboard+temas | menos " piezas sueltas" intercambiables |
| Desktop shell | **DankMaterialShell** | Quickshell + Go | Material 3 integral | otro ecosistema |
| Widget system | **AGS/Astal** | GTK + JS/TS | librerías de red/Bluetooth | sin hot-reload nativo |
| Widget system | **EWW** | GTK3 + Lisp (yuck) | sintaxis sencilla, SCSS | **GTK3 sin aceleración GPU**, depende de scripts externos |
| Widget system | **Quickshell** | Qt/QML | muy flexible | requiere programar QML |

> Nota documental: la wiki de Hyprland describe Noctalia como "built on Quickshell",
> mientras que el README actual (5.6.0) afirma que está construida "directamente sobre
> Wayland y OpenGL ES, sin dependencia de Qt ni GTK"
> ([Noctalia README](sources/2026-11-21-noctalia-readme.md) —
> https://github.com/noctalia-dev/noctalia/blob/main/README.md). La fuente del propio
> proyecto es la más reciente; conviene no repetir la afirmación antigua.

**Estado en este equipo: ✅ Noctalia; ❌ el resto.** Noctalia se lanza desde `autostart.lua`
y se configura en `~/.config/noctalia/config.toml` con hot-reload e IPC (`noctalia msg …`).
Barra `thickness=35`, `ui_scale=1.20`, esquinas cóncavas, groups `g1`
(`temp + gpu_temp + ram_used`) y widgets `workspaces`, `active_window`, `clock`, `media`,
`tray`, `notifications`, `network`, `volume`, `session`
([Noctalia Bar](sources/2026-11-21-noctalia-bar.md) —
https://github.com/noctalia-dev/noctalia/blob/main/docs/user/bar/index.mdx).

```fish
noctalia                              # iniciar el shell
noctalia msg panel-toggle launcher    # abrir launcher (atajo del usuario)
noctalia msg settings-toggle          # ajustes
noctalia config validate              # validar TOML → "✓ Config is valid"
noctalia config export                # volcar config activa
```

**Waybar (❌), por si se migra.** La wiki indica copiar `/etc/xdg/waybar/` a
`~/.config/waybar/`, sustituir `sway/workspaces` por `hyprland/workspaces` y
`sway/mode` por `hyprland/submap`; con UWSM basta
`systemctl --user enable --now waybar.service`
([Waybar README](sources/2026-11-21-waybar-readme.md) —
https://github.com/Alexays/Waybar/blob/master/README.md).

Ejemplo mínimo (no instalado): `"modules-center": ["hyprland/window"]` en
`~/.config/waybar/config.jsonc`.

---

## 4. Capa 3 · Launcher de aplicaciones

**Qué hace.** Un selector difuso para lanzar apps, ejecutar comandos y a veces calcular o
buscar archivos. Sin él, Hyprland necesita un bind a un programa externo
([ArchWiki](sources/2026-11-21-archwiki-hyprland.md) —
https://wiki.archlinux.org/title/Hyprland, §*Application launcher*).

**Alternativas.** `wofi` (GTK, muy integrado), `rofi` (X11/Wayland, extensible),
`fuzzel` (C, Wayland nativo, rapidísimo), `hyprlauncher` (del ecosistema Hypr), el
launcher de Noctalia, `dmenu` vía `noctalia dmenu`.

**Estado: ✅ integrado en Noctalia.** El widget `launcher` aparece en
`bar.default.start`, y los atajos delegan en `noctalia msg panel-toggle launcher` y
`noctalia msg window-switcher`. No hay `wofi`/`rofi`/`fuzzel` instalados (❌).

```fish
noctalia msg panel-toggle launcher
noctalia dmenu --help                 # alternativa tipo dmenu sobre stdin
# si se migrase a fuzzel:
fuzzel --dmenu                        # (no instalado)
# ejemplo de bind Lua con wofi (no instalado):
# hl.bind(mainMod .. " + F", hl.dsp.exec_cmd("wofi --show drun"))
```

---

## 5. Capa 4 · Wallpaper

**Qué hace.** Hyprland **no** pinta fondos por sí solo: requiere un daemon Wayland
externo. La wiki lista hyprpaper, swaybg, wpaperd, mpvpaper (vídeo), awww (animado),
waypaper (GUI) y wallrizz (TUI)
([Wallpapers](sources/2026-11-21-hyprland-wallpapers.md) —
https://wiki.hypr.land/useful-utilities/wallpapers/).

**Estado: ✅ Noctalia; ❌ los daemons sueltos.** `config.toml` usa
`[theme] source = "wallpaper"` y `wallpaper_scheme = "m3-tonal-spot"`: el fondo no solo
se muestra, sino que **genera la paleta Material You** que se propaga a btop, GTK3/4,
kcolorscheme (Qt), kitty, alacritty. El bind `SUPER+SHIFT+W` abre
`noctalia msg panel-toggle wallpaper`
([Noctalia Wallpaper](sources/2026-11-21-noctalia-wallpaper.md) —
https://github.com/noctalia-dev/noctalia/blob/main/docs/user/desktop/wallpaper.mdx;
[Templates](sources/2026-11-21-noctalia-builtin-templates.md) —
https://github.com/noctalia-dev/noctalia/blob/main/assets/templates/builtin.toml).

```fish
noctalia msg panel-toggle wallpaper
noctalia theme /ruta/imagen.png       # generar paleta desde una imagen
```

```toml
# ~/.config/noctalia/config.toml (real)
[theme]
mode = "dark"
source = "wallpaper"
wallpaper_scheme = "m3-tonal-spot"
[theme.templates]
builtin_ids = ["btop", "gtk3", "gtk4", "kcolorscheme", "kitty", "qt", "alacritty"]
```

**Alternativa clásica (❌)** — hyprpaper: `hl.exec_cmd("hyprpaper")` en `autostart.lua`
más `wallpaper { monitor = VGA-1, path = /…/wall.png, fit_mode = cover }` en
`~/.config/hypr/hyprpaper.conf`.

> **Advertencia de hardware (hecho + opinión):** `mpvpaper`/`awww` (vídeo/animación) son
> los peores candidatos para una iGPU Sandy Bridge con blur de 4 passes; se desaconseja
> añadirlos. `hyprpaper` o el selector de Noctalia con imagen estática son la opción sensata.

---

## 6. Capa 5 · Bloqueo de sesión e inactividad

**Bloqueo — Estado: ✅ vía Noctalia; ❌ hyprlock/swaylock.** La README de Noctalia
incluye *session lock* usando el protocolo `ext-session-lock-v1` de Wayland, y el config
real define `[[shell.session.actions]]` con `action = "lock"`, `lock_and_suspend`,
logout, reboot y shutdown (estos últimos con cuenta atrás). El atajo es `SUPER+L` →
`noctalia msg session lock`. `hyprlock` no figura en los 1232 paquetes.

**Inactividad — Estado: ⚠️ parcial.** Hay soporte de idle en Noctalia (Integración
Wayland directa, §*Scope*), y `loginctl` / `kidletime` / `knotifications` están
disponibles, pero **no hay `hypridle`, `swayidle` ni un `hypridle.conf`**. La receta
de referencia de ArchWiki sería:

```toml
# ~/.config/hypr/hypridle.conf  (NO presente actualmente)
general { lock_cmd = pidof hyprlock || hyprlock }
listener { timeout = 300, on-timeout = loginctl lock-session }
listener { timeout = 600, on-timeout = hyprctl dispatch dpms off
                          on-resume  = hyprctl dispatch dpms on }
listener { timeout = 900, on-timeout = systemctl suspend }
```

```lua
hl.on("hyprland.start", function() hl.exec_cmd("hypridle") end)
hl.bind("SUPER + L", hl.dsp.exec_cmd("hyprlock"))   -- alternativa sin Noctalia
```

([ArchWiki](sources/2026-11-21-archwiki-hyprland.md) —
https://wiki.archlinux.org/title/Hyprland, §*Idle*;
[Hypr ecosystem](sources/2026-11-21-hyprland-ecosystem-user.md) —
https://wiki.hypr.land/hypr-ecosystem/user/).

---

## 7. Capa 6 · Notificaciones

**Qué hace.** Un daemon D-Bus (`org.freedesktop.Notifications`) que muestra toasts,
historial y DND. La wiki avisa: **muchas apps (p. ej. Discord) se congelan sin uno**
([Must-have](sources/2026-11-21-hyprland-must-have.md) —
https://wiki.hypr.land/useful-utilities/must-have/).

**Alternativas.** `dunst`, `mako`, `fnott`, `swaync` (todas ❌ aquí); las bibliotecas
`libnotify 0.8.9` y `knotifications 6.32.0` sí están presentes (✅ como libs).

**Estado: ✅ Noctalia.** Su sistema de notificaciones incluye historial y *Do Not
Disturb*; el widget `notifications` está en el extremo derecho de la barra y el config
define `color = "secondary"`. No hace falta `mako`.

```fish
noctalia msg panel-toggle notifications   # (nombre orientativo; ver noctalia msg --help)
hyprctl dismissnotify 3                    # notificaciones nativas de Hyprland
```

---

## 8. Capa 7 · Clipboard

**Qué hace.** Guarda el historial de copias y gestiona selecciones Wayland
(`wl-clipboard` expone `wl-copy`/`wl-paste`).

**Alternativas.** `cliphist` (❌), `wl-paste | …` (✅), el panel de clipboard de un shell.

**Estado: ✅.** `wl-clipboard 1:2.3.0-1` instalado más el panel de clipboard de
Noctalia. Detalle relevante: `middle_click_paste = false` en `misc.lua` y la acción
`clipboard_image_action_command = "swash --stdin --name …"` (config real), de modo que
una imagen copiada se guarda como PNG con `swash`. El atajo es `SUPER+V`.

```fish
wl-paste                                  # leer selección
printf 'hola' | wl-copy                   # escribir selección
noctalia msg panel-toggle clipboard
swash --stdin --name "swash-$(date +'%Y-%m-%d_%H:%M:%S').png"
```

---

## 9. Capa 8 · Capturas de pantalla y selector de color

**Qué hace.** `grim` captura el escritorio Wayland, `slurp` permite seleccionar un
área interactivamente, `swash` es el visor/gestor de capturas del ecosistema CachyOS,
y `hyprpicker` extrae un color de la pantalla (útil para alimentar la paleta).

**Alternativas.** `swappy`/`satty` (anotación, ❌), `grimblast` (❌), `spectacle`, módulo
de captura del portal (✅ vía xdg-desktop-portal-hyprland).

**Estado: ✅ todo instalado** — `grim 1.5.0-2`, `slurp 1.5.0-2`, `swash 1.5.1-1`,
`hyprpicker 0.4.8-1`. La config real delega `Print` y `SUPER+Print` a
`noctalia msg screenshot-region` / `screenshot-fullscreen`, y Noctalia a su vez usa
`swash` como `pipe_command`. La wiki confirma que `hyprpicker` "no requiere ninguna
configuración" ([ArchWiki](sources/2026-11-21-archwiki-hyprland.md) —
https://wiki.archlinux.org/title/Hyprland, §*Hyprpicker*).

```fish
grim -g "$(slurp)" /tmp/recorte.png      # captura de región (clásico)
swash /tmp/recorte.png                   # abrir en swash
hyprpicker                               # copiar color al clipboard
hyprpicker -f hex                        # formato hexadecimal
```

---

## 10. Capa 9 · Salidas y selección de monitor

**Qué hace.** En Wayland el compositor expone los *wl_output* (los "roles" del protocolo,
no un paquete llamado `wl-roles`); las utilidades de salida permiten rotar, escalar o
configurar monitores en caliente.

**Alternativas.** `wdisplays` (GUI), `nwg-displays` (GUI), `kanshi` (perfiles
automáticos), `wlr-randr` (CLI). **Todas ❌.**

**Estado: ⚠️ suficiente pero no ampliable.** Hay un único `VGA-1` a 1440×900 @ 59.89 Hz,
escala 1, sRGB, definido en `config/monitors.lua`. Las reglas `MONITOR2/3` y
`NUM_WPM=3` ya están preparadas para crecer, pero hoy no se usan. Las variables de
entorno de la sesión están en `~/.config/uwsm/env` (copia en `configuracion-actual/shell/uwsm-env`).

```fish
hyprctl monitors                 # inventario de salidas
hyprctl monitors all             # incluye inactivas
wlr-randr                        # (no instalado) alternativa CLI
# nwg-displays / kanshi          # (no instalados) solo con múltiples pantallas
```

---

## 11. Capa 10 · Audio

**Qué hace.** PipeWire es el servidor multimedia; WirePlumber es el gestor de sesiones;
`pavucontrol` el mezclador GUI; `wpctl` la CLI. Sin PipeWire no funciona el
compartir pantalla ([Must-have](sources/2026-11-21-hyprland-must-have.md) —
https://wiki.hypr.land/useful-utilities/must-have/). La wiki advierte instalar
`wireplumber` **no** `pipewire-media-session`.

**Estado: ✅ completo.** `pipewire 1:1.6.11-2`, `libpipewire`, `pipewire-audio`,
`pipewire-pulse`, `pipewire-alsa`, `wireplumber 0.5.19-1`, `pavucontrol 1:6.2-2`,
además de `alsa-*`. No están `hyprpwcenter` (❌) ni `pulseaudio` puro (innecesario).

```fish
wpctl status                     # ver nodos/sinks
wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+
wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle
pavucontrol                      # GUI
pactl info                       # compatibilidad PulseAudio (pipewire-pulse)
```

Los widgets `volume` y `media` de la barra de Noctalia ya exponen controles, y los
atajos `volume-up` / `brightness-up` pasan por `noctalia msg …`.

---

## 12. Capa 11 · Tematizado GTK / Qt

**Qué hace.** Aplica esquemas de color y estilos a apps que no obedecen la paleta del
compositor. Aquí hay **dos fuentes de color conviviendo**: el verde CachyOS de
`colors.lua` (bordes de Hyprland) y el M3 azul/violeta generado por Noctalia (kitty,
alacritty, GTK, Qt, btop). Es la inconsistencia visual n.º 1 detectada en la auditoría.

| Herramienta | función | Estado |
|---|---|---|
| `noctalia` templates | propaga paleta a 7 destinos | ✅ |
| `nwg-look 1.2.1` | selector GTK (themes/icons/cursors/fonts) | ✅ |
| `adw-gtk-theme 6.5` + `adw-gtk3` | tema GTK3 estilo GNOME 4x | ✅ |
| `qt6ct 0.11-9` + `noctalia.colors` | esquema Qt6 | ✅ |
| `xsettingsd` config | ajustes XSettings (Bibata) | ⚠️ archivo presente, **binario/paquete ausente** |
| `qt5ct` | esquema Qt5 | ❌ (sí está `qt5-wayland`) |
| `kvantummanager` | motor Qt alternativo | ❌ (referenciado en `windowrules.lua`) |
| `lxappearance` | selector GTK clásico | ❌ (lo sustituye nwg-look) |

Fuentes: [adw-gtk3](sources/2026-11-21-adw-gtk3-readme.md) —
https://github.com/lassekongo83/adw-gtk3/blob/main/README.md;
[Noctalia app-theming](sources/2026-11-21-noctalia-app-theming.md) —
https://github.com/noctalia-dev/noctalia/blob/main/docs/user/theming/app-theming.mdx;
[Bibata](sources/2026-11-21-bibata-readme.md) —
https://github.com/ful1e5/Bibata_Cursor/blob/main/README.md.

```fish
nwg-look                          # elegir tema GTK, iconos, cursor
qt6ct                             # esquema Qt6 → ~/.local/share/color-schemes/noctalia.colors
nwg-look & xsettingsd &           # ⚠️ xsettingsd NO instalado: instalar antes de usar
```

El cursor **Bibata-Modern-Ice** está en `~/.local/share/icons` y el archivo
`iconos/Bibata-Modern-Ice-index.theme` fija `Inherits=Bibata-Modern-Ice`. Las fuentes
Nerd (`ttf-fantasque-nerd`, `ttf-meslo-nerd`, 3.5.1) cubren glifos de barra
([Nerd Fonts](sources/2026-11-21-nerd-fonts-readme.md) —
https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md).

---

## 13. Capa 12 · Terminales y editor

**Estado: ✅.** `kitty 0.51.0` (`background_opacity 0.6`, `window_padding_width 25`,
`include themes/noctalia.conf`), `alacritty 0.17.0` (importa `themes/noctalia.toml`,
pero el archivo principal aún conserva colores Nord → ⚠️ cosmético), `micro 2.0.15` con
4 esquemas Catppuccin, `vim 9.2`, `gnome-text-editor 51.0`. No hay `ghostty`/`wezterm`
(❌). El `enable_swallow = true` de Hyprland está calibrado para kitty/alacritty.

```fish
kitty --config ~/.config/kitty/kitty.conf      # forzar config
alacritty --config-file ~/.config/alacritty/alacritty.toml
micro -colorscheme mocha ~/.config/hypr/hyprland.lua
```

Catppuccin y Material You están archivados como referencia de paletas
([Catppuccin](sources/2026-11-21-catppuccin-readme.md) —
https://github.com/catppuccin/catppuccin/blob/main/README.md;
[Material You](sources/2026-11-21-material-you-color-system.md) —
https://github.com/material-foundation/material-color-utilities/blob/main/README.md).

---

## 14. Capa 13 · Portales, XWayland y agentes

**Qué hace.** `xdg-desktop-portal` es la API D-Bus que usan GTK/Qt/Firefox para
selectores de archivo, compartir pantalla y permisos. XWayland da compatibilidad a apps
X11. Un *polkit agent* muestra el diálogo de contraseña cuando una app escala privilegios.

**Estado: ✅ portales y XWayland; ⚠️ polkit.**

- `xdg-desktop-portal 1.22.1-2`, `xdg-desktop-portal-hyprland 1.5.0-1`,
  `xdg-desktop-portal-gtk 1.15.3-2`. La wiki confirma que XDP-Hyprland **no incluye
  selector de archivos**, por eso `xdg-desktop-portal-gtk` es necesario y aquí está
  instalado ([ArchWiki](sources/2026-11-21-archwiki-hyprland.md) —
  https://wiki.archlinux.org/title/Hyprland, §*XDG-Desktop-Portal-Hyprland*).
- `xorg-xwayland 24.1.15-1` ✅; `qt5-wayland` ✅; `qt6-wayland` ❌ (lo usual en Qt6 puro).
- Polkit: `polkit 128-1` y `gnome-keyring`/`kwallet` están, y `config.toml` fija
  `polkit_agent = true`, así que **Noctalia actúa de agente** (⚠️ en lugar de `hyprpolkitagent`).
- `hyprsunset` (filtro de luz azul, ❌), `hyprpolkitagent` (❌), `xdg-desktop-portal-wlr` (❌).

```fish
systemctl --user status xdg-desktop-portal-xdg-desktop-portal-hyprland.service
# alternativa documentada si se migrase:
# hl.exec_cmd("systemctl --user start hyprpolkitagent")
```

---

## 15. Tabla-resumen de estados

| Componente | Paquete real | Estado | Cubierto por |
|---|---|---|---|
| Compositor | hyprland 0.57.2-1 | ✅ | — |
| Shell/barra | noctalia 5.6.0-1 | ✅ | — |
| waybar / eww / AGS / Quickshell | — | ❌ | Noctalia |
| Launcher | noctalia (widget) | ✅ | — |
| wofi / rofi / fuzzel | — | ❌ | Noctalia |
| Wallpaper | noctalia (`source=wallpaper`) | ✅ | — |
| hyprpaper / swww / mpvpaper | — | ❌ | Noctalia |
| Lock | noctalia session lock | ✅ | — |
| hyprlock / swaylock | — | ❌ | Noctalia |
| Idle | — | ⚠️ | Noctalia + `loginctl` |
| hypridle | — | ❌ | — |
| Notificaciones | noctalia + libnotify | ✅ | — |
| mako / dunst / swaync | — | ❌ | Noctalia |
| Clipboard | wl-clipboard 2.3.0 + noctalia | ✅ | — |
| cliphist | — | ❌ | Noctalia |
| Capturas | grim 1.5.0 + slurp 1.5.0 + swash 1.5.1 | ✅ | — |
| Color picker | hyprpicker 0.4.8 | ✅ | — |
| Salidas | monitors.lua (VGA-1) | ⚠️ | Hyprland |
| wdisplays / nwg-displays / kanshi | — | ❌ | — |
| Audio | pipewire 1.6.11 + wireplumber 0.5.19 + pavucontrol 6.2 | ✅ | — |
| Tematizado | nwg-look + adw-gtk3 + qt6ct + plantillas | ⚠️ | falta qt5ct/Kvantum/xsettingsd |
| Terminal | kitty 0.51 + alacritty 0.17 | ✅ | — |
| Editor | micro 2.0.15 / vim 9.2 / gnome-text-editor | ✅ | — |
| Portales | xdg-desktop-portal + gtk + hyprland | ✅ | — |
| Polkit | polkit + noctalia `polkit_agent` | ⚠️ | hyprpolkitagent ❌ |

---

## 16. Stack ideal recomendado para este hardware (opinión)

**Hecho:** Sandy Bridge de 2.ª generación, 1440×900 @ 60 Hz, sin VRR/HDR, blur de 4
passes, direct scanout bloqueado por modo ventana. **Opinión:** el stack óptimo es
*menos procesos, no más*.

1. **Conservar Hyprland 0.57.2 + Noctalia 5.6.0 como núcleo.** Una sola shell evita
   duplicar barra, notificaciones y clipboard. No instalar waybar/mako/wofi/swaylock.
2. **Bajar blur a `passes=1–2`** y medir con `intel_gpu_top` + `hyprctl` antes de
   cualquier subida de efectos. Las animaciones `spring` y las transparencias son el
   siguiente gasto a revisar.
3. **Wallpaper estático** gestionado por Noctalia; descartar `mpvpaper`/`awww`.
4. **Mantener grim+slurp+swash+hyprpicker**: son ligeros y ya funcionan. No añadir
   `satty`/`swappy` salvo que se necesite anotación.
5. **Añadir solo tres piezas que faltan de verdad:** `hyprlock`+`hypridle` (o dejar que
   Noctalia cubra idle), `qt5ct` si se usan apps Qt5, y el binario `xsettingsd` para que
   el `xsettingsd.conf` existente no sea una configuración huérfana. `Kvantummanager`
   solo si se quiere cambiar el motor Qt.
6. **Unificar la paleta**: alimentar `colors.lua` desde el M3 generado por Noctalia para
   que el borde deje de ser verde CachyOS mientras el resto es azul/violeta.

Esta recomendación contradice deliberadamente los "must-have" genéricos (mako,
hyprpaper, hyprpolkitagent): son correctos para un Hyprland *desnudo*, pero redundantes
cuando Noctalia ya provee esos servicios
([Must-have](sources/2026-11-21-hyprland-must-have.md) —
https://wiki.hypr.land/useful-utilities/must-have/).

---

## 17. Fuentes citadas

Las citas aparecen junto a cada afirmación; índice de las principales:

- [Hyprland · Must-have](sources/2026-11-21-hyprland-must-have.md) — https://wiki.hypr.land/useful-utilities/must-have/
- [Hyprland · Status bars](sources/2026-11-21-hyprland-status-bars.md) — https://wiki.hypr.land/useful-utilities/status-bars/
- [Hyprland · Wallpapers](sources/2026-11-21-hyprland-wallpapers.md) — https://wiki.hypr.land/useful-utilities/wallpapers/
- [ArchWiki · Hyprland](sources/2026-11-21-archwiki-hyprland.md) — https://wiki.archlinux.org/title/Hyprland
- [Hyprland Releases](sources/2026-11-21-hyprland-releases.md) — https://github.com/hyprwm/Hyprland/releases
- [Waybar · README](sources/2026-11-21-waybar-readme.md) — https://github.com/Alexays/Waybar/blob/master/README.md
- [Noctalia · README](sources/2026-11-21-noctalia-readme.md) — https://github.com/noctalia-dev/noctalia/blob/main/README.md
- [Noctalia · Bar](sources/2026-11-21-noctalia-bar.md) — https://github.com/noctalia-dev/noctalia/blob/main/docs/user/bar/index.mdx
- [Nerd Fonts](sources/2026-11-21-nerd-fonts-readme.md) — https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md

*Datos locales: `00-perfil-del-sistema.md`, `apendices/paquetes-instalados.txt`,
`configuracion-actual/hypr/config/*.lua`, `configuracion-actual/noctalia/config.toml`.
Comandos de verificación ejecutados el 2026-11-21: `hyprland --verify-config` → `config ok`;
`noctalia config validate` → `✓ Config is valid`.*
