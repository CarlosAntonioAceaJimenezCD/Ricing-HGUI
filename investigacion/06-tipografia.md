# 06 · Tipografía aplicada al ricing

> Contexto: CachyOS · Hyprland 0.57.2 (config Lua) · Noctalia 5.6.0 · fish 4.9.3 + pure ·
> kitty 0.51.0 / alacritty 0.17.0 · monitor único 1440×900 @ ~60 Hz, escala 1.
>
> **Convención de rigor:** **[H]** = hecho verificable en la evidencia local; **[O]** = opinión,
> recomendación o juicio de diseño. Las rutas `sources/…` se escriben `../sources/…` desde este
> directorio (`investigacion/`); se indica además la URL original de cada fuente externa.
> Fuentes archivadas localmente: [Nerd Fonts README](../sources/2026-11-21-nerd-fonts-readme.md)
> (https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md),
> [Nerd Fonts website](../sources/2026-11-21-nerd-fonts-website.md) (https://www.nerdfonts.com/),
> [Noctalia Bar](../sources/2026-11-21-noctalia-bar.md)
> (https://github.com/noctalia-dev/noctalia/blob/main/docs/user/bar/index.mdx),
> [Catppuccin README](../sources/2026-11-21-catppuccin-readme.md)
> (https://github.com/catppuccin/catppuccin/blob/main/README.md),
> [Perfil del sistema](../00-perfil-del-sistema.md) y
> [familias-fuentes.txt](../apendices/familias-fuentes.txt) (documentos locales de auditoría).

---

## 0. Resumen ejecutivo

**[H]** El sistema ya tiene 885 entradas en `fc-list`, incluidas **FantasqueSansM Nerd Font** y
**Meslo\* Nerd Font** en variantes Mono/Propo, además de Noto (CJK, emoji, símbolos), Adwaita,
DejaVu, Liberation, Open Sans, Cantarell y Bitstream Vera
([Perfil](../00-perfil-del-sistema.md) §4; [familias-fuentes.txt](../apendices/familias-fuentes.txt)).
**[H]** Ni `kitty.conf`, ni `alacritty.toml`, ni `noctalia/config.toml` fijan hoy una familia
tipográfica: kitty solo declaró opacidad/padding/cursor e incluye el tema; alacritty usa el alias
genérico `monospace` a 12.0 pt; Noctalia hereda la fuente global del shell
([kitty.conf](../configuracion-actual/kitty/kitty.conf),
[alacritty.toml](../configuracion-actual/alacritty/alacritty.toml),
[config.toml](../configuracion-actual/noctalia/config.toml)).

**[O]** La decisión de mayor impacto no es instalar más fuentes, sino **nombrar explícitamente**
una familia Nerd Mono en los cuatro sitios que importan (kitty, alacritty, prompt de fish y
barra de Noctalia) y dejar todos los alias de `fontconfig` apuntando a esa misma familia.
Con FantasqueSansM Nerd Font Mono ya instalada, no hace falta descargar nada para empezar.

---

## 1. ¿Por qué la tipografía define un rice

**[O]** Un rice se percibe antes por la forma de las letras que por los colores: la tipografía
ocupa entre el 70 % y el 90 % de los píxeles informativos de la pantalla (barra, prompt,
notificaciones, editor). Un esquema de color consistente con una fuente inconsistente se lee
como "a medio terminar"; una paleta discreta con una fuente bien elegida se lee como intencional.
**[H]** En este equipo la paleta ya se propaga a siete destinos mediante las plantillas de
Noctalia (`btop`, `gtk3`, `gtk4`, `kcolorscheme`, `kitty`, `qt`, `alacritty`), pero esa
propagación es **solo de color**: no hay un mecanismo equivalente que propague la fuente
([Perfil](../00-perfil-del-sistema.md) §3; [config.toml](../configuracion-actual/noctalia/config.toml)
líneas 89–90). Esa es la laguna que esta guía cubre.

**[O]** Tres razones concretas para este hardware modesto (Intel Sandy Bridge, sin VRR/HDR):

1. **Coste cero:** cambiar `font_family` no añade ni un solo frame de blur; cambiar blur de
   4 passes sí puede costar frames ([Perfil](../00-perfil-del-sistema.md) §7).
2. **Densidad:** a 1440×900 con escala 1, la fuente determina cuántas líneas de `btop`, `eza`
   o `bat` caben. Una x-height generosa permite bajar de 12 a 11 pt sin perder legibilidad.
3. **Identidad:** los glyphs de Nerd Font en el prompt (``, ``, ``) convierten una
   instalación stock en un rice reconocible sin añadir widgets.

---

## 2. Anatomía y métricas que importan en un rice

| Métrica | Qué es | Por qué afecta al rice | Valoración para este equipo **[O]** |
|---|---|---|---|
| **x-height** | Altura de las minúsculas respecto al cuerpo | Define la legibilidad percibida a tamaños pequeños; fuentes con x-height alta "parecen" más grandes al mismo `font_size` | Fantasque y Meslo tienen x-height media-alta: buenas a 11–12 px |
| **Apertura (aperture)** | Cuánto se abren `c`, `e`, `s`, `a` | Apertura cerrada = `c/e` confusables en textos grises sobre fondo oscuro | Preferir apertura abierta para el tema M3 oscuro |
| **Contraste** | Grosor relativo de trazos finos/gruesos | Contraste alto = estética "technical"; contraste bajo = mejor en pantallas antiguas | Sandy Bridge + RGB sin subpixel Retina: evitar pesos `Thin`/`Light` |
| **Monospace vs. Proportional** | Ancho fijo vs. variable por glifo | Un terminal es una rejilla: una proporcional desalinea columnas, tablas y `btop` | **Siempre Mono** en terminal/prompt; Propo solo en UI |
| **Ligaduras (`liga`, `calt`)** | Fusión de `->`, `=>`, `!=` en un glifo | Muy vistoso en código, peligroso en prompt (puede confundir `|` con `¦`) | Activar en kitty/editor, desactivar en prompt de fish |
| **Números tabulares** | Dígitos con ancho idéntico | Imprescindible en reloj, `sysmon`, `btop` y tablas: evita que el texto "baile" | Exigir `font-variant-numeric: tabular-nums` o fuente con dígitos tabulares por defecto |

**[H]** La mayoría de las fuentes de programación son monospace por diseño; Nerd Fonts permite
además elegir el ancho de los **glyphs añadidos**, no solo el de la fuente base: el patcher tiene
`--single-width-glyphs` (Mono), `--variable-width-glyphs` (Propo) y `--mono` (fuerza todo a
ancho simple) ([Nerd Fonts README](../sources/2026-11-21-nerd-fonts-readme.md), bloque de opciones).
**[H]** El sitio oficial resume el principio: *"All patched fonts have Powerline symbols, extra
powerline symbols and many icons"* ([Nerd Fonts website](../sources/2026-11-21-nerd-fonts-website.md),
línea 144).

**[O]** Regla práctica: **una familia monospace para todo el escritorio y, como mucho, una
segunda familia para títulos**. Mezclar cuatro monospace distintas (una para kitty, otra para
alacritty, otra para waybar, otra para el editor) es el error más frecuente y más visible.

---

## 3. Escala tipográfica y jerarquía

### 3.1 Roles

**[O]** Con cinco roles basta para todo el rice. Los nombres son los de la práctica de diseño
de producto (`display`, `title`, `body`, `caption`, `label`) y conviene usarlos también como
nombres de variables en CSS/QML para no repetir valores:

| Rol | Uso en este equipo | Tamaño sugerido (escala 1, 1440×900) | Peso | Interlineado |
|---|---|---|---|---|
| `display` | `fastfetch` logo, greeter, título del launcher | 18–22 px | 600–700 | 1.1 |
| `title` | Título de ventana, encabezado de panel Noctalia | 15–16 px | 600 | 1.2 |
| `body` | Texto de terminal, `micro`, `gnome-text-editor` | 11.5–13 px | 400 | 1.4–1.5 |
| `caption` | Tooltips, notificaciones secundarias, `btop` labels | 11–12 px | 400 | 1.35 |
| `label` | Barra (reloj, workspaces, sysmon), pills | 11–12 px | 500 | 1.0–1.2 |

**[O]** La barra de Noctalia tiene `thickness = 35`, `scale = 1.10` y `ui_scale = 1.20`
([config.toml](../configuracion-actual/noctalia/config.toml)). Eso significa que un `label` de
11 px lógicos se renderiza cerca de 13–14 px físicos: **no subas el `font_size` de la terminal
por encima del de la barra**, o la barra parecerá pequeña y la terminal desproporcionada.

### 3.2 Line-height y measure (ancho de línea)

**[O]** En un rice, "measure" no es solo texto corriente: es el ancho de la salida de
`eza`/`bat` y el número de columnas de alacritty (`dimensions = { columns = 100, lines = 30 }`).
Con una monospace de ancho medio ~0.6 em y 12 px, 100 columnas ≈ 720 px: cabe holgadamente en
1440 px. Si cambias a una fuente más ancha, reduce columnas a 90–95 para no cortar `btop`.

```css
/* Referencia conceptual (CSS/QML), no un archivo a copiar tal cual */
:root {
  --font-ui:     "FantasqueSansM Nerd Font Mono", "Noto Sans", monospace;
  --font-display:"FantasqueSansM Nerd Font Mono", "Noto Sans", sans-serif;
  --step--1: 11px;   /* caption / label */
  --step-0:  12px;   /* body */
  --step-1:  15px;   /* title */
  --step-2:  20px;   /* display */
  --lh-body: 1.45;
  --lh-head: 1.15;
  --measure: 65ch;
}
label { font-weight: 500; line-height: 1.15; font-variant-numeric: tabular-nums; }
body  { line-height: var(--lh-body); max-width: var(--measure); }
```

**[H]** Noctalia expone controles exactos para esto: `font_scale` (0.2–2.5, "multiplies widget
text independently of icons"), `font_weight` (100–1000), `font_family` por barra y por widget, y
`scale` general ([Noctalia Bar](../sources/2026-11-21-noctalia-bar.md), líneas 58–61 y 177–179).
**[O]** Ajusta **`font_scale` antes que `scale`**: `scale` agranda también iconos y spacing y
puede desbordar una barra de 35 px de grosor.

```toml
# Fragmento sugerido para ~/.config/noctalia/config.toml (NO aplicado en esta investigación)
[bar.default]
font_family  = "FantasqueSansM Nerd Font Mono"
font_scale   = 1.0     # con ui_scale=1.20 ya es suficiente
font_weight  = 500     # evita 400 (se ve grisáceo) y 700 (se come el padding)
scale        = 1.10    # se mantiene
```

---

## 4. Nerd Fonts: qué son, licencias y variantes

### 4.1 Qué son

**[H]** Nerd Fonts es un *"iconic font aggregator, collection, and patcher"*: toma fuentes
orientadas a desarrolladores y añade glifos de Font Awesome, Devicons, Octicons, Powerline,
Material Design Icons, Weather, Font Logos, Pomicons, Codicons e IEC Power Symbols. El proyecto
reporta **67 familias parcheadas** y **más de 10 000 glifos** combinados; el sitio web cifra la
colección en **10 606+ iconos**
([Nerd Fonts README](../sources/2026-11-21-nerd-fonts-readme.md) §Features;
[Nerd Fonts website](../sources/2026-11-21-nerd-fonts-website.md) línea 52).

**[H]** El patcher es un script de FontForge/Python (`font-patcher`, v3.5.0-16 en la evidencia)
que admite `--complete`, `--mono`, `--single-width-glyphs`, `--variable-width-glyphs`,
`--powerline`, `--braille` y `--boxdrawing`, entre muchas opciones. El mismo README advierte que
**clonar el repositorio completo no es recomendable** y que las rutas en `master` no son estables:
hay que referirse a un tag de release
([Nerd Fonts README](../sources/2026-11-21-nerd-fonts-readme.md) §Important Notices).

### 4.2 Licencias

**[H]** El README enlaza el archivo `LICENSE` del proyecto para el parcheo y una tabla con la
columna `*RFN` (*Reserved Font Name*). Las fuentes que interesan aquí — **Fantasque, Fira Code,
JetBrains Mono, Iosevka, Meslo** — figuran con `RFN = NO`, es decir, no imponen reserva del
nombre al redistribuir la versión parcheada. **[O]** En la práctica: la licencia *upstream* de la
fuente base se mantiene (muchas son SIL OFL 1.1) y los glifos añadidos tienen sus propias
licencias; para auditoría, consulta `/usr/share/licenses/ttf-fantasque-nerd` y
`/usr/share/licenses/ttf-meslo-nerd` en tu máquina antes de redistribuir.

### 4.3 Las variantes: Mono / Propo / LGL / LGM / LGS / DZ

**[H]** Los sufijos no son decorativos; describen decisiones de metricación:

| Sufijo | Significado | Servicio |
|---|---|---|
| **Nerd Font** | Glifos con ancho **doble** (por defecto en el patcher) | Equilibrado; útil en UI |
| **Nerd Font Mono** | Glifos de **ancho simple** (`--single-width-glyphs` / `--mono`) | **Terminal y prompt**: mantiene la rejilla |
| **Nerd Font Propo** | Glifos de **ancho variable** (`--variable-width-glyphs`) | Interfaces gráficas; **nunca en terminal** |
| **LGL** | Variante de Meslo con glifos *Larger* para `ligatures/line/glyphs` | Compatibilidad amplia de Powerline |
| **LGM** | Meslo con ajuste distinto de la altura de línea | Terminales que recortan separadores |
| **LGS** | Variante recomendada por Oh My Zsh / Powerlevel para separadores limpios | Prompt con powerline |
| **DZ** | "Dotted Zero": cero con punto interior | Distingue `0` de `O` |

**[H]** Tu inventario contiene exactamente 21 familias Nerd: `FantasqueSansM Nerd Font`
(+ Mono, + Propo) y 6 bases Meslo (LGL, LGLDZ, LGM, LGMDZ, LGS, LGSDZ) × 3 variantes
([familias-fuentes.txt](../apendices/familias-fuentes.txt) líneas 14–39). **[O]** Para este
usuario, **la elección correcta es `FantasqueSansM Nerd Font Mono` en terminal/prompt** y, si se
prefiere un cero punteado y separadores impecables, `MesloLGS Nerd Font Mono` como alternativa;
reserva las variantes Propo para GTK/Qt si algún día se decide a usarlas en UI.

### 4.4 Instalación (y por qué ya está resuelta)

**[H]** El README documenta nueve caminos: archivo de release, Homebrew, script `install.sh`,
Chocolatey/Scoop, **paquetes de Arch `extra`**, PowerShell, font fallback, clonar el repo y
parchear la propia fuente ([Nerd Fonts README](../sources/2026-11-21-nerd-fonts-readme.md)
§Font Installation). **[H]** Tus paquetes `ttf-fantasque-nerd` y `ttf-meslo-nerd` 3.5.1 son
precisamente la vía Arch Extra (Opción 5), por lo que **no hay nada que instalar**.

Para futuras altas (si se quiere JetBrainsMono Nerd):

```sh
sudo pacman -S ttf-jetbrains-mono-nerd          # vía Arch Extra
# o, alternativamente, el instalador oficial:
curl -s https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/install.sh -o install.sh
chmod u+x install.sh && ./install.sh install JetBrainsMono
fc-cache -f                                     # regenera la caché de fontconfig
```

### 4.5 Uso real de los glyphs

**fish + pure.** **[H]** Pure prompt usa símbolos de Powerline (p. ej. ``) y flechas Unicode;
todas las fuentes Nerd parcheadas incluyen esos símbolos
([Nerd Fonts website](../sources/2026-11-21-nerd-fonts-website.md) línea 144). **[O]** En fish,
la fuente no se configura en `config.fish` sino en el emulador de terminal; lo único que conviene
hacer en fish es **no forzar símbolos exóticos** que tu fuente no tenga:

```fish
# ~/.config/fish/config.fish — sólo si quieres personalizar pure
set -g pure_symbol_prompt '❯'      # U+276F, presente en Fantasque/Meslo NF
set -g pure_symbol_git_branch ''  # U+E0A0, Powerline: requiere Nerd Font
# set -g pure_enable_git false     # plan B si aparecen cuadraditos
```

**[H]** Tu `fish-config.fish` solo cargó `cachyos-config.fish` y añadió `~/.opencode/bin` al PATH,
sin tocar la fuente ([fish-config.fish](../configuracion-actual/shell/fish-config.fish)).

**kitty.** **[H]** No hay `font_family` declarada; kitty usa su valor por defecto (`monospace`)
([kitty.conf](../configuracion-actual/kitty/kitty.conf)). **[O]**

```conf
# ~/.config/kitty/kitty.conf (añadir)
font_family      FantasqueSansM Nerd Font Mono
font_size        11.5
bold_font        auto
italic_font      auto
font_features    +liga +calt
# Opcional: emoji coloreados sin romper la rejilla (ancho forzado)
symbol_map       U+1F300-U+1FAFF Noto Color Emoji
```

**alacritty.** **[H]** Usa `family = "monospace"`, `size = 12.0` y/o importa colores Nord en el
archivo principal aunque el tema noctalia.toml sobrescribe los colores
([alacritty.toml](../configuracion-actual/alacritty/alacritty.toml)). **[O]**

```toml
[font]
normal = { family = "FantasqueSansM Nerd Font Mono", style = "Regular" }
bold = { family = "FantasqueSansM Nerd Font Mono", style = "Bold" }
italic = { family = "FantasqueSansM Nerd Font Mono", style = "Italic" }
size = 11.5
```

**btop.** **[O]** btop corre *dentro* de la terminal: **no elige fuente**, hereda la de kitty o
alacritty. Por eso la Nerd Mono debe tener box-drawing y braille sólidos (el patcher ofrece
`--boxdrawing` y `--braille` precisamente para eso). No intentes "configurar la fuente de btop":
configura la terminal desde la que lo lanzas.

**waybar / Noctalia.** **[H]** waybar no está instalada; Noctalia hace su papel. En waybar la
fuente se declara en CSS (`* { font-family: "JetBrainsMono Nerd Font"; }`); en Noctalia es
TOML: `font_family` en `[bar.default]`, `[widget.<name>]` o global en `[shell]`
([Noctalia Bar](../sources/2026-11-21-noctalia-bar.md) líneas 61, 179, 262).
**[O]** Ojo: los `glyph = "gpu-usage"` y `glyph = "cpu-2"` de tu config son **iconos QML propios
de Noctalia**, no Nerd Font glyphs; no necesitan Nerd Font para dibujarse
([config.toml](../configuracion-actual/noctalia/config.toml) líneas 118–127).

---

## 5. Fuentes recomendadas para 2026 (y licencias)

**[O]** Todas las siguientes son proyectos vivos y de licencia abierta; las URLs son las
fuentes primarias (no archivadas en `sources/`):

| Fuente | URL original | Licencia | Pros | Contras | Veredicto para ti |
|---|---|---|---|---|---|
| **Fantasque Sans Mono (Nerd)** | https://github.com/belluzj/fantasque-sans | OFL 1.1 | Personalidad fuerte, x-height alta, muy legible a 11 px, ya instalada | Curvas poco convencionales; ligaduras discretas | **Elección principal** (ya la tienes) |
| **MesloLGS (Nerd)** | https://github.com/andreberg/Meslo-Font | Ver licencia upstream del paquete | Cero punteado, separadores powerline impecables, clásico de prompts | Estética más "genérica"; más ancha | **Plan B** para prompt |
| **JetBrains Mono (Nerd)** | https://github.com/JetBrains/JetBrainsMono | OFL 1.1 | Ligaduras excelentes, tabular nums, muy equilibrada | No instalada; ~2–3 MB más | Instalar solo si quieres cambiar de aire |
| **Iosevka (Nerd)** | https://github.com/be5invis/Iosevka | OFL 1.1 | Infinitamente configurable, estilizada, gran densidad | Curva de aprendizaje; puede cansar en body | Para `display`/prompt, no para body |
| **Fira Code (Nerd)** | https://github.com/tonsky/FiraCode | OFL 1.1 | Ligaduras de referencia, base Firefox/Mozilla | Ligaduras agresivas en prompt | Editor sí, prompt no |
| **Inter** | https://rsms.me/inter/ | OFL 1.1 | UI neutral y moderna, tabular nums, óptima en pantallas sRGB | No es monospace; solo Propo | Para GTK/Qt/launcher, nunca terminal |
| **Noto Sans / CJK / Emoji** | https://github.com/notofonts/noto-fonts | OFL 1.1 | Cobertura universal; ya instalada | Emoji color rompe rejilla; CJK pesado | **Solo fallback** |

**[O]** Catppuccin, que ya usas en `micro` y como inspiración de paleta, recomienda oficialmente
temas para kitty, alacritty, fish, btop y waybar
([Catppuccin README](../sources/2026-11-21-catppuccin-readme.md), líneas 941, 1065, 1068,
1090, 1103, 1148); combinar su consistencia cromática con una sola Nerd Mono es la forma más
barata de subir el nivel visual del rice.

---

## 6. fontconfig: alias, hinting, antialiasing y DPI

**[H]** Tu GTK ya trae `gtk-xft-antialias=1`, `gtk-xft-hinting=1`,
`gtk-xft-hintstyle=hintslight`, `gtk-xft-rgba=rgb`
([settings.ini](../configuracion-actual/gtk/settings.ini) líneas 11–14). **[O]** Eso es correcto
para un panel sRGB sin escalado fraccional; no lo cambies salvo que veas franjas de color en
texto pequeño (entonces prueba `rgba=none`).

Ejemplo de `~/.config/fontconfig/fonts.conf` (**no creado en esta investigación**):

```xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <dir>~/.local/share/fonts</dir>

  <!-- Resolución y renderizado coherentes con gtk settings.ini -->
  <match target="pattern">
    <edit name="dpi" mode="assign"><double>96</double></edit>
    <edit name="antialias" mode="assign"><bool>true</bool></edit>
    <edit name="hinting" mode="assign"><bool>true</bool></edit>
    <edit name="hintstyle" mode="assign"><const>hintslight</const></edit>
    <edit name="rgba" mode="assign"><const>rgb</const></edit>
  </match>

  <!-- Alias: una sola monospace en todo el sistema -->
  <alias binding="strong">
    <family>monospace</family>
    <prefer><family>FantasqueSansM Nerd Font Mono</family></prefer>
  </alias>
  <alias binding="strong">
    <family>sans-serif</family>
    <prefer><family>Noto Sans</family></prefer>
  </alias>

  <!-- Reemplazo explícito para apps que pidan "Courier New" -->
  <match target="pattern">
    <test name="family"><string>Courier New</string></test>
    <edit name="family" mode="assign" binding="strong">
      <string>FantasqueSansM Nerd Font Mono</string>
    </edit>
  </match>

  <!-- Emoji y CJK por idioma, SIN forzarlos en la fuente principal -->
  <match target="pattern">
    <test name="lang" compare="contains"><string>emoji</string></test>
    <edit name="family" mode="append"><string>Noto Color Emoji</string></edit>
  </match>
  <match target="pattern">
    <test name="lang" compare="contains"><string>zh</string></test>
    <edit name="family" mode="append"><string>Noto Sans CJK SC</string></edit>
  </match>
</fontconfig>
```

Tras editar: `fc-cache -f && fc-match monospace`. **[O]** Usa `mode="append"` para fallbacks y
`binding="strong"` solo para alias que *quieres* que ganen; abusar de `strong` rompe el
fallback natural de fontconfig.

---

## 7. CJK, emoji y fallback

**[H]** El inventario incluye `Noto Sans CJK {JP,KR,SC,TC}`, `Noto Sans Mono CJK {…}`,
`Noto Serif CJK {…}`, `Noto Color Emoji`, `Noto Sans Symbols` y `Noto Sans Symbols 2`
([familias-fuentes.txt](../apendices/familias-fuentes.txt) líneas 40, 119–148, 287–296, 362–367).
**[O]** No hace falta instalar nada más. Pero dos precauciones:

1. **Emoji en la terminal:** `Noto Color Emoji` tiene ancho doble y puede desplazar la rejilla.
   Prefiere glyphs de Nerd Font (``, ``) antes que `😀`, o usa `symbol_map` en kitty para
   fijar el ancho.
2. **Idioma:** el teclado es `es`, así que el fallback CJK solo aparecerá al pegar texto; dejar
   que fontconfig lo resuelva por `lang` es más limpio que declarar CJK como familia principal
   (que ensuciaría el Latin con métricas equivocadas).

**[H]** El README de Nerd Fonts ofrece una alternativa oficial: fuentes `SymbolsOnly` más el
archivo `10-nerd-font-symbols.conf`, con *pro* ("una fuente de símbolos para todas") y *contra*
("escalado y colocación imprevisibles") ([Nerd Fonts README](../sources/2026-11-21-nerd-fonts-readme.md)
§Option 7).

---

## 8. Efecto en Wayland

**[H]** La sesión es `XDG_SESSION_TYPE=wayland` bajo UWSM ([Perfil](../00-perfil-del-sistema.md) §1).
**[H]** En Wayland, GTK (Pango/Cairo) y Qt siguen consultando fontconfig y `GtkSettings`, por lo
que `gtk-xft-*` de `settings.ini` continúa aplicando; las apps X11 lo hacen vía Xwayland.
**[O]** Implicaciones prácticas:

- No busques un "Xresources de Wayland" para la fuente: kitty y alacritty leen su propio config;
  Noctalia lee TOML; GTK lee `settings.ini`/CSS.
- `rgba=rgb` asume subpanel RGB. En un VGA-1 de 1440×900 a 60 Hz con escala 1 es una apuesta
  razonable, pero si el texto se ve "azulado/rojizo" en bordes, cambia a `none` (grayscale AA).
- `hintslight` + antialias es la combinación segura en resoluciones no-Retina; `hintfull`
  suele engordar las monospace en pantallas de 2011.
- El `ui_scale = 1.20` de Noctalia es el equivalente funcional de un DPI mayor: no lo dupliques
  subiendo también `font_scale`.

---

## 9. Testing y verificación

```sh
# 1) Qué fuente se está usando realmente
fc-match monospace
fc-match "FantasqueSansM Nerd Font Mono"
fc-match -f '%{family} | %{style} | %{file}\n' sans-serif

# 2) Verificar cobertura: inventario Nerd instalado
fc-list : family | sort -u | rg -i 'Fantasque|Meslo|Nerd Font'

# 3) ¿Existe un glifo concreto? (U+E0A0 = rama git de Powerline)
printf '\ue0a0\n'
fc-match -s ':charset=e0a0' | head -3

# 4) Emoji / CJK
fc-match ':charset=1f600'      # 😀 → Noto Color Emoji
fc-match ':charset=4e2d'       # 中  → Noto Sans CJK SC

# 5) Métricas de la fuente (ascenso/descenso; la x-height se mide con fontTools)
fc-query --format '%{family}\n  ascent=%{ascender} descent=%{descender}\n' \
  "$(fc-match -f '%{file}' 'FantasqueSansM Nerd Font Mono')"

# 6) Recarga y prueba visual
fc-cache -f
kitty +kitten show_key -m monospace 2>/dev/null | head -5   # opcional
```

**[O]** Prueba de legibilidad a 1440×900: abre kitty con `btop` y `eza --icons` a 11.5 px;
comprueba que (a) los separadores de powerline del prompt no dejan huecos, (b) los dígitos de
`sysmon` no bailan al cambiar de valor, (c) los caracteres de caja de `btop` no se solapan y
(d) el reloj de la barra no se corta con `{:%H:%M %A %m/%d/%y}`. Si (b) falla, la fuente no es
tabular; si (a) falla, estás usando Propo en vez de Mono.

---

## 10. Errores comunes

| Error | Síntoma | Solución |
|---|---|---|
| Mezclar demasiadas fuentes | Barra, prompt y editor "no pegados" | Una Nerd Mono para todo; máximo una segunda para `display` |
| Glifos faltantes | Cuadraditos `□` en el prompt | Usar variante **Nerd** (no la fuente base) y verificar `charset=e0a0` |
| Fuente sin Mono en terminal | Columnas desalineadas, `btop` torcido | Cambiar `Propo` → `Mono` en kitty/alacritty y en el alias `monospace` |
| Tamaños inconsistentes | Barra diminuta junto a terminal enorme | Alinear `font_size` de terminal con `label` de barra; tocar `font_scale`, no `scale` |
| Ligaduras en prompt | `->` se lee como un glifo raro; confusión con `|` | `font_features -liga` en kitty o desactivar en fish |
| Emoji color en la rejilla | Cursor y columnas desplazados | Glyphs Nerd en su lugar o `symbol_map` con ancho fijo |
| DPI/hinting agresivos | Texto engordado o con franjas de color | `hintslight` + `rgba=rgb` (o `none`), `dpi=96` |
| Olvidar `fc-cache` | La fuente nueva no aparece en selectores | `fc-cache -f` y reiniciar la app |
| Culpar a btop/Noctalia | "La fuente de btop está mal" | btop hereda la terminal; los glyphs de Noctalia son QML, no Nerd |

---

## 11. Tabla de recomendaciones concretas para este usuario

| Superficie | Estado actual **[H]** | Fuente recomendada **[O]** | Ajuste sugerido **[O]** |
|---|---|---|---|
| **Terminal principal (kitty)** | Sin `font_family`; tema noctalia importado | `FantasqueSansM Nerd Font Mono` | `font_size 11.5`, `font_features +liga +calt` |
| **Terminal secundaria (alacritty)** | `family="monospace"`, `size=12.0` | `FantasqueSansM Nerd Font Mono` | `size 11.5`; alinear con kitty |
| **Prompt fish + pure** | Sin símbolos personalizados | `FantasqueSansM Nerd Font Mono` (o `MesloLGS Nerd Font Mono`) | `pure_symbol_git_branch ''`; sin ligaduras |
| **Barra Noctalia** | Hereda fuente global; `scale=1.10`, `font_weight` no fijado | `FantasqueSansM Nerd Font Mono` | `font_family`, `font_weight 500`, `font_scale 1.0` |
| **Notificaciones / paneles Noctalia** | Sin `font_family` propio | Igual que la barra | Usar `caption` 11–12 px, tabular nums |
| **Editor (micro / vim / GNOME Text Editor)** | 4 esquemas Catppuccin en micro | `FantasqueSansM Nerd Font Mono` (kitty) / `JetBrainsMono Nerd Font` si se instala | Ligaduras sí en código, no en prompt |
| **btop / fastfetch / eza --icons** | Heredan terminal | Igual que kitty | Verificar braille y box-drawing |
| **Títulos / launcher / display** | Sin definir | `Iosevka Nerd Font` (si se instala) o la misma Fantasque | 18–22 px, peso 600–700 |
| **CJK / emoji (fallback)** | Noto completo ya instalado | `Noto Sans CJK SC` + `Noto Color Emoji` | Solo `append` por `lang`; nunca en `monospace` |

**Orden de ejecución recomendado [O]:** (1) fijar `font_family` en kitty y alacritty;
(2) añadir `font_family`/`font_weight` a `[bar.default]` de Noctalia; (3) verificar con
`fc-match` y el test de powerline; (4) recién entonces valorar instalar JetBrainsMono Nerd o
Iosevka Nerd. Todo lo demás (paleta M3, blur, bordes) ya está resuelto en el rice actual.

---

## 12. Fuentes citadas

**Archivadas en `sources/` (rutas relativas desde la raíz de `ricing`):**

- [Nerd Fonts · README](sources/2026-11-21-nerd-fonts-readme.md) — https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md
- [Nerd Fonts · Sitio oficial](sources/2026-11-21-nerd-fonts-website.md) — https://www.nerdfonts.com/
- [Noctalia · Bar](sources/2026-11-21-noctalia-bar.md) — https://github.com/noctalia-dev/noctalia/blob/main/docs/user/bar/index.mdx
- [Catppuccin · README](sources/2026-11-21-catppuccin-readme.md) — https://github.com/catppuccin/catppuccin/blob/main/README.md

**Auditoría local:** [Perfil del sistema](00-perfil-del-sistema.md),
[familias-fuentes.txt](apendices/familias-fuentes.txt),
[kitty.conf](configuracion-actual/kitty/kitty.conf),
[alacritty.toml](configuracion-actual/alacritty/alacritty.toml),
[noctalia/config.toml](configuracion-actual/noctalia/config.toml),
[gtk/settings.ini](configuracion-actual/gtk/settings.ini),
[fish-config.fish](configuracion-actual/shell/fish-config.fish).

**Fuentes primarias externas no archivadas (URL original):** https://rsms.me/inter/ ·
https://github.com/JetBrains/JetBrainsMono · https://github.com/be5invis/Iosevka ·
https://github.com/tonsky/FiraCode · https://github.com/belluzj/fantasque-sans ·
https://github.com/andreberg/Meslo-Font · https://github.com/notofonts/noto-fonts ·
https://nerdfonts.com/cheat-sheet.
