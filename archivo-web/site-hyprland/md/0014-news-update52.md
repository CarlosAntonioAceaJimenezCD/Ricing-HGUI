---
type: source
source_type: webpage
url: "https://hyprland.org/news/update52"
title: "Hyprland 0.52 out now! | Hyprland"
fetched_at: 2026-11-22T06:26:05+00:00
fetcher: "curl + markitdown"
site: "hyprland.org"
---
* [Get started](https://wiki.hypr.land/Getting-Started/Master-Tutorial/)
* [Wiki](https://wiki.hypr.land)
* [Forums](https://forum.hypr.land)
* [Account](https://account.hypr.land)
* [Hall of fame](/hall_of_fame)
* [News](/news)
* [Plugins](/plugins)

* [Support us](/support)
* [Install](https://wiki.hypr.land/Getting-Started/Installation/)

# Hyprland 0.52 out now!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) November 7, 2025

Hi fam, another Hyprland update time! There hasn’t been an update in a while, but we back.

Work is also focused a bit on improving our new [hyprtoolkit](https://github.com/hyprwm/hyprtoolkit) which
will power all hyprland gui apps in the future.

Anyways, hyprland.

## Breaking changes

`misc:disable_hyprland_qtutils_check` has been moved to `misc:disable_hyprland_guiutils_check` to reflect qtutils
being now archived in favor of guiutils.

## New stuff

Tons of new stuff dropped:

* you can now mark submaps as automatically closing after a keybind has been executed
* new dispatcher: `forceidle`
* `fullscreen` now has `set`, `unset` and `toggle` for less IPC queries
* new CM options: `dcip3`, `dp3` and `adobe`
* you can now set `rotation` for each input device that supports it
* `noscreenshare` now also available as a layerrule
* `cursor:zoom_disable_aa` for controlling whether you want a pixelated or blurry look when zooming into your cursor
* new `modal` prop for windowrules
* and much more!

## Fixes

Tons of fixes, some notable include:

* various improvements to rendering: more smooth surface resizes, damage fixes and some pixel-level improvements
* fixes to screencopy for 10b displays
* various crashes fixed
* function hook fixes for plugin crashes
* gesture fixes for a few config options being badly parsed
* various virtual keyboard (IME) fixes
* fixed slide/slidefade not accepting forced dirs
* fixed a rare dpms lockup state where monitors would not come back to life
* fixed a case where plugins could crash due to ABI breaks in deps
* tons more, as always

## The raw release

If you are one of these people that enjoy reading, check the release on [Github](https://github.com/hyprwm/Hyprland/releases/tag/v0.52.0).

Cheers,
vax

# More news

* [September 10, 2025

  ## Hyprland 0.51 dropped!](/news/update51)
* [July 28, 2025

  ## Hyprperks have been launched!](/news/hyprperks)
* [July 16, 2025

  ## Hyprland 0.50.0 released!](/news/update50)
* [May 8, 2025

  ## Hyprland 0.49.0 dropped!](/news/update49)

Humans

* [Vaxry [ Lead Developer ]](https://github.com/vaxerski)
* [Fufexan [ Supporting Developer ]](https://github.com/fufexan)
* [NotAShelf [ Community Manager ]](https://github.com/NotAShelf)
* [VDawg [ Webdesign and dev ]](https://github.com/vdawg-git)
* [and our fellow contributors](https://github.com/hyprwm/Hyprland/graphs/contributors)

Links

* [Wiki](https://wiki.hypr.land/)
* [Get started](https://wiki.hypr.land/Getting-Started/Master-Tutorial/)
* [Hall of fame](/hall_of_fame)
* [Forum](https://forum.hypr.land/)
* [Account](https://account.hypr.land/)

Socials

Hyprland is licensed under the BSD 3-Clause "New" or "Revised" License.

© Hyprland Development 2025.

Stay hydrated
