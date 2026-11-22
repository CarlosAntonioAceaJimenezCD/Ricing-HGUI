---
type: source
source_type: webpage
url: "https://aylur.github.io/ags/guide/quick-start.html"
title: "Quick Start | AGS"
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

# Quick Start [​](#quick-start)

It's as easy as a few lines to get a bar running on your screen.

## What will you be using [​](#what-will-you-be-using)

* [Gnome JavaScript (GJS)](https://gjs.guide/) is the JavaScript runtime
* [Astal](https://aylur.github.io/astal/) is a suite of libraries which lets you query and interact with parts of your system
* [Gnim](https://aylur.github.io/gnim/) is a library for GJS, which allows you to write widgets using JSX
* [AGS](https://aylur.github.io/ags/) is a CLI tool which lets you skip setting up a dev environment and jump straight into writing your Desktop Shell in TypeScript

## Single file start [​](#single-file-start)

First create a file anywhere on your system.

mybar.tsx

tsx

```
import app from "ags/gtk4/app"
import { Astal } from "ags/gtk4"
import { createPoll } from "ags/time"

app.start({
  main() {
    const { TOP, LEFT, RIGHT } = Astal.WindowAnchor
    const clock = createPoll("", 1000, "date")

    return (
      <window visible anchor={TOP | LEFT | RIGHT}>
        <label label={clock} />
      </window>
    )
  },
})
```

And run it using the following command:

sh

```
ags run ./mybar.tsx
```

Alternatively, you can add a shebang and make it executable

ts

```
#!/usr/bin/env -S ags run
import app from "ags/gtk4/app"

app.start({
  main() {
    // entry point
  },
})
```

sh

```
chmod +x mybar.tsx
./mybar.tsx
```

To setup a TypeScript environment use the `types` command

sh

```
ags types -u -d /path/to/project/root
```

## Using a template [​](#using-a-template)

It is recommended to start with a template which will setup files needed for TypeScript development environments.

You can get started using a template with this simple command

sh

```
ags init -d /path/to/project
```

If you are on nix, there is also a flake template

sh

```
nix flake init --template github:aylur/ags
```

[Edit this page on GitHub](https://github.com/aylur/ags/edit/main/docs/guide/quick-start.md)

Last updated:

Pager

[Previous pageInstallation](/ags/guide/install.html)

[Next pageFirst Widgets](/ags/guide/first-widgets.html)

Released under the GPL v3.0 License

Logo is created by VDawg
