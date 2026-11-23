#!/usr/bin/env python3
"""Ronda 2: sintaxis Lua generada, tipos raros y TAR hostil."""
from __future__ import annotations

import contextlib
import io
import json
import os
import subprocess
import tarfile
from pathlib import Path

# El arnés base prepara el árbol aislado y las constantes parcheadas.
with contextlib.redirect_stdout(io.StringIO()):
    import harness as h

cm, kb, ap, cr, mon, wp, sh, bm = h.cm, h.kb, h.ap, h.cr, h.mon, h.wp, h.sh, h.bm
TMP, write, run = h.TMP, h.write, h.run

RES = []


def check(name, fn):
    try:
        out = fn()
        RES.append((name, "PASS", repr(out)[:110]))
    except Exception as exc:  # noqa: BLE001
        RES.append((name, "EXC", f"{type(exc).__name__}: {exc}"[:150]))


def luac(code: str, tag: str):
    p = TMP / f"check-{tag}.lua"
    p.write_text(code, encoding="utf-8")
    r = subprocess.run(["luac", "-p", str(p)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr.strip()[:200]
    return f"luac ok ({len(code)} chars)"


# ---------------------------------------------------------- 1. Lua generado
def r_lua_keybinds():
    write(kb.DATA, json.dumps([
        {"key": 'SUPER + F35"); os.execute("touch /tmp/PWN") --', "kind": "exec",
         "action": 'btop"); os.execute("touch /tmp/PWN2") --',
         "description": 'mal\n-- os.execute("touch /tmp/PWN3")'},
        {"key": "SUPER + A", "kind": "lua", "action": "hl.dsp.window.close()\nos.execute('x')"},
        {"key": "SUPER + B", "kind": "lua", "action": "hl.dsp.window.close()",
         "old_key": 'X"); os.execute("x") --'},
        {"key": "", "kind": "exec", "action": "x"},
        "no soy un dict",
        None,
    ]))
    entries = kb.stored()
    kb._write_stored(entries)
    text = kb.LUA_MODULE.read_text(encoding="utf-8")
    assert "PWN" not in text, "inyección en ui-bindings.lua"
    return luac(text, "binds")


def r_lua_compact():
    rules = [
        {"id": "x", "mods": 'SUPER"); os.execute("touch /tmp/PWN") --',
         "family": "focus_same", "action": 'hl.dsp.focus({workspace=i})\nos.execute("x")',
         "start": -999, "end": 999, "enabled": True},
        {"id": "m", "mods": "SUPER + HYPER", "family": "move_mon",
         "action": "hl.dsp.window.move({monitor=ms[i]})", "start": -5, "end": 99, "enabled": True},
        {"id": "d", "mods": "", "family": "focus_abs", "action": "", "start": 1, "end": 2, "enabled": True},
        {"id": "n", "mods": "SUPER", "family": "otra", "action": "hl.dsp.focus({workspace=i})",
         "start": "abc", "end": None, "enabled": False},
    ]
    mons = ['DP-1", os.execute("touch /tmp/PWN2") --', "HDMI-A-1", "eDP-1", "VGA-1",
            "DP-2", "DP-3", "DP-4", "DP-5", "DP-6", "DP-7", "DP-8"]
    script = cr.build_script(rules, mons)
    # El nombre malicioso aparece como TEXTO ESCAPADO dentro de una cadena Lua:
    # lo prohibido es que aparezca como código (sin las comillas escapadas).
    assert 'os.execute("touch /tmp/PWN2")' not in script, "inyección en ui-workspace-rules.lua"
    assert 'os.execute("touch /tmp/PWN")' not in script, "inyección en mods"
    return luac(script, "compact")


def r_lua_config_extremo():
    vals = {o.id: (float("nan") if o.kind == "float" else
                   10**12 if o.kind == "int" else
                   'x"); os.execute("pwn") --' if o.kind in {"enum", "color"} else
                   True if o.kind == "bool" else None)
            for o in cm.OPTIONS}
    code = cm.build_hypr_config(vals)
    assert "pwn" not in code and "nan" not in code
    return luac("local function f()\n" + code + "\nend", "config")


def r_lua_apps_monitores():
    write(ap.VARS, 'TERMINAL = "kitty"\nBROWSER = "firefox"\nBROWSER_SECONDARY = ""\n'
                   'EDITOR = "nano"\nFILE_MANAGER = "dolphin"\nCALCULATOR = "bc"\n')
    ok, msg = ap.write_apps({r: 'cmd"); os.execute("pwn") --\nMALO = 1' for r in ap.ROLES})
    assert not ok, "write_apps aceptó saltos de línea"
    ok, msg = ap.write_apps({r: 'cmd"); os.execute("pwn") --' for r in ap.ROLES})
    assert ok, msg
    assert "pwn" not in ap.VARS.read_text().replace('os.execute(\\"pwn\\")', "")
    r = subprocess.run(["luac", "-p", str(ap.VARS)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:200]
    ok, msg = mon.write_variables([{"name": "DP-1"}, {"name": " HDMI-A-1 "}])
    assert not ok, "nombre con espacio aceptado"
    return f"luac ok variables.lua ({msg})"


# ---------------------------------------------------------- 2. Tipos raros
def r_tipos_keybinds():
    out = [kb.normalize_key(None), kb.normalize_key(7), kb.normalize_key(["SUPER", "A"]),
           kb.describe(None, None), kb.describe(42, 7), kb.check_conflict(None),
           kb.apply_bind(None), kb.add_or_update(None), kb.set_disabled(None, True),
           kb.delete(None)]
    return out[:4]


def r_tipos_cm():
    out = [cm.clean_value(None, 1), cm.by_id(None), cm._lua_value(None),
           cm._lua_value(float("inf")), cm.build_hypr_config({}), cm.persist({"no_existe": 1})]
    return out[:4]


def r_tipos_rest():
    out = [ap.validate(None), ap.sync_env(None), ap.ensure_secondary_bind(None),
           cr.build_script(None, None), cr.all_target_keys(None, None),
           mon.write_variables(None), mon.list_monitors(),
           wp.ratio_filter(None, "x"), wp.matches_ratio(None, None, None),
           sh.publish_gist({"token": 1}, None, None), sh.get_readme(None),
           sh.open_browser("file:///etc/passwd"),
           bm.get_backup_details(123), bm.delete_backup(None),
           bm.verify_backup("../x"), bm.read_file_from_backup("x", "../../etc/passwd")]
    return out[:5]


# ---------------------------------------------------------- 3. TAR hostil
def r_tar_hostil():
    import io
    victim = TMP.parent / "PWN_TAR"
    rel = os.path.relpath(victim, bm.BACKUP_DIR / "data")
    arch = bm.BACKUP_DIR / "backup-20990101-000000-hostil.tar.gz"
    man = {"created_at": "2099-01-01T00:00:00+00:00", "reason": "hostil",
           "file_count": 1, "files": [{"path": f"data/{rel}", "sha256": "x"}],
           "protected": False, "partial": False, "base": ""}
    with tarfile.open(arch, "w:gz") as t:
        data = json.dumps(man).encode()
        info = tarfile.TarInfo("manifest.json")
        info.size = len(data)
        t.addfile(info, io.BytesIO(data))
        mal = tarfile.TarInfo(f"data/{rel}")
        payload = b"hack"
        mal.size = len(payload)
        t.addfile(mal, io.BytesIO(payload))
        link = tarfile.TarInfo("data/enlace")
        link.type = tarfile.SYMTYPE
        link.linkname = "/etc/hostname"
        t.addfile(link)
    ok, msg = bm.restore_backup(arch.name)
    assert not (TMP.parent / "PWN_TAR").exists(), "traversal en restore"
    return ok, msg[:80]


def r_bundle_symlink_hostil():
    outside = TMP / "secreto-fuera.txt"
    write(outside, "CLAVE=secreta\n")
    link = TMP / "hypr/enlace-hostil"
    if link.exists() or link.is_symlink():
        link.unlink()
    link.symlink_to(outside)
    ok, msg = sh.create_bundle()
    assert ok, msg
    import zipfile
    z = sorted(sh.OUT.glob("rice-*.zip"))[-1]
    with zipfile.ZipFile(z) as zf:
        names = zf.namelist()
        assert not any("enlace" in n for n in names), "symlink en el bundle"
        for n in names:
            assert b"CLAVE=secreta" not in zf.read(n), "secreto filtrado"
    return f"{len(names)} entradas, sin symlinks"


# ---------------------------------------------------------- 4. Persistencia TOML
def r_toml_missing_section():
    write(cm.NOCTALIA_FILE, "[theme]\nmode = \"dark\"\n")
    cm.persist({"n_bar_thickness": 42, "n_show_labels": True, "n_ui_scale": float("nan")})
    import tomllib
    data = tomllib.loads(cm.NOCTALIA_FILE.read_text(encoding="utf-8"))
    assert data["bar"]["default"]["thickness"] == 42
    assert data["widget"]["workspaces"]["show_labels"] is True
    assert data["accessibility"]["ui_scale"] == 0.5
    return data


PRUEBAS = [
    ("r2/lua ui-bindings hostil", r_lua_keybinds),
    ("r2/lua compact rules hostil", r_lua_compact),
    ("r2/lua config 46 extremos", r_lua_config_extremo),
    ("r2/lua apps+monitores", r_lua_apps_monitores),
    ("r2/tipos keybinds", r_tipos_keybinds),
    ("r2/tipos config_model", r_tipos_cm),
    ("r2/tipos resto", r_tipos_rest),
    ("r2/tar hostil", r_tar_hostil),
    ("r2/bundle symlink hostil", r_bundle_symlink_hostil),
    ("r2/TOML secciones nuevas", r_toml_missing_section),
]

for nombre, fn in PRUEBAS:
    check(nombre, fn)

ancho = max(len(n) for n, _, _ in RES)
for nombre, estado, detalle in RES:
    print(f"{estado:5} {nombre:<{ancho}}  {detalle}")
print(f"\nRonda 2: {len(RES)} · PASS {sum(1 for _, e, _ in RES if e == 'PASS')} "
      f"· EXC {sum(1 for _, e, _ in RES if e == 'EXC')}")
