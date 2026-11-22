# 18 · Qué se personaliza en un rice (análisis de repositorios)

> Análisis de los 4 repos de dotfiles clonados (`noctalia`, `dots-hyprland`,
> `Hyprland-Dots`, `hyprmod`) más la configuración real del autor. Los repos son
> shallow (1 commit), así que se usó evidencia estructural: archivos marcados
> como editables, número de plantillas y áreas expuestas por GUIs del ecosistema.

## 1. Ranking de las 10 zonas más personalizadas

| # | Zona | Evidencia | Ejemplo de cambio |
|---:|---|---|---|
| 1 | **Paleta / tema global** | 171 `.conf` de temas en `Hyprland-Dots/config/kitty/kitty-themes/`; 59 CSS de Waybar; `colors.lua`, `noctalia.css`, `noctalia.colors` | Cambiar `$color12` por el generado por wallust, o `wallpaper_scheme = "m3-tonal-spot"` |
| 2 | **Barra** | `noctalia/config.toml` (widgets `start/center/end`, `capsule_group`, `thickness`); ~30 páginas de widgets en docs de Noctalia | Reordenar módulos, meter `group:g1` con temp/gpu/ram |
| 3 | **Keybinds de apps** | `binds.lua` (168 líneas, fix AZERTY); `UserKeybinds.conf` con instrucciones de `unbind`; página GUI dedicada en hyprmod | Reasignar `SUPER+W` a otro navegador |
| 4 | **Apps por defecto** | `variables.lua:3-7`; `01-UserDefaults.conf`; `custom/variables.lua` en dots-hyprland | `BROWSER = "firefox"` → `"zen-browser"` |
| 5 | **Animaciones** | 17 presets en `Hyprland-Dots/config/hypr/animations/`; `animations.lua` | Cambiar `speed`/spring o cargar `ML4W - fast.conf` |
| 6 | **Reglas de ventana** | `windowrules.lua` (128 líneas: PiP, Steam, Discord, Dolphin), 4 variantes de WindowRules.conf | Hacer flotante una app, fijarla a un monitor |
| 7 | **Autostart** | `autostart.lua`; `execs.lua`; `Startup_Apps.conf` | Añadir keyring, hypridle, clipboard |
| 8 | **Fuentes y cursor** | `uwsm-env` (`Bibata-Modern-Ice`, 24), `[font]` en alacritty, hyprlock | Cambiar fuente/cursor en todos lados a la vez |
| 9 | **Monitores / workspaces** | `monitors.lua`, `workspaces.lua`, `MONITOR1..3`, `NUM_WPM` | Añadir monitor, cambiar workspaces persistentes |
| 10 | **Bordes / gaps / blur** | `decorations.lua`; docenas de sub-opciones `decoration:blur:*` | `rounding`, `blur.size/passes`, gradientes |

## 2. Cómo representan las apps por defecto

| Repo | Formato | Detalle relevante |
|---|---|---|
| **CachyOS/Lua actual** | Variables Lua globales en `variables.lua` | `TERMINAL`, `FILE_MANAGER`, `BROWSER`, `EDITOR` (con argumentos), `CALCULATOR`. Los binds usan `launchPrefix .. VAR` |
| **noctalia** | Sin variables: $TERMINAL / MIME / PATH | `terminal_launch.cpp` lee `getenv("TERMINAL")`; URLs por default MIME (`xdg-mime`) |
| **dots-hyprland** | Variables minúsculas + script | `browser = launch_first_available.sh 'chrome' 'zen' 'firefox'…` ( patrón primario/secundario ya existe) |
| **Hyprland-Dots** | `01-UserDefaults.conf` | `$term`, `$files`, `$edit`, `$Search_Engine`; directorio `UserConfigs/` protegido en upgrades |
| **hyprmod** | Explícitamente fuera de alcance | README: default apps pertenece a un control center; pero aporta `desktop_apps.py` (picker de `.desktop`) |

## 3. Hallazgo accionable para este sistema

- `variables.lua` define **`TERMINAL`** pero `uwsm-env` exportaba **`TERM`**. Noctalia lee `TERMINAL`, así que no veía el terminal elegido. El editor de apps ahora sincroniza `export TERMINAL/BROWSER/EDITOR` en `uwsm-env`.
- El patrón **primaria + secundaria** de dots-hyprland se adoptó como: `BROWSER_SECONDARY` en `variables.lua` + un único bind extra en `binds.lua` (`SUPER+SHIFT+W`).
- Los binds **no se reescriben** al cambiar de app: siguen leyendo la variable. El cambio en vivo se hace con `hyprctl eval` (unbind + bind con el valor resuelto); el cambio de **entorno** requiere reiniciar sesión.

## 4. GUI añadida

Pestaña **Aplicaciones**: campos para `TERMINAL`, `FILE_MANAGER`, `BROWSER`,
`BROWSER_SECONDARY`, `EDITOR`, `CALCULATOR`, validación (`shutil.which`),
backup previo, escape Lua, sincronización de entorno y botón de recarga de Hyprland.

Módulo: `recursos/hypr-rice-gui/apps.py`.

## 5. Fuentes

- Repos clonados en `repositorios/` (ver `repositorios/README.md`).
- `configuracion-actual/hypr/config/variables.lua`, `binds.lua`, `shell/uwsm-env`.
- `sources/2026-11-21-hyprland-config-options.md` y docs de Noctalia en `archivo-web/`.
