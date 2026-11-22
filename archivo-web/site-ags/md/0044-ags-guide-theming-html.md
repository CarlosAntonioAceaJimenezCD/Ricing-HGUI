---
type: source
source_type: webpage
url: "https://aylur.github.io/ags/guide/theming.html"
title: "Theming | AGS"
fetched_at: 2026-11-22T06:24:53+00:00
fetcher: "curl + markitdown"
site: "aylur.github.io"
---
[Skip to content](#VPContent)

[AGS](/ags/)

Search`K`

 Main Navigation [Guide](/ags/guide/quick-start.html)

References

[Gjs Guide](https://gjs.guide/)

[Gjs References](https://gjs-docs.gnome.org/)

[Astal](https://aylur.github.io/astal/)

[Gnim](https://aylur.github.io/gnim/)

[xml version="1.0" encoding="utf-8"?](https://ko-fi.com/aylur)

Appearance

[xml version="1.0" encoding="utf-8"?](https://ko-fi.com/aylur)

Menu

Return to top

 Sidebar Navigation

[Installation](/ags/guide/install.html)

[Quick Start](/ags/guide/quick-start.html)

[First Widgets](/ags/guide/first-widgets.html)

[Theming](/ags/guide/theming.html)

[App and CLI](/ags/guide/app-cli.html)

[Utilities](/ags/guide/utilities.html)

[Resources](/ags/guide/resources.html)

[Intrinsics](/ags/guide/intrinsics.html)

[FAQ](/ags/guide/faq.html)

[Examples](/ags/guide/examples.html)

[Nix](/ags/guide/nix.html)

[Migration Guide](/ags/guide/migration-guide.html)

On this page

# Theming [​](#theming)

Since the widget toolkit is **GTK** theming is done with **CSS**.

* [CSS tutorial](https://www.w3schools.com/css/)
* Gtk4
  + [GTK4 CSS Overview wiki](https://docs.gtk.org/gtk4/css-overview.html)
  + [GTK4 CSS Properties Overview wiki](https://docs.gtk.org/gtk4/css-properties.html)
* Gtk3
  + [GTK3 CSS Overview wiki](https://docs.gtk.org/gtk3/css-overview.html)
  + [GTK3 CSS Properties Overview wiki](https://docs.gtk.org/gtk3/css-properties.html)

GTK is not the web

While most features are implemented in GTK, you can't assume anything that works on the web will work with GTK. Refer to the GTK docs to see what is supported.

## Loading static stylesheets [​](#loading-static-stylesheets)

You can import any `css` or `scss` file which will be inlined as a string which you can pass to the css property.

app.ts

ts

```
import css from "./style.css"
import scss from "./style.scss"

const inlineCss = `
  window {
    background-color: transparent;
  }
`

app.start({
  css: css,
  css: scss,
  css: inlineCss,
})
```

## Css Property on Widgets [​](#css-property-on-widgets)

You should always prefer to style using class names and stylesheets. But in those rare cases when you need apply a style based on a JavaScript value you can use the `css` property.

tsx

```
<box css="padding 1em; border: 1px solid red;" />
```

WARNING

The `css` property of a widget will not cascade to its children. You should generally avoid using `css` and instead use `class` and stylesheets.

## Apply Stylesheets at Runtime [​](#apply-stylesheets-at-runtime)

You can apply additional styles at runtime.

ts

```
app.apply_css("/path/to/file.css")
```

ts

```
app.apply_css(`
  window {
    background-color: transparent;
  }
`)
```

ts

```
app.reset_css() // reset if need
```

WARNING

`apply_css()` will apply on top of other stylesheets applied before. You can reset stylesheets with `reset_css()`

## Inspector [​](#inspector)

If you are not sure about the widget hierarchy or any CSS selector, you can use the [GTK inspector](https://wiki.gnome.org/Projects/GTK/Inspector)

sh

```
ags inspect
```

[Edit this page on GitHub](https://github.com/aylur/ags/edit/main/docs/guide/theming.md)

Last updated:

Pager

[Previous pageFirst Widgets](/ags/guide/first-widgets.html)

[Next pageApp and CLI](/ags/guide/app-cli.html)

Released under the GPL v3.0 License

Logo is created by VDawg
