---
type: source
source_type: webpage
url: "https://hyprland.org/news/update46"
title: "Hyprland 0.46.0 is upon us! | Hyprland"
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

# Hyprland 0.46.0 is upon us!

[![Picture of Vaxry](/imgs/profile_pictures/vaxry.webp)

by Vaxry](https://github.com/vaxerski/) December 17, 2024

Whoo! Just before Christmas, we’ve managed to get 0.46.0 ready for you!

## Breaking changes

Some stuff has changed:

### Nvidia Hardware cursors!

`cursor:dumb_copy` is now gone in favor of `cursor:use_cpu_buffer`. This should allow no-downsides Nvidia hardware cursors. Please note it’s experimental.

### Window/layer rules

Window/layer rule regexes now require a full match (not any match) to trigger.

For example, in the case of `jeremy`:

* `jeremy`: OK
* `^(jeremy)$`: OK
* `jer`: Used to match, now won’t. You’ll need to do `.*jer.*` to make it act like before. (Consider *not* doing that though, make a better regex.)

## New stuff

Tons of new stuff, you can think of all of these as Christmas presents.

* Color handling has been moved to OkLab from sRGB. This means gradients and color transitions will now look more natural.
* XWayland Drag and Drop is back! You can now drag stuff from your Wayland clients to X11 clients.
* New update screen! Whenever you update, you’ll get a small popup reassuring everything went well and reminding you to check the release notes.
* Window and layer rule handling has been improved and optimized, and regex handling is now done via RE2 from Google, which is faster and generally better.
* `cursor:warp_on_change_workspace` now accepts `force` to bypass `cursor:no_warps`.
* hyprctl: `clients` got `inhibitingIdle`, `monitors` got `directScanout`, `plugins list` got `-j` support.
* `cursor:warp_back_after_non_mouse_input` added, allowing you to keep touch / tablet input from messing with your mouse input.
* `lockdead_screen_delay` has been added if your lockscreen can’t appear fast enough to avoid the “lockscreen dead” from flashing for a moment.
* You can now blur IME popups with `decoration:blur:input_methods`
* Version requests now also show linked versions of hypr\* deps.
* New windowrules for mouse and touchpad scroll factors.
* Added some new festive splashes for xmas and new years :)
* And more!

## Fixes

As always, tons and tons of fixes. See the github release to read up more.

### Links

See the 0.46.0 release on Github: <https://github.com/hyprwm/Hyprland/releases/tag/v0.46.0>

**Merry Christmas!!!!**

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
