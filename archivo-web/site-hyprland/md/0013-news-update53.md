---
type: source
source_type: webpage
url: "https://hyprland.org/news/update53"
title: "Hyprland 0.53 dropped! | Hyprland"
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

# Hyprland 0.53 dropped!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) December 29, 2025

Hello there everyone! It’s time for 0.53!

This is a large update with a lot of things, and a few breaking changes.

## Breaking changes

Just two, but one big:

* Windowrule syntax has been completely overhauled. Please check the wiki: [here](https://wiki.hypr.land/Configuring/Window-Rules/)
* `misc:on_focus_under_fullscreen` replaces `misc:new_window_takes_over_fullscreen` and `master:inherit_fullscreen`

All of your windowrules will need to be re-written for the new syntax.

For an unofficial windowrule syntax converter, ItsOhen on Github created an automatic syntax fixer: [forum post](https://forum.hypr.land/t/0-53-window-layerrule-converter/1243).

## Major new stuff

### start-hyprland

Hyprland should no longer be launched via `Hyprland`, but rather `start-hyprland`. The new wrapper provides crash recovery and safe mode.

Important note for packagers: *safe mode will be quite a PITA without hyprland-guiutils installed, really consider it a hard dep*.

### Welcome

There is a new welcome app that introduces you to Hyprland if you’re launching for the first time. This requires hyprland-guiutils to be installed, and thus (as usual) we highly recommend packagers add hyprland-guiutils to hard deps of Hyprland.

### hyprpaper

Hyprpaper has been moved to hyprtoolkit + hyprwire with 0.8.0, which changes its IPC protocol. If you update hyprland to 0.53, make *sure* to update
hyprpaper to 0.8.0 as well. Please also note 0.8.0 breaks configs. Check the [wiki](https://wiki.hypr.land/Hypr-Ecosystem/hyprpaper/) for the new, simplified syntax.

### Other

* new universal submap bind flag
* new localization frameworks (translations) for GUI elements
* added an option to hide the cursor after tablet input
* groupbar can now be blurred
* hyprpm can now distinguish plugins with the same name but different author
* various CM/HDR fixes
* and a bunch more

## Fixes

Tons of fixes as always, in no particular order:

* pending keyboards are no longer enabled by default
* various focus and reserved area fixes
* fixed matching xdg tags
* improved uv scaling calculations for scales below 1
* improved ABI checks for plugins (less crashing)
* your classic “stability and performance improvements”

## The raw release

As always, if you prefer reading more, check the release on [Github](https://github.com/hyprwm/Hyprland/releases/tag/v0.53.0).

Cheers,
vax

### Additional releases

* hyprpaper [0.8.0](https://github.com/hyprwm/hyprpaper/releases/tag/v0.8.0)
* hyprland-guiutils [0.2.1](https://github.com/hyprwm/hyprland-guiutils/releases/tag/v0.2.1)
* hyprtoolkit [0.5.0](https://github.com/hyprwm/hyprtoolkit/releases/tag/v0.5.0)

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
