---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/widgets"
title: "Widgets | AGS Wiki"
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
* [Setup property](#setup-property)
* [Attribute property](#attribute-property)
* [Common Gtk properties](#common-gtk-properties)
* [toggleClassName](#toggleclassname)
  + [Window](#window)
  + [Box](#box)
  + [Button](#button)
  + [Calendar](#calendar)
  + [CenterBox](#centerbox)
  + [CircularProgress](#circularprogress)
  + [ColorButton](#colorbutton)
  + [DrawingArea](#drawingarea)
  + [Entry](#entry)
  + [EventBox](#eventbox)
  + [FileChooserButton](#filechooserbutton)
  + [Fixed](#fixed)
  + [FlowBox](#flowbox)
  + [FontButton](#fontbutton)
  + [Icon](#icon)
  + [Label](#label)
  + [LevelBar](#levelbar)
  + [ListBox](#listbox)
  + [Menu](#menu)
  + [MenuBar](#menubar)
  + [MenuItem](#menuitem)
  + [Overlay](#overlay)
  + [ProgressBar](#progressbar)
  + [Revealer](#revealer)
  + [Scrollable](#scrollable)
  + [Separator](#separator)
  + [Slider](#slider)
  + [SpinButton](#spinbutton)
  + [Spinner](#spinner)
  + [Stack](#stack)
  + [Switch](#switch)
  + [ToggleButton](#togglebutton)

## On this page

* [Overview](#_top)
* [Setup property](#setup-property)
* [Attribute property](#attribute-property)
* [Common Gtk properties](#common-gtk-properties)
* [toggleClassName](#toggleclassname)
  + [Window](#window)
  + [Box](#box)
  + [Button](#button)
  + [Calendar](#calendar)
  + [CenterBox](#centerbox)
  + [CircularProgress](#circularprogress)
  + [ColorButton](#colorbutton)
  + [DrawingArea](#drawingarea)
  + [Entry](#entry)
  + [EventBox](#eventbox)
  + [FileChooserButton](#filechooserbutton)
  + [Fixed](#fixed)
  + [FlowBox](#flowbox)
  + [FontButton](#fontbutton)
  + [Icon](#icon)
  + [Label](#label)
  + [LevelBar](#levelbar)
  + [ListBox](#listbox)
  + [Menu](#menu)
  + [MenuBar](#menubar)
  + [MenuItem](#menuitem)
  + [Overlay](#overlay)
  + [ProgressBar](#progressbar)
  + [Revealer](#revealer)
  + [Scrollable](#scrollable)
  + [Separator](#separator)
  + [Slider](#slider)
  + [SpinButton](#spinbutton)
  + [Spinner](#spinner)
  + [Stack](#stack)
  + [Switch](#switch)
  + [ToggleButton](#togglebutton)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Widgets

`Widget` functions return an instance of [Gtk.Widget](https://gjs-docs.gnome.org/gtk30~3.0/gtk.widget).
Most common widgets are subclassed and have a few additional properties.

These widgets have some additional properties on top of the base Gtk.Widget ones:

| Property | Type | Description |
| --- | --- | --- |
| class-name | `string` | List of class CSS selectors separated by white space. |
| class-names | `Array<string>` | List of class CSS selectors. |
| css | `string` | Inline CSS. e.g `label { color: white; }`. If no selector is specified `*` will be assumed. e.g `color: white;` will be inferred as `*{ color: white; }`. |
| hpack | `string` | Horizontal alignment, behaves like `halign`. `halign` takes an enum, but for convenience `hpack` can be given with a string, so one of `"start"`, `"center"`, `"end"`, `"fill"`. |
| vpack | `string` | Vertical alignment. |
| cursor | `string` | Cursor style when hovering over widgets that have hover states, e.g it won’t work on labels. [list of valid values](https://docs.gtk.org/gdk3/ctor.Cursor.new_from_name.html). |
| attribute | `any` | Any additional attributes on `self` |
| setup | `(self) => void` | A callback function to execute on `self` |

## Setup property

`setup` is a convenience prop to have imperative code inside declarative blocks

without `setup`

```
function MyWidget() {

const self = Widget.Button()

// imperative code

return self

}
```

using `setup`

```
const MyWidget = () => Widget.Button({

setup: self => {

// imperative code

}

})
```

## Attribute property

for attaching additional attributes on widgets `Object.assign` or
the `attribute` property can be used

```
function MyWidget() {

const self = Widget.Button()

return Object.assign(self, {

myPrimitiveProperty: "anything",

myObjectProperty: {

something: "anything",

key: "value",

},

})

}

const mywidget = MyWidget()

console.log(mywidget.myPrimitiveProperty) // anything

console.log(mywidget.myObjectProperty) // { something: "anything", key: "value" }
```

using `attribute` has the benefit of it being a gobject
which means it will signal `notify::attribute` when it changes

```
const MyWidget = () => Widget.Button({

attribute: "anything",

setup: self => self.on("notify::attribute", () => {

console.log(mywidget.attribute)

}),

})

const mywidget = MyWidget()

console.log(mywidget.attribute) // anything

// this line will invoke the above console.log in the setup

mywidget.attribute = "something else"
```

keep in mind that `attribute` will only signal if *its value* changes

```
const MyWidget = () => Widget.Button({

attribute: {

someKey: "value",

key: "value",

},

setup: self => self.on("notify::attribute", () => {

console.log(mywidget.attribute)

})

})

const mywidget = MyWidget()

// this line won't signal, because the attribute is still the same object

mywidget.attribute.key = "new value"

// to have it signal, assign a new object to it

mywidget.attribute = {

...mywidget.attribute,

key: "new value"

}
```

## Common Gtk properties

Some common Gtk.Widget properties you might want for example

| Property | Type | Description |
| --- | --- | --- |
| hexpand | `boolean` | Expand horizontally. |
| vexpand | `boolean` | Expand vertically. |
| sensitive | `boolean` | Makes the widget interactable. |
| tooltip-text | `string` | Tooltip popup when the widget is hovered over. |
| visible | `boolean` | Visibility of the widget. Setting this to `false` doesn’t have any effect if the parent container calls `show_all()`, for example when you set a Box’s children dynamically. |

## toggleClassName

If you don’t want to mutate the `classNames` array,
there is `toggleClassName`: `(name: string, enable: boolean) => void`

```
const label = Widget.Label('example-label')

// add class name

label.toggleClassName('my-awesome-label', true)

// remove class name

label.toggleClassName('my-awesome-label', false)
```

The properties listed here are just the additional properties on top of their
base Gtk.Widget classes. [Refer to the Gtk3 docs](https://gjs-docs.gnome.org/gtk30~3.0/)
for the rest of them.

### Window

subclass of [Gtk.Window](https://gjs-docs.gnome.org/gtk30~3.0/gtk.window)

the toplevel widget that holds everything

| Property | Type | Description |
| --- | --- | --- |
| child | `Widget` |  |
| name | `string` | Name of the window. This has to be unique, if you pass it in config. This will also be the name of the layer. |
| anchor | `string[]` | Valid values are `"top"`, `"bottom"`, `"left"`, `"right"`. Anchor points of the window. Leave it empty to make it centered. |
| exclusivity | `string` | Specify if the compositor should reserve space for the window automatically or how the window should interact with windows that do. Possible values: `exclusive` (space should be reserved), `normal` (the window should move if occluding another), `ignore` (the window should not be moved). Default: `normal`. |
| layer | `string` | Valid values are `"overlay"`, `"top"`, `"bottom"`, `"background"`. It is `"top"` by default. |
| margins | `number[]` | Corresponds to CSS notation: `[TOP, RIGHT, BOTTOM, LEFT]`, also `[0, 6]` would have 0 margin on the top and bottom and would have 6 on the right and left. |
| monitor | `number` | Which monitor to show the window on. If it is left undefined the window will show on the currently focused monitor. |
| keymode | `string` | Valid values are `"none"`, `"on-demand"`: can receive keyboard input if focused, `"exclusive"`: steal keyboard input on top and overlay layers |
| gdkmonitor | `Gdk.Monitor` | alternative to `monitor` |

```
const window = Widget.Window({

name: 'window-name',

anchor: ['top', 'left', 'right'],

exclusivity: 'normal',

keymode: 'on-demand',

layer: 'top',

margins: [0, 6],

monitor: 0,

child: Widget.Label('hello'),

})
```

### Box

subclass of [Gtk.Box](https://gjs-docs.gnome.org/gtk30~3.0/gtk.box)

the main container widget

| Property | Type | Description |
| --- | --- | --- |
| vertical | `bool` | setting `vertical: true` is the same as `orientation: 1` |
| children | `Widget[]` | List of child widgets. |

```
const box = Widget.Box({

spacing: 8,

homogeneous: false,

vertical: false,

children: [

// widgets

]

})
```

### Button

subclass of [Gtk.Button](https://gjs-docs.gnome.org/gtk30~3.0/gtk.button)

`on-clicked` will be executed on `Enter` if the button and its window has focus

| Property | Type |
| --- | --- |
| child | `Widget` |
| on-clicked | `() => void` |
| on-primary-click | `(event: Gdk.Event) => boolean` |
| on-secondary-click | `(event: Gdk.Event) => boolean` |
| on-middle-click | `(event: Gdk.Event) => boolean` |
| on-primary-click-release | `(event: Gdk.Event) => boolean` |
| on-secondary-click-release | `(event: Gdk.Event) => boolean` |
| on-middle-click-release | `(event: Gdk.Event) => boolean` |
| on-hover | `(event: Gdk.Event) => boolean` |
| on-hover-lost | `(event: Gdk.Event) => boolean` |
| on-scroll-up | `(event: Gdk.Event) => boolean` |
| on-scroll-down | `(event: Gdk.Event) => boolean` |

```
const button = Widget.Button({

child: Widget.Label('click me!'),

onClicked: () => print('hello'),

})
```

### Calendar

subclass of [Gtk.Calendar](https://gjs-docs.gnome.org/gtk30~3.0/gtk.calendar)

| Property | Type | Description |
| --- | --- | --- |
| date | `[number, number, number]` | readonly [year, month, day] |
| detail | `(number, number, number) => string | null` |  |
| on-day-selected | `() => void` |  |

```
const calendar = Widget.Calendar({

showDayNames: true,

showDetails: true,

showHeading: true,

showWeekNumbers: true,

detail: (self, y, m, d) => {

return `<span color="white">${y}. ${m}. ${d}.</span>`

},

onDaySelected: ({ date: [y, m, d] }) => {

print(`${y}. ${m}. ${d}.`)

},

})
```

### CenterBox

subclass of [Gtk.Box](https://gjs-docs.gnome.org/gtk30~3.0/gtk.box)

| Property | Type | Description |
| --- | --- | --- |
| vertical | `bool` | setting `vertical: true` is the same as `orientation: 1` |
| start-widget | `Gtk.Widget` |  |
| center-widget | `Gtk.Widget` |  |
| end-widget | `Gtk.Widget` |  |

```
const centerBox = Widget.CenterBox({

spacing: 8,

vertical: false,

startWidget: Widget.Label('left widget'),

centerWidget: Widget.Label('center widget'),

endWidget: Widget.Label('right widget'),

})
```

### CircularProgress

subclass of [Gtk.Bin](https://gjs-docs.gnome.org/gtk30~3.0/gtk.bin)

| Property | Type | Description |
| --- | --- | --- |
| start-at | `number` | Number between 0 and 1, e.g 0.75 is the top |
| end-at | `number` | Number between 0 and 1 |
| inverted | `boolean` |  |
| rounded | `boolean` | Wether the progress bar should have rounded ends |
| value | `number` | Number between 0 and 1 |

```
const progress = Widget.CircularProgress({

css: 'min-width: 50px;'  // its size is min(min-height, min-width)

+ 'min-height: 50px;'

+ 'font-size: 6px;' // to set its thickness set font-size on it

+ 'margin: 4px;' // you can set margin on it

+ 'background-color: #131313;' // set its bg color

+ 'color: aqua;', // set its fg color

rounded: false,

inverted: false,

startAt: 0.75,

value: battery.bind('percent').as(p => p / 100),

child: Widget.Icon({

icon: battery.bind('icon-name'),

}),

})
```

### ColorButton

subclass of [Gtk.ColorButton](https://gjs-docs.gnome.org/gtk30~3.0/gtk.colorbutton)

| Property | Type |
| --- | --- |
| on-color-set | `() => void` |

```
const colorbutton = Widget.ColorButton({

onColorSet: ({ rgba: { red, green, blue, alpha } }) => {

print(`rgba(${red * 255}, ${green * 255}, ${blue * 255}, ${alpha})`)

},

})
```

### DrawingArea

subclass of [Gtk.DrawingArea](https://gjs-docs.gnome.org/gtk30~3.0/gtk.drawingarea)

| Property | Type |
| --- | --- |
| draw-fn | `(cr: Cairo.Context, width: number, height: number) => void` |

```
const drawingarea = Widget.DrawingArea({

widthRequest: 50,

heightRequest: 50,

drawFn: (self, cr, w, h) => {

const center = {

x: w / 2,

y: h / 2,

};

cr.setSourceRGBA(1, 1, 1, 1)

cr.setLineWidth(8)

cr.arc(center.x, center.y, 2, 0, Math.PI * 2)

cr.stroke()

},

})
```

### Entry

subclass of [Gtk.Entry](https://gjs-docs.gnome.org/gtk30~3.0/gtk.entry)

| Property | Type |
| --- | --- |
| on-change | `() => void` |
| on-accept | `() => void` |

```
const entry = Widget.Entry({

placeholder_text: 'type here',

text: 'initial text',

visibility: true, // set to false for passwords

onAccept: ({ text }) => print(text),

})
```

### EventBox

subclass of [Gtk.EventBox](https://gjs-docs.gnome.org/gtk30~3.0/gtk.eventbox)

| Property | Type |
| --- | --- |
| child | `Widget` |
| on-primary-click | `(event: Gdk.Event) => boolean` |
| on-secondary-click | `(event: Gdk.Event) => boolean` |
| on-middle-click | `(event: Gdk.Event) => boolean` |
| on-primary-click-release | `(event: Gdk.Event) => boolean` |
| on-secondary-click-release | `(event: Gdk.Event) => boolean` |
| on-middle-click-release | `(event: Gdk.Event) => boolean` |
| on-hover | `(event: Gdk.Event) => boolean` |
| on-hover-lost | `(event: Gdk.Event) => boolean` |
| on-scroll-up | `(event: Gdk.Event) => boolean` |
| on-scroll-down | `(event: Gdk.Event) => boolean` |

### FileChooserButton

subclass of [Gtk.FileChooserButton](https://gjs-docs.gnome.org/gtk30~3.0/gtk.filechooserbutton)

| Property | Type | Description |
| --- | --- | --- |
| on-file-set | `() => void` |  |
| uri | `() => void` | convenience getter for `get_uri` |
| uris | `() => void` | convenience getter for `get_uris` |

```
const fbutton = Widget.FileChooserButton({

onFileSet: ({ uri }) => {

print(uri)

},

})
```

### Fixed

subclass of [Gtk.Fixed](https://gjs-docs.gnome.org/gtk30~3.0/gtk.fixed)

Note

`Gtk.Fixed` is not yet subclassed to be declarative and doesn’t have
any additional properties/methods on top of the base Gtk widget.

```
const fixed = Widget.Fixed({

setup(self) {

self.put(Widget.Label('hello'), 0, 0)

self.put(Widget.Label('hello'), 50, 50)

},

})
```

### FlowBox

subclass of [Gtk.FlowBox](https://gjs-docs.gnome.org/gtk30~3.0/gtk.flowbox)

Note

`Gtk.FlowBox` is not yet subclassed to be declarative and doesn’t have
any additional properties/methods on top of the base Gtk widget.

```
const flowbox = Widget.FlowBox({

setup(self) {

self.add(Widget.Label('hello'))

},

})
```

### FontButton

subclass of [Gtk.FontButton](https://gjs-docs.gnome.org/gtk30~3.0/gtk.fontbutton)

| Property | Type | Description |
| --- | --- | --- |
| on-font-set | `() => void` |  |

```
const fontbutton = Widget.FontButton({

onFontSet: ({ font }) => {

print(font)

},

})
```

### Icon

subclass of [Gtk.Image](https://gjs-docs.gnome.org/gtk30~3.0/gtk.image)

| Property | Type | Description |
| --- | --- | --- |
| icon | `string` | Name of an icon or path to a file |
| size | `number` | Forced size |

```
Widget.Icon({ icon: 'dialog-information-symbolic' })

// if you only want an icon, it can be shortened like this

Widget.Icon('dialog-information-symbolic')

// if you don't set a size, it will be computed from css font-size

Widget.Icon({

icon: 'dialog-information-symbolic',

css: 'font-size: 30px',

})

// NOTE:

// setting the icon dynamically has a flicker currently

// to fix it, use a forced size

Widget.Icon({

icon: 'dialog-information-symbolic',

size: 30,

})
```

### Label

subclass of [Gtk.Label](https://gjs-docs.gnome.org/gtk30~3.0/gtk.label)

| Property | Type | Description |
| --- | --- | --- |
| justification | `string` | Valid values are `"left"`, `"center"`, `"right"`, `"fill"`. Same as `justify` but represented as a string instead of enum. |
| truncate | `string` | Valid values are `"none"`, `"start"`, `"middle"`, `"end"`. Same as `ellipsize` but represented as a string instead of enum. |

```
const label = Widget.Label({

label: 'some text to show',

justification: 'left',

truncate: 'end',

xalign: 0,

maxWidthChars: 24,

wrap: true,

useMarkup: true,

})

// shorthand for { label: 'hello' }

Widget.Label('hello')
```

### LevelBar

subclass of [Gtk.LevelBar](https://gjs-docs.gnome.org/gtk30~3.0/gtk.levelbar)

| Property | Type | Description |
| --- | --- | --- |
| bar-mode | `string` | Valid values are `"continuous"`, `"discrete"`. Same as `mode` but represented as a string instead of enum. |
| vertical | `bool` | setting `vertical: true` is the same as `orientation: 1` |

```
const continuous = Widget.LevelBar({

widthRequest: 100,

value: battery.bind("percent").as(p => p / 100),

})

const discrete = Widget.LevelBar({

widthRequest: 100,

bar_mode: "discrete",

max_value: 10,

value: battery.bind("percent").as(p => p / 10),

})
```

### ListBox

subclass of [Gtk.ListBox](https://gjs-docs.gnome.org/gtk30~3.0/gtk.listbox)

Note

`Gtk.ListBox` is not yet subclassed to be declarative and doesn’t have
any additional properties/methods on top of the base Gtk widget.

```
const listbox = Widget.ListBox({

setup(self) {

self.add(Widget.Label('hello'))

},

})
```

### Menu

subclass of [Gtk.Menu](https://gjs-docs.gnome.org/gtk30~3.0/gtk.menu)

| Property | Type |
| --- | --- |
| children | `MenuItem[]` |
| on-popup | `(flipped_rect: void, final_rect: void, flipped_x: boolean, flipped_y: boolean) => void` |
| on-move-scroll | `(scroll_type: Gtk.ScrollType) => void` |

```
function RightClickMenu() {

const menu = Widget.Menu({

children: [

Widget.MenuItem({

child: Widget.Label('hello'),

}),

],

})

return Widget.Button({

on_primary_click: (_, event) => {

menu.popup_at_pointer(event)

},

})

}
```

### MenuBar

subclass of [Gtk.MenuBar](https://gjs-docs.gnome.org/gtk30~3.0/gtk.menubar)

Note

`Gtk.MenuBar` is not yet subclassed to be declarative and doesn’t have
any additional properties/methods on top of the base Gtk widget.

```
const menubar = Widget.MenuBar({

setup: self => {

self.append(Widget.Menu())

}

})
```

### MenuItem

subclass of [Gtk.MenuItem](https://gjs-docs.gnome.org/gtk30~3.0/gtk.menuitem)

| Property | Type |
| --- | --- |
| child | `Widget` |
| on-activate | `() => boolean` |
| on-select | `() => boolean` |
| on-deselect | `() => boolean` |

```
const menu = Widget.Menu({

children: [

Widget.MenuItem({

child: Widget.Label('hello'),

onActivate: () => {

print('clicked')

}

}),

],

})
```

### Overlay

subclass of [Gtk.Overlay](https://gjs-docs.gnome.org/gtk30~3.0/gtk.overlay)
Takes the size of its first child, then places subsequent children on
top of each other and won’t render them outside the container.

| Property | Type | Description |
| --- | --- | --- |
| child | `Widget` | Child which will determine the size of the overlay |
| overlays | `Widget[]` | Overlayed children |
| pass-through | `boolean` | Whether the overlay childs should pass the input through |

### ProgressBar

subclass of [Gtk.ProgressBar](https://gjs-docs.gnome.org/gtk30~3.0/gtk.progressbar)

Note

You might want to use `LevelBar` instead.

| Property | Type | Description |
| --- | --- | --- |
| vertical | `bool` | Setting `vertical: true` is the same as `orientation: 1` |
| value | `number` | Same as `ProgressBar.fraction` |

```
const progressbar = Widget.ProgressBar({

value: battery.bind("percent").as(p => p / 100),

})
```

### Revealer

subclass of [Gtk.Revealer](https://gjs-docs.gnome.org/gtk30~3.0/gtk.revealer)

| Property | Type | Description |
| --- | --- | --- |
| child | `Widget` |  |
| transition | `string` | Valid values are `"none"`, `"crossfade"`, `"slide_left"`, `"slide_right"`, `"slide_down"`, `"slide_up"`. This is `transitionType` represented as a string instead of enum. |

```
const revealer = Widget.Revealer({

revealChild: false,

transitionDuration: 1000,

transition: 'slide_right',

child: Widget.Label('hello!'),

setup: self => self.poll(2000, () => {

self.reveal_child = !self.reveal_child;

}),

})
```

### Scrollable

subclass of [Gtk.ScrolledWindow](https://gjs-docs.gnome.org/gtk30~3.0/gtk.scrolledwindow)

| Property | Type | Description |
| --- | --- | --- |
| child | `Widget` |  |
| hscroll | `string` | Valid values are `"always`, `"automatic"`, `"external"`, `"never"`. |
| vscroll | `string` | Valid values are `"always`, `"automatic"`, `"external"`, `"never"`. |

```
const scrollable = Widget.Scrollable({

hscroll: 'always',

vscroll: 'never',

css: 'min-width: 20px;',

child: Widget.Label('Lorem ipsum dolor sit amet, ' +

'officia excepteur ex fugiat reprehenderit enim ' +

'labore culpa sint ad nisi Lorem pariatur mollit'),

})
```

### Separator

subclass of [Gtk.Separator](https://gjs-docs.gnome.org/gtk30~3.0/gtk.separator)

| Property | Type | Description |
| --- | --- | --- |
| vertical | `bool` | Setting `vertical: true` is the same as `orientation: 1` |

```
const separator = Widget.Separator({

vertical: false,

})
```

### Slider

subclass of [Gtk.Scale](https://gjs-docs.gnome.org/gtk30~3.0/gtk.scale)

| Property | Type | Description |
| --- | --- | --- |
| vertical | `bool` | Setting `vertical: true` is the same as `orientation: 1` |
| value | `number` |  |
| min | `number` |  |
| max | `number` |  |
| marks | `tuple` or `number` | where tuple is `[number, string?, Position?]`, Position is `"top"`, `"left`, `"right`, `"bottom"` |
| on-change | `(event: Gdk.Event) => void` |  |

```
Widget.Slider({

onChange: ({ value }) => print(value),

vertical: true,

value: 0,

min: 0,

max: 1,

marks: [

1,

2,

[3, 'label'],

[4, 'label', 'bottom'],

],

})
```

### SpinButton

subclass of [Gtk.SpinButton](https://gjs-docs.gnome.org/gtk30~3.0/gtk.spinbutton)

| Property | Type |
| --- | --- |
| on-value-changed | `() => void` |
| range | `[min: number, max: number]` |
| increments | `[step: number, page: number]` |

```
const spinbutton = Widget.SpinButton({

range: [0, 100],

increments: [1, 5],

onValueChanged: ({ value }) => {

print(value)

},

})
```

### Spinner

subclass of [Gtk.Spinner](https://gjs-docs.gnome.org/gtk30~3.0/gtk.Spinner)
spinning icon showing that something is loading

```
const spinner = Widget.Spinner()
```

### Stack

subclass of [Gtk.Stack](https://gjs-docs.gnome.org/gtk30~3.0/gtk.stack)

| Property | Type | Description |
| --- | --- | --- |
| children | `{ [string]: Widget }` | name, Widget key-value pairs |
| shown | `string` | Name of the widget to show. This can’t be set on construction, instead the first given widget will be shown. |
| transition | `string` | `transitionType` represented as a string. Valid values are `none`, `crossfade`, `slide_right`, `slide_left`, `slide_up`, `slide_down`, `slide_left_right`, `slide_up_down`, `over_up`, `over_down`, `over_left`, `over_right`, `under_up`, `under_down`, `under_left`, `under_right`, `over_up_down`, `over_down_up`, `over_left_right`, `over_right_left` |

```
const stack = Widget.Stack({

children: {

'child1': Widget.Label('first child'),

'child2': Widget.Label('second child'),

},

shown: 'child2',

})
```

### Switch

subclass of [Gtk.Switch](https://gjs-docs.gnome.org/gtk30~3.0/gtk.switch)

| Property | Type |
| --- | --- |
| on-activate | `() => void` |

```
const switch = Widget.Switch({

onActivate: ({ active }) => print(active),

})
```

### ToggleButton

subclass of [Gtk.ToggleButton](https://gjs-docs.gnome.org/gtk30~3.0/gtk.togglebutton)

| Property | Type |
| --- | --- |
| on-toggled | `() => void` |

```
const togglebutton = Widget.ToggleButton({

onToggled: ({ active }) => print(active),

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/widgets.md)

[Previous
 CLI](/ags-docs/config/cli)   [Next
 Variables](/ags-docs/config/variables)
