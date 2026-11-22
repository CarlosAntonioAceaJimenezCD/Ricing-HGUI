---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/utils"
title: "Utils | AGS Wiki"
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
* [Running external commands](#running-external-commands)
  + [Synchronously](#synchronously)
  + [Asynchronously](#asynchronously)
* [Running external scripts](#running-external-scripts)
* [Writing and reading files](#writing-and-reading-files)
  + [Synchronously](#synchronously-1)
  + [Asynchronously](#asynchronously-1)
* [Monitoring files and directories](#monitoring-files-and-directories)
  + [Canceling the monitor](#canceling-the-monitor)
* [Timeout and Interval](#timeout-and-interval)
* [Lookup an Icon name](#lookup-an-icon-name)
* [Fetch](#fetch)
* [Authentication](#authentication)
* [Send Notifications](#send-notifications)

## On this page

* [Overview](#_top)
* [Running external commands](#running-external-commands)
  + [Synchronously](#synchronously)
  + [Asynchronously](#asynchronously)
* [Running external scripts](#running-external-scripts)
* [Writing and reading files](#writing-and-reading-files)
  + [Synchronously](#synchronously-1)
  + [Asynchronously](#asynchronously-1)
* [Monitoring files and directories](#monitoring-files-and-directories)
  + [Canceling the monitor](#canceling-the-monitor)
* [Timeout and Interval](#timeout-and-interval)
* [Lookup an Icon name](#lookup-an-icon-name)
* [Fetch](#fetch)
* [Authentication](#authentication)
* [Send Notifications](#send-notifications)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Utils

## Running external commands

### Synchronously

```
function exec(cmd: string): string
```

This is synchronous, meaning it will **block the eventloop**

```
const echo = Utils.exec('echo "Hi Mom"') // returns string

console.log(echo) // logs "Hi Mom"
```

```
const uptime = Utils.exec(`bash -c "uptime | awk '{print $3}' | tr ',' ' '"`)

console.log(uptime)
```

### Asynchronously

```
function execAsync(cmd: string | string[]): Promise<string>;
```

This won’t block,

```
Utils.execAsync(['echo', 'Hi Mom'])

.then(out => print(out))

.catch(err => print(err));
```

Note

Both `exec` and `execAsync` launches the given binary on its own,
meaning if you want to use `|` pipes or any other shell features
then you have to run it with bash.

```
Utils.execAsync(['bash', '-c', 'cmd | cmd && cmd']);

Utils.exec('bash -c "cmd | cmd && cmd"');
```

## Running external scripts

```
function subprocess(

cmd: string | string[],

callback: (out: string) => void,

onError = logError,

bind?: Gtk.Widget,

): Gio.Subprocess
```

Takes two to four arguments, returns [Gio.Subprocess](https://gjs-docs.gnome.org/gio20~2.0/gio.subprocess)

```
const proc = Utils.subprocess(

// command to run, in an array just like execAsync

['bash', '-c', 'path-to-bash-script'],

// callback when the program outputs something to stdout

(output) => print(output),

// callback on error

(err) => logError(err),

// optional widget parameter

// if the widget is destroyed the subprocess is forced to quit

widget,

)
```

Killing the process

```
proc.force_exit()
```

## Writing and reading files

```
function readFile(file: string | Gio.File): string

function readFileAsync(file: string | Gio.File): Promise<string>

function writeFileSync(string: string, path: string): Gio.File

function writeFile(string: string, path: string): Promise<Gio.File>
```

### Synchronously

```
const contents = Utils.readFile('/path/to/file')

Utils.writeFileSync('some content', '/path/to/file')
```

### Asynchronously

```
Utils.readFileAsync('path-to-file')

.then(content => print('contents of the file: ' + content))

.catch(logError)

Utils.writeFile('Contents: Hi Mom', 'path-to-file')

.then(file => print('file is the Gio.File'))

.catch(err => print(err))
```

## Monitoring files and directories

```
function monitorFile(

path: string,

callback?: (file: Gio.File, event: Gio.FileMonitorEvent) => void,

flags = Gio.FileMonitorFlags.NONE,

): Gio.FileMonitor | null
```

```
const monitor = Utils.monitorFile('/path/to/file', (file, event) => {

print(Utils.readFile(file), event)

})
```

Caution

`monitorFile` only reports events that a user-space program
triggers through the filesystem API. As a result, it does not catch
remote events that occur on network filesystems.
Furthermore, most pseudo-filesystems such as `/proc`, `/sys` and `/dev/pts`
cannot be monitored.

### Canceling the monitor

```
monitor.cancel()
```

## Timeout and Interval

You can use native JS `setTimeout` and `setInterval`, they return a [GLib.Source](https://docs.gtk.org/glib/struct.Source.html)

Timeout

```
const source = setTimeout(() => { /* callback */ }, 1000)
```

Interval

```
const source = setInterval(() => { /* callback */ }, 1000)
```

To cancel them use `GLib.Source.destroy`

```
source.destroy()
```

You can use the ones from `Utils`

```
function interval(

interval: number,

callback: () => void,

bind?: Gtk.Widget,

): number

function timeout(

ms: number,

callback: () => void,

): number
```

```
const id = Utils.timeout(1000, () => {

// runs with a second delay

})
```

The widget parameter is optional

```
const id = Utils.interval(1000, () => {

// runs immediately and once every second

})
```

If you pass a widget to `Utils.interval`, it will automatically be canceled,
when the widget is destroyed

```
const widget = Widget.Label()

const id = Utils.interval(1000, () => {}, widget)

widget.destroy()
```

To cancel them use `GLib.source_remove`

```
import GLib from 'gi://GLib'

GLib.source_remove(id)
```

## Lookup an Icon name

```
const icon = Utils.lookUpIcon('dialog-information-symbolic')

if (icon) {

// icon is the corresponding Gtk.IconInfo

}

else {

// null if it wasn't found in the current Icon Theme

}
```

## Fetch

should be pretty close to the web api

```
Utils.fetch('http://wttr.in/?format=3')

.then(res => res.text())

.then(print)

.catch(console.error)
```

## Authentication

authenticate a user using pam

Note

on NixOS make sure you have `security.pam.services.ags = {}` in `configuration.nix`

```
Utils.authenticate('password')

.then(() => print('authentication successful'))

.catch(err => logError(err, 'unsuccessful'))

Utils.authenticateUser("username", "password")

.then(() => print("authentication successful"))

.catch(err => logError(err, 'unsuccessful'))
```

## Send Notifications

```
Utils.notify('summary', 'body', 'icon-name')
```

```
const id = await Utils.notify({

summary: 'Title',

body: 'Description',

iconName: 'icon-name',

actions: {

'Click Me': () => print('clicked')

}

})

const notifications = await Service.import('notifications')

const n = notifications.getNotification(id)
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/utils.md)

[Previous
 Services](/ags-docs/config/services)   [Next
 App](/ags-docs/config/app)
