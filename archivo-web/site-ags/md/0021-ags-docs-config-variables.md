---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/variables"
title: "Variables | AGS Wiki"
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
  + [Polling and Listening to executables](#polling-and-listening-to-executables)
  + [Updating its value](#updating-its-value)
  + [Getting its value](#getting-its-value)
  + [Temporarily stopping it](#temporarily-stopping-it)
  + [Starting it](#starting-it)
  + [Getting if its active](#getting-if-its-active)
  + [Usage with widgets](#usage-with-widgets)
  + [Connecting to it directly](#connecting-to-it-directly)
  + [Dispose if no longer needed](#dispose-if-no-longer-needed)
  + [Example RAM and CPU usage](#example-ram-and-cpu-usage)
* [Derived Variables](#derived-variables)

## On this page

* [Overview](#_top)
  + [Polling and Listening to executables](#polling-and-listening-to-executables)
  + [Updating its value](#updating-its-value)
  + [Getting its value](#getting-its-value)
  + [Temporarily stopping it](#temporarily-stopping-it)
  + [Starting it](#starting-it)
  + [Getting if its active](#getting-if-its-active)
  + [Usage with widgets](#usage-with-widgets)
  + [Connecting to it directly](#connecting-to-it-directly)
  + [Dispose if no longer needed](#dispose-if-no-longer-needed)
  + [Example RAM and CPU usage](#example-ram-and-cpu-usage)
* [Derived Variables](#derived-variables)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Variables

Variable is just a simple `GObject` that holds a value.

Tip

The global `Variable` is a function that returns an instance
If you want to subclass this instead of `Service` import the class

```
import { Variable as Var } from 'resource:///com/github/Aylur/ags/variable.js'

class MyVar extends Var {

static { Service.register(this) }

}
```

### Polling and Listening to executables

```
const myVar = Variable('initial-value', {

// listen is what will be passed to Utils.subprocess, so either a string or string[]

listen: App.configDir + '/script.sh',

listen: 'bash -c "some-command"',

listen: ['bash', '-c', 'some-command'],

// can also take a transform function

listen: [App.configDir + '/script.sh', out => JSON.parse(out)],

listen: [['bash', '-c', 'some-command'], out => JSON.parse(out)],

// poll is a [interval: number, cmd: string[] | string, transform: (string) => any]

// cmd is what gets passed to Utils.execAsync

poll: [1000, 'some-command'],

poll: [1000, 'some-command', out => 'transformed output: ' + out],

poll: [1000, ['bash', '-c', 'some-command'], out => 'transformed output: ' + out],

// or [number, function]

poll: [1000, () => { return new Date(); }],

poll: [1000, Math.random],

});
```

### Updating its value

```
myVar.value = 'new-value'

myVar.setValue('new-value')
```

Caution

using `setValue` will force a new value and thus signal `changed`,
while setting `value` only signal if it gets a new value

```
const myVar = Variable({ key: "value" })

const value = myVar.value

value["new-key"] = "value"

myVar.value = value // won't emit, because its still the same object

myVar.setValue(value) // will emit the signal
```

### Getting its value

```
print(myVar.value)

print(myVar.getValue())
```

### Temporarily stopping it

```
variable.stopListen() // this kills the subprocess

variable.stopPoll()
```

### Starting it

It will start on construction, no need to explicitly call this.

```
variable.startListen() // launches the subprocess again

variable.startPoll()
```

### Getting if its active

```
print(variable.isListening)

print(variable.isPolling)
```

### Usage with widgets

```
const label = Widget.Label({

label: myVar.bind(),

// optional transform method

label: myVar.bind().as(value => value.toString()),

// hook to do more than an assignment on changed

setup: self => self.hook(myVar, () => {

self.label = myVar.value.toString();

})

})
```

### Connecting to it directly

```
myVar.connect('changed', ({ value }) => {

console.log(value);

});
```

### Dispose if no longer needed

This will stop the interval and force exit the subprocess

```
myVar.dispose();
```

### Example RAM and CPU usage

```
const divide = ([total, free]) => free / total

const cpu = Variable(0, {

poll: [2000, 'top -b -n 1', out => divide([100, out.split('\n')

.find(line => line.includes('Cpu(s)'))

.split(/\s+/)[1]

.replace(',', '.')])],

})

const ram = Variable(0, {

poll: [2000, 'free', out => divide(out.split('\n')

.find(line => line.includes('Mem:'))

.split(/\s+/)

.splice(1, 2))],

})

const cpuProgress = Widget.CircularProgress({

value: cpu.bind()

})

const ramProgress = Widget.CircularProgress({

value: ram.bind()

})
```

## Derived Variables

```
const a = Variable(2)

const b = Variable(3)

// first argument is a list of dependencies

// second argument is a transform function

const c = Utils.derive([a, b], (a, b) => {

return a * b

})
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/variables.md)

[Previous
 Widgets](/ags-docs/config/widgets)   [Next
 Services](/ags-docs/config/services)
