---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/app"
title: "App | AGS Wiki"
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
* [Window toggled signal](#window-toggled-signal)
* [Applying CSS](#applying-css)

## On this page

* [Overview](#_top)
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
* [Window toggled signal](#window-toggled-signal)
* [Applying CSS](#applying-css)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# App

This is the main `Gtk.Application` instance that is running.

## signals

* `window-toggled`: `(windowName: string, visible: boolean)`
* `config-parsed`: emitted on startup

## properties

* `windows`: `Gtk.Window[]`
* `configDir`: `string` path to the config directory
* `iconTheme`: `string`
* `cursorTheme`: `string`
* `gtkTheme`: `string`

## methods

* `addWindow`: `(window: Gtk.Window) => void`
* `removeWindow`: `(window: Gtk.Window) => void`
* `getWindow`: `(name: string) => Gtk.Window`
* `closeWindow`: `(name: string) => void`
* `openWindow`: `(name: string) => void`
* `toggleWindow`: `(name: string) => void`
* `quit`: `() => void`
* `resetCss`: `() => void`
* `applyCss`: `(path: string) => void`
* `addIcons`: `(path: string) => void`

## Window toggled signal

```
// this is only signaled for windows exported in config.js

// or added with App.addWindow

const label = Widget.Label()

.hook(App, (self, windowName, visible) => {

self.label = `${windowName} is ${visible ? 'visible' : 'not visible'}`;

}, 'window-toggled')

});
```

## Applying CSS

If you want to change the style sheet on runtime

specifying a css file

```
App.applyCss('/path/to/file.css');
```

applying a stylesheet

```
App.applyCss(`

window {

background-color: transparent;

}

`)
```

to reset applied stylesheets

```
App.resetCss();
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/app.md)

[Previous
 Utils](/ags-docs/config/utils)   [Next
 Custom Service](/ags-docs/config/custom-service)
