---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/greetd"
title: "Greetd | AGS Wiki"
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
* [methods](#methods)
* [Response](#response)
* [Example](#example)

## On this page

* [Overview](#_top)
* [methods](#methods)
* [Response](#response)
* [Example](#example)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Greetd

Look up how to enable and configure greetd for your distro.

## methods

* `login`: `(username: string, password: string, cmd: string | string[], env?: string[]) => Promise<Response>`: combines `createSession`, `postAuth`, `startSession`, `cancelSession`
* `createSession`: `(username: string) => Promise<Response>`
* `postAuth`: `(response: string) => Promise<Response>`
* `startSession`: `(cmd: string | string[], env?: string[]) => Promise<Response>`
* `cancelSession`: `() => Promise<Response>`

## Response

```
type Response = {

type: 'success'

} | {

type: 'error'

error_type: 'auth_error' | 'error'

description: string

} | {

type: 'auth_message'

auth_message_type: 'visible' | 'secret' | 'info' | 'error'

auth_message: string

}
```

## Example

/etc/greetd/greeter.js

```
const greetd = await Service.import('greetd');

const name = Widget.Entry({

placeholder_text: 'Username',

on_accept: () => password.grab_focus(),

})

const password = Widget.Entry({

placeholder_text: 'Password',

visibility: false,

on_accept: () => {

greetd.login(name.text || '', password.text || '', 'Hyprland')

.catch(err => response.label = JSON.stringify(err))

},

})

const response = Widget.Label()

const win = Widget.Window({

css: 'background-color: transparent;',

anchor: ['top', 'left', 'right', 'bottom'],

keymode: 'exclusive',

child: Widget.Box({

vertical: true,

hpack: 'center',

vpack: 'center',

hexpand: true,

vexpand: true,

children: [

name,

password,

response,

],

}),

})

App.config({ windows: [win] })
```

/etc/greetd/hyprland.conf

```
exec-once = ags --config /etc/greetd/greeter.js; hyprctl dispatch exit
```

/etc/greetd/config.toml

```
[default_session]

command = "Hyprland --config /etc/greetd/hyprland.conf"
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/greetd.md)

[Previous
 Bluetooth](/ags-docs/services/bluetooth/)   [Next
 Hyprland](/ags-docs/services/hyprland/)
