# 14 · Herramientas GUI de ricing: "tú eliges, el programa lo hace"

> Respuesta a la petición explícita: **programas con interfaz gráfica que automatizan
> el ricing**, de modo que no haya que editar a mano docenas de archivos. Aquí se
> distingue entre herramientas que *editan la configuración por ti* (settings GUI),
> las que *generan temas a partir de una imagen*, y las que *gestionan wallpapers*.
> Toda la evidencia está en `sources/2026-11-21-gui-*.md`.

## 1. Por qué una GUI cambia el problema

El ricing clásico es un flujo de **editar → recargar → observar → repetir** en
archivos de texto (Lua, JSONC, CSS, TOML). Una GUI de ricing sustituye ese bucle
por **elegir → previsualizar → guardar**. Según los README analizados, las
herramientas más serias comparten cuatro propiedades:

1. **Vista previa en vivo** (aplican al compositor en caliente antes de guardar).
2. **No destruyen tu config**: escriben en un archivo propio o hacen backup.
3. **Deshacer / restaurar**: `Ctrl+Z`, perfiles o copia de seguridad automática.
4. **Detección de lo instalado**: leen la config existente y generan los controles.

> **HECHO:** `hyprmod` y `Waybar Configurator GUI` declaran explícitamente
> *live preview* y *no tocar la config original* ([hyprmod](../sources/2026-11-21-gui-hyprmod.md),
> [waybar-configurator](../sources/2026-11-21-gui-waybar-configurator.md)).
> **INCIERTO:** que funcionen sin problemas con una config **modular en Lua** como la tuya
> (`require("config.*")`): hyprmod anuncia soporte Lua 0.55+, pero no documenta el caso
> de múltiples módulos. Probar en copia.

## 2. Mapa rápido (qué hace cada una por ti)

| Herramienta | Categoría | Qué automatiza | Toolkit | Estado / estrellas | Encaja contigo |
|---|---|---|---|---:|---|
| **hyprmod** | Settings Hyprland | Cualquier opción de Hyprland: curvas bezier, monitores, keybinds, window/layer/workspace rules, cursor, variables de entorno, perfiles | GTK4 + libadwaita (Python 3.12+) | Activo, ★1154,Actualizado 2026-11-16 | ⭐⭐⭐ Mejor opción global |
| **wpgtk** | Color + wallpaper + plantillas | Genera paleta con pywal, edita esquemas, guarda paleta por wallpaper, sustituye keywords en plantillas de cualquier archivo, temas GTK propios, 200+ esquemas | GTK3 (Python) | Activo, ★2193, actualizado 2026-08 | ⭐⭐⭐ Si quieres sustituir/augmentar Noctalia |
| **Themix GUI** (ex-oomox) | Diseño de temas | Diseña temas GTK2/3, iconos y exporta vía plugins (Oomox, Materia, Base16 → Alacritty, GTK4, KDE, Qt5ct/Qt6ct, Vim…) | GTK3 (Python) | Activo, ★2328, actualizado 2026-10 | ⭐⭐ Para temas a medida |
| **Kvantum Manager** | Tema Qt | Gestiona y crea temas Qt basados en SVG; control casi total de widgets | Qt (C++) | Activo, ★2054, actualizado 2026-11-20 | ⭐⭐ Si usas apps Qt (Dolphin, VLC) |
| **Gradience** | Tema GTK | Cambia Adwaita "con facilidad", editor visual de temas | GTK4 + libadwaita | **Archivado** (junio 2024), ★1282 | ⚠️ Solo por nostalgia |
| **Azote** | Wallpaper | Navegador +setter de fondos para wlroots/sway (swaybg), multi-monitor, recorte, gestión de color | GTK3 (Python) | Activo, ★406, actualizado 2025-05 | ⭐⭐ Alternativa al panel de Noctalia |
| **Variety** | Wallpaper | Descarga de Wallhaven/Unsplash/Bing/Reddit, rotación temporal, filtros, citas y reloj | GTK (Python) | **Modo mantenimiento**, ★1728 | ⚠️ Útil pero estancado |
| **HydraPaper** | Wallpaper multi-monitor | Fondos distintos por monitor en GNOME | GTK (Python) | Desde 2020, develop. movido a GitLab, ★180 | ❌ No aplica (GNOME, 1 monitor) |
| **Waybar Configurator GUI** | Barra (Waybar) | Edita módulos, colores, opacity, border-radius, posición; preview CSS; restore | GTK4 + libadwaita | WIP (v0.6b–1.0a), ★118 | ❌ No usas Waybar, usa Noctalia |
| **hyprland-guiutils** | Utilidades oficiales | `hyprland-run`, `hyprland-dialog`, `hyprland-welcome`, update/donate screens | Qt | **Instalado** (0.2.2-6), ★47 | ✅ Ya lo tienes |
| **nwg-look** | GTK look | Editor GUI de tema GTK, iconos, cursor y fuentes | GTK3 | **Instalado** (1.2.1) | ✅ Ya lo tienes |
| **Linux-Ricing-Settings** | Meta-GUI (experimental) | Detecta herramientas instaladas y genera UI desde la sintaxis real de cada config | Rust + Slint | ★0, prototipo | ⚠️ Concepto interesante, no para producción |

