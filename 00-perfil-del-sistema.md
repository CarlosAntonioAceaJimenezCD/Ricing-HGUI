# 00 · Perfil del sistema (auditoría real)

> Generado el 2026-11-21/22 desde la máquina de `thony70807`. Los datos crudos están en
> `apendices/`. Las copias de los archivos de configuración están en `configuracion-actual/`.
> Este documento es el punto de partida de toda la investigación: cada recomendación de
> `investigacion/12-hoja-de-ruta-personalizada.md` se deriva de aquí.

## 1. Sistema base

| Dato | Valor |
|---|---|
| Distribución | **CachyOS Linux** (derivada de Arch, rolling release) |
| Kernel | `7.3.5-2-cachyos` (x86_64, PREEMPT_DYNAMIC) |
| Shell de usuario | **fish 4.9.3** (con `fisher`, `fish-pure-prompt`, `fish-autopair`); también instalado `oh-my-zsh-git` |
| Paquetes instalados | **1232** (pacman) · 0 paquetes AUR/foreign · 0 flatpaks |
| Sesión | `XDG_CURRENT_DESKTOP=Hyprland`, `XDG_SESSION_TYPE=wayland` |
| UWSM | Sí: los lanzadores usan `uwsm app -- …`; variables en `~/.config/uwsm/env` |
| Monitor | Un único **VGA-1**, 1440×900 @ 59.89 Hz, escala 1, sRGB |
| GPU | **Intel 2nd Gen (Sandy Bridge) iGPU** — `00:02.0 VGA compatible controller` |
| VRR / HDR | No (`vrr: false`, `hdr: no`); `physical size 400×250 mm` |

**Implicación importante:** es un hardware muy modesto para los estándares de ricing.
Los efectos caros (blur de many-passes, transparencias, animaciones complejas, VRR,
HDR) deben presupuestarse con cuidado. El propio Hyprland reporta
`directScanoutBlockedBy: windowed mode, missing candidate` y
`tearingBlockedBy: … missing candidate, hw cursor`.

## 2. Compositor: Hyprland 0.57.2 (última rama estable)

```
Hyprland 0.57.2 built from branch v0.57.2 at commit 11cbc6c577b84ffb1edf4df3fc5b6128c3ae6947 clean
Date: Mon Nov 9 11:05:46 2026
Libraries:
  Hyprgraphics 0.6.0 (system 0.6.0)
  Hyprutils    0.14.3 (system 0.14.4)
  Hyprcursor   0.1.13 (system 0.1.14)
  Hyprlang     0.6.8  (system 0.6.8)
  Aquamarine   0.16.0 (system 0.16.0)
ABI: 11cbc6c…_aq_0.16_hu_0.14_hg_0.6_hc_0.1_hlg_0.6
```

Paquetes relacionados: `hyprland 0.57.2-1`, `hyprland-guiutils 0.2.2-6`,
`hyprlang 0.6.8-5`, `hyprcursor 0.1.14-1`, `hyprgraphics 0.6.0-2`,
`hyprutils 0.14.4-1`, `hyprpicker 0.4.8-1`, `hyprwire 0.3.1-3`,
`hyprtoolkit 0.6.0-3`, `wlroots0.20 0.20.2-1`,
`xdg-desktop-portal-hyprland 1.5.0-1`, `xorg-xwayland 24.1.15-1`.

### 2.1 Configuración en Lua (no `hyprland.conf` clásico)

El archivo de entrada es `~/.config/hypr/hyprland.lua`, que hace `require()` de 13 módulos:

```
config/animations.lua   config/autostart.lua   config/colors.lua
config/decorations.lua  config/environment.lua config/inputs.lua
config/binds.lua        config/misc.lua        config/monitors.lua
config/variables.lua    config/windowrules.lua config/workspaces.lua
xdph.conf
```

Esto coincide con la evolución oficial: 0.56.1 añadió un *aviso de deprecación* a los
configs `.conf` y 0.57 consolidó la API `hl.*` (`hl.config`, `hl.bind`, `hl.window_rule`,
`hl.animation`, `hl.curve`, `hl.on`, `hl.exec_cmd`, `hl.get_config`, `hl.gesture`, …).
Ver `sources/2026-11-22-hyprland-0-57-releases.md` y la wiki oficial.
El plugin de Noctalia también genera un `hyprland.lua` template
(`assets/templates/hyprland/hyprland.lua` en el repo clonado).

### 2.2 Ajustes visuales actuales (decorations.lua)

