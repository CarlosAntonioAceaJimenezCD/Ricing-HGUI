---
type: source
source_type: webpage
url: "https://hyprland.org/news/update40"
title: "A Hyprland mega-release 0.40.0 | Hyprland"
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

# A Hyprland mega-release 0.40.0

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) May 4, 2024

Changing over 15,000 lines of code, the Hyprland 0.40.0 update has finally dropped. This
is the biggest release by commit and LOC diff in history of Hyprland.

As we’re in the middle of slowly but surely moving off of depending on wlroots for our backend(s),
a lot of things are moving from wlroots’ C implementations into more memory-safe and cleaner C++ implementations instead.

Although the work is surely not done yet (from just the protocol implementations, about 60% has been rewritten so far),
this mega-release will also help test how the implementations fare in real world usage.

A few bugs and quirks have been ironed out during the development phase, and many previously long-standing bugs
have been fixed with these rewrites.

0.40.0 also brings a few community-requested QoL features, like:

* Better monitor auto-positioning
* Initial workspace tracking
* More workspace selectors
* Two new protocols supported, ext-foreign-toplevel and alpha-modifier
* A boatload of bugfixes
* And much more!

Hopefully the new implementations prove stable and resilient. Although we do not expect it to all be smooth
sailing, it should prove more stable, as we’ve seen before with other memory-safe re-implementations.

Check out the entire release on Github [here](https://github.com/hyprwm/Hyprland/releases/tag/v0.40.0)

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
