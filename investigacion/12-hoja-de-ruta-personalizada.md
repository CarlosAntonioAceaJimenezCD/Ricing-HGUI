# 12 · Hoja de ruta personalizada (tu sistema, tus próximos pasos)

> Este es el documento "y ahora qué". Prioriza los hallazgos de la investigación
> según tu equipo real: CachyOS, Hyprland 0.57.2 con config Lua, Noctalia 5.6.0,
> Intel Sandy Bridge, 1440×900, AZERTY, fish, kitty/alacritty y Nerd Fonts.

## 1. Resumen ejecutivo

Tu rice actual es **sorprendentemente coherente** para ser la configuración por
defecto de CachyOS: tiene un shell propio con theming generativo, animaciones
spring, reglas de ventana muy trabajadas y un fix AZERTY artesanal. Los problemas
no son estéticos, sino de **mantenimiento y consistencia**:

| # | Hallazgo | Severidad | Esfuerzo |
|---|---|:---:|:---:|
| 1 | `dampening` en `animations.lua` probablemente ignorado en 0.57 | 🔴 Alta | 2 min |
| 2 | Dos fuentes de color (Cachy green vs M3 azul) | 🟠 Media-alta | 30 min |
| 3 | Dotfiles sin control de versiones | 🔴 Alta (riesgo) | 1 h |
| 4 | Blur `passes=4` + transparencias en iGPU sin medir | 🟠 Media | 20 min |
| 5 | Fuentes Nerd no declaradas explícitamente en terminales | 🟡 Baja | 5 min |
| 6 | `MONITOR2/3` vacías con reglas que las referencian | 🟡 Baja | 0 (documentar) |
| 7 | Oportunidad: GUI propia / hyprmod para no editar Lua | 🟢 Oportunidad | 1-2 días |

## 2. Hallazgo 1: el typo `dampening` (arreglo inmediato)

Tus curvas spring:

```lua
hl.curve("easy",   { type = "spring", mass = 1, stiffness = 500, dampening = 35 })
hl.curve("rubber", { type = "spring", mass = 1, stiffness = 200,  dampening = 15 })
```

Pero las notas de **Hyprland 0.57.0** dicen textualmente:

> `config/lua: fix misspelling of damping as dampening for spring animations (#15993)`

y la wiki oficial usa `damping`:
`hl.curve(NAME, { type = "spring", mass = float, stiffness = float, damping = float })`.

**Acción:**

```bash
cp ~/.config/hypr/config/animations.lua ~/ricing/configuracion-actual/animations.lua.bak
sed -i 's/dampening/damping/g' ~/.config/hypr/config/animations.lua
hyprland --verify-config     # debe decir config ok
```

Luego reinicia Hyprland (`SUPER+M` → logout, o `hyprctl reload` para config en caliente)
y compara el rebote de las ventanas. Fuente:
[hyprland-releases.md](../sources/2026-11-21-hyprland-releases.md) y
[hyprland-animations.md](../sources/2026-11-21-hyprland-animations.md).

> **INCIERTO:** quizá 0.57 aún acepta `dampening` por compatibilidad. El cambio es
> inocuo y alinea tu config con la documentación actual.

## 3. Hallazgo 2: unificar la paleta (30 min)

Hoy: bordes verdes CachyOS (`#82dccc` → `#007d6f`) + resto azul M3 (`#6791e4`).

**Plan mínimo (sin romper nada):**

1. Añadir `"hyprland"` a `builtin_ids` en `~/.config/noctalia/config.toml`:
   ```toml
   [theme.templates]
   builtin_ids = [ "btop", "gtk3", "gtk4", "kcolorscheme", "kitty", "qt", "alacritty", "hyprland" ]
   ```
2. Revisar la plantilla generada y, si te gusta, copiar los tokens a
   `config/colors.lua` con **nombres de rol** (`ACCENT`, `MUTED`, `TEXT`) en lugar
   de `CACHYLGREEN`.
3. Cambiar el `link` GTK de `#695cd6` (3.25:1) a `#9f96e9` (~6:1) para texto.

Detalle y contrastes calculados: [05-sistema-de-colores.md](05-sistema-de-colores.md).

## 4. Hallazgo 3: versionar los dotfiles (1 h)

Hoy todo está en `~/.config` sin git: un `hyprctl reload` desafortunado o una
actualización puede dejarte sin rice.

**Plan rápido (bare repo, sin mover archivos):**

```bash
git init --bare ~/.dotfiles.git
alias dotfiles='git --git-dir=$HOME/.dotfiles.git --work-tree=$HOME'
dotfiles config --local status.showUntrackedFiles no
dotfiles add .config/hypr .config/noctalia .config/kitty .config/alacritty \
             .config/gtk-3.0 .config/fish/config.fish .config/uwsm/env \
             .local/share/color-schemes
dotfiles commit -m "rice: estado inicial Hyprland 0.57 + Noctalia"
```

**No versionar:** `fish_variables`, `keyrings`, cachés, `.local/share/opencode`,
tokens ni historiales. Detalle completo:
[10-dotfiles-y-gestion.md](10-dotfiles-y-gestion.md).

## 5. Hallazgo 4: presupuesto de GPU (20 min)

Tu Intel Sandy Bridge no tiene VRR ni HDR y ya paga blur de 4 passes. Mide antes
de añadir efectos:

