---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/subclassing-gtk-widgets"
title: "Subclassing GTK Widgets | AGS Wiki"
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
* [Using Gtk.Widgets not builtin](#using-gtkwidgets-not-builtin)
* [Custom Subclassing](#custom-subclassing)

## On this page

* [Overview](#_top)
* [Using Gtk.Widgets not builtin](#using-gtkwidgets-not-builtin)
* [Custom Subclassing](#custom-subclassing)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Subclassing GTK Widgets

## Using Gtk.Widgets not builtin

Use them like regular GTK widgets

```
import Gtk from 'gi://Gtk'

const calendar = new Gtk.Calendar({

showDayNames: false,

showHeading: true,

})
```

You can subclass Gtk.Widget not builtin to behave like AGS widgets.

```
const Calendar = Widget.subclass(Gtk.Calendar)

const myCalendar = Calendar({

showDayNames: false,

showHeading: true,

// now you can set AGS props

className: 'my-calendar',

setup(self) {

self.bind()

}

})
```

Tip

Calendar is available on `Widget`

Note

Open up an issue/PR if you want to see a widget to be available on `Widget` by default.

## Custom Subclassing

Usually in GTK custom widgets are achieved by subclassing.
The idea behind AGS is to use functions that create widgets
and utilize [closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures).

```
function CounterButton(({ color = 'aqua', ...rest })) {

const count = Variable(0)

const label = Widget.Label({

label: count.bind().as(v => `count: ${v}`),

style: `color: ${color}`,

})

return Widget.Button({

...rest, // spread passed parameters

child: label,

onClicked: () => count++,

})

}

// then simply call it

const button = CounterButton({

color: 'blue',

className: 'my-widget',

})
```

This approach comes with the limitation that parameters passed to these
functions are that, just parameters and not `GObject` properties.
If you still want to subclass, you can do so by subclassing
a Gtk.WIdget and registering it `Widget.register`.

```
class CounterButton extends Gtk.Button {

static {

Widget.register(this, {

properties: {

'count': ['int', 'rw']

}

})

}

// the super constructor will take care of setting the count prop

// so you don't have to explicitly set count in the constructor

constructor(props) {

super(props)

const label = new Gtk.Label({

label: `${this.count}`,

})

this.add(label)

this.connect('clicked', () => {

this.count++

label.label = `${this.count}`

})

}

get count() {

return this._count || 0

}

set count(num) {

this._count = num

this.notify('count')

}

}
```

You can now construct it like any other Gtk.Widget with the `new` keyword.

```
const counterButton = new CounterButton({

count: 0,

// you can set AGS widget props on it

className: '',

})

counterButton.connect('notify::count', ({ count }) => {

print(count);

})

counterButton.count += 1
```

Tip

You will never actually need to subclass, you can *fake* gobject props using Variables

```
function CounterButton({ count, ...props }) {

const counter = Variable(count)

const button = Widget.Button({

on_clicked: () => counter.value += 1,

child: Widget.Label({

label: counter.bind().as(c => `${c}`),

}),

...props,

})

return Object.assign(button, {

count: counter,

})

}

const counterButton = CounterButton({

count: 0,

})

counterButton.count.connect("changed", ({ value }) => {

print(value)

})

counterButton.count.value += 1
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/subclassing-gtk-widgets.md)

[Previous
 Custom Service](/ags-docs/config/custom-service)   [Next
 Examples](/ags-docs/config/examples)
