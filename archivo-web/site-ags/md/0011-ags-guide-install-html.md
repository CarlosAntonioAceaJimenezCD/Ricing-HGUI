---
type: source
source_type: webpage
url: "https://aylur.github.io/ags/guide/install.html"
title: "Installation | AGS"
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

# Installation [​](#installation)

## Arch [​](#arch)

maintainer: [@kotontrion](https://github.com/kotontrion)

sh

```
yay -S aylurs-gtk-shell-git
```

## Nix [​](#nix)

maintainer: [@Aylur](https://github.com/Aylur)

sh

```
nix shell github:aylur/ags
```

Read more about running AGS on [Nix](./nix.html)

## From Source [​](#from-source)

1. Install these three [Astal packages](https://aylur.github.io/astal/guide/installation)

   * astal-io
   * astal3
   * astal4
2. Install dependencies

   Arch Fedora

   sh

   ```
   sudo pacman -Syu \
       npm meson ninja go gobject-introspection \
       gtk3 gtk-layer-shell \
       gtk4 gtk4-layer-shell
   ```

   sh

   ```
   sudo dnf install \
       npm meson ninja golang gobject-introspection-devel \
       gtk3-devel gtk-layer-shell-devel \
       gtk4-devel gtk4-layer-shell-devel
   ```
3. Clone and install AGS

   sh

   ```
   git clone https://github.com/aylur/ags.git
   cd ags
   npm install
   meson setup build
   meson install -C build
   ```

IMPORTANT

By default, meson installs to `/usr/local`.

[Edit this page on GitHub](https://github.com/aylur/ags/edit/main/docs/guide/install.md)

Last updated:

Pager

[Next pageQuick Start](/ags/guide/quick-start.html)

Released under the GPL v3.0 License

Logo is created by VDawg
