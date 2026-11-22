---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/services/hyprland"
title: "Hyprland | AGS Wiki"
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
* [Active](#active)
* [Example Widget](#example-widget)

## On this page

* [Overview](#_top)
* [signals](#signals)
* [properties](#properties)
* [methods](#methods)
* [Active](#active)
* [Example Widget](#example-widget)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Hyprland

## signals

* `event`: `(name: string, data: string)`: [hyprland ipc events](https://wiki.hyprland.org/IPC/#events-list)
* `urgent-window`: `(windowaddress: string)`
* `keyboard-layout`: `(keyboardname: string, layoutname: string)`
* `submap`: `(name: string)`
* `monitor-added`: `(name: string)`
* `monitor-removed`: `(name: string)`
* `workspace-added`: `(name: string)`
* `workspace-removed`: `(name: string)`
* `client-added`: `(address: string)`
* `client-removed`: `(address: string)`

## properties

* `active`: `Active` see below
* `monitors`: `Monitor[]` a Monitor is the object you would get with `hyprctl monitors -j`
* `workspaces`: `Workspace[]` a Workspace is the object you would get with `hyprctl workspaces -j`
* `clients`: `Client[]` a Client is the object you would get with `hyprctl clients -j`

## methods

* `getMonitor`: `(id: number) => Monitor`
* `getWorkspace`: `(id: number) => Workspace`
* `getClient`: `(address: string) => Client`
* `message`: `(msg: string) => string`: send a message to the [hyprland socket](https://wiki.hyprland.org/IPC/#tmphyprhissocketsock)
* `messageAsync`: `(msg: string) => Promise<string>`: async version of message

## Active

```
interface Active {

monitor: {

id: number

name: string

},

workspace: {

id: number

name: string

},

client: {

address: string

title: string

class: string

},

}
```

The `active` property is composed by subservices, meaning you connect to any sub prop

```
const widget = Widget({

setup: self => self

.hook(hyprland, self => {})

.hook(hyprland.active, self => {})

.hook(hyprland.active.monitor, self => {})

.hook(hyprland.active.workspace, self => {})

.hook(hyprland.active.client, self => {})

.bind('prop', hyprland, 'active', active => {})

.bind('prop', hyprland.active, 'monitor', monitor => {})

.bind('prop', hyprland.active, 'workspace', ws => {})

.bind('prop', hyprland.active, 'client', client => {})

.bind('prop', hyprland.active.monitor, 'id', id => {})

.bind('prop', hyprland.active.workspace, 'id', id => {})

.bind('prop', hyprland.active.client, 'address', address => {}),

})
```

## Example Widget

```
const hyprland = await Service.import('hyprland')

const focusedTitle = Widget.Label({

label: hyprland.active.client.bind('title'),

visible: hyprland.active.client.bind('address')

.as(addr => addr !== "0x"),

})

const dispatch = ws => hyprland.messageAsync(`dispatch workspace ${ws}`);

const Workspaces = () => Widget.EventBox({

onScrollUp: () => dispatch('+1'),

onScrollDown: () => dispatch('-1'),

child: Widget.Box({

children: Array.from({ length: 10 }, (_, i) => i + 1).map(i => Widget.Button({

attribute: i,

label: `${i}`,

onClicked: () => dispatch(i),

})),

// remove this setup hook if you want fixed number of buttons

setup: self => self.hook(hyprland, () => self.children.forEach(btn => {

btn.visible = hyprland.workspaces.some(ws => ws.id === btn.attribute);

})),

}),

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/services/hyprland.md)

[Previous
 Greetd](/ags-docs/services/greetd/)   [Next
 Mpris](/ags-docs/services/mpris/)