Fuentes: [metadatos de GitHub](../sources/2026-11-21-gui-tools-metadata.md) y los README individuales.

## 3. Las tres herramientas que merecen análisis profundo

### 3.1 hyprmod — "Ajustes de Hyprland" como debe ser

Es un settings app **nativo GTK4/libadwaita** para Hyprland._lo más cercano a lo que pediste_:
abres una ventana, tocas un control y el compositor cambia al instante.

Características declaradas en su README ([fuente](../sources/2026-11-21-gui-hyprmod.md)):

- **Vista previa en vivo**: los cambios se aplican al compositor en ejecución.
- **Tu config queda intacta**: escribe sólamente en `hyprland-gui.conf`.
- **Deshacer con `Ctrl+Z`**, página de *Pending Changes* antes de guardar.
- **Perfiles**: guarda, nombra y comparte configuraciones completas como `.conf`;
  CLI: `hyprmod profile list|apply|next|previous`.
- **Soporte Lua** (0.55+): migra y edita `hyprland.lua` directamente.
- **Editor de curvas bezier con preview de animación**.
- **Editor de monitores** con VRR, detección de 10-bit y HDR con defaults seguros.
- **Editor de keybinds** con captura interactiva, incluidos `bindm` (ratón).
- **Editores de window rules, layer rules y workspace rules** con preview.
- **Autostart y variables de entorno**; selector de cursor con preview; búsqueda
  global (`Ctrl+F`); "Config DNA" (huella visual del perfil).
- Licencia GPL-3.0, Python 3.12+, disponible en AUR (`hyprmod`).

**Instalación en tu CachyOS** (tienes `yay`):

```bash
yay -S hyprmod          # AUR, preferido sobre el install.sh con curl|sh
hyprmod                 # primera ejecución: que detecte tu config
```

**Advertencias para tu caso:**

1. Tu configuración es **modular** (`hyprland.lua` → `require("config.*")`).
   hyprmod anuncia soporte Lua, pero no documenta módulos `require`d. Haz una copia
   (`cp -r ~/.config/hypr ~/ricing/configuracion-actual/hypr-backup`) antes de probar.
2. Usas **AZERTY con binds por `code:`**. El editor de keybinds captura teclas
   interactivamente: verifica que no reescriba `code:10…19` como caracteres `& é " '`.
3. Tu GPU no tiene VRR/HDR: ignora esas secciones del editor de monitores.
4. El instalador `curl … | sh` del README es menos deseable que el paquete AUR en
   un sistema Arch; además, la política de esta investigación prefiere paquetes.

