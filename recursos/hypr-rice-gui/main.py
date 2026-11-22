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
from gi.repository import Adw, GLib, Gtk  # noqa: E402

import backup_manager as bm  # noqa: E402
import config_model as cm  # noqa: E402
import keybinds as kb  # noqa: E402
import monitors as mon  # noqa: E402
import wallpapers as wp  # noqa: E402

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

    # ============ Pestaña 6: Keybinds ============
    kb_outer, kb_page = new_tab(stack, "keybinds", _("Keybinds"))
    kb_group = Adw.PreferencesGroup(
        title=_("Atajos de teclado"),
        description=_("Lista en vivo desde hyprctl. Edita o añade; se guarda en ui-bindings.lua."),
    )
    kb_page.add(kb_group)

    kb_list = Gtk.ListBox()
    kb_list.set_selection_mode(Gtk.SelectionMode.SINGLE)
    kb_scroll = Gtk.ScrolledWindow()
    kb_scroll.set_child(kb_list)
    kb_scroll.set_min_content_height(220)
    kb_scroll.set_max_content_height(360)
    kb_scroll.set_min_content_width(560)
    kb_group.add(kb_scroll)

    key_entry = Gtk.Entry()
    key_entry.set_placeholder_text(_("SUPER + CTRL + K"))
    key_entry.set_size_request(220, -1)
    row_key = Adw.ActionRow(title=_("Tecla"), subtitle=_("Modificadores + tecla o code:N"))
    row_key.add_suffix(key_entry)
    kb_group.add(row_key)

    kind_combo = Gtk.ComboBoxText()
    for opt in (_("Comando (exec)"), _("Expresión Lua")):
        kind_combo.append_text(opt)
    kind_combo.set_active(0)
    row_kind = Adw.ActionRow(title=_("Tipo de acción"))
    row_kind.add_suffix(kind_combo)
    kb_group.add(row_kind)

    action_entry = Gtk.Entry()
    action_entry.set_placeholder_text(_("kitty  ·  hl.dsp.window.close()"))
    action_entry.set_size_request(300, -1)
    row_action = Adw.ActionRow(title=_("Acción"), subtitle=_("Comando o expresión hl.dsp.*"))
    row_action.add_suffix(action_entry)
    kb_group.add(row_action)

    desc_entry = Gtk.Entry()
    desc_entry.set_placeholder_text(_("Descripción opcional"))
    row_desc = Adw.ActionRow(title=_("Descripción"))
    row_desc.add_suffix(desc_entry)
    kb_group.add(row_desc)

    repeat_sw = Gtk.Switch()
    locked_sw = Gtk.Switch()
    row_flags = Adw.ActionRow(title=_("Opciones"), subtitle=_("Repetible / disponible con pantalla bloqueada"))
    flags_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    flags_box.append(Gtk.Label(label=_("Repetir")))
    flags_box.append(repeat_sw)
    flags_box.append(Gtk.Label(label=_("Bloqueado")))
    flags_box.append(locked_sw)
    row_flags.add_suffix(flags_box)
    kb_group.add(row_flags)

    kb_status = Gtk.Label(label=_("Selecciona un atajo o escribe uno nuevo"), wrap=True)
    editing: dict[str, str] = {"old_key": ""}

    def refresh_binds() -> None:
        kb_list.remove_all()
        for b in kb.enriched_binds():
            label = f"{b['mods']} + {b['key']}"
            subtitle = b.get("source_action") or b["dispatcher"]
            row = Adw.ActionRow(title=label, subtitle=subtitle[:80])
            row.set_name(label)
            row.set_activatable(True)
            kb_list.append(row)

    def on_bind_selected(_list: Gtk.ListBox, row: Gtk.ListBoxRow | None) -> None:
        if row is None:
            return
        label = row.get_name()
        editing["old_key"] = label.split(" + ")[-1]
        key_entry.set_text(label)
        source_action = ""
        for b in kb.enriched_binds():
            if f"{b['mods']} + {b['key']}" == label:
                source_action = b.get("source_action", "")
                break
        if source_action and not source_action.startswith("HL.Dispatcher("):
            action_entry.set_text(source_action)
        desc_entry.set_text("")
        kb_status.set_label(_("Editando: ") + label + _(" · la acción se rellenó desde binds.lua"))

    kb_list.connect("row-selected", on_bind_selected)

    def save_bind(_btn: Gtk.Button) -> None:
        key = key_entry.get_text().strip()
        action = action_entry.get_text().strip()
        if not key or not action:
            kb_status.set_label(_("Faltan tecla o acción"))
            return
        entry = {
            "key": key,
            "kind": "exec" if kind_combo.get_active() == 0 else "lua",
            "action": action,
            "description": desc_entry.get_text().strip(),
            "repeat": repeat_sw.get_active(),
            "locked": locked_sw.get_active(),
            "old_key": editing["old_key"],
        }
        ok, msg = kb.add_or_update(entry)
        kb_status.set_label((_("Guardado: ") if ok else _("Error: ")) + msg)
        editing["old_key"] = ""
        refresh_binds()

    def remove_bind(_btn: Gtk.Button) -> None:
        key = key_entry.get_text().strip()
        if not key:
            kb_status.set_label(_("Escribe la tecla a eliminar"))
            return
        ok, msg = kb.delete(key)
        kb_status.set_label((_("Eliminado: ") if ok else _("Error: ")) + msg)
        refresh_binds()

    def toggle_bind(_btn: Gtk.Button) -> None:
        key = key_entry.get_text().strip()
        if not key:
            kb_status.set_label(_("Escribe la tecla"))
            return
        entry = next((e for e in kb.stored() if e.get("key") == key), None)
        disable = not (entry and entry.get("disabled"))
        ok, msg = kb.set_disabled(key, disable)
        kb_status.set_label((_("OK: ") if ok else _("Error: ")) + msg)
        refresh_binds()

    def new_bind(_btn: Gtk.Button) -> None:
        editing["old_key"] = ""
        key_entry.set_text("")
        action_entry.set_text("")
        desc_entry.set_text("")
        kb_status.set_label(_("Nuevo atajo · rellena los campos"))

    kb_actions = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6, margin_top=8)
    kb_actions.append(make_button(_("Nuevo"), new_bind))
    kb_actions.append(make_button(_("Guardar atajo"), save_bind))
    kb_actions.append(make_button(_("Desactivar/Activar"), toggle_bind))
    kb_actions.append(make_button(_("Eliminar"), remove_bind))
    kb_actions.append(make_button(_("Recargar lista"), lambda _b: refresh_binds()))
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
    for p in (_("Local (CachyOS)"), _("Wallhaven")):
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
        if provider_combo.get_active() == 0:
            items = wp.local_wallpapers()
        else:
            items = wp.search_wallhaven(search_entry.get_text().strip() or "wallpaper")
        results = {i: it for i, it in enumerate(items)}
        for i, it in enumerate(items):
            row = Adw.ActionRow(title=it.get("title", it.get("id", "")),
                                subtitle=f"{it.get('provider', '')} · {it.get('resolution', '')}")
            row.set_name(str(i))
            row.set_activatable(True)
            results_list.append(row)
        w_status.set_label(_("{n} resultado(s)").format(n=len(items)))

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
    refresh_monitors()
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
