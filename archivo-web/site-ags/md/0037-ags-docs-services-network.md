---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/network"
title: "Network | AGS Wiki"
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
* [properties](#properties)
* [methods](#methods)
* [Wifi](#wifi)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [AccessPoint](#accesspoint)
  + [properties](#properties-2)
* [Wired](#wired)
* [Vpn](#vpn)
  + [signals](#signals)
  + [properties](#properties-3)
  + [methods](#methods-2)
* [VpnConnection](#vpnconnection)
  + [properties](#properties-4)
  + [methods](#methods-3)
* [Example Widget](#example-widget)

## On this page

* [Overview](#_top)
* [properties](#properties)
* [methods](#methods)
* [Wifi](#wifi)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [AccessPoint](#accesspoint)
  + [properties](#properties-2)
* [Wired](#wired)
* [Vpn](#vpn)
  + [signals](#signals)
  + [properties](#properties-3)
  + [methods](#methods-2)
* [VpnConnection](#vpnconnection)
  + [properties](#properties-4)
  + [methods](#methods-3)
* [Example Widget](#example-widget)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Network

Note

package dependency: `network-manager`
This service is somewhat incomplete, feel free to open a PR to improve it

## properties

* `connectivity`: `"unknown" | "none" | "portal" | "limited" | "full"`
* `primary`: `"wifi" | "wired"`
* `wired`: `Wired`
* `wifi`: `Wifi`
* `vpn`: `Vpn`

## methods

* `toggleWifi`: `() => void`

## Wifi

### properties

* `ssid`: `string`
* `strength`: `number` 0..100
* `frequency`: `number`
* `internet`: `"connected" | "connecting" | "disconnected"`
* `enabled`: `boolean`
* `access-points`: `AccessPoint`
* `icon-name`: `string`
* `state`: `string`: [NM.DeviceState](https://gjs-docs.gnome.org/nm10~1.0/nm.devicestate) as lowercase string

### methods

* `scan`: `() => void`

## AccessPoint

access points are not a GObjects, just a regular js objects
meaning you can’t bind to it or use notify::prop signal

### properties

* `bssid`: `string`
* `address`: `string`
* `lastSeen`: `number`
* `ssid`: `string`
* `active`: `boolean`
* `strength`: `number`
* `frequency`: `number`
* `iconName`: `string` icon name representing its signal strength

## Wired

* `internet`: `"connected" | "connecting" | "disconnected"`
* `state`: `"enabled" | "disabled" | "unknown"`
* `state`: `string`: [NM.DeviceState](https://gjs-docs.gnome.org/nm10~1.0/nm.devicestate) as lowercase string
* `icon-name`: `string`

## Vpn

### signals

* `connection-added`: `(uuid: string)`
* `connection-removed`: `(uuid: string)`

### properties

* `connections`: `VpnConnection[]`
* `activated-connections`: `VpnConnection[]`

### methods

* `getConnection`: `(uuid: string) => VpnConnection`

## VpnConnection

### properties

* `uuid`: `string`
* `id`: `string`: The unique name of the connection
* `state`: `"connected" | "connecting" | "disconnecting" | "disconnected"`
* `vpn-state`: `"unknown" | "prepare" | "needs_auth" | "connect" | "ip_config" | "activated" | "failed" | "disconnected"`
* `icon-name`: `string`

### methods

* `setConnection`: `(connect: boolean) => void`

## Example Widget

```
const network = await Service.import('network')

const WifiIndicator = () => Widget.Box({

children: [

Widget.Icon({

icon: network.wifi.bind('icon_name'),

}),

Widget.Label({

label: network.wifi.bind('ssid')

.as(ssid => ssid || 'Unknown'),

}),

],

})

const WiredIndicator = () => Widget.Icon({

icon: network.wired.bind('icon_name'),

})

const NetworkIndicator = () => Widget.Stack({

children: {

wifi: WifiIndicator(),

wired: WiredIndicator(),

},

shown: network.bind('primary').as(p => p || 'wifi'),

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/network.md)

[Previous
 Mpris](/ags-docs/services/mpris/)   [Next
 Notifications](/ags-docs/services/notifications/)