**Veredicto [OPINIÓN]:** es la herramienta con mayor retorno para ti. Te permite
experimental con `rounding`, `blur`, curvas y reglas sin editar Lua a mano, y
encima no rompe tu archivo original.

### 3.2 wpgtk — paleta + wallpaper + plantillas en una GUI

`wpgtk` usa **pywal** como generador pero añade GUI y gestión:
([fuente](../sources/2026-11-21-gui-wpgtk.md))

- Guarda el esquema generado **junto al wallpaper** al que pertenece.
- Permite **editar los colores** generados (algo que pywal no hace) y ordenarlos
  para mejorar legibilidad.
- **Sistema de plantillas**: creas una plantilla de cualquier archivo de texto y
  wpgtk sustituye keywords al cambiar de tema. Ideal para `colors.lua`, GTK CSS,
  kitty.conf, btop, fish…
- Incluye los **200+ esquemas predefinidos** de pywal, modificables.
- Temas GTK propios, iconos dinámicos claro/oscuro, keywords personalizados.
- Licencia GPLv2, activo (actualizado agosto 2026).

**Relación con tu Noctalia:** hoy Noctalia ya hace wallpaper → paleta → 7 destinos.
wpgtk **solapa** con esa función. No conviene tener dos motores generando colores
a la vez. Las opciones sensatas son:

| Opción | Qué hacer | Cuándo |
|---|---|---|
| A. Mantener Noctalia | No instalar wpgtk; usar los templates de Noctalia y añadir `hyprland.lua` a `builtin_ids` | Recomendado: ya funciona y está integrado |
| B. wpgtk como fuente | Desactivar `theme.source = "wallpaper"` en Noctalia y dejar que wpgtk escriba las plantillas | Si quieres control manual fino de cada color |
| C. Híbrido | Usar wpgtk sólo como *galería* de esquemas y exportarlos a Noctalia | Curiosidad / inspiración |

### 3.3 Themix GUI y Kvantum — diseño de temas "de verdad"

- **Themix GUI** (antes oomox): aplicación gráfica para **diseñar temas** y
  exportarlos mediante plugins: Oomox/Materia (GTK2/3, Cinnamon, GNOME, Openbox,
  Xfwm), iconos (Archdroid, Numix, Papirus, Suru++), y Base16 que cubre
  **Alacritty, GTK4, KDE, Qt5ct, Qt6ct, Vim** y más. Tiene plugins de importación
  que generan paletas desde una imagen o desde Xresources
  ([fuente](../sources/2026-11-21-gui-themix.md)). En Arch: `yay -S themix-full-git`.
- **Kvantum Manager**: motor de temas **Qt basado en SVG**; permite controlar
  casi cada aspecto de los widgets y seleccionar/activar temas desde la GUI
  ([fuente](../sources/2026-11-21-gui-kvantum.md)). Tú ya lo referencias en
  `windowrules.lua` (`kvantummanager` flotante) pero **no está instalado**.

Para tu sistema, Kvantum tiene sentido por **Dolphin y VLC (Qt)**. Noctalia ya
genera `qt5ct/qt6ct`, pero Kvantum va un paso más allá en el estilo de widgets.

**Gradience** está **archivado desde 2024** ([fuente](../sources/2026-11-21-gui-gradience.md)):
no lo instales para un sistema que se actualiza en 2026.

## 4. Gestores de wallpaper con GUI

| Herramienta | Lo que hace por ti | Wayland | Veredicto para ti |
|---|---|---|---|
| **Noctalia wallpaper panel** (ya instalado) | Selecciona fondo y dispara regeneración de tema M3 | ✅ Nativo | ✅ **El que ya usas**: `SUPER+SHIFT+W` |
| **Azote** | Explorador + setter para wlroots vía `swaybg`, multi-head, recorte, gestión de color | ✅ (wlroots) | ⭐ Quite útil si algún día usas 2 monitores; hoy redundante |
| **Variety** | Descarga automática desde Wallhaven/Unsplash/Bing/Reddit, rotación, favoritos | ⚠️ Depende del DE | ⚠️ Modo mantenimiento; no probado en Hyprland |
| **HydraPaper** | Fondos distintos por monitor | ❌ GNOME/MATE/Budgie | ❌ Descartado |
| **WallLust** | Wallpaper daemon + GUI, transiciones y mpv video, integración pywal | ✅ (según descripción) | ⚠️ Muy nuevo, sin validar |