```bash
intel_gpu_top                      # si no está: sudo pacman -S intel-gpu-tools
hyprctl getoption decoration:blur:passes
hyprctl setoption debug:overlay 1  # superposición de rendimiento (si aplica)
```

**Si ves tirones:** bajar `passes` de 4 a 2-3, o reducir `blur.size` de 5 a 3.
No actives wobble ni blur proporcional (features nuevos de 0.57) sin medir.
Detalle: [08-animaciones-y-efectos.md](08-animaciones-y-efectos.md).

## 6. Hallazgo 5: tipografía explícita (5 min)

Declara la fuente en vez de heredar `monospace`:

```conf
# ~/.config/kitty/kitty.conf
font_family      MesloLGM Nerd Font Mono
font_size        11
```

```toml
# ~/.config/alacritty/alacritty.toml
[font]
normal = { family = "MesloLGM Nerd Font Mono", style = "Regular" }
```

Detalle y tabla por superficie: [06-tipografia.md](06-tipografia.md).

## 7. Hallazgos 6 y 7: documentar y decidir

- **Monitores:** `variables.lua` tiene `MONITOR1/2/3 = ""`. Hoy sólo existe
  `VGA-1`. Añade un comentario advirtiendo que las reglas para `MONITOR2/3`
  quedan inactivas; si conectas otro monitor, rellena con `hyprctl monitors`.
- **GUI:** si quieres dejar de editar Lua, instala `yay -S hyprmod` y **prueba
  sobre copia** de tu config. O crea la tuya:
  [15-crear-tu-propia-gui.md](15-crear-tu-propia-gui.md).

## 8. Plan por fases

### Fase 0 — Hoy (15-30 min) · "Quick wins"

- [ ] Arreglar `dampening` → `damping` y verificar config.
- [ ] Declarar Nerd Font en kitty y alacritty.
- [ ] Copiar tu config actual a `~/ricing/configuracion-actual/` (ya hecho).
- [ ] Leer [00-perfil-del-sistema.md](../00-perfil-del-sistema.md) y este documento.

### Fase 1 — Esta semana (2-3 h) · "Coherencia"

- [ ] Unificar paleta (Hyprland ← M3 de Noctalia).
- [ ] Iniciar el repo bare de dotfiles y hacer el primer commit.
- [ ] Medir GPU con `intel_gpu_top`; ajustar blur si hace falta.
- [ ] Cambiar `link` GTK a un tono con contraste ≥4.5:1.

### Fase 2 — Próximas 2 semanas (4-6 h) · "Herramientas"

- [ ] Probar `hyprmod` en una copia de la config; valorar si sustituye la edición manual.
- [ ] Instalar `kvantum` si Dolphin/VLC se ven inconsistentes.
- [ ] Guardar la semilla del wallpaper y los archivos generados (doc 09).
- [ ] Añadir `hyprland.lua` a los templates de Noctalia.

### Fase 3 — Mes 1+ · "Crear tu propia GUI"

- [ ] Seguir el plan de 6 pasos de [15-crear-tu-propia-gui.md](15-crear-tu-propia-gui.md).
- [ ] Empezar con el prototipo de `rounding`/`blur` (ya tienes el código en
      `recursos/hypr-rice-gui/main.py`).
- [ ] Definir `ui-settings.lua` como fuente de verdad y conectarlo a `decorations.lua`.
- [ ] Externalizar textos con gettext desde el primer commit (español-base).

## 9. Checklist de verificación final

```bash
hyprland --verify-config                       # config ok
noctalia config validate                       # ✓ Config is valid
hyprctl getoption decoration:rounding          # valor esperado
grep '@define-color accent_color' ~/.config/gtk-3.0/noctalia.css
fc-match 'MesloLGM Nerd Font Mono'             # fuente correcta
dotfiles status --short                        # sin secretos
```

## 10. Qué NO hacer

1. No instalar Waybar Configurator GUI (no usas Waybar).
2. No instalar Gradience (archivado en 2024).
3. No activar VRR/HDR en la config: tu GPU no los expone.
4. No tener dos motores de color generando a la vez (Noctalia + wpgtk/matugen).
5. No editar la config del usuario directamente desde un script sin backup.
6. No meter `fish_variables`, keyrings ni tokens en el repo de dotfiles.
7. No copiar dotfiles de Internet sin leerlos: revisa especialmente `autostart`,
   `exec-once` y cualquier `curl | sh`.

## 11. Fuentes de esta hoja de ruta

- [Perfil del sistema](../00-perfil-del-sistema.md) ·
  [arquitectura](03-arquitectura-de-un-rice.md) ·
  [Hyprland 0.57](02-hyprland-0-57.md) ·
  [animaciones](08-animaciones-y-efectos.md)
- [colores](05-sistema-de-colores.md) · [tipografía](06-tipografia.md) ·
  [iconos](07-iconos-y-cursores.md) · [wallpapers](09-wallpapers-y-generative-theming.md)
- [dotfiles](10-dotfiles-y-gestion.md) ·
  [herramientas GUI](14-herramientas-gui-de-ricing.md) ·
  [crear tu GUI](15-crear-tu-propia-gui.md)
- [Notas de release 0.57](../sources/2026-11-21-hyprland-releases.md) ·
  [animaciones oficiales](../sources/2026-11-21-hyprland-animations.md)
