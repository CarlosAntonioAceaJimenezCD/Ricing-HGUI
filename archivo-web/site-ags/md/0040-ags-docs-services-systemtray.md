---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/systemtray"
title: "System Tray | AGS Wiki"
fetched_at: 2026-11-22T06:24:53+00:00
fetcher: "curl + markitdown"
site: "aylur.github.io"
---
[Skip to content](#_top)

[AGS Wiki](/ags-docs/)

Search

Cancel

[GitHub](https://github.com/Aylur/ags) [Discord](https://discord.gg/CXQpHwDuhY)

  Select theme   DarkLightAuto

* Configuration

  + [Installation](/ags-docs/config/installation)
  + [JavaScript](/ags-docs/config/javascript)
  + [First Widgets](/ags-docs/config/first-widgets)
  + [Reactivity](/ags-docs/config/reactivity)
  + [Theming](/ags-docs/config/theming)
  + [Config Object](/ags-docs/config/config-object)
  + [Type Checking](/ags-docs/config/type-checking)
  + [CLI](/ags-docs/config/cli)
  + [Widgets](/ags-docs/config/widgets)
  + [Variables](/ags-docs/config/variables)
  + [Services](/ags-docs/config/services)
  + [Utils](/ags-docs/config/utils)
  + [App](/ags-docs/config/app)
  + [Custom Service](/ags-docs/config/custom-service)
  + [Subclassing GTK Widgets](/ags-docs/config/subclassing-gtk-widgets)
  + [Examples](/ags-docs/config/examples)
  + [Common Issues](/ags-docs/config/common-issues)
* Builtin Services

  + [Applications](/ags-docs/services/applications/)
  + [Audio](/ags-docs/services/audio/)
  + [Backlight](/ags-docs/services/backlight/)
  + [Battery](/ags-docs/services/battery/)
  + [Bluetooth](/ags-docs/services/bluetooth/)
  + [Greetd](/ags-docs/services/greetd/)
  + [Hyprland](/ags-docs/services/hyprland/)
  + [Mpris](/ags-docs/services/mpris/)
  + [Network](/ags-docs/services/network/)
  + [Notifications](/ags-docs/services/notifications/)
  + [Power Profiles](/ags-docs/services/powerprofiles/)
  + [System Tray](/ags-docs/services/systemtray/)
* Builtin Widgets

  + [Window](/ags-docs/config/widgets#window)
  + [Box](/ags-docs/config/widgets#box)
  + [Button](/ags-docs/config/widgets#button)
  + [Calendar](/ags-docs/config/widgets#calendar)
  + [CenterBox](/ags-docs/config/widgets#centerbox)
  + [CircularProgress](/ags-docs/config/widgets#circularprogress)
  + [ColorButton](/ags-docs/config/widgets#colorbutton)
  + [DrawingArea](/ags-docs/config/widgets#drawingarea)
  + [Entry](/ags-docs/config/widgets#entry)
  + [EventBox](/ags-docs/config/widgets#eventbox)
  + [FileChooserButton](/ags-docs/config/widgets#filechooserbutton)
  + [Fixed](/ags-docs/config/widgets#fixed)
  + [FlowBox](/ags-docs/config/widgets#flowbox)
  + [FontButton](/ags-docs/config/widgets#fontbutton)
  + [Icon](/ags-docs/config/widgets#icon)
  + [Label](/ags-docs/config/widgets#label)
  + [LevelBar](/ags-docs/config/widgets#levelbar)
  + [ListBox](/ags-docs/config/widgets#listbox)
  + [Menu](/ags-docs/config/widgets#menu)
  + [MenuBar](/ags-docs/config/widgets#menubar)
  + [MenuItem](/ags-docs/config/widgets#menuitem)
  + [OverLay](/ags-docs/config/widgets#overlay)
  + [ProgressBar](/ags-docs/config/widgets#progressbar)
  + [Revealer](/ags-docs/config/widgets#revealer)
  + [Scrollable](/ags-docs/config/widgets#scrollable)
  + [Separator](/ags-docs/config/widgets#separator)
  + [Slider](/ags-docs/config/widgets#slider)
  + [SpinButton](/ags-docs/config/widgets#spinbutton)
  + [Spinner](/ags-docs/config/widgets#spinner)
  + [Stack](/ags-docs/config/widgets#stack)
  + [Switch](/ags-docs/config/widgets#switch)
  + [ToggleButton](/ags-docs/config/widgets#togglebutton)

[GitHub](https://github.com/Aylur/ags) [Discord](https://discord.gg/CXQpHwDuhY)

  Select theme   DarkLightAuto

On this page

* [Overview](#_top)
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
* [TrayItem](#trayitem)
  + [signals](#signals-1)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example Widget](#example-widget)

## On this page

* [Overview](#_top)
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
* [TrayItem](#trayitem)
  + [signals](#signals-1)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example Widget](#example-widget)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# System Tray

Note

package dependency: `libdbusmenu-gtk3`

## signals

* `added`: `(busName: string)` emitted when a new TrayItem is added
* `removed`: `(busName: string)` emitted when a TrayItem is removed

## properties

* `items`: `TrayItem[]`

## methods

* `getItem`: `(busName: string) => TrayItem`

## TrayItem

### signals

* `changed`: emitted on any change of the TrayItem
* `removed`: `(busName: string)` emitted when this TrayItem is removed

### properties

* `menu`: [Gtk.Menu](https://gjs-docs.gnome.org/gtk30~3.0/gtk.menu) | `undefined`
* `category`: `string` possible values: `ApplicationStatus`, `Communications`, `SystemServices`, `Hardware`
* `id`: `string`
* `title`: `string`
* `status`: `string` possible values: `Passive`, `Active`, `NeedsAttention`
* `window-id`: `number`
* `is-menu`: `boolean` if true, showing the menu is preferred over activate
* `tooltip-markup`: `string`
* `icon`: `string | GdkPixbuf.Pixbuf`

### methods

* `activate`: `(event: Gdk.Event) => void`
* `secondaryActivate`: `(event: Gdk.Event) => void`
* `scroll`: `(event: Gdk.EventScroll) => void`
* `openMenu`: `(event: Gdk.Event) => void`

## Example Widget

```
const systemtray = await Service.import('systemtray')

/** @param {import('types/service/systemtray').TrayItem} item */

const SysTrayItem = item => Widget.Button({

child: Widget.Icon().bind('icon', item, 'icon'),

tooltipMarkup: item.bind('tooltip_markup'),

onPrimaryClick: (_, event) => item.activate(event),

onSecondaryClick: (_, event) => item.openMenu(event),

});

const sysTray = Widget.Box({

children: systemtray.bind('items').as(i => i.map(SysTrayItem))

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/systemtray.md)

[Previous
 Power Profiles](/ags-docs/services/powerprofiles/)   [Next
 Window](/ags-docs/config/widgets#window)
