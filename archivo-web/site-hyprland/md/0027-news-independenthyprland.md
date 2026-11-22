---
type: source
source_type: webpage
url: "https://hyprland.org/news/independentHyprland"
title: "Hyprland is now fully independent! | Hyprland"
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

# Hyprland is now fully independent!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) July 21, 2024

With great pleasure may I announce that our move off of wlroots is now complete and [MR 6608](https://github.com/hyprwm/Hyprland/pull/6608) is
now merged.

After over 1000 comments on 6608 alone, and over 3 months of the entire process, the rewrite is done.

With it, Hyprland is no longer a wlroots-based Wayland compositor, and instead, a fully independent implementation of the protocol.

Don’t worry though, all your wlroots apps will still work.

## Timeline

As I’ve outlined in my [blogpost on blog.vaxry.net](https://blog.vaxry.net/articles/2024-wlrootsRewrite) in May, the rewrite took
place in two parts.

The first part was rewriting all protocol implementations. This has been finished on June 8th, with [MR 6268](https://github.com/hyprwm/Hyprland/pull/6268) being merged.

The second part was rewriting the backend implementation, i.e. the low-level backend stuff (KMS/DRM/libinput et al) which is now done with 6608.

## Changes under the hood

All protocol implementations are now integrated into Hyprland itself, and written with C++. This should reduce the amount of memory issues and bugs compared to wlroots implementations
and has already been doing that.

The backend rendering stuff has been migrated into a library written from scratch called [aquamarine](https://github.com/hyprwm/aquamarine).

Aquamarine is *not* a competitor to wlroots - wlroots is a library for building Wayland compositors, while aquamarine is a tiny library providing an abstraction on top of the very low-level
backend stuff, that also allows your program to run on either a Wayland compositor (in a window) or on a DRM session (tty).

Additionally, many new interfaces have been added to `hyprutils`, and `hyprwayland-scanner` has gotten the ability to generate client code, already used by aquamarine and hyprpaper.

## Changes for the user

See the [wiki MR](https://github.com/hyprwm/hyprland-wiki/pull/721) for the changes to config options, environment variables, etc.

Apart from a few minor changes to how things are called, nothing else should change for you, the user.

## When will I get it?

The changes are staged for 0.42.0. If you want to test them right away, check out the -git branch, as usual.

## Special thanks

Massive thanks to all the people who helped in the long process (what was it, like 3 months?) of rewriting the wlroots stack to a nicer language.

Special thanks to:

* Agent00Ming (testing and patience)
* Ikalco (tons of patches)
* gulafaran (patches and testing)
* phonetic112 (testing)
* UjinT34 (testing and patches)
* fufexan (nix and meson)
* And everyone who helped test here and there! There’s been 38 participants in the aquamarine MR alone!

Cheers and ad meliora,
vaxry.

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
