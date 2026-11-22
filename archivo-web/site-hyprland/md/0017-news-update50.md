---
type: source
source_type: webpage
url: "https://hyprland.org/news/update50"
title: "Hyprland 0.50.0 released! | Hyprland"
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

# Hyprland 0.50.0 released!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) July 16, 2025

A short wait, finally concluded: 0.50.0 is here.

This update brings a lot of new stuff and fixes, here are just a few notable ones.

## Breaking changes

* Legacy renderer has been dropped. Hyprland now requires at least GLES 3.0 to function
* `explicit_sync` related settings in `render:` have been nuked. Explicit sync is always used by default.
* render-ahead-of-time settings have been nuked. They weren’t used anymore.

## Notable new stuff

### New render scheduling

There’s a new option under render, `render:new_render_scheduling`. It will dynamically switch to triple buffering when your
system cannot keep up. This can drastically improve FPS on underpowered devices, while coming at no performance or latency cost
when the system is doing alright.

Please note this option is disabled by default and experimental, as we’ve had some select setups struggle with it. Hopefully by 0.51
we can iron out those issues and have it on by default.

### No screen share

There’s a new rule, `noscreenshare`, which will black out any window with it in screensharing, for privacy.

### Internal test framework

We’ve finally (after a few months) managed to finalize the test framework. Each commit is now automatically tested
with a range of automatic tests, to hopefully catch regressions earlier. It can’t test *everything*, but it can test
a bunch of things, and we hope to get more and more tests there as time goes on.

### Other

Other new stuff include amongst others:

* New `monitorv2` syntax for monitor configs that are less cluttered
* tons of small optimizations (thanks Tom!)
* new `ext_workspace_v1` support
* multi-gpu support for `drm_lease`
* CM fixes for mpv crashes
* new `unbind = all` option for the config
* new `cm_auto_hdr` for automatic HDR
* new `group:` selector for windowrules
* new permission management for keyboards
* and more…

### Fixes

Tons of fixes, including:

* fixes for some `hyprpm` and hyprland crashes.
* fixed some minor blur artifacts on popups
* snap now respects outer gaps
* hyprpm will now print out what’s wrong instead of just dying when trying to add a new repo without an update first
* some minor xwayland fixes
* ANR dialog will now disappear if the app dies
* hyprland will no longer crash if a monitor’s driver rejects all available modes
* fixed some missing window fade out cases (esp. around special workspaces)
* fixed some crashes around switching cursor themes on the fly
* a few textures are now loaded dynamically to save VRAM when not needed
* screencopy selection boxes are now calculated properly for transformed monitors
* workspaces behind screen locks are no longer rendered for privacy reasons (this can be disabled in the config)

## The raw release

If you are one of these people that enjoy reading, check the release on [Github](https://github.com/hyprwm/Hyprland/releases/tag/v0.50.0).

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
