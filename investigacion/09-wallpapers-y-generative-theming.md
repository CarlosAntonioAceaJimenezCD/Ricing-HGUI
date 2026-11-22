# 09 · Wallpapers y generación de temas a partir de imágenes

> En el ricing moderno, el wallpaper **no es sólo decoración**: es la semilla de
> la que se derivan todos los colores del sistema. Este documento explica el
> pipeline completo, por qué tu esquema `m3-tonal-spot` importa y cómo hacer que
> el resultado sea reproducible.

## 1. El wallpaper como fuente de verdad

Tu sistema ya funciona así:

```
/usr/share/wallpapers/cachyos-wallpapers/*
/usr/share/noctalia/assets/noctalia-wallpaper.png
        │
        ▼ (SUPER+SHIFT+W → noctalia panel-toggle wallpaper)
Noctalia extrae color → esquema m3-tonal-spot → tokens
        │
        ▼
GTK · Qt · kitty · alacritty · btop · kcolorscheme · barra
```

Fuentes: [Noctalia wallpaper](../sources/2026-11-21-noctalia-wallpaper.md),
[Noctalia paleta](../sources/2026-11-21-noctalia-theming-palette.md),
[Hyprland wallpapers](../sources/2026-11-21-hyprland-wallpapers.md).

La wiki de Hyprland recomienda `hyprpaper` como setter nativo, pero en tu sistema
**no está instalado**: Noctalia gestiona el fondo y el tema a la vez. Es una
decisión acertada para un rice coherente (un solo componente se encarga del proceso).

## 2. Cómo se extrae una paleta de una imagen

Aunque Noctalia no publica el algoritmo exacto en sus docs, los generadores del
ecosistema siguen tres enfoques:

| Enfoque | Qué hace | Herramientas |
|---|---|---|
| **Cuantización de color** | Reduce la imagen a N colores representativos (median-cut / k-means) | pywal, wallust |
| **Color semilla + esquema** | Elige un color dominante y deriva tonos con reglas perceptuales | Material You / matugen / Noctalia M3 |
| **Paleta fija con ImageMagick** | Extrae el color más frecuente y lo mapea a una paleta curada | scripts caseros |

**Material Color Utilities** (usado por M3) describe el proceso como: extraer un
color semilla → generar cinco *key colors* (primary, secondary, tertiary, error,
neutral, neutral-variant) → producir tonos 0–100 con espaciado perceptual
([fuente](../sources/2026-11-21-material-you-color-system.md)).

### 2.1 Qué significa `m3-tonal-spot`

Es una de las variantes de *dynamic color* de Material 3. En lugar de tomar un
color cualquiera, **busca un color de acento en una región limitada del wallpaper**
(el "tonal spot"). Resultado: acentos más limpios y menos "barro" que con un
promedio global.

En tu caso produce:

| Token | Hex generado |
|---|---|
| primary / accent | `#6791e4` |
| on-primary | `#181d25` |
| surface | `#1e1e20` |
| surface elevado | `#27282a` |
| outline / muted | `#afb1b6` |
| error | `#fd4663` |

Si cambias a otro esquema M3 (`m3-vibrant`, `m3-expressive`, etc.), el mismo
wallpaper dará acentos distintos. Lo interestante es que **no necesitas cambiar
el wallpaper para cambiar el ánimo del rice**: cambia el esquema.

## 3. Generadores disponibles (y cuál usar)

| Herramienta | Entrada | Algoritmo | GUI | Integración contigo |
|---|---|---|---|---|
| **Noctalia** (instalado) | Wallpaper | M3 tonal spot y otros | Sí (panel) | ⭐ Nativa, ya funciona |
| [matugen](../sources/2026-11-21-matugen-readme.md) | Imagen/vídeo | Material You + plantillas | No (CLI) | Muy compatible; genera configs Hyprland |
| [wallust](../sources/2026-11-21-wallust-readme.md) | Imagen | Cuantización + plantillas | No (CLI) | Rápido (Rust), alternativa a pywal |
| [pywal](../sources/2026-11-21-pywal-readme.md) | Imagen | 16 colores + plantillas | No (CLI) | El clásico; referencia histórica |
| [wpgtk](../sources/2026-11-21-gui-wpgtk.md) | Imagen + edición | pywal + GUI | **Sí** | Si quieres editar colores a mano |
| Variety / Azote | Imagen | Sólo cambian el fondo | Sí | Ver [doc 14](14-herramientas-gui-de-ricing.md) |

**Recomendación [OPINIÓN]:** mantén Noctalia. Si algún día quieres exportar la
paleta a una app que Noctalia no cubre, `matugen` es el complemento más natural
porque también habla Material You.

