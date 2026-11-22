---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/davatorium/rofi/xkbcommon-FAQ.md"
title: "My distribution only has an ancient version!"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/davatorium/rofi/wiki"
---
This page will list frequent questions and errors related to xkbcommon


# My distribution only has an ancient version!

In this case, you’re most likely on Debian or Ubuntu. You have several options to fix that:
- Use backports if the version is new enough.
- Build libxkbcommon by hand (not that complicated) but *with a few configure switches*: `./configure --with-x-locale-root=/usr/share/X11/locale --with-xkb-config-root=/usr/share/X11/xkb` (or whatever correct prefix your system uses). This will make sure libxkbcommon knows where to look for files.
- Use the [repository maintained](http://debian.sur5r.net/i3) for the [i3 window manager](https://i3wm.org/docs/repositories.html), which contains a recent libxkbcommon.

# Compose

## xkbcommon: ERROR: couldn't find a Compose file for locale `<your locale>`

If you see that in rofi’s output, here are the possible reasons and their solution:

### Your installed libxkbcommon use a different prefix than your Compose file package
If you built libxkbcommon yourself, you will have to rebuild it but with `./configure --with-x-locale-root=/usr/share/X11/locale --with-xkb-config-root=/usr/share/X11/xkb` (or whatever correct prefix your system uses).
If you used a custom repository, please contact the owner so they fixes their package.

### You use an unknown locale
Just check for the best locale in `/usr/share/X11/locale/compose.dir`, then use it.

### You use an unknown alias
Just check for variants of your locale in `/usr/share/X11/locale/compose.dir` and `/usr/share/X11/locale/locale.alias`, then use it.
Example: `en_US.utf8` might not exist, try `en_US.UTF-8`.

Related issues: [#400](../issues/400) [#582](../issues/582)

# Keymaps

## Supported keymap files features

Some keymaps are using features that used to exist in X11 XKB, but were removed in xkbcommon. You can find a complete list [here](https://xkbcommon.org/doc/current/md_doc_compat.html).

These features are often not necessary and mostly used in customized or variants keymaps.

Related issues: [#354](../issues/354)