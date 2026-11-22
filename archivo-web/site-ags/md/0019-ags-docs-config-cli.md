---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/cli"
title: "CLI | AGS Wiki"
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
* [Bus Name](#bus-name)
* [Config file](#config-file)
* [Toggle Window](#toggle-window)
* [Running arbitrary JavaScript code on runtime](#running-arbitrary-javascript-code-on-runtime)
* [Examples](#examples)

## On this page

* [Overview](#_top)
* [Bus Name](#bus-name)
* [Config file](#config-file)
* [Toggle Window](#toggle-window)
* [Running arbitrary JavaScript code on runtime](#running-arbitrary-javascript-code-on-runtime)
* [Examples](#examples)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# CLI

Terminal window

```
$ ags --help

USAGE:

ags [OPTIONS]

OPTIONS:

-h, --help              Print this help and exit

-v, --version           Print version and exit

-q, --quit              Kill AGS

-c, --config            Path to the config file.

-b, --bus-name          Bus name of the process

-i, --inspector         Open up the Gtk debug tool

-t, --toggle-window     Show or hide a window

-r, --run-js            Execute string as an async function

-f, --run-file          Execute file as an async function

--init                  Initialize the configuration directory

--clear-cache           Remove $HOME/.cache/ags
```

## Bus Name

It is possible to run multiple instances with `--bus-name`. It defaults to `"ags"`.
When an instance is running, executing `ags` is actually a client process that
will try to connect to the instance with the specified bus name.

Terminal window

```
ags # starts an instance with bus name "ags"

ags -i # opens up the inspector on the ags instance with bus name "ags"

ags --bus-name test # starts an instance with bus name "test"

ags -b test -i # opens the inspector on instance with bus name "test"

ags --quit

ags -b test --quit
```

Tip

The dbus name is `com.github.Aylur.ags.<bus-name>`,
so the default one is `com.github.Aylur.ags.ags`

## Config file

`--config` defaults to `$HOME/.config/ags/config.js`

Terminal window

```
# example

ags --config $HOME/.config/some-dir/main.js
```

## Toggle Window

`--toggle-window` is just there for the sake of it,
if you want to have more control use `--run-js`

Terminal window

```
# example

ags --toggle-window "bar"
```

## Running arbitrary JavaScript code on runtime

With `--run-js` it is possible to execute code when `ags` is already running.
It is useful for: calling Service methods, updating Variable values,
debugging or anything else.
`--run-js` expects a string which will be the body of an *async function*
executed relative to `app.ts`.

If there is no `;` character in the string, `return` keyword will be inserted automatically

Terminal window

```
ags -r "'hello'" # prints hello

ags -r "'hello';" # prints undefined

ags -r "return 'hello';" # prints hello
```

`print` will print on the client side, `console.log` and other
console methods will log on the main process’s stdout

Terminal window

```
ags -r "print('hello')" # prints "hello undefined"

ags -r "console.log('hello')" # prints "undefined"
```

`--run-file` reads the content of a file and passes it to `--run-js`

Terminal window

```
# these two are equivalent

ags --run-file /path/to/file.js

ags --run-js "$(cat /path/to/file.js)"
```

It is useful for shebangs

```
#!/usr/bin/env -S ags --run-file

return 'hello from a file'
```

Since `--run-js` is the body of a function, you can’t use top level static imports

The function gets executed relative to `app.ts`, which means
importing a module from your config needs a full path.

this throws

```
#!/usr/bin/env -S ags --run-file

import Module from 'file:///path/to/file.js' // throws
```

You can use `import` as an **async** method

```
#!/usr/bin/env -S ags --run-file

const Module = (await import('file:///path/to/file.js')).default;
```

## Examples

Let’s say you have a `Variable` in `$HOME/.config/ags/vars.js`
that you want set from cli.

vars.js

```
export const myVar = Variable(0);
```

You can import this module and access this variable

Terminal window

```
ags -r "(await import('file://$HOME/.config/ags/vars.js')).myVar++"
```

Your can make `myVar` global, to avoid writing out the import statement

vars.js

```
export const myVar = Variable(0);

globalThis.myVar = myVar;
```

Terminal window

```
ags -r "myVar++"
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/cli.md)

[Previous
 Type Checking](/ags-docs/config/type-checking)   [Next
 Widgets](/ags-docs/config/widgets)
