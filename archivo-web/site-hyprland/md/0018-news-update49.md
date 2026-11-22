---
type: source
source_type: webpage
url: "https://hyprland.org/news/update49"
title: "Hyprland 0.49.0 dropped! | Hyprland"
fetched_at: 2026-11-22T06:26:05+00:00
fetcher: "curl + markitdown"
site: "hyprland.org"
---
* [Get started](https://wiki.hypr.land/getting-started/master-tutorial/)
* [Wiki](https://wiki.hypr.land)
* [Forums](https://forum.hypr.land)
* [Account](https://account.hypr.land)
* [Hall of fame](/hall_of_fame)
* [News](/news)
* [Plugins](/plugins)

* [Support us](/support)
* [Install](https://wiki.hypr.land/getting-started/installation/)

# Hyprland 0.49.0 dropped!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) May 8, 2025

After about 2 or so months, we got 0.49.0!

A lot of changes in this update as usual, let’s do a quick summary.

## Breaking changes

A few breaking changes this time:

* `cursor:warp_on_change_workspace` no longer controls warps for special workspaces. Use `warp_on_toggle_special` for more fine control.
* `master:center_master_slaves_on_right` has been changed to `master:center_master_fallback` providing more options than just right.
* you’ll now need to input your sudo password for sensitive hyprpm operations. Due to that change your repositories and enabled plugins will be reset.

## New stuff

### Permission management

Previously, (and in every other wayland compositor to this day) any app on your system
would be able to record and screenshot your screen without any permissions. This would be doable by directly
using the wayland protocols instead of the portal.

No more.

With permission management, both that, and other sensitive actions are now guarded by permissions, where you
can specify which apps can do what, and if you don’t, you’ll get an android / iOS / MacOS style popup asking you
for confirmation.

**Permission management is disabled by default for now**, read up more about it on [the wiki](https://wiki.hypr.land/Configuring/Permissions/).

### New protocols

Some new protocols are now supported in Hyprland, including `xdg-system-bell` and `xdg-toplevel-tag`.

### Other new changes

Other new stuff include:

* keybinds can now be disabled per-device
* ANR’s missed pings (delay) is now configurable
* you can now bind click and drag actions separately with your mouse
* groupbar got some new stuff: font weight, gaps, text offset, etc.
* a few new socket2 events: monitorremovedv2, minimized
* new windowrules: `nofollowmouse` and `noclosefor`
* and more

## Fixes

As usual, tons of fixes for crashes, bugs, etc.

## The raw release

if you are the type that enjoys reading, check the release out on [Github](https://github.com/hyprwm/Hyprland/releases/tag/v0.49.0).

Cheers,
vax.

# More news

* [October 28, 2026

  ## Hyprland 0.57 is finally here!](/news/update57)
* [July 20, 2026

  ## Hyprland 0.56 has arrived!](/news/update56)
* [May 18, 2026

  ## 5th Ricing Competition starts now!](/news/ricingComp5)
* [May 9, 2026

  ## Hyprland 0.55 is here and you don't want to miss it!](/news/update55)

Exclusive sponsor

[![Omarchy](/imgs/sponsors/omarchy.svg "Omarchy")](https://omarchy.org)

Humans

* [Vaxry [ Lead Developer ]](https://github.com/vaxerski)
* [Fufexan [ Supporting Developer ]](https://github.com/fufexan)
* [NotAShelf [ Community Manager ]](https://github.com/NotAShelf)
* [VDawg [ Webdesign and dev ]](https://github.com/vdawg-git)
* [and our fellow contributors](https://github.com/hyprwm/Hyprland/graphs/contributors)

Links

* [Wiki](https://wiki.hypr.land/)
* [Get started](https://wiki.hypr.land/getting-started/master-tutorial/)
* [Hall of fame](/hall_of_fame)
* [Forum](https://forum.hypr.land/)
* [Account](https://account.hypr.land/)
* [Trademark Usage](/trademark-usage)

Socials

Hyprland is licensed under the BSD 3-Clause "New" or "Revised" License.

The name "Hyprland" and the logo are registered trademarks of Hyprland Development.

© Hyprland Development 2026.

Stay hydrated
