---
type: source
source_type: webpage
url: "https://hyprland.org/news/update41"
title: "A huge Hyprland release 0.41.0 | Hyprland"
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

# A huge Hyprland release 0.41.0

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) June 10, 2024

Just as we thought 0.40.0 was a mega-release, we now proudly present 0.41.0, which is almost twice as sizeable.

0.41.0 changes over 25000 lines of code over almost 200 commits from dozens of contributors.

See the release on [Github](https://github.com/hyprwm/Hyprland/releases/tag/v0.41.0).

## Ongoing work to detach from wlroots

As I’ve explained in [my blogpost on vaxry.net](https://blog.vaxry.net/articles/2024-wlrootsRewrite) there’s currently
a large ongoing effort to move away from wlroots, which requires essentially re-implementing all wlroots’ features in hyprland.

The work is going mostly smoothly, with some inevitable small bugs here and there, but overall not that many.

As we stand right now, 0.41.0 has completely gotten rid of wlroots for handling anything related to wayland, so the entire Wayland stack
is now wlroots-free. The only thing remaining now is the backend (kms / libinput / drm) which will be the target of most likely 0.42 (maybe 0.43)
quite soon. After that, Hyprland will become a new, fully independent Wayland implementation.

## New stuff

0.41.0 also brings a ton of new goodies and fixes. Many annoying issues from 0.40.0 (lockscreens, keybinds, hyprpm etc) have been fixed
and some new features include:

* New IPC events for groups
* A few QoL features for keybinds (sendshortcut, new monitor flags, keybind combos)
* New QoL stuff for hyprctl (—quiet, fixes for batch, config flag for systeminfo)
* New protocol impl: hyprland\_focus\_grab
* Ability to configure the position of the error bar
* Tons of bugfixes
* And much much more!

## Closer

The current roadmap mostly focuses on migrating from wlroots, and after that is done, I plan on focusing on any bugs that arose from it, and possibly polishing the
ecosystem a bit (hyprpaper, xdph, etc) to provide a bit smoother of an experience.

Cheers
~ vaxry

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
