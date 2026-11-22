---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/bluetooth"
title: "Bluetooth | AGS Wiki"
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
* [Device](#device)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example Widgets](#example-widgets)

## On this page

* [Overview](#_top)
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
* [Device](#device)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example Widgets](#example-widgets)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Bluetooth

Note

package dependency: `gnome-bluetooth-3.0`
for the battery percentage to work, make sure you have `Experimental = true` in `/etc/bluetooth/main.conf`

## signals

* `device-added`: `(address: string)`
* `device-removed`: `(address: string)`

## properties

* `enabled`: `boolean`: writable
* `devices`: `Device[]`
* `connected-devices`: `Device[]`

## methods

* `toggle`: `() => void`
* `getDevice`: `(address: string) => Device`

## Device

### properties

* `address`: `string`
* `battery-level`: `number`
* `battery-percentage`: `number`
* `connected`: `boolean`
* `icon-name`: `string`
* `alias`: `string`
* `name`: `string`
* `trusted`: `boolean`
* `paired`: `boolean`

### methods

* `setConnection`: `(connect: boolean) => void`

## Example Widgets

```
const bluetooth = await Service.import('bluetooth')

const connectedList = Widget.Box({

setup: self => self.hook(bluetooth, self => {

self.children = bluetooth.connected_devices

.map(({ icon_name, name }) => Widget.Box([

Widget.Icon(icon_name + '-symbolic'),

Widget.Label(name),

]));

self.visible = bluetooth.connected_devices.length > 0;

}, 'notify::connected-devices'),

})

const indicator = Widget.Icon({

icon: bluetooth.bind('enabled').as(on =>

`bluetooth-${on ? 'active' : 'disabled'}-symbolic`),

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/bluetooth.md)

[Previous
 Battery](/ags-docs/services/battery/)   [Next
 Greetd](/ags-docs/services/greetd/)
