---
type: source
source_type: webpage
url: "https://hyprland.org/news/update54"
title: "Hyprland 0.54 is upon us! | Hyprland"
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

# Hyprland 0.54 is upon us!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) February 27, 2026

It’s been a while, but we wanted to polish this one! This is a **massive** update with no
understatement. After a quite tame 0.53 and a few patch releases, we finally can proudly announce
0.54 is out.

Special thanks to our HIs (Human Intelligences) for powering Hyprland development.

## Breaking changes

* `togglesplit` and `swapsplit` dispatchers have been finally removed after being long deprecated. Please use `layoutmsg` now.
* `single_window_aspect_ratio` and `single_window_aspect_ratio_tolerance` have been migrated from dwindle to layout, and are layout-agnostic.

## Per-workspace layouts

The biggest change to how our layouts work since Hyprland’s inception. Layouts now are much simpler, easier to write and
maintain.

With this, you can finally have per-workspace layouts (or per-monitor, etc), which means you can have workspaces 1-4 on dwindle,
5-8 on master, and 9-10 on scroll.

Wait… scroll?

## New layouts

With 0.54 and the layout rewrite, the `hyprscrolling` plugin has been migrated into core, and a `monocle` layout has also
been added. Check the wiki pages for each for config options and layout messages.

## Massive performance improvements

Especially on iGPUs, thanks to massive work from Tom, Ujin and yours truly, we’ve managed to improve performance anywhere
from 50% to 500%, depending on your exact hardware. No more dropped frames, rejoice!

The battle is not over, but we already beat many other environments in performance and continue to work on it.

## Full Hyprnix integration

The hyprnix integration is now complete. We will continue testing it over the next few weeks and plan to recommend it by
default for distros other than Arch / Nix in the future.

Hyprpm and start-hyprland now have full nix integrations.

## Other new stuff

Other new stuff include:

* new cursor zoom gesture
* new groupbar text padding options
* a few new fields in hyprctl
* minor misc improvements

## Fixes

As usual, tons of fixes, too many to list:

* various X11 compat fixes
* fifo improvements
* tons of renderer fixes
* various DRM and syncobj fixes
* error bar padding fixes
* dynamic layer rule applying fixed
* tons of crashes fixed
* and more, I’m too lazy to list…

## The raw release

As always, if you prefer reading more, check the release on [Github](https://github.com/hyprwm/Hyprland/releases/tag/v0.54.0).

Cheers,
vax

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
