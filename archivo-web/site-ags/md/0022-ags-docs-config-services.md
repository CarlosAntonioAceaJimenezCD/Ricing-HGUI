---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/services"
title: "Services | AGS Wiki"
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
* [List of builtin services](#list-of-builtin-services)

## On this page

* [Overview](#_top)
* [List of builtin services](#list-of-builtin-services)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Services

A Service is an instance of a [GObject.Object](https://gjs-docs.gnome.org/gobject20~2.0/gobject.object)
that emits signals when its state changes.
Widgets can connect to them and execute a callback function on their signals
which are usually functions that updates the widget’s properties.

```
Widget.Label({

// the signal is 'changed' if not specified

// [Service, callback, signal = 'changed']

setup: self => self.hook(someService, function(self, ...args) {

// there can be other arguments based on signals

self.label = 'new label'

}, 'changed')

})
```

```
Widget.Label({

label: someService.bind('service-prop').as(serviceProp => {

return `transformed ${serviceProp}`

}),

})
```

Utility to have multiple bindings as one

```
Widget.Label({

label: Utils.merge([service1.bind("prop1"), service2.bind("prop2")], (p1, p2) => {

return `service1.prop1: ${p1}, service2.prop2: ${p2}`

}),

})
```

Services can be also connected outside of widgets

```
someService.connect('changed', (service, ...args) => {

print(service, ...args)

})
```

Caution

If you reference a widget inside `someService.connect`, make sure to
handle disconnection as well if that widget is destroyed

## List of builtin services

use `Service.import`

```
const battery = await Service.import('battery')
```

or if you prefer static import

```
import { battery } from 'resource:///com/github/Aylur/ags/service/battery.js';
```

Caution

Import `default` and don’t import the service class from the module,
unless you need the type when using typescript.

```
// this is the service singleton instance

import Battery from 'resource:///com/github/Aylur/ags/service/battery.js';

// this is also the service singleton instance

import { battery } from 'resource:///com/github/Aylur/ags/service/battery.js';

Battery === battery // true
```

```
// DON'T import it this way, this is the class

import { Battery } from 'resource:///com/github/Aylur/ags/service/battery.js';
```

Tip

Every service has a `"changed"` signal which is emitted
on any kind of state change, unless stated otherwise.

* [applications](../../services/applications)
* [audio](../../services/audio)
* [battery](../../services/battery)
* [bluetooth](../../services/bluetooth)
* [greetd](../../services/greetd)
* [hyprland](../../services/hyprland)
* [mpris](../../services/mpris)
* [network](../../services/network)
* [notifications](../../services/notifications)
* [powerprofiles](../../services/powerprofiles)
* [systemtray](../../services/systemtray)

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/services.md)

[Previous
 Variables](/ags-docs/config/variables)   [Next
 Utils](/ags-docs/config/utils)
