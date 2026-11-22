#!/usr/bin/env python3
# =============================================================================
# AUDITORÍA · main.py — punto de entrada de la GUI Ricing HGUI
# -----------------------------------------------------------------------------
# Qué hace: construye una ventana GTK4/libadwaita con pestañas y delega la
# lógica a módulos pequeños (backup_manager, config_model, keybinds, monitors,
# wallpapers). NO contiene lógica de negocio duplicada: toda opción proviene de
# config_model y todo guardado pasa por backup_manager.
#
# Efectos externos:
#   - ejecuta `hyprctl` (eval/getoption/monitors/binds) vía los módulos;
#   - escribe ~/.config/hypr/config/ui-settings.lua y ui-bindings.lua;
#   - escribe ~/.config/noctalia/config.toml al guardar opciones de Noctalia;
#   - descarga wallpapers a ~/Imágenes/ricing-wallpapers;
#   - crea backups en ~/.local/share/hypr-rice-gui/backups.
# Seguridad: no usa root, no lee secretos, no ejecuta código remoto; todas las
# acciones son locales salvo la API pública de Wallhaven.
# Invariante: `pending`/`dirty` son la única fuente de cambios sin guardar.
# =============================================================================
"""Prototipo de GUI de ricing para Hyprland 0.57 + Noctalia.

- Vista previa EN VIVO con hyprctl eval + hl.config (sintaxis de 0.57).
- El botón "Guardar" sólo persiste la configuración (con backup).
- Backups automáticos, historial de puntos en el pasado e identidad Config DNA.
- Navegación por categorías mediante pestañas.

Requisitos: python3, python-gobject, gtk4, libadwaita (ya en CachyOS).
Ejecutar: python3 main.py
"""
import gettext
import os
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
gi.require_version("GLib", "2.0")
gi.require_version("Gdk", "4.0")
from gi.repository import Adw, Gdk, GLib, Gtk  # noqa: E402

import backup_manager as bm  # noqa: E402
import config_model as cm  # noqa: E402
import keybinds as kb  # noqa: E402
import monitors as mon  # noqa: E402
import wallpapers as wp  # noqa: E402
import wallpaper_engine as we  # noqa: E402
import sharing as sh  # noqa: E402

gettext.bindtextdomain("hypr-rice-gui", os.path.expanduser("~/.local/share/locale"))
gettext.textdomain("hypr-rice-gui")
_ = gettext.gettext

_timer_id: int | None = None


# --------------------------------------------------------------------------- widgets
def make_button(label: str, callback, *args) -> Gtk.Button:
    b = Gtk.Button(label=label)
    b.connect("clicked", callback, *args)
    return b


def show_text_window(parent: Gtk.Window, title: str, text: str) -> None:
    win = Gtk.Window(title=title, transient_for=parent, default_width=760, default_height=520)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6,
                  margin_start=10, margin_end=10, margin_top=10, margin_bottom=10)
    view = Gtk.TextView()
    view.set_editable(False)
    view.set_monospace(True)
    view.get_buffer().set_text(text)
    scroll = Gtk.ScrolledWindow()
    scroll.set_child(view)
    scroll.set_vexpand(True)
    box.append(scroll)
    box.append(make_button(_("Cerrar"), lambda _b: win.close()))
    win.set_child(box)
    win.present()


def new_tab(stack: Gtk.Stack, name: str, title: str) -> tuple[Gtk.Box, Adw.PreferencesPage]:
    outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12,
                    margin_start=16, margin_end=16, margin_top=16, margin_bottom=16)
    page = Adw.PreferencesPage()
    outer.append(page)
    stack.add_titled(outer, name, title)
    return outer, page


