---
type: source
source_type: webpage
url: "https://hyprland.org/news/update43"
title: "Hyprland 0.43.0 released! | Hyprland"
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

# Hyprland 0.43.0 released!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) September 8, 2024

Quite a while after 0.42.0, 0.43.0 has finally been released.

This update focuses mostly on polishing up annoying issues from 0.42.0, especially those with random crashes and monitors
not turning on/displaying garbage.

Most (like 95%) of the “monitor not on” issues have now been fixed with 0.43, though please also use aquamarine 0.4.1 as
some fixes were done in aquamarine itself.

Additionally to all the bugfixes, some new features have been added, for example:

* New windowrule to keep windows rendered when invisible ([#7582](https://github.com/hyprwm/Hyprland/pull/7582))
* `exec-shutdown` added to the config to execute something on hyprland exit
* Animations got `workspacein` and `workspaceout` configs
* `hyprctl switchxkblayout` now can also take `current` and `all` for keyboard param
* `HYPRLAND_NO_SD_VARS` environment has been added to prevent Hyprland from updating systemd’s environment
* New screens for when your lockscreen dies instead of the infamous red screen of death, with information on recovering
* `xwayland:enabled` has been added to runtime-disable xwayland
* `cursor:sync_gsettings_theme` has been added to sync the cursor theme to system gsettings
* and much much more!

Hyprland continues being the most advanced independent wayland compositor, all thanks to the amazing community and the huge
influx of new contributors! Your contributions are greatly appreciated.

See the full release [on github](https://github.com/hyprwm/Hyprland/releases/tag/v0.43.0).

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
