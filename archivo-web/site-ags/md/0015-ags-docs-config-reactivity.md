---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/reactivity"
title: "Reactivity | AGS Wiki"
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
* [Property Bindings](#property-bindings)
* [Hooks](#hooks)
  + [Hook](#hook)
  + [On](#on)
  + [Poll](#poll)
  + [Keybind](#keybind)

## On this page

* [Overview](#_top)
* [Property Bindings](#property-bindings)
* [Hooks](#hooks)
  + [Hook](#hook)
  + [On](#on)
  + [Poll](#poll)
  + [Keybind](#keybind)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Reactivity

In order for widgets to have dynamic content we pass `Binding`s as properties
or setup a `hook`.
A `Binding` is just an object that holds information for widget constructors
to setup a listener.

Caution

`Binding` is a regular JavaScript object,
it cannot be used in template strings

```
const label = Variable("hello")

Label({

// [Object object] world

label: `${label.bind()} world`,

// hello world

label: label.bind().as(hello => `${hello} world`)

})
```

## Property Bindings

We can make a `Binding` from a Variable

```
const percent = Variable(0.5)

const slider = Widget.Slider({

value: percent.bind(),

onChange: ({ value }) => percent.value = value,

})
```

From a `Service`

```
const { speaker } = await Service.import("audio")

const slider = Widget.Slider({

value: speaker.bind("volume"),

onChange: ({ value }) => speaker.volume = value,

})
```

Merge any number of `Binding`s into another `Binding`

```
const a = Variable(0.3)

const b = Variable(0.7)

const merged = Utils.merge([a.bind(), b.bind()], (a, b) => {

return a * b

})

const level = Widget.LevelBar({

value: merged

})
```

Turn one or multiple Service signals into a `Binding`

```
const mpris = await Service.import("mpris")

const label = Widget.Label({

label: Utils.watch("initial-label", mpris, "player-added", (busName) => {

return `player ${busName} was added`

})

})

const label = Widget.Label({

label: Utils.watch("initial-label", [

[mpris, "player-added"],

[mpris, "player-removed"],

], (busName) => {

return `player ${busName} was added or removed`

})

})
```

A `Binding` can be transformed according to need

```
const num = Variable(0)

const label = Widget.Label({

// will throw an error, because number is not assignable to string

label: num.bind(),

// will have to be transformed

label: num.bind().as(n => n.toString()),

label: num.bind().as(String)

})
```

## Hooks

You can call these on any Widget that you have a reference on.
They will return `this` reference, meaning you
can chain them up in any order in any number.

```
const widget = Widget()

widget.hook()

widget.on()

widget.poll()

widget.keybind()
```

```
const widget = Widget()

.hook()

.on()
```

```
const widget = Widget({

setup: self => {

self.hook()

self.on()

}

})
```

```
const widget = Widget({

setup: self => self

.hook()

.on()

})
```

### Hook

`hook` will setup a listener to a `GObject` and will handle disconnection
when the widget is destroyed. It will connect
to the `changed` signal by default when not specified otherwise.

```
const battery = await Service.import("battery")

// .hook(GObject, callback, signal?)

const BatteryPercent = () => Label()

.hook(battery, self => {

self.label = `${battery.percent}%`

self.visible = battery.available

}, "changed")
```

Caution

A `hook` callback will be executed on startup.
If you are connecting to a signal that has an argument
you will need to check if its defined first

```
const mpris = await Service.import("mpris")

const label = Widget.Label().hook(mpris, (self, busName) => {

if (!busName)

return // skip startup execution

self.label = busName

}, "player-added")
```

### On

`on` is the same as `connect` but instead of the signal handler id,
it returns a reference to the widget. `on` will setup a callback on a widget signal.

These two are equivalent

```
function MyButton() {

const self = Widget.Button()

self.connect("clicked", () => {

print(self, "is clicked")

})

return self

}
```

```
const MyButton = () => Widget.Button()

.on("clicked", self => {

print(self, "is clicked")

})
```

Note

Most signals like `clicked` are available as a property on the widget.
So its rare that `.on` or `.connect` will be needed.

```
Widget.Button({

on_clicked: self => print(self, "was clicked")

})
```

### Poll

Avoid using this as much as possible, using this is considered bad practice.

These two are equivalent

```
function MyLabel() {

const self = Widget.Label()

Utils.interval(1000, () => {

self.label = Utils.exec('date')

}, self)

return self

}
```

```
const MyLabel = () => Widget.Label()

.poll(1000, self => {

self.label = Utils.exec('date')

})
```

### Keybind

It is possible to setup keybindings on focused widgets

```
// usually this way

Widget.Button().on("key-press-event", (self, event) => {

// check event for keys

})

// with .keybind()

Widget.Button().keybind(["MOD1", "CONTROL"], "a", (self, event) => {

print("alt+control+a was pressed")

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/reactivity.md)

[Previous
 First Widgets](/ags-docs/config/first-widgets)   [Next
 Theming](/ags-docs/config/theming)
