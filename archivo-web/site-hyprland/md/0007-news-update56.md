---
type: source
source_type: webpage
url: "https://hyprland.org/news/update56"
title: "Hyprland 0.56 has arrived! | Hyprland"
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

# Hyprland 0.56 has arrived!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) July 20, 2026

Hey hey folks, it’s time for Hyprland 0.56! This update includes a lot of fixes and new features,
after about 2.5 months of hard work from all of our contributors and maintainers.

This time, get it, *no breaking changes*! Truly incredible.

Let’s get on to the stuff.

## New features

### Layout improvements

New scrolling and master stuff include:

* for scrolling:
  + `fit_into_view`
  + `fit expand`
  + `inhibit_scroll`
* for master:
  + `focus_master_on_close`

### Lua API expansion

New lua APIs include:

* `change_id` workspace API
* `get_loaded_plugins`
* `clear_crashed_lockscreen` for easier recovery from a crashed lockscreen
* `is_key_down` and key events for more direct key state querying
* custom live gestures
* `physical_width` and height, CM, and reserved area for monitor objects
* `exec_scheduled_prop_refresh_immediately` to refresh props immediately and not lazy schedule them
* various `set_` functions for raw workspace management on monitors
* event registering and dispatching

### Other

Other stuff include:

* new REPL mode for lua in hyprctl
* groupbar’s `disable_when_only` option
* new windowrule `stableid:` field
* new windowrules effects for `no_auto_hdr`, `suppress_event` for X11 configure events, and a silent monitor option
* XDG interactive drags support (dragging CSD titlebars)
* glow now supports gradients
* and much more…

## Fixes

Tons of issues fixed, as usual. I don’t think you care for me to list them all, so let’s just say the classic
“stability and performance improvements”. You can read all of the fixes in the raw release on GitHub. :)

## The raw release

As always, if you prefer reading more, check the release on [Github](https://github.com/hyprwm/Hyprland/releases/tag/v0.56.0).

Cheers,
vax

# More news

* [October 28, 2026

  ## Hyprland 0.57 is finally here!](/news/update57)
* [May 18, 2026

  ## 5th Ricing Competition starts now!](/news/ricingComp5)
* [May 9, 2026

  ## Hyprland 0.55 is here and you don't want to miss it!](/news/update55)
* [April 26, 2026

  ## Lua-ification of Hyprland configs](/news/26_lua)

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