Fuentes: [azote](../sources/2026-11-21-gui-azote.md),
[variety](../sources/2026-11-21-gui-variety.md),
[hydrapaper](../sources/2026-11-21-gui-hydrapaper.md),
[metadatos](../sources/2026-11-21-gui-tools-metadata.md).

## 5. Qué NO conviene instalar en tu sistema

1. **Waybar Configurator GUI**: edita `~/.config/waybar/config.jsonc` y `style.css`.
   Tú no usas Waybar: usas Noctalia. Instalarlo sería añadir un segundo editor para
   un archivo que no existe. (Sí sería útil si algún día cambias de shell.)
2. **Gradience**: archivado.
3. **HydraPaper**: GNOME y multi-monitor.
4. **Variety como reemplazo de Noctalia**: en modo mantenimiento y su integración
   con Wayland es incierta; además duplicaría la gestión de wallpapers.
5. **Linux-Ricing-Settings**: ★0, prototipo sin documentación. Interesante como
   idea (generar UI desde la sintaxis real de cada config), pero no para producción.
6. **Instaladores `curl | sh`** cuando exista paquete AUR: en CachyOS, `yay -S` es
   más auditable y reversible.

## 6. Tabla de decisión final [OPINIÓN]

| Necesidad | Herramienta recomendada | Por qué |
|---|---|---|
| Cambiar opciones de Hyprland sin editar Lua | **hyprmod** | Live preview, no toca tu config, soporta Lua, perfiles |
| Cambiar paleta/wallpaper | **Noctalia** (ya instalado) | Integrado, es el corazón de tu rice |
|editar colores finamente / plantillas | **wpgtk** (opcional) | GUI para edición de paleta + keywords |
| Temas GTK a medida | **Themix GUI** | Exporta a GTK/GTK4/Base16 |
| Temas Qt para Dolphin/VLC | **Kvantum Manager** | Widgets SVG, GUI dedicada |
| Ajustes GTK básicos | **nwg-look** (ya instalado) | Cubre tema/iconos/cursor/fuentes |
| Fondos multi-monitor futuros | **Azote** | wlroots nativo, vía swaybg |
| Ver qué utilidades GUI trae Hyprland | **hyprland-guiutils** (ya instalado) | `hyprland-run`, `hyprland-dialog` |

**Orden de instalación sugerido:** 1) `yay -S hyprmod` → 2) probar en copia de la
config → 3) `yay -S kvantum` si quieres Dolphin/VLC más coherentes → 4) Themix sólo
si vas a diseñar tu propio tema GTK → 5) wpgtk sólo si abandonas el theming de Noctalia.

## 7. Fuentes

- [hyprmod README](../sources/2026-11-21-gui-hyprmod.md) · [wpgtk README](../sources/2026-11-21-gui-wpgtk.md)
- [Themix GUI README](../sources/2026-11-21-gui-themix.md) · [Kvantum README](../sources/2026-11-21-gui-kvantum.md)
- [Gradience README](../sources/2026-11-21-gui-gradience.md) · [Azote README](../sources/2026-11-21-gui-azote.md)
- [Variety README](../sources/2026-11-21-gui-variety.md) · [HydraPaper README](../sources/2026-11-21-gui-hydrapaper.md)
- [Waybar Configurator README](../sources/2026-11-21-gui-waybar-configurator.md)
- [metadatos de GitHub](../sources/2026-11-21-gui-tools-metadata.md)
- [perfil del sistema](../00-perfil-del-sistema.md)
