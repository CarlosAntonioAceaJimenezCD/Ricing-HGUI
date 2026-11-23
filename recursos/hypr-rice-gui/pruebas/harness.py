#!/usr/bin/env python3
"""Laboratorio de pruebas extremas para Ricing HGUI.

Todo se ejecuta sobre un árbol temporal: ninguna prueba toca ~/.config real.
Los módulos se importan y se parchean sus constantes de ruta.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path.home() / "ricing/recursos/hypr-rice-gui"))

import config_model as cm
import keybinds as kb
import apps as ap
import compact_rules as cr
import monitors as mon
import wallpapers as wp
import sharing as sh
import backup_manager as bm

TMP = Path(os.environ.get("HGUI_LAB", "/tmp/opencode/hgui-lab/work"))
if TMP.exists():
    shutil.rmtree(TMP)
TMP.mkdir(parents=True)
(TMP / "hypr/config").mkdir(parents=True)
(TMP / "backups").mkdir()
(TMP / "downloads").mkdir()
(TMP / "imports").mkdir()
(TMP / "out").mkdir()

# ------------------------------------------------------------------ aislamiento
cm.STATE_FILE = TMP / "hypr/config/ui-settings.lua"
cm.NOCTALIA_FILE = TMP / "noctalia.toml"
cm.NOCTALIA_FILE.write_text("[theme]\nmode = \"dark\"\n[bar.default]\nthickness = 34\n", encoding="utf-8")

kb.DATA = TMP / "keybinds.json"
kb.LUA_MODULE = TMP / "hypr/config/ui-bindings.lua"
kb.SOURCE_BINDS = TMP / "hypr/config/binds.lua"
kb.SOURCE_VARS = TMP / "hypr/config/variables.lua"

ap.VARS = TMP / "hypr/config/variables.lua"
ap.BINDS = TMP / "hypr/config/binds.lua"
ap.UWSM_ENV = TMP / "uwsm-env"
ap.UWSM_ENV.write_text("export TERMINAL=kitty\n", encoding="utf-8")

cr.DATA = TMP / "compact-rules.json"
cr.LUA = TMP / "hypr/config/ui-workspace-rules.lua"
cr.SOURCE_BINDS = TMP / "hypr/config/binds.lua"

mon.VARIABLES = TMP / "hypr/config/variables.lua"
mon.CONFIG_DIR = TMP / "hypr"

wp.DOWNLOADS = TMP / "downloads"

sh.OUT = TMP / "out"
sh.IMPORTADOS = TMP / "imports"
sh.BUNDLE_PATHS = [TMP / "hypr"]
# El laboratorio vive bajo /tmp/opencode: "opencode" está en EXCLUDED y
# descartaría todos los archivos; se ajusta sólo en el arnés.
sh.EXCLUDED = {"fish_variables", "keyrings", "cache", ".git"}

bm.APP_DIR = TMP / "app"
bm.BACKUP_DIR = TMP / "backups"
bm.SETTINGS_FILE = TMP / "app/settings.json"
bm.IDENTITIES_FILE = TMP / "app/identities.json"
bm.DEFAULT_TARGETS = (TMP / "hypr",)

# ------------------------------------------------------------------ utilidades
RESULTS: list[tuple[str, str, str]] = []
FAKE_CALLS: list[list[str]] = []
FAKE_MODE = {"mode": "ok"}


def fake_hyprctl(*args: str) -> str:
    FAKE_CALLS.append(list(args))
    if FAKE_MODE["mode"] == "fail":
        return ""
    if args[:1] == ("binds",):
        return json.dumps([
            {"modmask": 65, "key": "", "keycode": 10, "dispatcher": "HL.Dispatcher(focus)",
             "arg": "1", "description": "ir 1", "repeat": False, "locked": False},
            {"modmask": 65, "key": "F35", "keycode": 0, "dispatcher": "HL.Dispatcher(exec_cmd)",
             "arg": "btop", "description": "btop", "repeat": False, "locked": False},
            {"modmask": 384, "key": "mouse:275", "keycode": 0, "dispatcher": "HL.Dispatcher(exec_cmd)",
             "arg": "x", "description": "", "repeat": True, "locked": False},
            {"modmask": 0, "key": None, "keycode": 0, "dispatcher": "", "arg": "", "description": ""},
        ])
    return "ok"


kb.hyprctl = fake_hyprctl


def run(name: str, fn) -> None:
    try:
        out = fn()
        RESULTS.append((name, "PASS", repr(out)[:120]))
    except Exception as exc:  # noqa: BLE001 - el laboratorio debe capturar todo
        RESULTS.append((name, "EXC", f"{type(exc).__name__}: {exc}"[:160]))


def expect_raises(name: str, fn, types=(Exception,)) -> None:
    try:
        fn()
    except types as exc:
        RESULTS.append((name, "RAISES", f"{type(exc).__name__}: {exc}"[:160]))
    except Exception as exc:  # noqa: BLE001
        RESULTS.append((name, "EXC-RARO", f"{type(exc).__name__}: {exc}"[:160]))
    else:
        RESULTS.append((name, "NO-RAISES", "debería fallar y no falló"))


def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


# ================================================================== config_model
def t_cm_extremos():
    vals = {
        "gaps_in": 9999, "gaps_out": -50, "border_size": 10**9,
        "active_opacity": float("nan"), "inactive_opacity": float("inf"),
        "blur_passes": 100, "accel_profile": "flat", "vrr": "3",
        "blur_variant": 99, "no_hardware_cursors": 2,
    }
    code = cm.build_hypr_config(vals)
    assert "gaps_in = 9999" not in code, "gaps_out no se recortó al rango"
    assert "nan" not in code and "inf" not in code, "valor no finito generado"
    assert "active_opacity = 0.0" in code, "opacidad no se recortó"
    return code


def t_cm_injection():
    code = cm.build_hypr_config({"accel_profile": 'flat")\nos.execute("touch /tmp/pwned") --'})
    return code


def t_cm_lua_escape():
    return cm._lua_value('a"b\\c\nd\te]]')


def t_cm_persist_sin_noctalia():
    cm.NOCTALIA_FILE = TMP / "no-existe.toml"
    try:
        cm.persist({"n_bar_thickness": 40})
    finally:
        cm.NOCTALIA_FILE = TMP / "noctalia.toml"


def t_cm_persist_toml_raro():
    write(TMP / "noctalia.toml", "[theme]\nmode = dark\n[theme]\nmode = light\n")
    cm.persist({"n_theme_mode": "light"})


def t_cm_snapshot_sin_hyprctl():
    orig = cm.subprocess.run

    class R:
        stdout = ""

    cm.subprocess.run = lambda *a, **k: R()
    try:
        out = cm.snapshot()
        assert out["gaps_in"] is None
    finally:
        cm.subprocess.run = orig


def t_cm_by_id_raro():
    assert cm.by_id("") is None
    assert cm.by_id("gaps_in") is not None
    assert cm.by_id("gaps_in\n") is None


# ================================================================== keybinds
def t_kb_normalize():
    casos = ["SUPER + SHIFT + code:10", "shift+super+code:10", "", "  +  ",
             "SUPER + + F35", "SUPER + HYPER + mouse:275"]
    return [kb.normalize_key(c) for c in casos]


def t_kb_action_vacia():
    kind, action = kb.action_from_ui(5, "")
    assert action == ""
    ok, msg = kb.apply_bind({"key": "SUPER + F35", "kind": kind, "action": action})
    # Con acción vacía ya no se envía nada a hyprctl (antes generaba Lua inválido).
    assert not ok and not FAKE_CALLS
    return ok, msg


def t_kb_key_vacia():
    return kb.apply_bind({"key": "", "kind": "exec", "action": "btop"})


def t_kb_key_inyectada():
    return kb.apply_bind({"key": 'SUPER + F35")\nos.execute("x") --', "kind": "exec", "action": "btop"})


def t_kb_lua_module_inyectado():
    write(kb.DATA, json.dumps([{
        "key": 'SUPER + F35")\nos.execute("touch /tmp/pwned") --',
        "kind": "exec", "action": 'btop")\nos.execute("touch /tmp/pwned2") --',
        "description": 'x"]\nos.execute("touch /tmp/pwned3") --',
    }]))
    kb._write_stored(json.loads(kb.DATA.read_text()))
    return kb.LUA_MODULE.read_text()


def t_kb_entry_sin_key():
    return kb.add_or_update({"kind": "exec", "action": "btop"})


def t_kb_stored_corrupto():
    write(kb.DATA, "{no es json")
    return kb.stored(), kb.check_conflict("SUPER + F35")


def t_kb_binds_json_raro():
    FAKE_MODE["mode"] = "raw"
    orig = kb.hyprctl
    kb.hyprctl = lambda *a: '{"modmask": "x"}' if a[:1] == ("binds",) else "ok"
    try:
        return kb.list_binds()
    finally:
        kb.hyprctl = orig
        FAKE_MODE["mode"] = "ok"


def t_kb_describe_locos():
    acciones = [
        "hl.dsp.exec_cmd(\"sh -c 'echo hola | cowsay'\")",
        "hl.dsp.window.move({workspace=\"special:scratch\"})",
        "hl.dsp.focus({monitor=\"DP-9\"})",
        "hl.dsp.group.toggle()",
        "hl.dsp.window.pin()",
        "hl.dsp.submap(\"resize\")",
        "hl.dsp.global(\"quickshell:launcher\")",
        "hl.dsp.send_shortcut({mods=\"SUPER\", key=\"Q\"})",
        "HL.Dispatcher(group:next) 1",
        "",
    ]
    return [kb.describe(a) for a in acciones]


def t_kb_conflicto_masivo():
    entries = [{"key": f"SUPER + {c}", "action": "btop", "description": "x"}
               for c in ("A", "B", "C", "D")]
    write(kb.DATA, json.dumps(entries))
    return kb.check_conflict("SUPER + C")


# ================================================================== apps
def t_ap_comandos_locos():
    casos = [
        "env FOO=bar firefox",
        "flatpak run org.mozilla.firefox",
        "sh -c 'echo \"hola mundo\"'",
        "fish -c 'cd /tmp; ls'",
        "firefox --private-window 'https://x.y/?a=1&b=2'",
        "~/bin/miapp --flag=1",
        "$HOME/bin/app",
        "app \u00f1and\u00fa",
        "app\nrm -rf /",
        'app"); os.execute("rm -rf /") --',
        "",
    ]
    return [ap.validate({"TERMINAL": c, "FILE_MANAGER": "dolphin", "BROWSER": "firefox",
                         "BROWSER_SECONDARY": "", "EDITOR": "nano", "CALCULATOR": "bc"})
            for c in casos]


def t_ap_write_newline():
    write(ap.VARS, 'TERMINAL = "kitty"\nBROWSER = "firefox"\nBROWSER_SECONDARY = ""\n'
                   'EDITOR = "nano"\nFILE_MANAGER = "dolphin"\nCALCULATOR = "bc"\n')
    return ap.write_apps({"TERMINAL": "kitty\nMALO = true", "FILE_MANAGER": "dolphin",
                          "BROWSER": "firefox", "BROWSER_SECONDARY": "",
                          "EDITOR": "nano", "CALCULATOR": "bc"}), ap.VARS.read_text()


def t_ap_write_inyeccion():
    write(ap.VARS, 'TERMINAL = "kitty"\nBROWSER = "firefox"\nBROWSER_SECONDARY = ""\n'
                   'EDITOR = "nano"\nFILE_MANAGER = "dolphin"\nCALCULATOR = "bc"\n')
    return ap.write_apps({"TERMINAL": 'kitty"); os.execute("touch /tmp/pwned") --',
                          "FILE_MANAGER": "dolphin", "BROWSER": "firefox",
                          "BROWSER_SECONDARY": "", "EDITOR": "nano", "CALCULATOR": "bc"}), \
        ap.VARS.read_text()


def t_ap_read_raro():
    write(ap.VARS, 'TERMINAL = "kitty \\"especial\\""\n-- BROWSER = "comentado"\n'
                   'BROWSER="firefox" # inline\nBROWSER_SECONDARY = "chromium --incognito"\n')
    return ap.read_apps()


def t_ap_secondary_falso_positivo():
    write(ap.BINDS, '-- BROWSER_SECONDARY estará aquí pronto\nhl.bind(mainMod .. " + Return", hl.dsp.exec_cmd(launchPrefix .. TERMINAL))\n')
    return ap.ensure_secondary_bind({"BROWSER_SECONDARY": "chromium"})


def t_ap_sync_env_comillas():
    write(ap.UWSM_ENV, "export TERMINAL=kitty\n")
    ap.sync_env({"TERMINAL": 'sh -c "echo hola"', "BROWSER": "firefox", "EDITOR": "nano"})
    return ap.UWSM_ENV.read_text()


# ================================================================== compact_rules
def t_cr_rangos_locos():
    out = []
    for start, end in ((1, 10), (0, 0), (-5, 2), (10, 1), (1, 99), (5, 5)):
        r = {"id": "focus_same", "mods": "SUPER", "family": "focus_same",
             "action": 'hl.dsp.focus({workspace="m~"..i})', "start": start, "end": end, "enabled": True}
        out.append((start, end, cr.rule_lua(r)))
    return out


def t_cr_monitores_locos():
    r = {"id": "move_mon", "mods": "SUPER + SHIFT + CTRL", "family": "move_mon",
         "action": "hl.dsp.window.move({monitor=ms[i]})", "start": 1, "end": 6, "enabled": True}
    return cr.rule_lua(r, ['DP-1"', "HDMI-A-1", "eDP-1"])


def t_cr_mods_locos():
    return [cr.build_script([{"id": "x", "mods": m, "family": "focus_same",
                              "action": "hl.dsp.focus({workspace=i})", "start": 1, "end": 2,
                              "enabled": True}], ["VGA-1"])
            for m in ("", "CTRL", "CONTROL", "SUPER + + ALT", "HYPER")]


def t_cr_all_keys_invertido():
    return cr.all_target_keys([{"mods": "SUPER", "start": 9, "end": 2}])


def t_cr_num_wpm_loco():
    out = []
    for val in ("0", "999", "-3", "abc"):
        write(cr.SOURCE_BINDS.parent / "variables.lua", f"NUM_WPM = {val}\n")
        out.append((val, cr.num_wpm()))
    return out


def t_cr_save_con_monitor_vacio():
    return cr.save_rules(cr.defaults([]), [])


# ================================================================== monitors
def t_mon_write_nombre_inyectado():
    write(mon.VARIABLES, 'MONITOR1 = ""\nMONITOR2 = ""\nMONITOR3 = ""\n')
    return mon.write_variables([{"name": 'DP-1")\nos.execute("touch /tmp/pwned") --'}])


def t_mon_sync_cero():
    write(mon.CONFIG_DIR / "config/variables.lua",
          'MONITOR1 = "VGA-1"\nMONITOR2 = ""\n-- MONITOR3 = "x"\n')
    write(mon.CONFIG_DIR / "config/binds.lua",
          'hl.bind("SUPER + SHIFT + 2", hl.dsp.window.move({ monitor = MONITOR2 }))\n')
    return mon.sync_monitor_config(0)


def t_mon_sync_seis():
    return mon.sync_monitor_config(6)


def t_mon_json_raro():
    orig = mon.subprocess.run

    class R:
        stdout = '[{"id": 1, "refreshRate": "nan", "scale": null}]'

    mon.subprocess.run = lambda *a, **k: R()
    try:
        return mon.list_monitors()
    finally:
        mon.subprocess.run = orig


# ================================================================== wallpapers
def t_wp_ratios():
    casos = [(0, 0), (1440, 900), (7680, 4320), (3440, 1440), (1080, 1920),
             (-1920, 1080), (1, 1), (3840, 1600)]
    return [(w, h, wp.ratio_filter(w, h)) for w, h in casos]


def t_wp_matches():
    casos = [("basura", 1920, 1080), ("0x0", 1920, 1080), ("8K", 1920, 1080),
             (" 1920 X 1080 ", 1920, 1080), ("1920x1080", 0, 0),
             ("1080x1920", 1920, 1080), ("32x9", 5120, 1440)]
    return [(r, wp.matches_ratio(r, w, h)) for r, w, h in casos]


def t_wp_download_traversal():
    item = {"id": "../../../../tmp/opencode/hgui-lab/EVIL", "url": "file:///etc/hostname",
            "provider": "x", "path": ""}
    return wp.download(item)


def t_wp_download_url_local():
    p = TMP / "local.jpg"
    p.write_bytes(b"x" * 6000)
    return wp.download({"path": str(p), "url": "", "id": "a", "provider": "Local"})


def t_wp_unsplash_headers():
    return wp.search_unsplash("montaña", "clave-falsa", 3, 1920, 1080)


def t_wp_pexels_headers():
    return wp.search_pexels("montaña", "clave-falsa", 3, 1920, 1080)


def t_wp_query_loca():
    return wp.search_wallhaven("gótico & cyberpunk \"neón\" <script>", 2, 0, 0)


# ================================================================== sharing
def t_sh_import_ext():
    return sh.import_repo("ext::sh -c 'touch /tmp/opencode/hgui-lab/PWNED'")


def t_sh_import_file():
    return sh.import_repo("file:///etc")


def t_sh_import_flag():
    return sh.import_repo("--upload-pack=touch /tmp/opencode/hgui-lab/PWNED2")


def t_sh_import_vacio():
    return sh.import_repo("")


def t_sh_bundle_symlink():
    target = TMP / "hypr/secreto.txt"
    write(target, "TOKEN=super-secreto\n")
    link = TMP / "hypr/enlace"
    if link.exists() or link.is_symlink():
        link.unlink()
    link.symlink_to("/etc/hostname")
    ok, msg = sh.create_bundle()
    if not ok:
        return ok, msg
    import zipfile
    z = sorted(sh.OUT.glob("rice-*.zip"))[-1]
    with zipfile.ZipFile(z) as zf:
        names = zf.namelist()
        assert "hypr/enlace" not in names, "symlink incluido en el ZIP"
        assert "hypr/secreto.txt" in names, "archivo normal no incluido"
        return names


def t_sh_token_none():
    return sh.publish_gist(None, "x", False)


# ================================================================== backup
def t_bm_delete_traversal():
    fuera = TMP / "FUERA.tar.gz"
    fuera.write_bytes(b"x")
    return bm.delete_backup("../FUERA.tar.gz"), fuera.exists()


def t_bm_restore_prefix():
    # Miembro que escapa por prefijo: .restore-X-evil empieza por .restore-X
    import tarfile
    arch = bm.BACKUP_DIR / "backup-20260101-000000-evil.tar.gz"
    man = {"created_at": "2026-01-01T00:00:00+00:00", "reason": "evil",
           "file_count": 1, "files": [{"path": "tmp/opencode/hgui-lab/work/HACK", "sha256": "x"}],
           "protected": False, "partial": False, "base": ""}
    with tarfile.open(arch, "w:gz") as t:
        import io
        data = json.dumps(man).encode()
        info = tarfile.TarInfo("manifest.json")
        info.size = len(data)
        t.addfile(info, io.BytesIO(data))
        payload = b"hack"
        info2 = tarfile.TarInfo("data/tmp/opencode/hgui-lab/work/HACK")
        info2.size = len(payload)
        t.addfile(info2, io.BytesIO(payload))
    try:
        return bm.restore_backup(arch.name)
    finally:
        pass


def t_bm_next_due_raro():
    write(bm.SETTINGS_FILE, json.dumps({"auto_backup": True, "interval_minutes": "mucho"}))
    return bm.next_due()


def t_bm_manifest_corrupto():
    arch = bm.BACKUP_DIR / "backup-20260102-000000-roto.tar.gz"
    arch.write_bytes(b"no soy un tar")
    return bm.list_backups(), bm.verify_backup(arch.name), bm.get_backup_details(arch.name)


# ================================================================== main (lógica pura)
def t_main_import():
    import ast
    src = (Path.home() / "ricing/recursos/hypr-rice-gui/main.py").read_text(encoding="utf-8")
    ast.parse(src)
    return "main.py parsea"


# ================================================================== ejecución
PRUEBAS = [
    ("cm/extremos sin validar", t_cm_extremos),
    ("cm/injection enum", t_cm_injection),
    ("cm/escape lua", t_cm_lua_escape),
    ("cm/persist noctalia ausente", t_cm_persist_sin_noctalia),
    ("cm/persist toml duplicado", t_cm_persist_toml_raro),
    ("cm/snapshot sin hyprctl", t_cm_snapshot_sin_hyprctl),
    ("cm/by_id raro", t_cm_by_id_raro),
    ("kb/normalize", t_kb_normalize),
    ("kb/acción vacía", t_kb_action_vacia),
    ("kb/key vacía", t_kb_key_vacia),
    ("kb/key inyectada", t_kb_key_inyectada),
    ("kb/lua module inyectado", t_kb_lua_module_inyectado),
    ("kb/entry sin key", t_kb_entry_sin_key),
    ("kb/stored corrupto", t_kb_stored_corrupto),
    ("kb/binds json raro", t_kb_binds_json_raro),
    ("kb/describe locos", t_kb_describe_locos),
    ("kb/conflicto masivo", t_kb_conflicto_masivo),
    ("ap/comandos locos", t_ap_comandos_locos),
    ("ap/write newline", t_ap_write_newline),
    ("ap/write inyección", t_ap_write_inyeccion),
    ("ap/read raro", t_ap_read_raro),
    ("ap/secondary falso positivo", t_ap_secondary_falso_positivo),
    ("ap/sync env comillas", t_ap_sync_env_comillas),
    ("cr/rangos locos", t_cr_rangos_locos),
    ("cr/monitores locos", t_cr_monitores_locos),
    ("cr/mods locos", t_cr_mods_locos),
    ("cr/all keys invertido", t_cr_all_keys_invertido),
    ("cr/num wpm loco", t_cr_num_wpm_loco),
    ("cr/save monitor vacío", t_cr_save_con_monitor_vacio),
    ("mon/write nombre inyectado", t_mon_write_nombre_inyectado),
    ("mon/sync cero", t_mon_sync_cero),
    ("mon/sync seis", t_mon_sync_seis),
    ("mon/json raro", t_mon_json_raro),
    ("wp/ratios", t_wp_ratios),
    ("wp/matches", t_wp_matches),
    ("wp/download traversal", t_wp_download_traversal),
    ("wp/download local", t_wp_download_url_local),
    ("wp/unsplash headers", t_wp_unsplash_headers),
    ("wp/pexels headers", t_wp_pexels_headers),
    ("wp/query loca", t_wp_query_loca),
    ("sh/import ext", t_sh_import_ext),
    ("sh/import file", t_sh_import_file),
    ("sh/import flag", t_sh_import_flag),
    ("sh/import vacío", t_sh_import_vacio),
    ("sh/bundle symlink", t_sh_bundle_symlink),
    ("sh/token none", t_sh_token_none),
    ("bm/delete traversal", t_bm_delete_traversal),
    ("bm/restore prefijo", t_bm_restore_prefix),
    ("bm/next due raro", t_bm_next_due_raro),
    ("bm/manifest corrupto", t_bm_manifest_corrupto),
    ("main/parse", t_main_import),
]

for nombre, fn in PRUEBAS:
    run(nombre, fn)

ancho = max(len(n) for n, _, _ in RESULTS)
for nombre, estado, detalle in RESULTS:
    print(f"{estado:9} {nombre:<{ancho}}  {detalle}")
print(f"\nTotal: {len(RESULTS)} · PASS {sum(1 for _, e, _ in RESULTS if e == 'PASS')} "
      f"· EXC {sum(1 for _, e, _ in RESULTS if e == 'EXC')} "
      f"· RAISES {sum(1 for _, e, _ in RESULTS if e == 'RAISES')}")
