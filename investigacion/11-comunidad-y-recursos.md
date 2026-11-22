# 11 · Comunidad y recursos

> Documento de investigación · Proyecto de ricing para CachyOS + Hyprland 0.57.2 (Lua) + Noctalia 5.6.0
> Fuentes consultadas el 2026-11-21/22, archivadas en `sources/`. Repositorios de referencia clonados en `repositorios/`.

## Convención y alcance

| Marca | Significado |
|---|---|
| **HECHO** | Verificable en una fuente archivada o en un repositorio clonado. |
| **OPINIÓN** | Recomendación del autor de este documento. |
| **INCIERTO** | Convención comunitaria no documentada en el corpus o dato que debe verificarse en el sitio original. |

Este documento es un **mapa**, no un tutorial: indica dónde está la información, qué fiabilidad tiene y cómo usarla sin copiar ciegamente. Las URLs originales se citan tal como aparecen en el frontmatter de cada fuente.

---

## 1. Mapa general de la comunidad

La escena del ricing no es un único foro, sino varias capas que se solapan:

| Capa | Función | Ejemplos documentados en el corpus |
|---|---|---|
| **Galerías / escaparate** | Mostrar el resultado y motivar | r/unixporn (mencionado en [pywal](sources/2026-11-21-pywal-readme.md)), [Hyprland Showcase / Hall of Fame](sources/2026-11-21-hyprland-lua-utilities.md) ([URL](https://hypr.land/hall_of_fame)) |
| **Repositorios de dotfiles** | Distribuir la configuración completa | [Preconfigured setups](sources/2026-11-21-hyprland-preconfigured-setups.md): Omarchy, ML4W, end-4, HyDE, Dank Linux, JaKooLit, etc. |
| **Documentación oficial** | Fuente de verdad técnica | [Hyprland Wiki](sources/2026-11-21-hyprland-must-have.md), [ArchWiki](sources/2026-11-21-archwiki-hyprland.md), [Noctalia Docs](sources/2026-11-21-noctalia-readme.md) |
| **Proyectos de tema** | Paletas y fundamentos reutilizables | [Catppuccin](sources/2026-11-21-catppuccin-readme.md), [Material Color Utilities](sources/2026-11-21-material-you-color-system.md), [Nerd Fonts](sources/2026-11-21-nerd-fonts-readme.md), [Bibata](sources/2026-11-21-bibata-readme.md) |
| **Chats y canales** | Resolución rápida de dudas | Discord de [Noctalia](sources/2026-11-21-noctalia-readme.md), [Catppuccin](sources/2026-11-21-catppuccin-readme.md) y [JaKooLit](sources/2026-11-21-jakoolit-hyprland-dots.md); Matrix de [wallust](sources/2026-11-21-wallust-readme.md) |
| **Creadores / YouTube** | Tutoriales paso a paso | Canales de [ML4W y JaKooLit](sources/2026-11-21-hyprland-preconfigured-setups.md) enlazados por la wiki oficial |

**OPINIÓN.** Para este usuario, el orden de utilidad es: documentación oficial → repositorios clonados → galerías → vídeos. Las galerías inspiran, pero rara vez explican *por qué* una configuración funciona.

---

## 2. r/unixporn y sus normas de publicación

**HECHO (mínimo).** El README de pywal enlaza explícitamente una búsqueda en `https://www.reddit.com/r/unixporn/search?q=wal&restrict_sr=on&sort=relevance&t=all` como ejemplo de capturas de pantalla de la comunidad ([pywal · README](sources/2026-11-21-pywal-readme.md), [URL original](https://github.com/dylanaraps/pywal/blob/master/README.md)). Eso acredita que el subreddit es el escaparate histórico de la escena, pero **nada más**.

**INCIERTO — leer antes de publicar.** El corpus **no contiene una copia de las normas de r/unixporn**. La convención que suele describirse —publicar una **captura de pantalla** del escritorio, indicar el stack en el título con un *tag* tipo `[HYPR]`, y **acompañar los dotfiles** (enlace a GitHub) en un comentario— es una práctica reportada por la comunidad, **no verificada aquí**. Antes de publicar, consulta la sidebar/reglas actuales del subreddit; las normas cambian y una publicación que no las cumple se elimina.

**OPINIÓN.** La lógica de esa convención es sana: la imagen muestra el *resultado* y los dotfiles permiten *reproducirlo*. Sin dotfiles, una captura es publicidad; sin captura, un repo es solo código. En este proyecto, la pareja natural sería `captura.png` + enlace a una rama versionada de `~/.config` + una línea de `fastfetch` con el stack (§6).

---

## 3. GitHub: cómo buscar y qué repos mirar

### 3.1 Estrategia de búsqueda

**OPINIÓN.** Búsquedas que funcionan mejor en GitHub (`https://github.com/search`):

- `hyprland dotfiles`, `hyprland-dots`, `dots-hyprland`, `hyprland lua config` — para configs completas.
- `noctalia theme`, `quickshell bar`, `material you hyprland` — para la capa de shell/tema.
- `catppuccin kitty`, `nerd font fish prompt` — para piezas concretas.
- Filtros útiles: `stars:>100`, `pushed:>2026-01-01`, `language:Lua`. **INCIERTO:** la sintaxis exacta de los calificadores debe verificarse en la ayuda de GitHub; se cita por costumbre, no por fuente archivada.

**HECHO.** La wiki oficial ya mantiene una lista curada de setups preconfigurados con enlaces a GitHub: Omarchy (`https://omarchy.org/`), ML4W (`https://github.com/mylinuxforwork/dotfiles`), end-4 (`https://github.com/end-4/dots-hyprland`), HyDE (`https://github.com/HyDE-Project/HyDE`), Dank Material Shell (`https://github.com/AvengeMedia/DankMaterialShell`), JaKooLit (`https://github.com/JaKooLit/Hyprland-Dots`) y otros ([Hyprland · Preconfigured setups](sources/2026-11-21-hyprland-preconfigured-setups.md), [URL original](https://wiki.hypr.land/getting-started/preconfigured-setups/)). Es el mejor punto de partida porque alguien ya ha filtrado por "mantenido".

### 3.2 Señales de calidad en un repo

| Señal | Por qué importa | Evidencia |
|---|---|---|
| **Estrellas** | Popularidad, no garantía de calidad | Noctalia: **12 172 estrellas, 1 013 forks**, C++, creado el 2025-07-11 ([metadatos](sources/2026-11-21-noctalia-repo-metadata.md), [API](https://api.github.com/repos/noctalia-dev/noctalia)) |
| **Último commit / actividad** | Indica si sobrevive a la next update de Hyprland | Badges de "last commit" en [JaKooLit](sources/2026-11-21-jakoolit-hyprland-dots.md) y [Noctalia](sources/2026-11-21-noctalia-readme.md) |
| **Avisos de archivado** | Cambio de mantenedor o abandono | JaKooLit anuncia archivo en marzo de 2026 → `LinuxBeginnings/Hyprland-Dots` ([README](sources/2026-11-21-jakoolit-hyprland-dots.md)) |
| **LICENSE presente** | Permite reutilizar con seguridad | Ver §7 |
| **Script de instalación legible** | Evita sorpresas | La wiki avisa de configs que "se inyectan en profundidad" y cuyo desinstalador puede no limpiar ([Preconfigured setups](sources/2026-11-21-hyprland-preconfigured-setups.md)) |

### 3.3 Los tres repos clonados en este proyecto

| Repo (ruta local) | Licencia verificada | Qué aporta | Fiabilidad |
|---|---|---|---|
| `repositorios/noctalia` (`https://github.com/noctalia-dev/noctalia`) | **MIT** (`LICENSE`, `Copyright (c) 2026 noctalia-dev`) + `CREDITS.md` con atribuciones (Tabler Icons, Material Color Utilities, Luau, Wuffs, etc.) | Shell Wayland: barra, panel, launcher, theming, plantillas (`assets/templates/`), integración Hyprland | **Alta**: código fuente oficial + documentación; ver [README](sources/2026-11-21-noctalia-readme.md) |
| `repositorios/dots-hyprland` (`https://github.com/end-4/dots-hyprland`) | **GPL-3.0** (`LICENSE`); carpeta `licenses/` con LGPL-3.0 y MIT para código de terceros | Dotfiles estilo Material: carpetas `dots/`, `dots-extra/`, `sdata/`, scripts `setup` y `diagnose` | **Media-alta**: fuente directa, pero no hay README archivado en `sources/` (solo un stub en `.staging/`); listado en la [wiki](sources/2026-11-21-hyprland-preconfigured-setups.md) |
| `repositorios/Hyprland-Dots` (`https://github.com/JaKooLit/Hyprland-Dots`) | **GPL-3.0** (`LICENSE.md`) | Configs + scripts (`copy.sh`, `upgrade.sh`), wallpapers, wiki, changelogs; avisos para fish y backups | **Media**: muy completo pero **en transición a otro mantenedor** ([README](sources/2026-11-21-jakoolit-hyprland-dots.md)) |

**HECHO.** El README de JaKooLit contiene detalles operativos valiosos: `copy.sh`/`release.sh`/`upgrade.sh` crean backups pero recomiendan **backup manual**; los dots están ajustados por defecto a 1440p sin escalado; y advierten "si usas FISH SHELL, no uses esta función, clona Distro-Hyprland y ejecuta `install.sh`" ([JaKooLit · README](sources/2026-11-21-jakoolit-hyprland-dots.md)). El último punto afecta directamente a este usuario (fish 4.9.3).

**HECHO.** Los repos de dotfiles no son fuentes de paquetes: el propio README dice "este repo **no contiene ni instalará** paquetes; son solo configuraciones" ([JaKooLit](sources/2026-11-21-jakoolit-hyprland-dots.md)).

---

## 4. Wikis y documentación oficial

| Recurso | URL | Qué aporta | Fiabilidad |
|---|---|---|---|
| **Hyprland Wiki** | `https://wiki.hypr.land/` | Config (binds, animaciones, reglas, colores), utilidades imprescindibles, barras, wallpapers, performance, setups preconfigurados | **Alta**, oficial; ejemplos: [Must-have](sources/2026-11-21-hyprland-must-have.md), [Status Bars](sources/2026-11-21-hyprland-status-bars.md), [Performance](sources/2026-11-21-hyprland-performance.md), [Wallpapers](sources/2026-11-21-hyprland-wallpapers.md) |
| **ArchWiki · Hyprland** | `https://wiki.archlinux.org/title/Hyprland` | Instalación, teclado, UWSM, hyprctl/IPC, ecosistema hypr\*, trucos (launcher, wallpaper, notificaciones) | **Alta**, comunidad Arch; [fuente archivada](sources/2026-11-21-archwiki-hyprland.md) |
| **CachyOS Wiki** | `https://wiki.cachyos.org/` (URL declarada, **no archivada** con frontmatter en `sources/`) | Específico de la distro del usuario (instalación, paquetes, Hyprland preconfigurado) | **INCIERTO en este corpus**: verificar in situ; el perfil local sí acredita `cachyos-hypr-noctalia 1.2.6-1` |
| **Noctalia Docs** | `https://docs.noctalia.dev/` | Barra, theming, paleta, plantillas, integración Hyprland | **Alta**, oficial; índice en [README](sources/2026-11-21-noctalia-readme.md), páginas archivadas: [paleta](sources/2026-11-21-noctalia-theming-palette.md), [plantillas](sources/2026-11-21-noctalia-templates.md), [barra](sources/2026-11-21-noctalia-bar.md) |

**HECHO.** La wiki de Hyprland se actualizó el 20 de noviembre de 2026 según el pie de las páginas archivadas, es decir, es coetánea de la versión 0.57.2. Eso la hace preferible a cualquier blog antiguo. **INCIERTO / CONFLICTO:** la propia wiki dice que Noctalia está basada en Quickshell ([Status Bars](sources/2026-11-21-hyprland-status-bars.md)), mientras el README oficial afirma que no depende de Qt/GTK ([README](sources/2026-11-21-noctalia-readme.md)). Ante dudas, manda la documentación del proyecto.

---

## 5. Awesome-lists y agregadores

**INCIERTO.** No se archivó ninguna *awesome-list* (por ejemplo, listas de Wayland/tiling WMs en GitHub) como fuente con frontmatter. Su existencia es conocida en la comunidad, pero **este corpus no permite citarlas**; cualquier URL concreta debe verificarse.

**HECHO.** El equivalente más cercano y fiable dentro del material disponible son:

- La página oficial [Preconfigured setups](sources/2026-11-21-hyprland-preconfigured-setups.md) ([URL](https://wiki.hypr.land/getting-started/preconfigured-setups/)), una lista curada **con aviso de seguridad**.
- El [Showcase / Hall of Fame](sources/2026-11-21-hyprland-lua-utilities.md) de Hyprland ([URL](https://hypr.land/hall_of_fame)), visible en la navegación de la wiki.
- Las listas internas de proyectos: la [tabla de barras/shells/widget systems](sources/2026-11-21-hyprland-status-bars.md), el catálogo [builtin.toml](sources/2026-11-21-noctalia-builtin-templates.md) de Noctalia y los "ports" de [Catppuccin](sources/2026-11-21-catppuccin-readme.md).

**OPINIÓN.** Una *awesome-list* es un índice, no una garantía: cruza siempre sus recomendaciones con la wiki oficial y con la fecha del último commit.

---

## 6. Blogs, canales y comunidades en tiempo real

| Recurso | URL (de las fuentes) | Qué aporta | Fiabilidad |
|---|---|---|---|
| Canal YouTube de ML4W | `https://www.youtube.com/@mylinuxforwork` | Tutoriales del setup "DE-like" | **Media** (terceros enlazados por la [wiki](sources/2026-11-21-hyprland-preconfigured-setups.md)) |
| Canal YouTube de JaKooLit | `https://www.youtube.com/@Ja.KooLit` | Walkthroughs de sus dotfiles | **Media** ([wiki](sources/2026-11-21-hyprland-preconfigured-setups.md); [README](sources/2026-11-21-jakoolit-hyprland-dots.md)) |
| Discord de Noctalia | `https://discord.noctalia.dev` | Ayuda y feedback del shell usado por el usuario | **Alta** para soporte, **baja** como documentación persistente ([README](sources/2026-11-21-noctalia-readme.md)) |
| Discord de Catppuccin | `https://discord.com/servers/907385605422448742` | Comunidad del tema | **Media-alta** ([README](sources/2026-11-21-catppuccin-readme.md)) |
| r/catppuccin | `https://reddit.com/r/catppuccin` | Galería y combinaciones de paleta | **Media** ([README](sources/2026-11-21-catppuccin-readme.md)) |
| Matrix `#wal-lust` | `https://matrix.to/#/#wal-lust:matrix.org` | Soporte de wallust | **Media** ([README](sources/2026-11-21-wallust-readme.md)) |
| Fosstodon @catppuccin | `https://fosstodon.org/@catppuccin` | Novedades del proyecto | **Media** ([README](sources/2026-11-21-catppuccin-readme.md)) |
| Discord de Noctalia (badge alterno) y KooL Tech World | `https://discord.noctalia.dev`, `https://discord.gg/kool-tech-world` | Soporte comunitario | **Media** ([Noctalia](sources/2026-11-21-noctalia-readme.md), [JaKooLit](sources/2026-11-21-jakoolit-hyprland-dots.md)) |

**OPINIÓN.** Para un problema técnico concreto, un issue de GitHub bien buscado suele ser más duradero que un mensaje de Discord; los chats son útiles para descartar errores locales.

---

## 7. Licencias y atribución

**HECHO.** Licencias verificadas en las fuentes y repos clonados:

| Proyecto | Licencia | Fuente |
|---|---|---|
| Noctalia | MIT | [README](sources/2026-11-21-noctalia-readme.md), `LICENSE`, [metadatos API](sources/2026-11-21-noctalia-repo-metadata.md) |
| Catppuccin | MIT | [README](sources/2026-11-21-catppuccin-readme.md) |
| pywal | MIT | [README](sources/2026-11-21-pywal-readme.md) |
| dots-hyprland (end-4) | GPL-3.0; `licenses/` incluye LGPL-3.0 y MIT para código de terceros | `repositorios/dots-hyprland/LICENSE`, `licenses/README.md` |
| Hyprland-Dots (JaKooLit) | GPL-3.0 | `repositorios/Hyprland-Dots/LICENSE.md` |
| Nerd Fonts | README remite a su `LICENSE` (no reproducido en el corpus) | [README](sources/2026-11-21-nerd-fonts-readme.md), [URL](https://github.com/ryanoasis/nerd-fonts/blob/-/LICENSE) |
| Bibata Cursor | **INCIERTO**: el README archivado no declara licencia; sí incluye créditos a Adwaita, Dmz y Yaru | [README](sources/2026-11-21-bibata-readme.md) |

**HECHO.** Noctalia mantiene un `CREDITS.md` explícito: logo (MrDowntempo), mascota (SaberJ2X), Tabler Icons, Material Color Utilities (Apache-2.0), Luau, Wuffs, bibliotecas del sistema, etc. Es un buen modelo a imitar si se publica un rice que incluya assets de terceros.

**HECHO.** El README de Bibata incluye una sección "Credit" con Adwaita, Dmz y Yaru ([Bibata](sources/2026-11-21-bibata-readme.md)); Catppuccin recomienda seguir su *style guide* para usar la paleta ([Catppuccin](sources/2026-11-21-catppuccin-readme.md), [URL](https://github.com/catppuccin/catppuccin/blob/main/docs/style-guide.md)); wallust documenta el origen de los wallpapers de sus capturas (GNOME backgrounds, Pexels, Wikipedia, etc.) ([wallust](sources/2026-11-21-wallust-readme.md)).

**OPINIÓN — checklist de atribución al publicar:**

1. Wallpaper: indicar autor y fuente (o usar uno propio). Los dotfiles de JaKooLit incluyen una carpeta `wallpapers/` y un Wallpaper-Bank externo ([README](sources/2026-11-21-jakoolit-hyprland-dots.md)).
2. Tema/paleta: citar el proyecto y su licencia (Catppuccin MIT, Material You Apache-2.0).
3. Fuentes: Nerd Fonts parchea fuentes de terceros; conviene nombrar la familia base (en este caso Fantasque/Meslo Nerd).
4. Iconos y cursores: Bibata y el set de iconos usado.
5. Código: si copias fragmentos de un repo GPL-3.0, respeta su licencia; si solo tomas ideas, menciona el origen.

---

## 8. Herramientas para mostrar un rice

**HECHO.** ArchWiki documenta `hyprsysteminfo` como "un programa de información del sistema como neofetch o fastfetch", instalable desde AUR ([ArchWiki · Hyprland](sources/2026-11-21-archwiki-hyprland.md), [URL](https://wiki.archlinux.org/title/Hyprland)). En este equipo **ya está instalado `fastfetch 2.71.0`** (auditoría local §5), así que no hace falta añadir nada.

**HECHO (fuente local).** Para capturas, Noctalia 5.6.0 integra herramienta de screenshot y delega en **swash 1.5.1** (`swash --stdin --name …`) según el perfil (§3). La wiki de Hyprland menciona `hyprpicker` como selector de color del ecosistema, no como capturador ([User ecosystem](sources/2026-11-21-hyprland-ecosystem-user.md), [ArchWiki](sources/2026-11-21-archwiki-hyprland.md)).

**INCIERTO.** Utilidades clásicas de captura en Wayland (por ejemplo `grim`/`slurp`) no aparecen en ninguna fuente archivada: se mencionan por costumbre comunitaria, pero **no se afirma aquí como dato verificado**. Para este usuario, la vía documentada es la integración de Noctalia + swash.

**OPINIÓN.** Una captura reveladora incluye: una ventana de terminal con `fastfetch`, otra con código o `btop`, el launcher abierto y la barra visible; así se muestran paleta, tipografía, bordes, gaps y shell de un vistazo.

---

## 9. Cómo publicar un rice (checklist)

> **OPINIÓN** basada en las convenciones descritas arriba; las normas concretas del destino deben verificarse (§2).

1. **Estabiliza**: comprueba que no haya dependencias muertas (notificaciones, portal, polkit) según [Must-have](sources/2026-11-21-hyprland-must-have.md).
2. **Versiona**: publica los dotfiles con un README que indique versiones (Hyprland 0.57.2, Noctalia 5.6.0) y orden de instalación; recuerda el aviso sobre configs invasivas ([Preconfigured setups](sources/2026-11-21-hyprland-preconfigured-setups.md)).
3. **Documenta la paleta**: declara de dónde sale cada color (wallpaper + M3) y añade atribuciones (§7).
4. **Haz la captura** con la herramienta integrada y `fastfetch` visible (§8).
5. **Escribe el título** con stack y versión; incluye enlace a dotfiles en el primer comentario.
6. **Avisa de la particularidad local**: teclado AZERTY con atajos `code:` e iGPU antigua con blur moderado (auditoría §§2.3, 7). Eso hace la publicación útil, no solo bonita.
7. **Mantén**: cuando Hyprland o Noctalia cambien de API, actualiza el repo (lección de los avisos de deprecación en [Releases](sources/2026-11-21-hyprland-releases.md)).

---

## 10. Tabla maestra de recursos

| Recurso | URL | Tipo | Qué aporta | Fiabilidad |
|---|---|---|---|---|
| Hyprland Wiki · Must-have | `https://wiki.hypr.land/useful-utilities/must-have/` | Wiki oficial | Servicios invisibles imprescindibles | **Alta** ([fuente](sources/2026-11-21-hyprland-must-have.md)) |
| Hyprland Wiki · Status bars | `https://wiki.hypr.land/useful-utilities/status-bars/` | Wiki oficial | Barras, shells y sistemas de widgets; tabla de lenguajes | **Alta** ([fuente](sources/2026-11-21-hyprland-status-bars.md)) |
| Hyprland Wiki · Preconfigured setups | `https://wiki.hypr.land/getting-started/preconfigured-setups/` | Wiki oficial | Lista curada + advertencia de seguridad | **Alta** ([fuente](sources/2026-11-21-hyprland-preconfigured-setups.md)) |
| Hyprland Wiki · Performance | `https://wiki.hypr.land/configuring/extra/performance/` | Wiki oficial | Blur, escalado, iGPU/TLP | **Alta** ([fuente](sources/2026-11-21-hyprland-performance.md)) |
| Hyprland Wiki · Wallpapers | `https://wiki.hypr.land/useful-utilities/wallpapers/` | Wiki oficial | hyprpaper, swaybg, wpaperd, mpvpaper, awww, waypaper | **Alta** ([fuente](sources/2026-11-21-hyprland-wallpapers.md)) |
| ArchWiki · Hyprland | `https://wiki.archlinux.org/title/Hyprland` | Wiki comunitaria | Instalación, UWSM, hyprctl, hyprsysteminfo | **Alta** ([fuente](sources/2026-11-21-archwiki-hyprland.md)) |
| GitHub Releases de Hyprland | `https://github.com/hyprwm/Hyprland/releases` | Fuente primaria | Cambios 0.56–0.57, deprecación `.conf`, API Lua | **Alta** ([fuente](sources/2026-11-21-hyprland-releases.md)) |
| Noctalia (repo + docs) | `https://github.com/noctalia-dev/noctalia` · `https://docs.noctalia.dev/` | Proyecto oficial | Shell, plantillas, paleta, integración | **Alta** ([README](sources/2026-11-21-noctalia-readme.md), [metadatos](sources/2026-11-21-noctalia-repo-metadata.md)) |
| Catppuccin | `https://github.com/catppuccin/catppuccin` | Proyecto de tema | Paleta MIT, filosofía, guía de estilo, ports | **Alta** ([fuente](sources/2026-11-21-catppuccin-readme.md)) |
| Material Color Utilities | `https://github.com/material-foundation/material-color-utilities` | Fuente primaria | Fundamentos de Material You/HCT/contraste | **Alta** ([fuente](sources/2026-11-21-material-you-color-system.md)) |
| pywal / wallust / matugen | `https://github.com/dylanaraps/pywal` · `https://codeberg.org/explosion-mental/wallust` · `https://github.com/InioX/matugen` | Herramientas | Generación de paletas desde imagen | **Media-alta** ([pywal](sources/2026-11-21-pywal-readme.md), [wallust](sources/2026-11-21-wallust-readme.md), [matugen](sources/2026-11-21-matugen-readme.md)) |
| Nerd Fonts | `https://www.nerdfonts.com/` · `https://github.com/ryanoasis/nerd-fonts` | Proyecto | Glifos; cheatsheet; parcheo de fuentes | **Alta** ([web](sources/2026-11-21-nerd-fonts-website.md), [README](sources/2026-11-21-nerd-fonts-readme.md)) |
| Bibata Cursor | `https://github.com/ful1e5/Bibata_Cursor` | Proyecto | Cursores; créditos; variantes Ice | **Media** (licencia no en README) ([fuente](sources/2026-11-21-bibata-readme.md)) |
| JaKooLit Hyprland-Dots | `https://github.com/JaKooLit/Hyprland-Dots` | Dotfiles | Scripts, wallpapers, wiki, avisos fish/backups | **Media** (en archivado/migración) ([fuente](sources/2026-11-21-jakoolit-hyprland-dots.md)) |
| end-4 dots-hyprland | `https://github.com/end-4/dots-hyprland` | Dotfiles | Estética Material, scripts `setup`/`diagnose` | **Media-alta** (clonado localmente; sin README archivado) ([wiki](sources/2026-11-21-hyprland-preconfigured-setups.md)) |
| r/unixporn | `https://www.reddit.com/r/unixporn/` | Galería | Inspiración; publicación con captura + dotfiles | **INCIERTO en normas** (solo mención indirecta vía [pywal](sources/2026-11-21-pywal-readme.md)) |
| CachyOS Wiki | `https://wiki.cachyos.org/` | Wiki de distro | Específico de CachyOS | **INCIERTO** (no archivada; verificar) |

---

## 11. Límites

- No hay fuente archivada con las **normas completas** de r/unixporn ni con estadísticas de la comunidad; §2 es deliberadamente prudente.
- No se archivaron *awesome-lists*; §5 se apoya solo en listas oficiales.
- La licencia de Bibata y la URL de la wiki de CachyOS requieren verificación directa.
- Las valoraciones de "fiabilidad" son **OPINIÓN** calculada con estos criterios: oficialidad, fecha de actualización, licencia visible y presencia de avisos de mantenimiento.