| Parámetro | Valor |
|---|---|
| `gaps_in` / `gaps_out` | 3 / 8 |
| `border_size` | 2, `extend_border_grab_area=10`, `resize_on_border=true` |
| Borde activo | gradiente `rgba(82dcccff)` → `rgba(007d6fff)` a 45° |
| Borde inactivo | `rgba(798bb2ff)` |
| `rounding` | 10 |
| `active_opacity` / `inactive_opacity` | 0.95 / 0.85 |
| `blur` | `size=5`, `passes=4`, `special=true` |
| `dim_special` | 0.3 |
| Animaciones | global `speed=3 bezier=quick`; ventanas `spring=easy` (`slide`); workspaces `speed=5 slide`; special in/out `slide top/bottom` |
| Curvas | beziers `easeOutQuint`, `easeInOutCubic`, `linear`, `almostLinear`, `quick`, `overshoot`; springs `easy` y `rubber` |
| `vrr` / `direct_scanout` | 3 / 2 (aunque el hardware no expone VRR) |
| `enable_swallow` | true (regex kitty/ghostty/konsole/alacritty/… ) |
| `middle_click_paste` | false |
| Teclado | `kb_layout="es"`, `accel_profile="flat"` |

### 2.3 Personalizaciones del usuario detectadas

- **Fix AZERTY**: la fila de números emite símbolos (`& é " ' …`) sin Shift, así que
  los atajos usan `digitCode(d)` → `code:10…19` en vez de caracteres.
- Reglas de **gaming** muy elaboradas: workspace `name:gaming`, `content="game"`,
  `xdg_tag`, `steam_app*`, PiP flotante y fijado, supresión de maximizar.
- Reglas flotantes para diálogos, launchers, `vesktop`, `dolphin` (con clamping),
  `noctalia`, `swash`, `kvantummanager`, `pavucontrol`, etc.
- Regla de capa `noctalia` con `no_anim`, `ignore_alpha=0.5`, `blur`, `blur_popups`.
- `workspace_rule` persistentes 1-3 en `MONITOR1` (variable vacía → autodetección).

## 3. Shell de escritorio: Noctalia 5.6.0

Es el elemento más relevante del rice actual. Paquetes: `noctalia 5.6.0-1`,
`noctalia-greeter 1.7.1-1`, `cachyos-hypr-noctalia 1.2.6-1`. Se lanza desde
`autostart.lua` con `hl.exec_cmd("noctalia")`. No es waybar: es un shell QML con
barra, panel de control, launcher, notificaciones, clipboard, wallpaper picker,
screenshot, session control y **motor de temas generativo**.

`~/.config/noctalia/config.toml` (copia en `configuracion-actual/noctalia/`):

- `[theme]`: `mode = "dark"`, `source = "wallpaper"`,
  `wallpaper_scheme = "m3-tonal-spot"` → **Material You** derivado del wallpaper.
- `templates.builtin_ids = ["btop","gtk3","gtk4","kcolorscheme","kitty","qt","alacritty"]`
  → el mismo esquema se propaga a 7 destinos.
- Barra: `thickness=35`, `scale=1.10`, `ui_scale=1.20`, esquinas cóncavas
  (`concave_edge_corners=true`), radios superiores 0 / inferiores 12,
  `capsule_group g1` con `temp + gpu_temp + ram_used`.
- Widgets: `workspaces` (pills, sin labels), `active_window`, `clock`
  (`{:%H:%M %A %m/%d/%y}`), `media`, `tray`, `notifications`, `network`,
  `volume`, `session` (color `error`).
- Screenshot y clipboard/image → **`swash 1.5.1`** (`swash --stdin --name …`).
- Polkit agent, greeter sync desactivado, `settings_show_advanced=true`.

Los atajos de Hyprland delegan casi todo a `noctalia msg …`
(`window-switcher`, `settings-toggle`, `panel-toggle launcher/clipboard/control-center`,
`volume-up`, `brightness-up`, `screenshot-region`, `session lock`, `wallpaper`, etc.).

## 4. Terminales, fuentes, iconos y cursores

| Capa | Estado real |
|---|---|
| Terminal principal | **kitty 0.51.0** — `background_opacity 0.6`, `window_padding_width 25`, `cursor_trail 1`, `include themes/noctalia.conf` |
| Terminal secundaria | **alacritty 0.17.0** — `opacity 0.8`, `dynamic_padding`, importa `themes/noctalia.toml`; el archivo principal aún contiene colores Nord de base |
| Temas terminal | `kitty/themes/noctalia.conf` y `alacritty/themes/noctalia.toml` (paleta generada por Noctalia) |
| Editor | `gnome-text-editor` (por defecto), `micro 2.0.15` con **4 esquemas Catppuccin** (latte, frappe, macchiato, mocha), `vim 9.2` |
| Fuentes Nerd | **`ttf-fantasque-nerd 3.5.1`** y **`ttf-meslo-nerd 3.5.1`** (variantes LGL/LGLDZ/LGM/LGS + Propo/Mono) · `awesome-terminal-fonts`, `powerline-fonts` |
| Otras fuentes | Noto (CJK, emoji, etc.), Adwaita Sans/Mono, DejaVu, Liberation, Cantarell, Open Sans, Bitstream Vera — **885 entradas** en `fc-list` |
| Cursor | **Bibata-Modern-Ice** (`~/.local/share/icons/`) configurado en GTK y xsettingsd; Adwaita cursors |
| Iconos | Adwaita / AdwaitaLegacy / breeze / breeze-dark / hicolor / locolor |
| GTK | `adw-gtk-theme 6.5-1`, `adw-gtk3`, `gtk-application-prefer-dark-theme=1`, CSS generado por Noctalia con `@define-color` |
| Qt | `qt5ct` / `qt6ct 0.11-9`, esquema `noctalia.colors` en `~/.local/share/color-schemes/` |
| Herramientas de tema | `nwg-look 1.2.1`, `qt5ct`, `qt6ct`, `xsettingsd` (kvantummanager se referencia en windowrules pero **no está instalado**) |