## 4. Elegir wallpapers que generen buenas paletas

No todas las imágenes producen un buen esquema. Criterios prácticos:

1. **Un color dominante claro**: imágenes monocromáticas con un acento producen
   paletas limpias; las fotos muy saturadas y multicolor producen acentos "barrosos".
2. **Evita fondos casi blancos o casi negros**: no hay suficiente información
   cromática para derivar tonos intermedios.
3. **Piensa en modo oscuro**: tu rice es `mode = "dark"`. Un wallpaper oscuro con
   un punto de luz suele dar mejores `surface` y `accent`.
4. **Comprueba el contraste resultante**: la paleta debe dar ≥4.5:1 para texto
   sobre fondo (ver [05-sistema-de-colores.md](05-sistema-de-colores.md)).
5. **Resolución acorde al monitor**: 1440×900. Un 4K se reescala y puede perder
   el detalle que servía de semilla.

Fuentes de wallpapers con licencia clara:

- `/usr/share/wallpapers/cachyos-wallpapers` (incluidos con CachyOS).
- Wallhaven / Unsplash (revisa la licencia de cada imagen antes de redistribuir).
- La [galería de Catppuccin](../sources/2026-11-21-catppuccin-readme.md) tiene
  wallpapers oficiales que combinan con su paleta.

## 5. Wallpapers animated / vídeo (advertencia para tu GPU)

`mpvpaper` y `swww` con transiciones permiten fondos animados. En tu Intel Sandy
Bridge (sin VRR, sin HDR) esto es una mala idea: el compositor ya paga blur de
4 passes y transparencias. Si lo pruebas:

```bash
mpvpaper -o "no-audio --loop-file=inf" VGA-1 wallpaper.mp4
```

...y observa `intel_gpu_top`. **OPINIÓN:** quédate con wallpapers estáticos; el
contraste entre un fondo animado y un compositor que ya va justo es más costoso
que espectacular.

## 6. Reproducibilidad: fija la semilla

Un rice generativo tiene un problema: si mañana cambias el wallpaper, toda la
paleta cambia. Para que sea reproducible guarda, junto con el dotfile:

```text
recursos/wallpaper-semilla/
├── wallpaper.png            # la imagen exacta
├── seed-color.txt           # p. ej. #6791e4
├── scheme.txt               # m3-tonal-spot
└── generated/
    ├── noctalia.css
    ├── kitty.conf
    ├── alacritty.toml
    └── colors.lua
```

Y un script `apply-theme.sh` que copie esos archivos generados a su sitio. Así
puedes recuperar el look exacto aunque Noctalia cambie de versión.

Comandos útiles:

```bash
# Ver el tema que Noctalia tiene ahora
grep -A5 '^\[theme\]' ~/.config/noctalia/config.toml

# Ver los colores que efectivamente se aplicaron
grep '@define-color' ~/.config/gtk-3.0/noctalia.css | head
grep -E '^(background|foreground|color0) ' ~/.config/kitty/themes/noctalia.conf

# Ver el wallpaper actual (variable de entorno que pone el shell)
echo "${WALLPAPER:-no WALLPAPER env var}"
```

## 7. Casos de uso concretos en tu sistema

| Quieres... | Haz esto |
|---|---|
| Cambiar sólo el ánimo, no la imagen | Cambia `wallpaper_scheme` en `config.toml` |
| Un acento verde CachyOS | Elige un wallpaper verde O usa `colors.lua` con los tokens verdes (ver doc 05) |
| Añadir Hyprland al theming | Añade `"hyprland"` a `builtin_ids` |
| Editar un color generado a mano | Noctalia no lo permite directamente → usa wpgtk (doc 14) |
| Volver al look anterior | Guarda la semilla como en la sección 6 |

## 8. Fuentes

- [Noctalia wallpaper](../sources/2026-11-21-noctalia-wallpaper.md) ·
  [Noctalia theming](../sources/2026-11-21-noctalia-theming-index.md) ·
  [paleta](../sources/2026-11-21-noctalia-theming-palette.md) ·
  [templates](../sources/2026-11-21-noctalia-templates.md)
- [Material Color Utilities](../sources/2026-11-21-material-you-color-system.md)
- [hyprpaper / Hyprland wallpapers](../sources/2026-11-21-hyprland-wallpapers.md)
- [matugen](../sources/2026-11-21-matugen-readme.md) ·
  [wallust](../sources/2026-11-21-wallust-readme.md) ·
  [pywal](../sources/2026-11-21-pywal-readme.md)
- [wpgtk GUI](../sources/2026-11-21-gui-wpgtk.md)
