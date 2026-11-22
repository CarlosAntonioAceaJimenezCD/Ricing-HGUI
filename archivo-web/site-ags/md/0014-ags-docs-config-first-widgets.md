---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/first-widgets"
title: "Your First Widget | AGS Wiki"
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
* [Top Level: Window](#top-level-window)
* [Reusable Widgets](#reusable-widgets)
* [Dynamic Content](#dynamic-content)
* [Signals](#signals)
* [Avoiding external scripts](#avoiding-external-scripts)

## On this page

* [Overview](#_top)
* [Top Level: Window](#top-level-window)
* [Reusable Widgets](#reusable-widgets)
* [Dynamic Content](#dynamic-content)
* [Signals](#signals)
* [Avoiding external scripts](#avoiding-external-scripts)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Your First Widget

Start by creating `~/.config/ags/config.js`

~/.config/ags/config.js

```
App.config({

windows: [

// this is where window definitions will go

]

})
```

then run `ags` in the terminal

Terminal window

```
ags
```

You will see nothing happen, just AGS hanging,
this is because you have an empty config.
Running `ags` will execute the config like a regular script,
it is just a library over GTK, and its on **you** to program your windows and widgets.

Tip

run `ags --init` to generate a `tsconfig.json` and **symlink** the generated types,
that will provide typesafety and autosuggestions

## Top Level: Window

The top level container is a Window that will hold widgets.

```
const myLabel = Widget.Label({

label: 'some example content',

})

const myBar = Widget.Window({

name: 'bar',

anchor: ['top', 'left', 'right'],

child: myLabel,

})

App.config({ windows: [myBar] })
```

Tip

GObject properties can be accessed or set in several ways:
with `camelCase`, `snake_case`, and `kebab-case`

```
const w = Widget({

className: 'my-label',

class_name: 'my-label',

'class-name': 'my-label',

})

w.className = ''

w.class_name = ''

w['class-name'] = ''

w['className'] = ''

w['class_name'] = ''
```

## Reusable Widgets

Both `myLabel` and `myBar` constants we declared are a **single instance**
of a `Gtk.Widget`. What if you have two monitors and want to have
a bar for each? Make a function that returns a `Gtk.Widget` instance.

```
function Bar(monitor = 0) {

const myLabel = Widget.Label({

label: 'some example content',

})

return Widget.Window({

monitor,

name: `bar${monitor}`, // this name has to be unique

anchor: ['top', 'left', 'right'],

child: myLabel,

})

}

App.config({

windows: [

Bar(0), // can be instantiated for each monitor

Bar(1),

],

})
```

Note

The `name` attribute only has to be unique,
if it is passed to `windows` in the exported object.

Calling `Widget.Window` will create and show the window by default.
It is not necessary to pass a reference to `windows` in
the config object, but if it is not,
it can’t be toggled with `ags --toggle-window` or through `App.toggleWindow`

## Dynamic Content

Alright, but **static** text is boring, let’s make it **dynamically** change by updating the label every second with a `date`.

```
function Bar(monitor = 0) {

const myLabel = Widget.Label({

label: 'some example content',

})

Utils.interval(1000, () => {

myLabel.label = Utils.exec('date')

})

return Widget.Window({

monitor,

name: `bar${monitor}`,

anchor: ['top', 'left', 'right'],

child: myLabel,

})

}
```

Note

JavaScript is **single threaded** and `exec` is a **blocking operation**,
for a `date` call it’s fine, but usually you want to use its **async** version: `execAsync`.

Looking great, but that code has too much boilerplate.
Let’s use a [fat arrow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
instead of the `function` keyword, and instead of calling `interval`
let’s use the `poll` method.

```
const Bar = (monitor = 0) => Widget.Window({

monitor,

name: `bar${monitor}`,

anchor: ['top', 'left', 'right'],

child: Widget.Label()

.poll(1000, label => label.label = Utils.exec('date')),

})
```

Tip

That is still not the best solution, because when you instantiate multiple
instances of `Bar` each will call `exec` separately.
What you want to do is move the date into a `Variable` and `bind` it.

```
const date = Variable('', {

poll: [1000, 'date'],

})

const Bar = () => Widget.Window({

name: 'bar',

anchor: ['top', 'left', 'right'],

child: Widget.Label({ label: date.bind() })

})
```

## Signals

Usually it is best to avoid polling. Rule of thumb: the less intervals the better.
This is where `GObject` shines. We can use **signals** for pretty much everything.

anytime `myVariable.value` changes it will send a signal
and things can react to it

```
const myVariable = Variable(0)
```

for example execute a callback

```
myVariable.connect('changed', ({ value }) => {

print('myVariable changed to ' + `${value}`)

})
```

**bind** its value to a widget’s property

```
const bar = Widget.Window({

name: 'bar',

anchor: ['top', 'left', 'right'],

child: Widget.Label({

label: myVariable.bind().as(v => `value: ${v}`)

}),

})
```

incrementing the `value` causes the label to update and the callback to execute

```
myVariable.value++
```

For example with `pactl` it is possible to query information about the volume level,
but we don’t want to have an interval that checks it periodically.
We want a **signal** that signals every time its **changed**,
so that we only do operations when its needed, and therefore we don’t waste resources.
`pactl subscribe` writes to stdout everytime there is a **change**.

```
const pactl = Variable({ count: 0, msg: '' }, {

listen: ['pactl subscribe', (msg) => ({

count: pactl.value.count + 1,

msg: msg,

})],

})

pactl.connect('changed', ({ value }) => {

print(value.msg, value.count)

})

const label = Widget.Label({

label: pactl.bind().as(({ count, msg }) => {

return `${msg} ${count}`

}),

})

// widgets are GObjects too

label.connect('notify::label', ({ label }) => {

print('label changed to ', label)

})
```

## Avoiding external scripts

For *most* of your system, you don’t have to use external
scripts and binaries to query information.
AGS has builtin [Services](../services).
They are just like [Variables](../variables) but instead
of a single `value` they have more attributes and methods on them.

```
const battery = await Service.import('battery')

const batteryProgress = Widget.CircularProgress({

value: battery.bind('percent').as(p => p / 100),

child: Widget.Icon({

icon: battery.bind('icon_name'),

}),

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/first-widgets.md)

[Previous
 JavaScript](/ags-docs/config/javascript)   [Next
 Reactivity](/ags-docs/config/reactivity)