## 5. Aplicaciones instaladas (selección)

- Navegador: **firefox 160.0.1** · Archivos: **dolphin 26.08.3** (KDE)
- Sistema: **btop 1.4.8**, **fastfetch 2.71.0**, pavucontrol, pipewire/wireplumber,
  power-profiles-daemon, polkit
- Utilidades CLI modernas: `fzf`, `ripgrep`, `ripgrep-all`, `fd`, `eza`, `bat`, `jq`,
  `wget`, `curl`, `git`, `ffmpeg`, `imagemagick`(vía dependencias)
- Multimedia: VLC (plugins completos), `mpv` no aparece en la lista filtrada
- Ofimática: LibreOffice Fresh 26.8.3
- Juegos: Steam/gamescope referenciados en reglas (no confirmados en la lista filtrada)

## 6. Paleta actual (dos fuentes conviviendo)

**Paleta CachyOS** (`config/colors.lua`, usada por bordes de Hyprland):

| Token | Valor | Uso |
|---|---|---|
| `CACHYLGREEN` | `rgba(82dcccff)` | borde activo (inicio del gradiente), splash |
| `CACHYMGREEN` | `rgba(00aa84ff)` | — |
| `CACHYDGREEN` | `rgba(007d6fff)` | borde activo (fin del gradiente) |
| `CACHYLBLUE` | `rgba(01ccffff)` | groupbar activo |
| `CACHYMBLUE` | `rgba(182545ff)` | — |
| `CACHYDBLUE` | `rgba(111826ff)` | groupbar bloqueado |
| `CACHYWHITE/GREY/GRAY` | `ffffffff` / `ddddddff` / `798bb2ff` | bordes inactivos |

**Paleta Noctalia / M3-tonal-spot** (kitty, alacritty, GTK, Qt, btop):

| Rol | Hex | Rol | Hex |
|---|---|---|---|
| background | `#1e1e20` | foreground | `#f2f2f3` |
| surface | `#27282a` | muted | `#afb1b6` |
| accent (primary) | `#6791e4` | on-accent | `#181d25` |
| destructive/error | `#fd4663` | link | `#695cd6` |
| terminal colors 1-7 | `#fd4663 #6791e4 #7f75f1 #ad69cf #93b1ec #9f96e9 #afb1b6` | bright 8-15 | `#66696c #ff6a7b #70a1ff #8f86ff #cc68ff #a2c1ff #afa5ff #f2f2f3` |

> **Hallazgo relevante:** conviven dos sistemas de color. El borde de Hyprland usa verde
> CachyOS, mientras que el resto del escritorio usa un esquema azul/violeta derivado del
> wallpaper. Esto es una oportunidad clara de unificación (ver hoja de ruta).

## 7. Restricciones y riesgos detectados

1. **GPU antigua**: Intel Sandy Bridge (2011). Blur `passes=4` + transparencias + springs
   pueden costar frames. Medir con `hyprctl` / `intel_gpu_top` antes de subir efectos.
2. **Sin VRR/HDR**: descartar recomendaciones que dependan de esas características.
3. **Un solo monitor 1440×900**: las reglas para `MONITOR2/3` y `NUM_WPM=3` están
   preparadas para crecer, pero hoy no se usan.
4. **AZERTY**: cualquier atajo nuevo debe usar `code:` o verificar el layout, no caracteres.
5. **Config Lua reciente**: muchos tutoriales antiguos siguen usando `hyprland.conf`;
   hay que traducirlos a la API `hl.*`.
6. **Doble fuente de color**: CachyOS green vs. M3 azul → inconsistencia visual.

## 8. Reproducibilidad

Los comandos usados están en `apendices/comandos-auditoria.sh`. Los crudos en:

- `apendices/paquetes-instalados.txt` · `apendices/familias-fuentes.txt`
- `apendices/hyprland-version.txt` · `apendices/hyprctl-monitors.txt` · `apendices/lspci.txt`
- `configuracion-actual/` (copia completa de los archivos citados)
