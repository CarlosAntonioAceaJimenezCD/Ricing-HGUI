# Laboratorio de estrés creativo

Dos arneses **aislados** (no tocan `~/.config` ni `~/.local/share` reales) que
someten cada módulo de la GUI a entradas deliberadamente absurdas:

```bash
cd recursos/hypr-rice-gui/pruebas
python3 harness.py   # ronda 1: 51 casos
python3 round2.py    # ronda 2: 10 casos (importa harness.py)
```

`harness.py` parchea las constantes de ruta de los módulos para trabajar bajo
`/tmp/opencode/hgui-lab/work` y simula `hyprctl`. `round2.py` additionally
valida además con `luac -p` todo el Lua generado.

## Resultado

| Ronda | Casos | Excepciones | Sintaxis Lua |
|---|---:|---:|---|
| 1 · robustez y security | 51 | 0 | — |
| 2 · Lua hostil, tipos raros y TAR malicioso | 10 | 0 | `luac -p` ok |

**Total: 61/61.** `hyprland --verify-config` → `config ok`; la GUI arranca sin
tracebacks (sólo los avisos conocidos de Vulkan y `Gtk.ComboBoxText`).

## Lo que se intentó romper (y ahora se soporta)

- `config_model.py`: NaN/Inf, `gaps_in=9999`, `border_size=10**9`, enums
  inyectados, archivo Noctalia ausente, TOML duplicado, secciones/claves nuevas.
  Los numéricos se recortan al rango declarado; los enums desconocidos se omiten;
  las cadenas se escapan para Lua y TOML.
- `keybinds.py`: tecla vacía, acción vacía, `old_key` con `"); os.execute(...)`,
  descripciones con saltos de línea, JSON corrupto, `hyprctl binds -j` con un
  objeto en vez de una lista, `modmask` como texto, `key=None`, tipos no string.
  Todo lo que llega a `hl.bind`/`hl.unbind` se valida y se escapa.
- `apps.py`: comandos con comillas, `~/bin`, `$HOME`, unicode, nueva línea,
  inyección Lua, valores parciales (ya no borran los roles no enviados),
  `uwsm-env` con `sh -c "…"` (ahora citado con `shlex.quote`), comentario con
  `BROWSER_SECONDARY` que impedía añadir el bind.
- `compact_rules.py`: `start=-999`, `end=999`, `start="abc"`, mods vacíos o
  maliciosos, 11 monitores con comillas, action con salto de línea, reglas
  desactivadas. Se sanea todo y se valida el Lua resultante con `luac -p`.
- `monitors.py`: JSON con `refreshRate="nan"`/`scale=null`, `activeWorkspace`
  nulo, nombres de conector con comillas o espacios (rechazados), y
  `sync_monitor_config(0)` que antes comentaba también `MONITOR1..3` en
  `variables.lua` y dejaba el rice sin arrancar.
- `wallpapers.py`: `0x0` → ZeroDivisionError, proporciones negativas, URLs
  `file://`, ids con `../../..`, cabeceras de Unsplash/Pexels (antes `_curl` no
  las aceptaba), respuestas de API que no son listas.
- `sharing.py`: `ext::sh …`, `file://`, `--upload-pack=…` (antes se pasaban a
  `git clone`), token `None`, URL `file://` a `xdg-open`, symlinks en el ZIP y
  rutas fuera de `$HOME`. Ahora sólo http(s), `--` delante de la URL, y los
  symlinks se excluyen del bundle.
- `backup_manager.py`: `delete_backup("../FUERA.tar.gz")` borraba fuera del
  directorio, nombres de backup con `/`, miembros TAR con `../` y con prefijo
  `.restore-X-evil`, `interval_minutes="mucho"`, manifiestos corruptos. Se
  centralizó `_archive_path()`, se usa `Path.is_relative_to()` y
  `tar.extractall(..., filter="data")`.

## Notas

- Los casos de red usan claves falsas: no se llama a GitHub, Unsplash ni Pexels.
- Los parches son mínimos y están comentados con `AUDITORÍA` en cada módulo.
- Para repetir tras cambios: `python3 -m py_compile *.py && python3 pruebas/harness.py && python3 pruebas/round2.py`.
