# 10 · Dotfiles como práctica y sistema (gestión, backup y reproducibilidad)

> Escrito el 2026-11-21/22 para `thony70807`. Datos comprobados en esta máquina:
> `pacman -Q | wc -l` → **1232** paquetes, `pacman -Qqe | wc -l` → **182** explícitos,
> `pacman -Qm` → **0** foreign/AUR, `pacman -Qdtq` → **0** huérfanos. HOME **no es** un
> repo Git y no existe `~/.dotfiles` ni `~/.local/share/chezmoi`.
>
> **Convención de este documento:** **[Hecho]** = verificable en los apéndices, fuentes o
> comandos ejecutados. **[Opinión]** = recomendación del autor, discutible y ligada al
> hardware modesto y al perfil de usuario. Las fuentes se citan como
> `[Fuente](sources/…)` con su URL original; las herramientas sin copia local se citan
> directamente y se marca "(sin copia en `sources/`)".

---

## 1. Qué son y un poco de historia

**[Hecho]** Un *dotfile* es un archivo de configuración cuyo nombre empieza por punto
(`.bashrc`, `.config/...`) y que tradicionalmente reside en el directorio `~` del
usuario. La convención surge de Unix: el sistema guarda los valores por defecto en
`/etc` y cada usuario los sobreescribe en su casa. Con el tiempo la XDG Base Directory
Specification etiquetó la mayoría de esos archivos bajo `~/.config/`, pero el nombre
"dotfiles" se conservó. Hoy un "repo de dotfiles" es un repositorio que versiona esa
capa de configuración personal.

