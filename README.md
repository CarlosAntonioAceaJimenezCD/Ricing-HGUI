# Ricing HGUI

Investigación exhaustiva sobre **ricing** (personalización avanzada de escritorios Linux),
centrada en el sistema real del autor: **CachyOS + Hyprland 0.57.2 (config Lua) +
Noctalia 5.6.0**, sobre Intel Sandy Bridge, 1440×900, fish, kitty/alacritty y Nerd Fonts.

> Propósito: servir como base de conocimiento y como punto de partida para crear
> **tu propia GUI de ricing** (de ahí "HGUI": *Hyprland GUI*).

## 🚀 Empezar aquí

| Si quieres... | Lee |
|---|---|
| Entender qué es el ricing | [01 · Qué es ricing](investigacion/01-que-es-ricing.md) |
| Ver tu sistema auditado | [00 · Perfil del sistema](00-perfil-del-sistema.md) |
| **Saber qué hacer NOW** | [12 · Hoja de ruta personalizada](investigacion/12-hoja-de-ruta-personalizada.md) |
| Entender tu Hyprland 0.57 | [02 · Hyprland 0.57](investigacion/02-hyprland-0-57.md) |
| Unificar colores | [05 · Sistema de colores](investigacion/05-sistema-de-colores.md) |
| Herramientas con GUI que lo hacen por ti | [14 · Herramientas GUI](investigacion/14-herramientas-gui-de-ricing.md) |
| **Crear tu propia GUI** | [15 · Crear tu propia GUI](investigacion/15-crear-tu-propia-gui.md) |
| Glosario | [13 · Glosario](investigacion/13-glosario.md) |

## 📚 Índice completo de la investigación

| # | Documento | Contenido |
|---|---|---|
| 00 | [Perfil del sistema](00-perfil-del-sistema.md) | Inventario real: 1232 paquetes, GPU, monitor, configs, paletas |
| 01 | [Qué es ricing](investigacion/01-que-es-ricing.md) | Definición, historia, cultura, estilos, tendencias 2025-2026 |
| 02 | [Hyprland 0.57](investigacion/02-hyprland-0-57.md) | Arquitectura, releases 0.56→0.57.2, API `hl.*`, migración |
| 03 | [Arquitectura de un rice](investigacion/03-arquitectura-de-un-rice.md) | 6 capas, flujo de color, puntos de control |
| 04 | [Componentes del escritorio](investigacion/04-componentes-del-escritorio.md) | Catálogo de 14 capas con estado ✅/⚠️/❌ |
| 05 | [Sistema de colores](investigacion/05-sistema-de-colores.md) | OKLCH, tokens, WCAG con ratios reales, Material You |
| 06 | [Tipografía](investigacion/06-tipografia.md) | Nerd Fonts, escala, fontconfig, recomendaciones |
| 07 | [Iconos y cursores](investigacion/07-iconos-y-cursores.md) | XDG vs QML vs glyphs, SVG, Bibata, accesibilidad |
| 08 | [Animaciones y efectos](investigacion/08-animaciones-y-efectos.md) | Bezier vs springs, blur, wobble, coste en iGPU |
| 09 | [Wallpapers y generative theming](investigacion/09-wallpapers-y-generative-theming.md) | m3-tonal-spot, pywal/wallust/matugen, semilla reproducible |
| 10 | [Dotfiles y gestión](investigacion/10-dotfiles-y-gestion.md) | Git, Stow, chezmoi, Nix; backup/restore |
| 11 | [Comunidad y recursos](investigacion/11-comunidad-y-recursos.md) | r/unixporn, GitHub, wikis, licencias, cómo publicar |
| 12 | [Hoja de ruta personalizada](investigacion/12-hoja-de-ruta-personalizada.md) | Quick wins, fases, checklist, qué NO hacer |
| 13 | [Glosario](investigacion/13-glosario.md) | Términos de ricing, Wayland, Hyprland |
| 14 | [Herramientas GUI de ricing](investigacion/14-herramientas-gui-de-ricing.md) | hyprmod, wpgtk, Themix, Kvantum, Azote… |
| 15 | [Crear tu propia GUI](investigacion/15-crear-tu-propia-gui.md) | Python + GTK4/libadwaita, backups automáticos, código, i18n |
| 16 | [Archivo web oficial](investigacion/16-archivo-web-oficial.md) | 744 páginas de documentación oficial, criterios y fallos |
| 17 | [Inventario de opciones](investigacion/17-inventario-de-opciones.md) | 184 opciones reales inventariadas con tipos, rangos y mapeo a `hl.config` |

