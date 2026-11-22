---
type: source
source_type: webpage
url: "https://hyprland.org/news/update44"
title: "Hyprland 0.44.0 is out! | Hyprland"
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

# Hyprland 0.44.0 is out!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) October 6, 2024

0.44.0 is finally upon us!

This update mostly focuses on further bugfixes over actually implementing new stuff,
but we have quite a bunch of both!

When it comes to new stuff, we have, amongst others:

* A new argument `--version` for checking the Hyprland binary’s version instead of `hyprctl version`
* Same spirit as above, `--systeminfo`.
* A new layerrule `order` for ordering layers on the same plane
* A new `HYPRLAND_CONFIG` envvar for another method of passing an explicit config instead of `--config`
* Dwindle has got some new stuff: `movetoroot` layout message and `split_bias` config option
* Layout-general, auto-grouping is now configurable
* hyprctl has some new stuff, a few more props to `monitors` and `workspacerules` requests, and a new `submap` request.
* A new user-check for the `XDG_CURRENT_DESKTOP` env has been added as Hyprland no longer overwrites it
* Implemented the single-pixel-buffer protocol

For fixes, notable ones include:

* Various fixes to surface UV and positioning calculations: chromium windows no longer go crazy when resizing, and resizing other apps should generally feel much smoother
* Various text-input fixes for IME users
* XWayland handling fixes for monitors being misplaced and input not translating correctly after monitors were unplugged / replugged.
* Some drag-n-drop edge cases have been fixed
* Initial cursor warping has been fixed
* Various crashes fixed
* Lots of cleanups of the underlying codebase :)

Generally, this update shouldn’t impact you negatively, and only polish some rough edges.

See the full release notes on [Github](https://github.com/hyprwm/Hyprland/releases/tag/v0.44.0).

Cheers, vax.

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
