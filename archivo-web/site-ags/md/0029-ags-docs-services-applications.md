---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/applications"
title: "Applications | AGS Wiki"
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
* [methods](#methods)
* [properties](#properties)
* [Application](#application)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example Applauncher](#example-applauncher)

## On this page

* [Overview](#_top)
* [signals](#signals)
* [methods](#methods)
* [properties](#properties)
* [Application](#application)
  + [properties](#properties-1)
  + [methods](#methods-1)
* [Example Applauncher](#example-applauncher)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Applications

## signals

* `changed` should emit when an app is installed or uninstalled but doesn’t always work

## methods

* `query`: `(string) => App[]` takes a string and returns a list of apps that match one of the following: app name, app description, executable name or .desktop file.
* `reload`: `() => void` explicitly reload the application `list`.

## properties

* `list`: `Application[]` a full list of available applications

## Application

### properties

* `app`: [Gio.DesktopAppInfo](https://gjs-docs.gnome.org/gio20~2.0/gio.desktopappinfo) the corresponding app info object
* `name`: `string` name of the app
* `desktop`: `string | null` the .desktop file
* `description`: `string | null` description of the app
* `executable`: `string` name of the executable binary
* `icon-name`: `string` the Icon entry in the corresponding .desktop file, can be a named icon or a path to an image
* `frequency`: ‘number’ number to take into consideration when sorting on `query` calls

### methods

* `launch`: `() => void` launches the app, you could also do `Utils.execAsync(['bash', '-c', app.executable])`, but the launch method keeps track of the frequency of launches which is used to sort the query
* `match`: `(string) => boolean` returns whether a search term matches the app
* `reload`: `() => void` rereads .desktop files

## [Example Applauncher](https://github.com/Aylur/ags/tree/main/example/applauncher)

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/applications.md)

[Previous
 Common Issues](/ags-docs/config/common-issues)   [Next
 Audio](/ags-docs/services/audio/)
