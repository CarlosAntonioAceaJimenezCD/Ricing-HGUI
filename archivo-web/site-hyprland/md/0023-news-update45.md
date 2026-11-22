---
type: source
source_type: webpage
url: "https://hyprland.org/news/update45"
title: "Hyprland 0.45.0 has dropped! | Hyprland"
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

# Hyprland 0.45.0 has dropped!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) November 9, 2024

After a while, we finally got 0.45.0! This release comes with a *lot* of new stuff and improvements, while also, as always,
squashing a few dozen bugs.

## Breaking changes

Some stuff has changed. `no_gaps_when_only` is now gone in favor of workspace rules. See [here](https://wiki.hypr.land/Configuring/Workspace-Rules/#smart-gaps).

This has some advantages on the code side (less clutter and bugs), but also for the user: the layout provider no longer needs to implement this, as it’s layout-agnostic.

Additionally, `decoration:shadow_` stuff has moved, see [here](https://wiki.hypr.land/Configuring/Variables/#shadow) for the new names.

## New stuff

* improved the algorithm used to round edges. Rounded corners, borders, rectangles, should all now be considerably smoother.
* improved default behavior for hardware cursors on nvidia. They will now be automatically disabled by default as they are buggy. (I am planning to try and fix them altogether in 0.46)
* groups got a few new stuff like `group_on_movetoworkspace`, `merge_groups_on_groupbar`, `drag_into_group`, `merge_floated_into_tiled_on_groupbar`.
* `hyprland-ctm-control` is now supported, meaning `hyprsunset` will work.
* Hyprland will now warn you if you have incorrectly installed assets instead of quietly failing and rendering black.
* Window snapping for floating windows has been added.
* The default behavior of expanding undersized textures introduced in 0.44.0 is now configurable with `expand_undersized_textures`
* shadow now has a `sharp` option for no blur.
* hyprctl got a few new props for keyboard’s locked mod state(s) and monitors’ mirror status
* the hyprland config error bar will now reserve space instead of obstructing vision

## Fixes

As always, tons and tons of fixes. See the github release to read up more.

## Additional releases

* aquamarine v0.4.4 released: [Github](https://github.com/hyprwm/aquamarine/releases/tag/v0.4.4)
* hyprutils v0.2.4 released: [Github](https://github.com/hyprwm/hyprutils/releases/tag/v0.2.4)
* hyprsunset v0.1.0 released: [Github](https://github.com/hyprwm/hyprsunset/releases/tag/v0.1.0)

### Links

See the 0.45.0 release on Github: <https://github.com/hyprwm/Hyprland/releases/tag/v0.45.0>

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