## 📁 Estructura del repositorio

```text
ricing/
├── 00-perfil-del-sistema.md     # auditoría del equipo
├── investigacion/               # 16 documentos de análisis
├── sources/                     # 49 fuentes archivadas con frontmatter
│                                # (URL, título, fecha, conversor)
├── configuracion-actual/        # copia de los dotfiles del sistema (sin secretos)
├── recursos/
│   └── hypr-rice-gui/main.py    # prototipo funcional de GUI (GTK4)
├── archivo-web/                 # 744 páginas oficiales archivadas (ver INDICE.md)
├── repositorios/                # clones de referencia (ver su README)
├── apendices/                   # inventarios y scripts de auditoría/conversión
├── .staging/                    # artefactos crudos descargados (ignorado en git)
└── .tools/                      # venv con markitdown (ignorado en git)
```

## 🔎 Metodología

1. **Auditoría local** (`apendices/comandos-auditoria.sh`) → `00-perfil-del-sistema.md`.
2. **Descarga de fuentes primarias** con `curl` (wiki de Hyprland, GitHub, docs de
   Noctalia, READMEs de herramientas) → `.staging/`.
3. **Conversión a Markdown** con `markitdown` (instalado en `.tools/venv`) → `sources/`.
   Cada archivo lleva frontmatter con `url`, `title`, `fetched_at` y `fetcher`.
4. **Síntesis** en `investigacion/`, distinguiendo **[HECHO]**, **[OPINIÓN]** e
   **[INCIERTO]** y citando `sources/`.
5. **Prototipo** ejecutable en `recursos/hypr-rice-gui/main.py`, con **backups automáticos**
   (`backup_manager.py`): antes de cada cambio, temporizados, con SHA-256, retención,
   **historial de puntos en el pasado** (inspeccionar archivos, comparar, restaurar o borrar cualquier copia),
   **identidad Config DNA**, un **modelo genérico de 46 opciones** (`config_model.py`) con controles generados automáticamente y vista previa en vivo,
   **editor de keybinds** (`keybinds.py`), **detección de monitores** (`monitors.py`) e **integración con Wallhaven/local** (`wallpapers.py`).

## 🛠️ Usar el prototipo de GUI

Requisitos ya presentes en CachyOS: Python 3.14, `python-gobject`, `gtk4`, `libadwaita`.

```bash
python3 recursos/hypr-rice-gui/main.py
```

El prototipo aplica `rounding`/`blur` en vivo con `hyprctl` y persiste el estado en
`~/.config/hypr/config/ui-settings.lua` **haciendo backup** antes de sobrescribir.
Antes de usarlo, conecta ese módulo a tu config según
[15-crear-tu-propia-gui.md](investigacion/15-crear-tu-propia-gui.md#31-el-archivo-de-estado-lua-para-encajar-con-tu-config).

## ⚠️ Notas

- Los documentos están en **español**; los comandos, rutas y nombres de variables se
  mantienen en su idioma original técnico.
- El código del prototipo y los scripts de `apendices/` son propios; las fuentes en
  `sources/` y los clones en `repositorios/` conservan la licencia de sus autores.
- No se incluyen secretos: se excluyeron `fish_variables`, keyrings y credenciales.
- Repositorios de referencia clonados se ignoran en Git para mantener el repo ligero;
  `repositorios/README.md` explica cómo recuperarlos.

## Créditos

Investigación realizada con foco en la configuración real de `thony70807` (CachyOS).
Fuentes primarias: Hyprland Wiki, Hyprland Releases, Noctalia Docs, ArchWiki, Material
Color Utilities, y los README de wpgtk, Themix, Kvantum, Azote, Variety, HydraPaper,
Waybar Configurator, hyprmod, Nerd Fonts, Catppuccin, Bibata y adw-gtk3.