**[Hecho]** La documentación oficial de Hyprland describe el archivo de entrada como
`~/.config/hypr/hyprland.lua` —generado automáticamente si no existe, con una copia de
ejemplo en `/usr/share/hypr/hyprland.lua`— y permite partirlo con `require()`
([ArchWiki](sources/2026-11-21-archwiki-hyprland.md) —
https://wiki.archlinux.org/title/Hyprland). La versión 0.56 añadió un aviso de
deprecación a los configs `.conf` y 0.57 consolidó la API Lua `hl.*`
([Releases](sources/2026-11-21-hyprland-releases.md) —
https://github.com/hyprwm/Hyprland/releases). Ese cambio reciente es, precisamente, un
argumento para tener historial: poder hacer `git diff` cuando una actualización rompe
la sintaxis.

**[Hecho]** La distribución de dotfiles completos se popularizó con GitHub: repos como
[JaKooLit/Hyprland-Dots](sources/2026-11-21-jakoolit-hyprland-dots.md) —
https://github.com/JaKooLit/Hyprland-Dots/blob/main/README.md — publican recursivamente
`config/`, `scripts/`, `wallpapers/` y scripts `copy.sh` / `release.sh` / `upgrade.sh`,
con avisos explícitos de "crea backups antes de copiar" y de que el repo **no instala
paquetes**. El repo `Hyprland-Dots` clonado en `repositorios/` muestra esa estructura
(`config/hypr`, `config/kitty`, `config/qt6ct`, `config/rofi`, `config/swaync`, …),
mientras `dots-hyprland/` separa `dots/`, `dots-extra/`, `setup/`, `sdata/` y `licenses/`.

**[Opinión]** El valor real no es "tener mis configs en GitHub", sino poder responder
tres preguntas: *¿qué cambié?*, *¿cuándo funcionaba?* y *¿cómo lo reconstruyo en 20
minutos?*. En un rolling release como CachyOS, la tercera pregunta es la crítica.

---

## 2. Qué versionar y qué NO

| ✅ Versionar | 🚫 No versionar (y por qué) |
|---|---|
| `~/.config/hypr/hyprland.lua` + `config/*.lua` + `xdph.conf` | Claves SSH (`~/.ssh/id_*`), GPG, `~/.gnupg` → secreto |
| `~/.config/noctalia/config.toml` y temas propios | Tokens, `.env`, `~/.config/gh/hosts.yml`, `netrc` → credenciales |
| `~/.config/kitty/`, `alacritty/`, `gtk/`, `fish/` | Historiales: `~/.local/share/fish/fish_history`, `~/.bash_history`, `~/.lesshst` → privacidad |
| `~/.config/qt6ct/`, `~/.local/share/color-schemes/` | Cachés: `~/.cache/*`, `~/.config/hypr/*.log`, `/hyprland.log` → ruido y datos volátiles |
| `~/.config/xsettingsd/xsettingsd.conf` (pero instalar el binario) | `~/.local/share/Noctalia/state*`, session state → estado de ejecución |
| `scripts/`, `Makefile`, `justfile`, `README.md`, `LICENSE` | Wallpapers pesados y binarios >~10 MB → usar Git LFS o guardar solo la ruta |
| Listas de paquetes y pinned versions (`pacman -Qqe`, `pacman -Q`) | `/etc/machine-id`, claves de red, `~/.config/pulse/cookie` → identificadores de máquina |
| `~/.config/uwsm/env` **sanitizado** (sin tokens) | Directorios completos de navegador / perfil de Firefox → datos personales y tamaño |

**.gitignore recomendado** (a la raíz del repo):

```gitignore
# secretos
.ssh/
.gnupg/
.env
*.env
.envrc
netrc
.config/gh/hosts.yml

# historiales y estado
.config/*/history
.local/share/fish/fish_history
.local/share/Noctalia/state*
.cache/

# ruido
*.log
*.swp
.DS_Store
__pycache__/
*.pyc

# binarios grandes (guardar fuera del repo o con LFS)
*.png
*.jpg
*.mp4
!docs/screenshots/*.png
```

**[Hecho]** El riesgo no es teórico: los propios dotfiles de terceros avisan de que sus
scripts de copia generan backups en `~/.config` y hay que revisarlos manualmente
([JaKooLit](sources/2026-11-21-jakoolit-hyprland-dots.md) —
https://github.com/JaKooLit/Hyprland-Dots/blob/main/README.md). Nunca adoptes un
`copy.sh` ajeno sin leer qué sobrescribe.

---

## 3. Estructura recomendada para este usuario

Partir de `configuracion-actual/` es natural: ya es un espejo XDG de lo que hay en
`~/.config`. Estructura propuesta en `~/dotfiles`:

```text
~/dotfiles/
├── README.md              # qué instala, versiones, atajos, capturas
├── LICENSE                # MIT para tus configs; licencias de assets en licenses/
├── .gitignore
├── Makefile               # make link / check / backup / restore (o justfile)
├── hypr/                  # -> ~/.config/hypr
│   ├── .config/hypr/hyprland.lua
│   ├── .config/hypr/config/{animations,autostart,binds,colors,…}.lua
│   └── .config/hypr/xdph.conf
├── noctalia/              # -> ~/.config/noctalia
│   └── .config/noctalia/config.toml
├── terminals/             # -> ~/.config/kitty, ~/.config/alacritty
├── gtk-qt/                # -> ~/.config/gtk-3.0, ~/.config/qt6ct, color-schemes
├── fish/                  # -> ~/.config/fish/config.fish
├── shell/                 # -> ~/.config/uwsm/env (sanitizado)
├── system/
│   ├── packages/pacman-native.txt        # pacman -Q
│   ├── packages/pacman-explicit.txt      # pacman -Qqe
│   ├── packages/pacman-foreign.txt       # pacman -Qm  (vacío = 0 AUR)
│   └── pacman.conf / pacman.d/           # repos de CachyOS
├── scripts/               # check-configs.fish, wallpaper-random, restore.fish
├── docs/                  # capturas y notas de diseño
└── licenses/              # Bibata, Nerd Fonts, Catppuccin, CachyOS wallpapers
```

**[Opinión]** Para Stow, cada subcarpeta debe replicar la ruta completa desde `~`
(por eso aparece `.config/hypr/…` dentro de `hypr/`). Para el repo *bare*, en cambio,
se versiona directamente el árbol de `$HOME` y se filtra con `.gitignore`. Mezclar
ambos modelos es el error más habitual.

---

## 4. Estrategias: ventajas, desventajas y comandos

### 4.1 Git bare repo (repo desnudo con `--work-tree=$HOME`)

**Qué es.** Un repo Git sin directorio de trabajo ubicado en `~/.dotfiles.git`, usando `$HOME`
como árbol de trabajo. Popularizado por el artículo *“Using Git and Github to manage
your dotfiles”*.

```fish
git init --bare $HOME/.dotfiles.git
git --git-dir=$HOME/.dotfiles.git --work-tree=$HOME config status.showUntrackedFiles no

# ~/.config/fish/config.fish
function dots --description 'Gestionar dotfiles'
    git --git-dir=$HOME/.dotfiles.git --work-tree=$HOME $argv
end

dots add ~/.config/hypr/hyprland.lua ~/.config/noctalia/config.toml
dots commit -m 'Sync Hyprland 0.57.2 + Noctalia 5.6.0'
dots remote add origin git@github.com:thony70807/dotfiles.git
dots push -u origin main
```

| Ventaja | Desventaja |
|---|---|
| Cero herramientas nuevas: solo Git | `git status` ruidoso si olvidas `showUntrackedFiles no` |
| Cualquier archivo de `$HOME` se versiona con un comando | Fácil commitear secretos por accidente |
| `dots log -p` da historial completo | Restaurar en máquina nueva requiere mover archivos existentes antes del checkout |

### 4.2 GNU Stow (symlinks por paquete)

**Qué es.** Un *symlink farm manager*: crea enlaces simbólicos desde `~/dotfiles/<paquete>/…`
hacia `$HOME` replicando la estructura
([GNU Stow manual](https://www.gnu.org/software/stow/manual/stow.html), sin copia en `sources/`).

```fish
sudo pacman -S stow                      # CachyOS: paquete oficial, sin AUR
cd ~/dotfiles
stow -n hypr                             # -n/--dry-run: NO escribe nada
stow hypr noctalia terminals fish        # aplicar
stow -D hypr                             # des-enlazar (unstow)
stow -R hypr                             # restow tras añadir archivos
find ~/.config -maxdepth 2 -type l -ls   # verificar enlaces
```

| Ventaja | Desventaja |
|---|---|
| Semántica de "paquete": activar/desactivar bloques enteros | Los directorios destino no deben existir como reales |
| Independiente del shell (funciona con fish sin adaptación) | `stow --adopt` puede absorber archivos ajenos: usar con cuidado |
| Diff legible: todo son archivos normales en el repo | No gestiona plantillas por máquina ni secretos |

### 4.3 Symlinks manuales

```fish
ln -s ~/dotfiles/hypr/.config/hypr/hyprland.lua ~/.config/hypr/hyprland.lua
readlink -f ~/.config/hypr/hyprland.lua
```

**[Opinión]** Es transparentemente simple, pero no escala a 40+ archivos y no documenta qué
enlace pertenece a qué bloque. Solo recomendable como paso de aprendizaje o para un
par de archivos.

### 4.4 chezmoi

**Qué es.** Gestor multi-máquina con plantillas (Go `text/template`), secretos integrados
(vía `age`/1Password/etc.) y comandos de diff/apply
([chezmoi docs](https://www.chezmoi.io/), sin copia en `sources/`).

```fish
sudo pacman -S chezmoi                   # disponible en repos oficiales
chezmoi init
chezmoi add ~/.config/noctalia/config.toml
chezmoi cd                               # abre el repo de trabajo
chezmoi diff
chezmoi apply --dry-run --verbose
chezmoi apply
chezmoi update                           # git pull + apply
```

Ejemplo de plantilla (`dot_config/hypr/config/variables.lua.tmpl`):

```lua
local MONITOR1 = "{{ .hostname | upper }}"
local IS_LAPTOP = {{ eq .hostname "cachyos-nuc" }}
```

| Ventaja | Desventaja |
|---|---|
| Plantillas por máquina/SO; secretos cifrados nativos | Curva de aprendizaje y terminología propia (`dot_`, `private_`, `symlink_`) |
| `chezmoi apply` idempotente y con dry-run | Añade una capa entre el archivo y su destino |
| Muy bueno para sincronizar varios equipos | Overkill para una sola máquina |

### 4.5 Nix / home-manager

**Qué es.** Configuración declarativa: el estado del home se describe en Nix y se
materializa con `home-manager switch`. La wiki de Hyprland dedica una sección completa
a *Configuring Hyprland with Home Manager*
(https://wiki.hypr.land/nix/configuring-hyprland-with-home-manager/, sin copia local).

```fish
nix-shell -p home-manager
home-manager switch --flake ~/dotfiles#thony70807
```

| Ventaja | Desventaja |
|---|---|
| Reproducibilidad más fuerte del ecosistema | Exige adoptar Nix sobre CachyOS (otro gestor de paquetes) |
| Rolls back atómicos por generación | Convivir con 1232 paquetes pacman duplica la fuente de verdad |
| Config declarativa de Hyprland | Los 0 paquetes AUR dejan de ser una ventaja clara |

### 4.6 Ansible

**Qué es.** Automatización por YAML con módulos `file`, `copy`, `template`, `package`.

```yaml
- name: Enlazar config de Hyprland
  ansible.builtin.file:
    src: "{{ ansible_env.HOME }}/dotfiles/hypr/.config/hypr"
    dest: "{{ ansible_env.HOME }}/.config/hypr"
    state: link
    force: false
```
```fish
ansible-playbook -i localhost, -c local site.yml --check --diff
```

| Ventaja | Desventaja |
|---|---|
| Instala paquetes **y** config en un solo playbook | Verboso para un solo equipo |
| `--check --diff` muy seguro | Python/Ansible añaden dependencias no necesarias aquí |

### 4.7 Tabla comparativa

| Estrategia | Curva | Multi-máquina | Secretos | Ideal para |
|---|---|---|---|---|
| Git bare | Baja | Media (manual) | ✗ (con .gitignore) | Un equipo, usuario técnico Git |
| **GNU Stow** | Baja-Media | Media | ✗ | **Este caso: single machine, XDG limpio** |
| Symlinks manuales | Muy baja | ✗ | ✗ | 2–3 archivos |
| chezmoi | Media | ✅ | ✅ (age) | Varios equipos, perfiles distintos |
| Nix/home-manager | Alta | ✅ | Parcial | Reproducibilidad extrema |
| Ansible | Media-Alta | ✅ | Con vault | Parques de máquinas |

---

## 5. Cuál conviene a este usuario (opinión)

**[Hecho]** CachyOS es rolling release; hay 1232 paquetes (182 explícitos), 0 AUR, 0
huérfanos; el shell es fish 4.9.3; la configuración ya está dividida en módulos Lua y TOML
bajo `~/.config/`; no existe infraestructura Nix ni Ansible.

**[Opinión]** La mejor elección es **GNU Stow + Git**, con `chezmoi` como evolución
opcional si aparece un segundo equipo. Motivos:

1. El árbol `configuracion-actual/` ya está preparado para convertirse en paquetes Stow
   sin reescribir nada.
2. stow y git están en los repos oficiales de CachyOS: **no hace falta AUR**, algo que
   encaja con el perfil (0 foreign packages).
3. Funciona igual con fish; no hay que traducir scripts bash ni aprender plantillas.
4. Hyprland cambia deprisa (0.56 → 0.57 Lua): lo que más se agradece es `git diff`, no
   una capa de abstracción declarativa.
5. Nix/home-manager y Ansible son excelentes, pero aquí duplicarían la fuente de verdad
   frente a `pacman`, con un coste de migración alto para un único monitor y un único
   equipo.

**[Opinión]** Añadir `hypridle`/`hyprlock` (ver doc 04) o cambiar la paleta no debería
adelantar la decisión de Nix: primero se estabiliza el rice, luego se decide si la
reproducibilidad cruzada justifica el coste.

---

## 6. Flujo de backup y restore

### Backup (cada cambio, o diario)

```fish
# 1) sincronizar configs al repo Stow (copiar, no mover, hasta validar)
rsync -a --delete ~/.config/hypr/  ~/dotfiles/hypr/.config/hypr/
rsync -a --delete ~/.config/noctalia/ ~/dotfiles/noctalia/.config/noctalia/

# 2) congelar inventario de paquetes
pacman -Q        > ~/dotfiles/system/packages/pacman-native.txt
pacman -Qqe      > ~/dotfiles/system/packages/pacman-explicit.txt
pacman -Qm       > ~/dotfiles/system/packages/pacman-foreign.txt   # 0 líneas
pacman -Qdtq     > ~/dotfiles/system/packages/pacman-orphans.txt   # 0 líneas

# 3) validar y commitear
cd ~/dotfiles
fish scripts/check-configs.fish
git add -A && git commit -m "sync $(date +%F)"
git push
```

### Restore en máquina nueva

```fish
sudo pacman -S --needed git stow              # (o chezmoi)
git clone <URL> ~/dotfiles
cd ~/dotfiles
stow -n hypr noctalia terminals gtk-qt fish   # dry-run primero
# Si los archivos destino ya existen: moverlos a ~/.config-backup-<fecha> antes
stow hypr noctalia terminals gtk-qt fish
sudo pacman -S --needed - < system/packages/pacman-explicit.txt
noctalia config validate
hyprland --verify-config
```

**[Hecho]** Con el repo *bare* alternativo, el restore es
`git clone --bare <URL> ~/.dotfiles.git` seguido de
`git --git-dir=$HOME/.dotfiles.git --work-tree=$HOME checkout -f`; si hay conflictos,
Git se negará a sobrescribir y habrá que retirar los archivos previos. Es el mismo
aviso que dan los scripts de terceros sobre backups
([JaKooLit](sources/2026-11-21-jakoolit-hyprland-dots.md) —
https://github.com/JaKooLit/Hyprland-Dots/blob/main/README.md).

---

## 7. Pinned versions y reproducibilidad

**[Hecho]** `pacman -Q` congela el número exacto de **cada** paquete instalado; en este
equipo incluye, entre otros:

```text
hyprland 0.57.2-1
hyprland-guiutils 0.2.2-6
hyprlang 0.6.8-5
hyprcursor 0.1.14-1
xdg-desktop-portal-hyprland 1.5.0-1
noctalia 5.6.0-1
kitty 0.51.0-1
alacritty 0.17.0-1
fish 4.9.3-1
```

**[Hecho]** `pacman -Qqe` (182 líneas) es la lista mínima para reinstalar;
`pacman -S --needed - < archivo` instala solo lo que falta. `pacman -Qm` vacío confirma
que **no hay dependencias AUR**, lo que simplifica enormemente el restore. También
conviene versionar `/etc/pacman.conf` y `/etc/pacman.d/` porque CachyOS añade repos
propios: sin ellos `pacman -S` no resolvería los mismos paquetes.

**[Hecho vs. opinión]** Congelar `pacman -Q` es un *registro* de lo que había, no un
*bloqueo* reproducible: al reinstalar desde un rolling release se obtendrán versiones
más nuevas salvo que se use un snapshot de archivo o Nix. La reproducibilidad total,
en CachyOS, es imposible solo con dotfiles. **[Opinión]** Por eso la lista debe
acompañarse de un `README.md` con la fecha del snapshot, el kernel (`7.3.5-2-cachyos`)
y una nota de "probado con Hyprland 0.57.2 / Noctalia 5.6.0". Es una verdad documental
barata que evita horas de debugging.

---

## 8. Hooks, testing y validación de configs

**[Hecho]** Los comandos de validación disponibles en este equipo, ejecutados el
2026-11-21, son:

```fish
hyprland --verify-config      # → "config ok"  (no inicia sesión)
noctalia config validate      # → "✓ Config is valid" (TOML, secciones, tipos)
hyprctl configerrors          # errores del config ya cargado
hyprctl reload config-only    # recargar sin reiniciar monitores
fish -n ~/.config/fish/config.fish    # -n/--no-execute: solo chequeo de sintaxis
git diff --check              # detecta espacios en blanco al final
```

Matiz importante: en esta versión **`hyprctl` no tiene `-c` de "check"**; `-c` es el
flag de `hyprland` para `--config FILE`. La validación se llama
`hyprland --verify-config`. `hyprctl` sí ofrece `configerrors` y `reload config-only`
(verificado con `hyprctl --help`). La config se recarga sola al guardar
([ArchWiki](sources/2026-11-21-archwiki-hyprland.md) —
https://wiki.archlinux.org/title/Hyprland), y `hl.on("hyprland.start", …)` evita lanzar
daemons duplicados en cada recarga.

**Script `scripts/check-configs.fish`:**

```fish
#!/usr/bin/env fish
set -l failed 0

hyprland --verify-config >/dev/null 2>&1
or begin; echo "✗ hyprland config"; set failed 1; end

noctalia config validate >/dev/null 2>&1
or begin; echo "✗ noctalia config"; set failed 1; end

fish -n $HOME/.config/fish/config.fish
or begin; echo "✗ fish config"; set failed 1; end

git -C $HOME/dotfiles diff --check
or set failed 1

exit $failed
```

**Hook `pre-commit`** (instalado en `.git/hooks/pre-commit`, o gestionado con
`core.hooksPath=~/dotfiles/hooks`):

```fish
#!/usr/bin/env fish
~/dotfiles/scripts/check-configs.fish
or begin
    echo "Config inválida: commit abortado"
    exit 1
end
```

**[Opinión]** Un hook que bloquea el commit puede ser molesto si se hacen cambios
incrementales; una alternativa más suave es un hook `pre-push` o un workflow de CI que
solo avise. Para un rice personal, `pre-push` suele ser el equilibrio razonable.

---

## 9. Documentación y licencias

**[Opinión]** Un repo sin README es un backup, no un sistema. `README.md` debería
contener: versión de Hyprland/Noctalia, lista de paquetes explícitos, atajos
problemáticos (el fix AZERTY con `digitCode`/`code:10…19`), la decisión de no instalar
waybar/mako y un índice de capturas.

**[Hecho]** Las licencias importan porque el rice mezcla assets de terceros:

| Asset | Licencia / uso | Fuente |
|---|---|---|
| Noctalia | MIT | [README](sources/2026-11-21-noctalia-readme.md) — https://github.com/noctalia-dev/noctalia/blob/main/README.md |
| Bibata Cursor (Bibata-Modern-Ice) | proyecto open source con licencia propia | [README](sources/2026-11-21-bibata-readme.md) — https://github.com/ful1e5/Bibata_Cursor/blob/main/README.md |
| Nerd Fonts (Fantasque/Meslo) | licencias upstream de cada fuente; verificar antes de redistribuir | [README](sources/2026-11-21-nerd-fonts-readme.md) — https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md |
| Catppuccin (esquemas micro) | licencia del proyecto Catppuccin | [README](sources/2026-11-21-catppuccin-readme.md) — https://github.com/catppuccin/catppuccin/blob/main/README.md |
| adw-gtk3 | GPL-3.0-or-later (tema) | [README](sources/2026-11-21-adw-gtk3-readme.md) — https://github.com/lassekongo83/adw-gtk3/blob/main/README.md |
| Configs propios | recomendación: MIT o CC0 | decisión del usuario |

**[Hecho]** Los repos de dotfiles de terceros incluyen `LICENSE.md`, `CONTRIBUTING.md`
y guías de mensajes de commit
([JaKooLit](sources/2026-11-21-jakoolit-hyprland-dots.md) —
https://github.com/JaKooLit/Hyprland-Dots/blob/main/README.md). Copiar su estructura es
razonable, pero no copiar su contenido sin atribución. Guarda `licenses/` con el texto de cada
asset redistribuido y un `THIRD_PARTY.md` que diga de dónde viene cada tema.

---

## 10. Plan de migración en 5 pasos

1. **Inventario y saneado (día 1, ~30 min).** Copiar `~/.config/hypr`, `noctalia`,
   `kitty`, `alacritty`, `gtk`, `qt6ct`, `fish` a `~/dotfiles/` manteniendo la ruta
   `.config/…`. Escribir `.gitignore` con la tabla del §2. Ejecutar `pacman -Q`,
   `-Qqe`, `-Qm` hacia `system/packages/`. Verificar que no hay secretos:
   `rg -i 'token|password|api[_-]?key' ~/dotfiles`.

2. **Elegir herramienta e inicializar (día 1, ~20 min).** `sudo pacman -S git stow`;
   `git init` en `~/dotfiles`; `stow -n hypr` (dry-run) y corregir directorios que ya
   existen moviéndolos a `~/.config-backup-<fecha>`; aplicar `stow`. Confirmar con
   `readlink -f ~/.config/hypr/hyprland.lua`.

3. **Primera versión etiquetada (día 2).** `scripts/check-configs.fish` + hook
   `pre-push`; `git add -A && git commit -m "bootstrap: CachyOS + Hyprland 0.57.2"`;
   `git tag v1.0.0`; `git remote add origin …` y `git push -u origin main --tags`.
   El tag es el punto de restore conocido.

4. **Validación en caliente (día 2–3).** Cambiar un valor menor (p. ej. `gaps_out`),
   guardar, comprobar recarga automática, ejecutar `hyprctl configerrors` y
   `noctalia config validate`. Probar `stow -D hypr && stow hypr` y verificar que la
   sesión vuelve al mismo estado. Anotar en `README.md` los dos avisos (AZERTY y
   doble paleta).

5. **Restore de prueba y mantenimiento (día 3 y continuo).** En un usuario nuevo o una
   VM: clonar, `stow -n`, `stow`, `pacman -S --needed - < pacman-explicit.txt`, validar.
   Si funciona, el sistema está cerrado. Regla de oro: **todo cambio en `~/.config`
   se copia al repo y se commitea el mismo día**; el `backup` nunca es una tarea
   pendiente para "cuando tenga tiempo".

---

## 11. Fuentes citadas

- [ArchWiki · Hyprland](sources/2026-11-21-archwiki-hyprland.md) — https://wiki.archlinux.org/title/Hyprland
- [Hyprland Releases](sources/2026-11-21-hyprland-releases.md) — https://github.com/hyprwm/Hyprland/releases
- [JaKooLit · Hyprland-Dots README](sources/2026-11-21-jakoolit-hyprland-dots.md) — https://github.com/JaKooLit/Hyprland-Dots/blob/main/README.md
- [Noctalia · README](sources/2026-11-21-noctalia-readme.md) — https://github.com/noctalia-dev/noctalia/blob/main/README.md
- [Hyprland Wiki · Must-have utilities](sources/2026-11-21-hyprland-must-have.md) — https://wiki.hypr.land/useful-utilities/must-have/
- [Hyprland Wiki · Using hyprctl](https://wiki.hypr.land/configuring/core/advanced-configuration/using-hyprctl/) (sin copia local)
- [GNU Stow manual](https://www.gnu.org/software/stow/manual/stow.html) (sin copia local)
- [chezmoi documentation](https://www.chezmoi.io/) (sin copia local)
- [Hyprland Wiki · Home Manager](https://wiki.hypr.land/nix/configuring-hyprland-with-home-manager/) (sin copia local)
- [Ansible documentation](https://docs.ansible.com/) (sin copia local)
- [adw-gtk3 · README](sources/2026-11-21-adw-gtk3-readme.md) — https://github.com/lassekongo83/adw-gtk3/blob/main/README.md
- [Bibata Cursor · README](sources/2026-11-21-bibata-readme.md) — https://github.com/ful1e5/Bibata_Cursor/blob/main/README.md
- [Nerd Fonts · README](sources/2026-11-21-nerd-fonts-readme.md) — https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md
- [Catppuccin · README](sources/2026-11-21-catppuccin-readme.md) — https://github.com/catppuccin/catppuccin/blob/main/README.md

*Datos locales: `00-perfil-del-sistema.md`, `apendices/paquetes-instalados.txt`,
`configuracion-actual/`, repos clonados en `repositorios/`. Comandos ejecutados el
2026-11-21: `pacman -Q | wc -l` → 1232, `pacman -Qqe | wc -l` → 182, `pacman -Qm | wc -l`
→ 0, `pacman -Qdtq | wc -l` → 0, `hyprland --verify-config` → `config ok`,
`noctalia config validate` → `✓ Config is valid`.*