# --------------------------------------------------------------------------- app
def on_activate(app: Adw.Application) -> None:
    win = Adw.ApplicationWindow(application=app, title=_("Ricing HGUI"))
    win.set_default_size(1024, 820)
    settings = bm.get_settings()

    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
    switcher = Gtk.StackSwitcher()
    switcher.set_stack(stack)
    switcher.set_halign(Gtk.Align.CENTER)

    # AUDITORÍA: antes existía una pestaña "Apariencia" con slider de rounding y
    # switch de blur que duplicaban las opciones del modelo. Se eliminó; ahora
    # rounding y blur SIEMPRE se editan en la pestaña "Opciones" (categorías
    # "Decoración" y "Blur"). `status` se muestra allí.
    _opt_timer: int | None = None
    _ready = {"value": False}
    status = Gtk.Label(label=_("Ajusta las opciones: cambios en vivo"), margin_top=6, wrap=True)

    # ============ Pestaña 2: Backups ============
    _box_bk, page_bk = new_tab(stack, "backups", _("Backups"))
    bg = Adw.PreferencesGroup(
        title=_("Backups automáticos"),
        description=_("Copias de los dotfiles antes de cada cambio y de forma periódica."),
    )
    page_bk.add(bg)

    row_auto = Adw.ActionRow(title=_("Activados"), subtitle=_("Copiar configs periódicamente"))
    auto_switch = Gtk.Switch()
    auto_switch.set_active(bool(settings.get("auto_backup", True)))
    auto_switch.set_valign(Gtk.Align.CENTER)
    row_auto.add_suffix(auto_switch)
    bg.add(row_auto)

    row_int = Adw.ActionRow(title=_("Intervalo (minutos)"), subtitle=_("Cada cuánto se crea un backup"))
    spin_int = Gtk.SpinButton.new_with_range(1, 1440, 1)
    spin_int.set_value(int(settings.get("interval_minutes", 15)))
    spin_int.set_valign(Gtk.Align.CENTER)
    row_int.add_suffix(spin_int)
    bg.add(row_int)

    row_keep = Adw.ActionRow(title=_("Conservar últimos N"), subtitle=_("Los demás se borran solos"))
    spin_keep = Gtk.SpinButton.new_with_range(1, 100, 1)
    spin_keep.set_value(int(settings.get("keep_last", 10)))
    spin_keep.set_valign(Gtk.Align.CENTER)
    row_keep.add_suffix(spin_keep)
    bg.add(row_keep)

    # ============ Pestaña 3: Historial ============
    box_hist, page_hist = new_tab(stack, "historial", _("Historial"))
    hg = Adw.PreferencesGroup(
        title=_("Puntos en el pasado"),
        description=_("Selecciona cualquier copia para inspeccionarla, compararla o restaurarla."),
    )
    page_hist.add(hg)

    history_list = Gtk.ListBox()
    history_list.set_selection_mode(Gtk.SelectionMode.SINGLE)
    history_scroll = Gtk.ScrolledWindow()
    history_scroll.set_child(history_list)
    history_scroll.set_min_content_height(200)
    history_scroll.set_max_content_height(320)
    hg.add(history_scroll)

    detail = Gtk.Label(label=_("Selecciona un backup"), wrap=True)
    files_combo = Gtk.ComboBoxText()
    row_files = Adw.ActionRow(title=_("Archivos del backup"), subtitle=_("Elige uno para verlo"))
    row_files.add_suffix(files_combo)
    hg.add(row_files)

    backup_status = Gtk.Label(label="", wrap=True)
    selected: dict[str, str] = {}

    def populate_files(name: str) -> None:
        files_combo.remove_all()
        m = bm.get_backup_details(name) or {}
        for rec in m.get("files", []):
            files_combo.append_text(rec["path"])
        if m.get("files"):
            files_combo.set_active(0)

    def on_row_selected(_list: Gtk.ListBox, row: Gtk.ListBoxRow | None) -> None:
        if row is None:
            return
        name = row.get_name()
        selected["name"] = name
        selected["dna"] = bm.dna_of_backup(name) or ""
        b = next((x for x in bm.list_backups() if x["name"] == name), {})
        ident = bm.get_identity(selected["dna"])
        detail.set_label(
            f"{b.get('created_at', '').replace('T', ' ')[:19]} · {b.get('reason', '')} · "
            f"{b.get('file_count', 0)} archivos · {selected['dna']} · "
            f"{ident.get('label') or _('sin etiqueta')}"
        )
        populate_files(name)

    def refresh_history() -> None:
        history_list.remove_all()
        for b in bm.list_backups():
            row = Adw.ActionRow(
                title=b["created_at"].replace("T", " ")[:19],
                subtitle=f"{b['reason']} · {b['file_count']} archivos · {bm.dna_of_backup(b['name']) or ''}",
            )
            row.set_name(b["name"])
            row.set_activatable(True)
            history_list.append(row)
        if not bm.list_backups():
            detail.set_label(_("Sin backups todavía"))

    history_list.connect("row-selected", on_row_selected)

    def create_now(_btn: Gtk.Button) -> None:
        bm.create_backup(reason="manual")
        backup_status.set_label(_("Backup manual creado ✓"))
        refresh_history()

    def view_file(_btn: Gtk.Button) -> None:
        name = selected.get("name")
        idx = files_combo.get_active()
        if not name or idx < 0:
            backup_status.set_label(_("Selecciona un backup y un archivo"))
            return
        path = files_combo.get_active_text() or ""
        text = bm.read_file_from_backup(name, path)
        show_text_window(win, f"{name} · {path}", text or _("No se pudo leer el archivo"))

    def compare(_btn: Gtk.Button) -> None:
        name = selected.get("name")
        if not name:
            backup_status.set_label(_("Selecciona un backup"))
            return
        d = bm.compare_with_current(name)
        backup_status.set_label(
            _("Cambios: {n} modificados, {m} ausentes, {s} iguales").format(
                n=len(d["changed"]), m=len(d["missing"]), s=len(d["same"]))
        )

    def restore(_btn: Gtk.Button) -> None:
        name = selected.get("name")
        if not name:
            backup_status.set_label(_("Selecciona un backup"))
            return
        ok, msg = bm.restore_backup(name)
        backup_status.set_label(_("Restaurado: ") + msg if ok else _("Error: ") + msg)
        refresh_history()

    def delete(_btn: Gtk.Button) -> None:
        name = selected.get("name")
        if not name:
            return
        ok, msg = bm.delete_backup(name)
        backup_status.set_label(_("Eliminado") if ok else _("Error: ") + msg)
        refresh_history()

    hist_actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=8)
    for label, cb in [(_("Crear ahora"), create_now), (_("Ver archivo"), view_file),
                      (_("Comparar"), compare), (_("Restaurar"), restore), (_("Borrar"), delete)]:
        hist_actions.append(make_button(label, cb))
    hg.add(hist_actions)
    box_hist.append(detail)
    box_hist.append(backup_status)

    # ============ Pestaña 4: Identidad ============
    _box_id, page_id = new_tab(stack, "identidad", _("Identidad"))
    ig = Adw.PreferencesGroup(
        title=_("Identidad de la configuración"),
        description=_("Huella única (Config DNA) para reconocer y nombrar cada rice."),
    )
    page_id.add(ig)

    dna_now = bm.current_dna()
    ident_now = bm.get_identity(dna_now)
    ig.add(Adw.ActionRow(title=_("ID actual"),
                         subtitle=f"{dna_now} · {ident_now.get('label') or _('sin etiqueta')}"))

    label_entry = Gtk.Entry()
    label_entry.set_text(ident_now.get("label", ""))
    label_entry.set_placeholder_text(_("Ej. Rice azul minimal / Gaming"))
    row_label = Adw.ActionRow(title=_("Etiqueta"), subtitle=_("Se guarda para esta huella"))
    row_label.add_suffix(label_entry)
    ig.add(row_label)

    notes_entry = Gtk.Entry()
    notes_entry.set_text(ident_now.get("notes", ""))
    notes_entry.set_placeholder_text(_("Notas opcionales"))
    row_notes = Adw.ActionRow(title=_("Notas"), subtitle=_("Descripción del punto en el pasado"))
    row_notes.add_suffix(notes_entry)
    ig.add(row_notes)

    def save_identity(_btn: Gtk.Button) -> None:
        dna = selected.get("dna") or dna_now
        bm.set_identity_label(dna, label_entry.get_text().strip(), notes_entry.get_text().strip())
        status.set_label(_("Identidad guardada: ") + dna)
        refresh_history()

    def show_identity(_btn: Gtk.Button) -> None:
        dna = selected.get("dna") or dna_now
        inf = bm.identify_backup(selected["name"]) if selected.get("name") else {
            "dna": dna, "label": bm.get_identity(dna).get("label", ""),
            "notes": bm.get_identity(dna).get("notes", ""), "reason": "actual", "file_count": 0,
        }
        same = bm.find_backups_by_dna(dna)
        coincide = _("sí") if dna == bm.current_dna() else _("no")
        text = (
            f"DNA: {inf['dna']}\n"
            f"Etiqueta: {inf.get('label') or '(sin etiqueta)'}\n"
            f"Notas: {inf.get('notes') or '-'}\n"
            f"Motivo: {inf.get('reason', '-')}\n"
            f"Archivos: {inf.get('file_count', 0)}\n"
            f"Coincide con el estado actual: {coincide}\n"
            f"Backups con esta identidad ({len(same)}):\n  " + "\n  ".join(same) + "\n"
        )
        show_text_window(win, _("Identidad de configuración"), text)

    id_actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=8)
    id_actions.append(make_button(_("Guardar etiqueta"), save_identity))
    id_actions.append(make_button(_("Ver identidad"), show_identity))
    ig.add(id_actions)

    # ============ Pestaña 5: Opciones (modelo genérico) ============
    opt_outer, _opt_page = new_tab(stack, "opciones", _("Opciones"))
    opt_stack = Gtk.Stack()
    opt_sidebar = Gtk.StackSidebar()
    opt_sidebar.set_stack(opt_stack)
    opt_sidebar.set_size_request(195, -1)
    opt_stack.set_hexpand(True)
    opt_stack.set_vexpand(True)
    opt_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
    opt_hbox.append(opt_sidebar)
    opt_hbox.append(opt_stack)
    opt_hbox.set_hexpand(True)
    opt_hbox.set_vexpand(True)
    opt_outer.append(opt_hbox)

    pending = cm.snapshot()
    dirty: set[str] = set()
    opt_widgets: dict[str, tuple[object, object]] = {}

    # AUDITORÍA: el cambio se applying en vivo con un debounce de 150 ms.
    # Esto evita lanzar un `hyprctl eval` por cada píxel que se arrastra el slider.
    def schedule_option_live() -> None:
        nonlocal _opt_timer
        if not _ready["value"]:
            return
        if _opt_timer is not None:
            GLib.source_remove(_opt_timer)
        _opt_timer = GLib.timeout_add(150, apply_options_live)

    def apply_options_live() -> bool:
        nonlocal _opt_timer
        _opt_timer = None
        known = [(oid, cm.by_id(oid)) for oid in dirty]
        hypr = {oid: pending[oid] for oid, opt in known
                if opt is not None and opt.source == "hyprland" and pending.get(oid) is not None}
        if hypr:
            cm.apply_live(hypr)
        noct = sum(1 for oid, opt in known if opt is not None and opt.source == "noctalia")
        extra = f" · {noct} de Noctalia al guardar" if noct else ""
        status.set_label(_("Vista previa en vivo ✓") + extra)
        return False

    def mark_dirty(oid: str, value) -> None:
        if cm.by_id(oid) is None:
            return
        pending[oid] = value
        dirty.add(oid)
        schedule_option_live()

    def on_scale(scale_widget, oid: str, label: Gtk.Label, opt: cm.Option) -> None:
        raw = scale_widget.get_value()
        value = int(raw) if opt.kind == "int" else round(raw, 3)
        label.set_label(str(value))
        mark_dirty(oid, value)

    for category, opts in cm.categories().items():
        cat_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12,
                          margin_start=12, margin_end=12, margin_top=12, margin_bottom=12)
        cat_page = Adw.PreferencesPage()
        cat_box.append(cat_page)
        group_c = Adw.PreferencesGroup(title=category)
        cat_page.add(group_c)
        scroll_c = Gtk.ScrolledWindow()
        scroll_c.set_child(cat_box)
        scroll_c.set_hexpand(True)
        scroll_c.set_vexpand(True)
        scroll_c.set_min_content_width(620)
        cat_box.set_hexpand(True)
        opt_stack.add_titled(scroll_c, category, category)

        for opt in opts:
            value = pending.get(opt.id)
            subtitle = opt.path + (f" · {opt.note}" if opt.note else "")
            row = Adw.ActionRow(title=opt.label, subtitle=subtitle)

            if opt.kind == "bool":
                widget = Gtk.Switch()
                widget.set_active(bool(value))
                widget.set_valign(Gtk.Align.CENTER)
                widget.connect("notify::active",
                               lambda w, oid=opt.id: mark_dirty(oid, w.get_active()))
                row.add_suffix(widget)
                opt_widgets[opt.id] = (widget, row)

            elif opt.kind in ("int", "float"):
                widget = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL,
                                                  opt.minimum or 0, opt.maximum or 100, opt.step)
                widget.set_value(float(value if value is not None else (opt.minimum or 0)))
                widget.set_hexpand(True)
                widget.set_size_request(280, -1)
                value_label = Gtk.Label(label=str(value))
                value_label.set_size_request(56, -1)
                holder = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                holder.append(widget)
                holder.append(value_label)
                widget.connect("value-changed",
                               lambda w, oid=opt.id, lab=value_label, o=opt: on_scale(w, oid, lab, o))
                row.add_suffix(holder)
                opt_widgets[opt.id] = (widget, value_label)

            elif opt.kind == "enum":
                widget = Gtk.ComboBoxText()
                for choice in opt.choices:
                    widget.append_text(choice)
                try:
                    widget.set_active(list(opt.choices).index(str(value)))
                except ValueError:
                    widget.set_active(0)
                widget.connect("changed",
                               lambda w, oid=opt.id, o=opt: mark_dirty(
                                   oid, int(w.get_active_text()) if o.choices and o.choices[0].isdigit()
                                   else w.get_active_text()))
                row.add_suffix(widget)
                opt_widgets[opt.id] = (widget, row)

            else:  # color como texto
                widget = Gtk.Entry()
                widget.set_text(str(value or ""))
                widget.set_size_request(110, -1)
                widget.connect("changed", lambda w, oid=opt.id: mark_dirty(oid, w.get_text()))
                row.add_suffix(widget)
                opt_widgets[opt.id] = (widget, row)

            group_c.add(row)

    def save_options(_btn: Gtk.Button) -> None:
        bm.create_backup(reason="guardar-opciones")
        cm.persist(pending)
        dirty.clear()
        status.set_label(_("Opciones guardadas ✓"))
        refresh_history()

    opt_outer.append(status)
    opt_outer.append(make_button(_("Guardar todas las opciones"), save_options))

    # ============ Pestaña 6: Keybinds (carpetas + edición independiente) ============
    # AUDITORÍA: cada atajo tiene su propio modo edición (en su menú "…").
    # El modo "Añadir" elige primero la acción, luego captura la tecla (5 s)
    # y kb.describe() decide automáticamente la carpeta destino.
    kb_outer, kb_page = new_tab(stack, "keybinds", _("Keybinds"))
    kb_group = Adw.PreferencesGroup(
        title=_("Atajos activos"),
        description=_("Carpetas por categoría · puntos: activo/inactivo · menú «…»: editar o borrar."),
    )
    kb_page.add(kb_group)

    from gi.repository import Gio

    binds_cache: list[dict] = []
    stored_cache: list[dict] = []

    def reload_binds() -> None:
        nonlocal binds_cache, stored_cache
        binds_cache = kb.enriched_binds()   # cache: evita 14 ms por clic
        stored_cache = kb.stored()
        render_binds()

    def render_binds() -> None:
        for child in list(kb_group):
            if isinstance(child, Adw.ExpanderRow):
                kb_group.remove(child)
        por_cat: dict[str, list[dict]] = {}
        for b in binds_cache:
            label = b.get("source_key") or f"{b['mods']} + {b['key']}"
            action = b.get("source_action") or b["dispatcher"]
            cat, desc = kb.describe(action, b["dispatcher"])
            por_cat.setdefault(cat, []).append({"key": label, "desc": desc, "action": action})
        for cat, items in sorted(por_cat.items()):
            folder = Adw.ExpanderRow(title=cat, subtitle=_("{n} atajo(s)").format(n=len(items)))
            for it in items:
                key = it["key"]
                row = Adw.ActionRow(title=key, subtitle=it["desc"])
                saved = next((e for e in stored_cache if e.get("key") == key), None)
                disabled = bool(saved and saved.get("disabled"))

                box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=8)
                dot_on = Gtk.CheckButton()
                dot_on.set_tooltip_text(_("Activo"))
                dot_off = Gtk.CheckButton()
                dot_off.set_tooltip_text(_("Inactivo"))
                dot_on.set_active(not disabled)
                dot_off.set_active(disabled)

                def on_dot(widget, active_flag, other, k=key):
                    if widget.get_active():
                        if other.get_active():
                            other.set_active(False)
                        kb.set_disabled(k, not active_flag)
                        kb_status.set_label(_("Estado: ") + k)
                    elif not other.get_active():
                        other.set_active(True)

                dot_on.connect("toggled", lambda w, o=dot_off: on_dot(w, True, o))
                dot_off.connect("toggled", lambda w, o=dot_on: on_dot(w, False, o))
                box.append(dot_on)
                box.append(dot_off)

                menu = Gio.Menu()
                item_e = Gio.MenuItem.new(_("Editar atajo…"), "win.edit-bind")
                item_e.set_attribute_value("target", GLib.Variant("s", key))
                item_d = Gio.MenuItem.new(_("Borrar atajo"), "win.delete-bind")
                item_d.set_attribute_value("target", GLib.Variant("s", key))
                menu.append_item(item_e)
                menu.append_item(item_d)
                mb = Gtk.MenuButton(icon_name="open-menu-symbolic")
                mb.set_tooltip_text(_("Acciones de este atajo"))
                mb.set_popover(Gtk.PopoverMenu.new_from_model(menu))
                box.append(mb)
                row.add_suffix(box)
                folder.add_row(row)
            kb_group.add(folder)

    def delete_by_key(key: str) -> None:
        ok, msg = kb.delete(key)
        kb_status.set_label((_("Borrado: ") if ok else _("Error: ")) + key + " · " + msg)
        reload_binds()

    del_action = Gio.SimpleAction.new("delete-bind", GLib.VariantType.new("s"))
    del_action.connect("activate", lambda _a, param: delete_by_key(param.get_string()))
    win.add_action(del_action)

    # ---- captura temporizada reutilizable (5 s tras la última tecla) ----
    def start_capture(on_done) -> None:
        kb.notify_info(_("Ricing HGUI · Atajo"),
                       _("Pulsa la combinación. Se registrará 5 s después de la última tecla. Enter también vale."))
        dialog = Gtk.Window(title=_("Determinando atajo…"), transient_for=win,
                            default_width=440, default_height=130)
        label = Gtk.Label(label=_("Pulsa la combinación… 5 s tras la última tecla."), wrap=True)
        dialog.set_child(label)
        cap: dict = {"mods": set(), "key": "", "timer": None}

        def finish() -> bool:
            cap["timer"] = None
            orden = ("CTRL", "ALT", "SUPER", "SHIFT")
            partes = [m for m in orden if m in cap["mods"]]
            if cap["key"]:
                partes.append(cap["key"])
            combo = " + ".join(partes)
            if combo:
                label.set_label(_("Registrado: ") + combo)
                on_done(combo)
            dialog.close()
            return False

        def arm() -> None:
            if cap["timer"] is not None:
                GLib.source_remove(cap["timer"])
            cap["timer"] = GLib.timeout_add_seconds(5, finish)

        ctrl = Gtk.EventControllerKey()

        def on_key(_c, keyval: int, _code: int, state: int) -> bool:
            name = Gdk.keyval_name(keyval) or str(keyval)
            if name in {"Control_L", "Control_R"}:
                cap["mods"].add("CTRL")
            elif name in {"Alt_L", "Alt_R"}:
                cap["mods"].add("ALT")
            elif name in {"Super_L", "Super_R"}:
                cap["mods"].add("SUPER")
            elif name in {"Shift_L", "Shift_R"}:
                cap["mods"].add("SHIFT")
            else:
                cap["key"] = "Return" if name in {"Return", "KP_Enter", "Enter"} else name
            arm()
            return True

        ctrl.connect("key-pressed", on_key)
        dialog.add_controller(ctrl)
        dialog.present()

    # ---- diálogo de edición INDEPENDIENTE para un atajo ----
    def edit_dialog(key: str, action: str) -> None:
        d = Gtk.Window(title=_("Editar: ") + key, transient_for=win, default_width=520, default_height=430)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10,
                      margin_start=16, margin_end=16, margin_top=16, margin_bottom=16)
        d.set_child(box)

        key_entry = Gtk.Entry()
        key_entry.set_text(key)
        key_row = Adw.ActionRow(title=_("Atajo"), subtitle=_("Se vuelve a capturar con el botón inferior"))
        key_row.add_suffix(key_entry)
        box.append(key_row)

        combo = Gtk.ComboBoxText()
        for opt in (_("Ejecutar un programa"), _("Cerrar la ventana"),
                    _("Alternar ventana flotante"), _("Pantalla completa"),
                    _("Enviar mensaje a Noctalia"), _("Avanzado (expresión Lua)")):
            combo.append_text(opt)
        idx, param0 = kb.action_to_ui(action)
        combo.set_active(idx)
        kind_row = Adw.ActionRow(title=_("Qué hace"))
        kind_row.add_suffix(combo)
        box.append(kind_row)

        param = Gtk.Entry()
        param.set_text(param0)
        param_row = Adw.ActionRow(title=_("Datos"), subtitle=_("Programa / mensaje / parámetro"))
        param_row.add_suffix(param)
        box.append(param_row)

        status = Gtk.Label(label="", wrap=True)
        box.append(status)

        def recapture(_b) -> None:
            start_capture(lambda k: key_entry.set_text(k))

        def save(_b) -> None:
            new_key = key_entry.get_text().strip()
            conflicts = kb.check_conflict(new_key, key)
            if conflicts:
                kb.notify_conflict(new_key, conflicts)
                status.set_label(_("Conflicto con: ") + ", ".join(x["key"] for x in conflicts))
                return
            kind, act = kb.action_from_ui(combo.get_active(), param.get_text())
            ok, msg = kb.add_or_update({"key": new_key, "kind": kind, "action": act,
                                        "description": "", "repeat": False, "locked": False,
                                        "old_key": key})
            status.set_label((_("Guardado: ") if ok else _("Error: ")) + msg)
            if ok:
                d.close()
                reload_binds()

        row_btns = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        row_btns.append(make_button(_("Cambiar tecla (5 s)"), recapture))
        row_btns.append(make_button(_("Guardar"), save))
        box.append(row_btns)
        d.present()

    edit_action = Gio.SimpleAction.new("edit-bind", GLib.VariantType.new("s"))
    def on_edit_action(_a, param):
        key = param.get_string()
        for b in binds_cache:
            label = b.get("source_key") or f"{b['mods']} + {b['key']}"
            if label == key:
                edit_dialog(key, b.get("source_action") or b["dispatcher"])
                return
    edit_action.connect("activate", on_edit_action)
    win.add_action(edit_action)

    # ---- modo AÑADIR: acción -> tecla -> categoría automática ----
    def add_dialog() -> None:
        d = Gtk.Window(title=_("Añadir atajo"), transient_for=win, default_width=520, default_height=430)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10,
                      margin_start=16, margin_end=16, margin_top=16, margin_bottom=16)
        d.set_child(box)

        combo = Gtk.ComboBoxText()
        for opt in (_("Ejecutar un programa"), _("Cerrar la ventana"),
                    _("Alternar ventana flotante"), _("Pantalla completa"),
                    _("Enviar mensaje a Noctalia"), _("Avanzado (expresión Lua)")):
            combo.append_text(opt)
        combo.set_active(0)
        kind_row = Adw.ActionRow(title=_("¿Qué hará el atajo?"), subtitle=_("Elige primero la acción"))
        kind_row.add_suffix(combo)
        box.append(kind_row)

        param = Gtk.Entry()
        param.set_placeholder_text(_("Ej.: kitty · launcher · volume-up"))
        param_row = Adw.ActionRow(title=_("Datos de la acción"))
        param_row.add_suffix(param)
        box.append(param_row)

        key_entry = Gtk.Entry()
        key_entry.set_placeholder_text(_("Se determina con el botón inferior"))
        key_row = Adw.ActionRow(title=_("Tecla"), subtitle=_("5 s tras la última pulsación"))
        key_row.add_suffix(key_entry)
        box.append(key_row)

        status = Gtk.Label(label=_("1 · elige la acción   2 · determina la tecla   3 · guarda"), wrap=True)
        box.append(status)

        def determine(_b) -> None:
            start_capture(lambda k: (key_entry.set_text(k),
                                     status.set_label(_("Tecla lista: ") + k)))

        def save(_b) -> None:
            key = key_entry.get_text().strip()
            if not key:
                status.set_label(_("Primero determina la tecla"))
                return
            conflicts = kb.check_conflict(key)
            if conflicts:
                kb.notify_conflict(key, conflicts)
                status.set_label(_("Conflicto con: ") + ", ".join(x["key"] for x in conflicts))
                return
            kind, act = kb.action_from_ui(combo.get_active(), param.get_text())
            ok, msg = kb.add_or_update({"key": key, "kind": kind, "action": act,
                                        "description": "", "repeat": False, "locked": False,
                                        "old_key": ""})
            cat, _desc = kb.describe(act)
            status.set_label((_("Añadido en «") + cat + _("»: ") if ok else _("Error: ")) + msg)
            if ok:
                d.close()
                reload_binds()

        row_btns = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        row_btns.append(make_button(_("Determinar tecla (5 s)"), determine))
        row_btns.append(make_button(_("Guardar atajo"), save))
        box.append(row_btns)
        d.present()

    kb_status = Gtk.Label(label=_("Usa «+ Añadir atajo» o el menú «…» de cada atajo"), wrap=True)
    kb_actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=8)
    kb_actions.append(make_button(_("+ Añadir atajo"), lambda _b: add_dialog()))
    kb_actions.append(make_button(_("Recargar"), lambda _b: reload_binds()))
    kb_group.add(kb_actions)
    kb_outer.append(kb_status)

    # ============ Pestaña 7: Monitores ============
    m_outer, m_page = new_tab(stack, "monitores", _("Monitores"))
    m_group = Adw.PreferencesGroup(
        title=_("Monitores detectados"),
        description=_("Propiedades leídas directamente de hyprctl monitors -j."),
    )
    m_page.add(m_group)
    m_list = Gtk.ListBox()
    m_scroll = Gtk.ScrolledWindow()
    m_scroll.set_child(m_list)
    m_scroll.set_min_content_height(200)
    m_scroll.set_min_content_width(560)
    m_group.add(m_scroll)
    m_status = Gtk.Label(label=_("Detectando…"), wrap=True)
    detected: list[dict] = []

    def refresh_monitors() -> None:
        nonlocal detected
        m_list.remove_all()
        detected = mon.list_monitors()
        for m in detected:
            row = Adw.ActionRow(
                title=f"{m['name']} · {m['width']}x{m['height']}@{m['refresh']}",
                subtitle=(f"{m['make']} {m['model']} · escala {m['scale']} · "
                          f"VRR {m['vrr']} · HDR {m['hdr']} · {m['format']} · "
                          f"workspace {m['workspace']} · S/N {m['serial']}"),
            )
            m_list.append(row)
        m_status.set_label(_("{n} monitor(es) detectado(s)").format(n=len(detected)))

    def save_monitors(_btn: Gtk.Button) -> None:
        ok, msg = mon.write_variables(detected)
        m_status.set_label((_("Variables actualizadas: ") if ok else _("Error: ")) + msg)

    m_actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=8)
    m_actions.append(make_button(_("Redetectar"), lambda _b: refresh_monitors()))
    m_actions.append(make_button(_("Escribir MONITOR1..3"), save_monitors))

    def adapt_monitors(_btn: Gtk.Button | None = None) -> None:
        rep = mon.sync_monitor_config(len(detected))
        if rep["cambios"]:
            m_status.set_label(_("Config adaptada a {n} monitor(es): ").format(n=rep["detectados"])
                               + ", ".join(f"{k} ({v})" for k, v in rep["archivos"].items()))
        else:
            m_status.set_label(_("Config ya coherente con {n} monitor(es)").format(n=rep["detectados"]))

    m_actions.append(make_button(_("Adaptar config a monitores"), adapt_monitors))
    m_group.add(m_actions)
    m_outer.append(m_status)

    # ============ Pestaña 8: Wallpapers ============
    w_outer, w_page = new_tab(stack, "wallpapers", _("Wallpapers"))
    w_group = Adw.PreferencesGroup(
        title=_("Fondos de pantalla"),
        description=_("Proveedores oficiales/públicos + Noctalia IPC (wallpaper-set)."),
    )
    w_page.add(w_group)

    provider_combo = Gtk.ComboBoxText()
    for p in (_("Local (CachyOS)"), _("Wallhaven"), _("Unsplash (clave)"),
              _("Pexels (clave)"), _("Wallpaper Engine")):
        provider_combo.append_text(p)
    provider_combo.set_active(0)
    row_provider = Adw.ActionRow(title=_("Proveedor"))
    row_provider.add_suffix(provider_combo)
    w_group.add(row_provider)

    search_entry = Gtk.Entry()
    search_entry.set_placeholder_text(_("Búsqueda en Wallhaven, p. ej. nature"))
    search_entry.set_size_request(260, -1)
    row_search = Adw.ActionRow(title=_("Búsqueda"))
    row_search.add_suffix(search_entry)
    w_group.add(row_search)

    api_entry = Gtk.Entry()
    api_entry.set_placeholder_text(_("Clave de Unsplash (opcional, no se guarda)"))
    api_entry.set_width_chars(34)
    row_api = Adw.ActionRow(title=_("Clave API"), subtitle=_("Unsplash / Pexels; nunca se almacena"))
    row_api.add_suffix(api_entry)
    w_group.add(row_api)

    results_list = Gtk.ListBox()
    results_scroll = Gtk.ScrolledWindow()
    results_scroll.set_child(results_list)
    results_scroll.set_min_content_height(220)
    results_scroll.set_max_content_height(340)
    results_scroll.set_min_content_width(560)
    w_group.add(results_scroll)

    connector_combo = Gtk.ComboBoxText()
    row_target = Adw.ActionRow(title=_("Aplicar a monitor"), subtitle=_("Todos si no se elige uno"))
    row_target.add_suffix(connector_combo)
    w_group.add(row_target)

    w_status = Gtk.Label(label=_("Elige proveedor y busca"), wrap=True)
    results: list[dict] = {}

    def refresh_connectors() -> None:
        connector_combo.remove_all()
        connector_combo.append_text(_("Todos los monitores"))
        for m in mon.list_monitors():
            connector_combo.append_text(m["name"])
        connector_combo.set_active(0)

    def do_search(_btn: Gtk.Button) -> None:
        nonlocal results
        results_list.remove_all()
        # AUDITORÍA: si el usuario eligió monitor, sus especificaciones
        # (resolución y proporción) se aplican como filtro automático.
        width = height = 0
        name = connector_combo.get_active_text()
        if connector_combo.get_active() > 0 and name:
            for m in detected:
                if m["name"] == name:
                    width, height = m["width"], m["height"]
                    break
        filtro = ""
        if width and height:
            filtro = _("{w}x{h} · proporción {r}").format(
                w=width, h=height, r=wp.ratio_filter(width, height))

        provider = provider_combo.get_active()
        query = search_entry.get_text().strip() or "wallpaper"
        if provider == 0:
            items = wp.local_wallpapers()
        elif provider == 1:
            items = wp.search_wallhaven(query, width=width, height=height)
        elif provider == 4:
            items = we.list_wallpapers()
            if not items:
                info = we.detect()
                w_status.set_label(_("Wallpaper Engine no detectado. ") + info.get("note", ""))
                we.open_store()
                return
        else:
            key = api_entry.get_text().strip()
            if not key:
                w_status.set_label(_("Este proveedor necesita una clave API (no se guarda)"))
                return
            items = (wp.search_unsplash(query, key, width=width, height=height)
                     if provider == 2 else
                     wp.search_pexels(query, key, width=width, height=height))
        results = {i: it for i, it in enumerate(items)}
        for i, it in enumerate(items):
            row = Adw.ActionRow(title=it.get("title", it.get("id", "")),
                                subtitle=f"{it.get('provider', '')} · {it.get('resolution', '')}")
            row.set_name(str(i))
            row.set_activatable(True)
            results_list.append(row)
        sufijo = _(" · filtro automático: ") + filtro if filtro else ""
        w_status.set_label(_("{n} resultado(s)").format(n=len(items)) + sufijo)

    def download_apply(_btn: Gtk.Button) -> None:
        row = results_list.get_selected_row()
        if row is None:
            w_status.set_label(_("Selecciona un wallpaper"))
            return
        item = results.get(int(row.get_name()))
        if not item:
            return
        ok, path = wp.download(item)
        if not ok:
            w_status.set_label(_("Error al descargar: ") + path)
            return
        idx = connector_combo.get_active()
        connector = None
        if idx > 0:
            connector = connector_combo.get_active_text()
        ok2, msg2 = wp.set_wallpaper(path, connector)
        w_status.set_label((_("Aplicado: ") if ok2 else _("Descargado pero no aplicado: ")) + path + " · " + msg2)

    w_actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=8)
    w_actions.append(make_button(_("Buscar"), do_search))
    w_actions.append(make_button(_("Descargar y aplicar"), download_apply))
    w_actions.append(make_button(_("Recargar monitores"), lambda _b: refresh_connectors()))
    w_group.add(w_actions)
    w_outer.append(w_status)

    # ============ Pestaña 9: Web / Compartir ============
    s_outer, s_page = new_tab(stack, "web", _("Web / Compartir"))
    s_group = Adw.PreferencesGroup(
        title=_("Descubrir y compartir rices"),
        description=_("GitHub, Gists y Dotfyle. Publicar requiere un token que no se guarda."),
    )
    s_page.add(s_group)

    source_combo = Gtk.ComboBoxText()
    for src in (_("GitHub · repositorios"), _("GitHub · Gists"), _("Dotfyle · destacados")):
        source_combo.append_text(src)
    source_combo.set_active(0)
    row_source = Adw.ActionRow(title=_("Fuente"))
    row_source.add_suffix(source_combo)
    s_group.add(row_source)

    web_search = Gtk.Entry()
    web_search.set_placeholder_text(_("Ej. hyprland dotfiles  ·  topic:hyprland rice"))
    web_search.set_size_request(300, -1)
    row_wsearch = Adw.ActionRow(title=_("Búsqueda"))
    row_wsearch.add_suffix(web_search)
    s_group.add(row_wsearch)

    web_list = Gtk.ListBox()
    web_scroll = Gtk.ScrolledWindow()
    web_scroll.set_child(web_list)
    web_scroll.set_min_content_height(190)
    web_scroll.set_max_content_height(300)
    web_scroll.set_min_content_width(560)
    s_group.add(web_scroll)

    web_status = Gtk.Label(label=_("Busca para ver resultados"), wrap=True)
    web_results: dict[int, dict] = {}

    def web_do_search(_btn: Gtk.Button) -> None:
        nonlocal web_results
        web_list.remove_all()
        q = web_search.get_text().strip()
        opt = source_combo.get_active()
        if opt == 0:
            items = sh.search_repos(q)
        elif opt == 1:
            items = sh.search_gists(q)
        else:
            items = sh.dotfyle_featured()
        web_results = {i: it for i, it in enumerate(items)}
        for i, it in enumerate(items):
            row = Adw.ActionRow(title=it["name"], subtitle=f"★ {it['stars']} · {it['description'][:70]}")
            row.set_name(str(i))
            row.set_activatable(True)
            web_list.append(row)
        web_status.set_label(_("{n} resultado(s)").format(n=len(items)))

    def web_url() -> str:
        row = web_list.get_selected_row()
        if row is None:
            return ""
        item = web_results.get(int(row.get_name()), {})
        return item.get("url", "")

    def web_open(_btn: Gtk.Button) -> None:
        url = web_url()
        if not url:
            web_status.set_label(_("Selecciona un resultado"))
            return
        ok, msg = sh.open_browser(url)
        web_status.set_label((_("Abriendo: ") if ok else _("Error: ")) + url + " " + msg)

    def web_readme(_btn: Gtk.Button) -> None:
        row = web_list.get_selected_row()
        if row is None:
            web_status.set_label(_("Selecciona un resultado"))
            return
        item = web_results[int(row.get_name())]
        repo = "/".join(item["url"].rstrip("/").split("/")[-2:])
        show_text_window(win, _("README · ") + repo, sh.get_readme(repo))

    def web_import(_btn: Gtk.Button) -> None:
        url = web_url()
        if not url:
            web_status.set_label(_("Selecciona un resultado"))
            return
        ok, msg = sh.import_repo(url)
        web_status.set_label((_("Importado: ") if ok else _("Error: ")) + msg)

    token_entry = Gtk.Entry()
    token_entry.set_placeholder_text(_("ghp_…  (no se guarda)"))
    token_entry.set_visibility(False)
    row_token = Adw.ActionRow(title=_("Token de GitHub"), subtitle=_("Solo para publicar; se olvida al cerrar"))
    row_token.add_suffix(token_entry)
    s_group.add(row_token)

    gist_desc = Gtk.Entry()
    gist_desc.set_placeholder_text(_("Descripción del Gist"))
    row_gdesc = Adw.ActionRow(title=_("Descripción"))
    row_gdesc.add_suffix(gist_desc)
    s_group.add(row_gdesc)

    def make_bundle(_btn: Gtk.Button) -> None:
        ok, msg = sh.create_bundle()
        web_status.set_label((_("ZIP creado: ") if ok else _("Error: ")) + msg)

    def publish(_btn: Gtk.Button) -> None:
        ok, msg = sh.publish_gist(token_entry.get_text().strip(),
                                  gist_desc.get_text().strip(), True)
        web_status.set_label((_("Publicado: ") if ok else _("Error: ")) + msg)
        if ok:
            token_entry.set_text("")  # no conservar el token en memoria de la UI

    web_actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=8)
    for label, cb in [(_("Buscar"), web_do_search), (_("Abrir"), web_open),
                      (_("Ver README"), web_readme), (_("Importar repo"), web_import),
                      (_("Crear ZIP"), make_bundle), (_("Publicar Gist"), publish)]:
        web_actions.append(make_button(label, cb))
    s_group.add(web_actions)
    s_outer.append(web_status)

    # ============ Común ============
    def persist_settings(*_args) -> None:
        s = bm.get_settings()
        s["auto_backup"] = auto_switch.get_active()
        s["interval_minutes"] = int(spin_int.get_value())
        s["keep_last"] = int(spin_keep.get_value())
        bm.save_settings(s)
        install_timer(s["interval_minutes"] if s["auto_backup"] else 0, on_timer)

    auto_switch.connect("notify::active", persist_settings)
    spin_int.connect("value-changed", persist_settings)
    spin_keep.connect("value-changed", persist_settings)

    def on_timer() -> bool:
        bm.create_backup(reason="auto")
        refresh_history()
        return True

    root = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12,
                   margin_start=12, margin_end=12, margin_top=12, margin_bottom=12)
    root.append(switcher)
    root.append(stack)
    win.set_content(root)

    refresh_history()
    reload_binds()       # informe de debug: cargar atajos al arrancar
    refresh_monitors()
    # AUDITORÍA: NO se modifica la config al arrancar. La sincronización
    # (comentar MONITORn inexistentes) sólo ocurre al pulsar su botón.
    refresh_connectors()
    _ready["value"] = True
    s = bm.get_settings()
    install_timer(s["interval_minutes"] if s.get("auto_backup", True) else 0, on_timer)

    def on_close(_win) -> bool:
        global _timer_id
        if _opt_timer is not None:
            GLib.source_remove(_opt_timer)
        if _timer_id is not None:
            GLib.source_remove(_timer_id)
            _timer_id = None
        return False

    win.connect("close-request", on_close)
    win.present()


def install_timer(interval_minutes: int, callback) -> None:
    global _timer_id
    if _timer_id is not None:
        GLib.source_remove(_timer_id)
        _timer_id = None
    if interval_minutes > 0:
        _timer_id = GLib.timeout_add_seconds(interval_minutes * 60, callback)


def main() -> int:
    app = Adw.Application(application_id="com.tu.hypr-rice-gui")
    app.connect("activate", on_activate)
    return app.run(None)


if __name__ == "__main__":
    raise SystemExit(main())
