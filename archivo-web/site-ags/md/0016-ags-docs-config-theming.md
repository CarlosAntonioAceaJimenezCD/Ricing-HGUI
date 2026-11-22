---
type: source
source_type: webpage
url: "https://aylur.github.io/ags-docs/config/theming"
title: "Theming | AGS Wiki"
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
* [From file at startup](#from-file-at-startup)
* [Css Property on Widgets](#css-property-on-widgets)
* [Apply Stylesheets at Runtime](#apply-stylesheets-at-runtime)
* [Inspector](#inspector)
* [Using pre-processors like SCSS](#using-pre-processors-like-scss)
* [Autoreload Css](#autoreload-css)

## On this page

* [Overview](#_top)
* [From file at startup](#from-file-at-startup)
* [Css Property on Widgets](#css-property-on-widgets)
* [Apply Stylesheets at Runtime](#apply-stylesheets-at-runtime)
* [Inspector](#inspector)
* [Using pre-processors like SCSS](#using-pre-processors-like-scss)
* [Autoreload Css](#autoreload-css)

You are looking at the legacy documentation of AGS v1. Go to [aylur.github.io/ags](https://aylur.github.io/ags/) for AGS v2.

# Theming

Since the widget toolkit is **GTK3** theming is done with **CSS**.

* [CSS tutorial](https://www.w3schools.com/css/)
* [GTK CSS Overview wiki](https://docs.gtk.org/gtk3/css-overview.html)
* [GTK CSS Properties Overview wiki](https://docs.gtk.org/gtk3/css-properties.html)

GTK is not the web

While most features are implemented in GTK,
you can’t assume anything that works on the web will work with GTK.
Refer to the [GTK docs](https://docs.gtk.org/gtk3/css-overview.html)
to see what is available.

So far every widget you made used your default GTK3 theme.
To make them more custom, you can apply stylesheets to them,
which are either imported `css` files or `inline css` applied
with the `css` property.

## From file at startup

config.js

```
App.config({

// this style attribute takes a full path to a css file

style: '/home/username/.config/ags/style.css',

// or relative to config.js

style: './style.css',

})
```

## Css Property on Widgets

```
Widget.Label({

css: 'color: blue; padding: 1em;',

label: 'hello'

})
```

## Apply Stylesheets at Runtime

Caution

`App.applyCss` will apply over other stylesheets applied before.
You can reset stylesheets with `App.resetCss`

```
App.applyCss('/path/to/file.css')
```

```
App.applyCss(`

window {

background-color: transparent;

}

`)
```

```
App.resetCss() // reset if need
```

## Inspector

If you are not sure about the widget hierarchy or any CSS selector,
you can use the [GTK inspector](https://wiki.gnome.org/Projects/GTK/Inspector)

Terminal window

```
# to bring up the inspector run

ags --inspector
```

## Using pre-processors like SCSS

config.js

```
// main scss file

const scss = `${App.configDir}/style.scss`

// target css file

const css = `/tmp/my-style.css`

// make sure sassc is installed on your system

Utils.exec(`sassc ${scss} ${css}`)

App.config({

style: css,

windows: [ /* windows */ ],

})
```

## Autoreload Css

```
Utils.monitorFile(

// directory that contains the scss files

`${App.configDir}/style`,

// reload function

function() {

// main scss file

const scss = `${App.configDir}/style.scss`

// target css file

const css = `/tmp/my-style.css`

// compile, reset, apply

Utils.exec(`sassc ${scss} ${css}`)

App.resetCss()

App.applyCss(css)

},

)
```

[Edit page](https://github.com/Aylur/ags-docs/tree/main/src/content/docs/config/theming.md)

[Previous
 Reactivity](/ags-docs/config/reactivity)   [Next
 Config Object](/ags-docs/config/config-object)
