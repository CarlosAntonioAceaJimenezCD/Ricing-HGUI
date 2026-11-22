---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/elkowar/eww/master/docs/src/working_with_gtk.md"
title: "GTK"
fetched_at: 2026-11-22T06:19:30+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/elkowar/eww"
---
# GTK

## Gtk-theming

Eww is styled in GTK CSS.
You can use `Vanilla CSS` or `SCSS` to make theming even easier. The latter is compiled into CSS for you.
If you don't know any way to style something check out the [GTK CSS Overview wiki](https://docs.gtk.org/gtk3/css-overview.html),
the [GTK CSS Properties Overview wiki ](https://docs.gtk.org/gtk3/css-properties.html),
or use the [GTK-Debugger](#gtk-debugger).

If you have **NO** clue about how to do CSS, check out some online guides or tutorials.

SCSS is _very_ close to CSS, so if you know CSS you'll have no problem learning SCSS.

## GTK-Debugger

The debugger can be used for **a lot** of things, especially if something doesn't work or isn't styled right.

To open the GTK debugger, simply run

```bash
eww inspector
```

If a style or something similar doesn't work, you can click on the icon in the top left to select the thing that isn't being styled correctly.

Then you can click on the drop down menu in the top right corner and select CSS Nodes. Here you will see everything about styling it, CSS Properties, and how it's structured.
