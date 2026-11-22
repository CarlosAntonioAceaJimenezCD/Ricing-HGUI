---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/custom-service"
title: "Custom Service | AGS Wiki"
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
  + [Usage](#usage)

## On this page

* [Overview](#_top)
  + [Usage](#usage)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Custom Service

Writing a custom Service is as simple as

* declaring a class
* defining its signals and properties
* declaring get/set for properties

This is an example Service for backlight using `brightnessctl`
to set the brightness and `Utils.monitorFile` to watch for changes.

brightness.js

```
class BrightnessService extends Service {

// every subclass of GObject.Object has to register itself

static {

// takes three arguments

// the class itself

// an object defining the signals

// an object defining its properties

Service.register(

this,

{

// 'name-of-signal': [type as a string from GObject.TYPE_<type>],

'screen-changed': ['float'],

},

{

// 'kebab-cased-name': [type as a string from GObject.TYPE_<type>, 'r' | 'w' | 'rw']

// 'r' means readable

// 'w' means writable

// guess what 'rw' means

'screen-value': ['float', 'rw'],

},

);

}

// this Service assumes only one device with backlight

#interface = Utils.exec("sh -c 'ls -w1 /sys/class/backlight | head -1'");

// # prefix means private in JS

#screenValue = 0;

#max = Number(Utils.exec('brightnessctl max'));

// the getter has to be in snake_case

get screen_value() {

return this.#screenValue;

}

// the setter has to be in snake_case too

set screen_value(percent) {

if (percent < 0)

percent = 0;

if (percent > 1)

percent = 1;

Utils.execAsync(`brightnessctl set ${percent * 100}% -q`);

// the file monitor will handle the rest

}

constructor() {

super();

// setup monitor

const brightness = `/sys/class/backlight/${this.#interface}/brightness`;

Utils.monitorFile(brightness, () => this.#onChange());

// initialize

this.#onChange();

}

#onChange() {

this.#screenValue = Number(Utils.exec('brightnessctl get')) / this.#max;

// signals have to be explicitly emitted

this.emit('changed'); // emits "changed"

this.notify('screen-value'); // emits "notify::screen-value"

// or use Service.changed(propName: string) which does the above two

// this.changed('screen-value');

// emit screen-changed with the percent as a parameter

this.emit('screen-changed', this.#screenValue);

}

// overwriting the connect method, let's you

// change the default event that widgets connect to

connect(event = 'screen-changed', callback) {

return super.connect(event, callback);

}

}

// the singleton instance

const service = new BrightnessService;

// export to use in other modules

export default service;
```

Caution

`Utils.monitorFile` only reports events that a user-space program
triggers through the filesystem API. As a result, it does not catch
remote events that occur on network filesystems.
Furthermore, most pseudo-filesystems such as `/proc`, `/sys` and `/dev/pts`
cannot be monitored.

Note

For `bind` to work, the property has to be defined in `Service.register`

### Usage

Using it with widgets is as simple as using the builtin ones.

```
import brightness from './brightness.js';

const slider = Widget.Slider({

on_change: self => brightness.screen_value = self.value,

value: brightness.bind('screen-value'),

});

const label = Label({

label: brightness.bind('screen-value').as(v => `${v}`),

setup: self => self.hook(brightness, (self, screenValue) => {

// screenValue is the passed parameter from the 'screen-changed' signal

self.label = screenValue ?? 0;

// NOTE:

// since hooks are run upon construction

// the passed screenValue will be undefined the first time

// all three are valid

self.label = `${brightness.screenValue}`;

self.label = `${brightness.screen_value}`;

self.label = `${brightness['screen-value']}`;

}, 'screen-changed'),

});
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/custom-service.md)

[Previous
 App](/ags-docs/config/app)   [Next
 Subclassing GTK Widgets](/ags-docs/config/subclassing-gtk-widgets)
