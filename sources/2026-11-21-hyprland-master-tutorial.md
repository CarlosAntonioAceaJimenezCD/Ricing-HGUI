---
type: source
source_type: webpage
url: "https://wiki.hypr.land/getting-started/master-tutorial/"
title: "Hyprland · Master Tutorial"
fetched_at: 2026-11-22T00:51:12+00:00
fetcher: curl + markitdown
---

[Skip to content](#content)

[![Logo](/favicon.svg)
![Dark Logo](/favicon-dark.svg)
Hyprland Wiki](/)[Latest git](/version-selector/)[Wiki](/)[Home](https://hypr.land/)[Showcase](https://hypr.land/hall_of_fame)[News](https://hypr.land/news)Search...
`CTRL K`
[GitHub](https://github.com/hyprwm/Hyprland "GitHub")

* [Wiki](/)

  + [Version selector ⚙️](/version-selector/)
  + [Getting Started](/getting-started/)

    - [Installation](/getting-started/installation/)
    - [Master tutorial](/getting-started/master-tutorial/)

      * [Install Hyprland](#install-hyprland)
      * [NVIDIA?](#nvidia)
      * [VM?](#vm)
      * [Launching Hyprland](#launching-hyprland)
      * [DE-like pre-configured setups](#de-like-pre-configured-setups)
      * [In Hyprland with the default config](#in-hyprland-with-the-default-config)
      * [Monitors config](#monitors-config)
      * [Fully configure Hyprland](#fully-configure-hyprland)
      * [Important software](#important-software)
      * [Apps / X11 replacements](#apps--x11-replacements)
      * [Force apps to use Wayland](#force-apps-to-use-wayland)
      * [Themes](#themes)
      * [Cursors](#cursors)
    - [Preconfigured setups](/getting-started/preconfigured-setups/)
  + [Configuring](/configuring/)

    - [Naming conventions](/configuring/naming-conventions/)
    - [Selectors](/configuring/selectors/)
    - [Core](/configuring/core/)

      * [Monitors](/configuring/core/monitors/)
      * [Config options](/configuring/core/config-options/)
      * [Devices](/configuring/core/devices/)
      * [Dispatchers](/configuring/core/dispatchers/)
      * [Binds](/configuring/core/binds/)
      * [Rules](/configuring/core/rules/)
      * [Environment variables](/configuring/core/environment-variables/)
      * [Animations](/configuring/core/animations/)
      * [Autostart](/configuring/core/autostart/)
      * [Advanced configuration](/configuring/core/advanced-configuration/)
    - [Layouts](/configuring/layouts/)

      * [Dwindle layout](/configuring/layouts/dwindle-layout/)
      * [Scrolling layout](/configuring/layouts/scrolling-layout/)
      * [Master layout](/configuring/layouts/master-layout/)
      * [Monocle layout](/configuring/layouts/monocle-layout/)
      * [Custom layouts](/configuring/layouts/custom-layouts/)
    - [Extra](/configuring/extra/)

      * [Multi-GPU](/configuring/extra/multi-gpu/)
      * [Virtual GPU](/configuring/extra/virtual-gpu/)
      * [Performance](/configuring/extra/performance/)
      * [Tearing](/configuring/extra/tearing/)
      * [Xwayland](/configuring/extra/xwayland/)
      * [Systemd](/configuring/extra/systemd/)
    - [Lua code snippets](/configuring/code-snippets/)
  + [Hypr Ecosystem](/hypr-ecosystem/)

    - [User apps and utilities](/hypr-ecosystem/user/)

      * [hyprpaper](/hypr-ecosystem/user/hyprpaper/)
      * [hyprpicker](/hypr-ecosystem/user/hyprpicker/)
      * [hyprlauncher](/hypr-ecosystem/user/hyprlauncher/)
      * [hypridle](/hypr-ecosystem/user/hypridle/)
      * [hyprlock](/hypr-ecosystem/user/hyprlock/)
      * [xdg-desktop-portal-hyprland](/hypr-ecosystem/user/xdg-desktop-portal-hyprland/)
      * [hyprsysteminfo](/hypr-ecosystem/user/hyprsysteminfo/)
      * [hyprsunset](/hypr-ecosystem/user/hyprsunset/)
      * [hyprpolkitagent](/hypr-ecosystem/user/hyprpolkitagent/)
      * [hyprland-qt-support](/hypr-ecosystem/user/hyprland-qt-support/)
      * [hyprqt6engine](/hypr-ecosystem/user/hyprqt6engine/)
      * [hyprpwcenter](/hypr-ecosystem/user/hyprpwcenter/)
      * [hyprshutdown](/hypr-ecosystem/user/hyprshutdown/)
      * [hyprtoolkit (user docs)](/hypr-ecosystem/user/hyprtoolkit/)
      * [hyprcursor](/hypr-ecosystem/user/hyprcursor/)
    - [Developer libs and toolkits](/hypr-ecosystem/dev/)

      * [aquamarine](/hypr-ecosystem/dev/aquamarine/)
      * [hyprgraphics](/hypr-ecosystem/dev/hyprgraphics/)
      * [hyprland-guiutils](/hypr-ecosystem/dev/hyprland-guiutils/)
      * [hyprlang](/hypr-ecosystem/dev/hyprlang/)
      * [hyprtoolkit (developer docs)](/hypr-ecosystem/dev/hyprtoolkit/)
      * [hyprutils](/hypr-ecosystem/dev/hyprutils/)
      * [hyprwayland-scanner](/hypr-ecosystem/dev/hyprwayland-scanner/)
  + [Hyprland plugins](/hyprland-plugins/)

    - [Using plugins](/hyprland-plugins/using-plugins/)
    - [Development](/hyprland-plugins/development/)

      * [Getting started](/hyprland-plugins/development/getting-started/)
      * [Plugin guidelines](/hyprland-plugins/development/plugin-guidelines/)
      * [Advanced](/hyprland-plugins/development/advanced/)
  + [Useful utilities](/useful-utilities/)

    - [Must-have](/useful-utilities/must-have/)
    - [Status bars](/useful-utilities/status-bars/)
    - [Wallpapers](/useful-utilities/wallpapers/)
    - [Screen sharing](/useful-utilities/screen-sharing/)
    - [Screenshots and recording](/useful-utilities/screenshots-and-recording/)
    - [App launchers](/useful-utilities/app-launchers/)
    - [App clients](/useful-utilities/app-clients/)
    - [Phone connect](/useful-utilities/phone-connect/)
    - [Color pickers](/useful-utilities/color-pickers/)
    - [Clipboard managers](/useful-utilities/clipboard-managers/)
    - [File managers](/useful-utilities/file-managers/)
    - [Other](/useful-utilities/other/)
    - [Hypr ecosystem](/useful-utilities/hypr-ecosystem/)
    - [UWSM](/useful-utilities/uwsm/)
  + [Nix](/nix/)

    - [Hyprland on any distro using Nix](/nix/hyprland-on-any-distro-using-nix/)
    - [Hyprland on NixOS](/nix/installing-hyprland-on-nixos/)
    - [Configuring Hyprland with Hjem](/nix/configuring-hyprland-with-hjem/)
    - [Configuring Hyprland with Home Manager](/nix/configuring-hyprland-with-home-manager/)
    - [Cachix](/nix/cachix/)
    - [Advanced](/nix/advanced/)
    - [Contributing and Debugging](/nix/contributing-and-debugging/)
  + [NVIDIA](/nvidia/)
  + [IPC](/ipc/)
  + [Crashes and Bugs](/crashes-and-bugs/)
  + [FAQ](/faq/)
  + [Community](/community/)
  + [Contributing and debugging](/contributing-and-debugging/)

    - [Wiki writing guidelines](/contributing-and-debugging/wiki-guidelines/)
    - [Issue guidelines](/contributing-and-debugging/issue-guidelines/)
    - [PR guidelines](/contributing-and-debugging/pr-guidelines/)
    - [Tests](/contributing-and-debugging/tests/)
    - [Translations](/contributing-and-debugging/translations/)
* [Home](https://hypr.land/)
* [Showcase](https://hypr.land/hall_of_fame)
* [News](https://hypr.land/news)

* [Version selector ⚙️](/version-selector/)
* [Getting Started](/getting-started/)

  + [Installation](/getting-started/installation/)
  + [Master tutorial](/getting-started/master-tutorial/)
  + [Preconfigured setups](/getting-started/preconfigured-setups/)
* [Configuring](/configuring/)

  + [Naming conventions](/configuring/naming-conventions/)
  + [Selectors](/configuring/selectors/)
  + [Core](/configuring/core/)

    - [Monitors](/configuring/core/monitors/)

      * [Output selection](/configuring/core/monitors/output-selection/)
      * [Positioning](/configuring/core/monitors/positioning/)
      * [Monitor modes](/configuring/core/monitors/modes/)
      * [Colors and colorspaces](/configuring/core/monitors/colors/)
    - [Config options](/configuring/core/config-options/)
    - [Devices](/configuring/core/devices/)
    - [Dispatchers](/configuring/core/dispatchers/)
    - [Binds](/configuring/core/binds/)

      * [Flags](/configuring/core/binds/flags/)
      * [Keyboard layouts](/configuring/core/binds/keyboard-layouts/)
      * [Device binds](/configuring/core/binds/devices/)
      * [Submaps](/configuring/core/binds/submaps/)
      * [Global hotkeys and binds](/configuring/core/binds/globals/)
      * [Switches](/configuring/core/binds/switches/)
      * [Gestures](/configuring/core/binds/gestures/)
    - [Rules](/configuring/core/rules/)

      * [Window Rules](/configuring/core/rules/window-rules/)
      * [Workspace Rules](/configuring/core/rules/workspace-rules/)
      * [Layer rules](/configuring/core/rules/layer-rules/)
    - [Environment variables](/configuring/core/environment-variables/)
    - [Animations](/configuring/core/animations/)
    - [Autostart](/configuring/core/autostart/)
    - [Advanced configuration](/configuring/core/advanced-configuration/)

      * [Lua events](/configuring/core/advanced-configuration/events/)
      * [Lua utilities](/configuring/core/advanced-configuration/lua-utilities/)
      * [Using hyprctl](/configuring/core/advanced-configuration/using-hyprctl/)
      * [Notifications](/configuring/core/advanced-configuration/notifications/)
      * [Permissions](/configuring/core/advanced-configuration/permissions/)
  + [Layouts](/configuring/layouts/)

    - [Dwindle layout](/configuring/layouts/dwindle-layout/)
    - [Scrolling layout](/configuring/layouts/scrolling-layout/)
    - [Master layout](/configuring/layouts/master-layout/)
    - [Monocle layout](/configuring/layouts/monocle-layout/)
    - [Custom layouts](/configuring/layouts/custom-layouts/)
  + [Extra](/configuring/extra/)

    - [Multi-GPU](/configuring/extra/multi-gpu/)
    - [Virtual GPU](/configuring/extra/virtual-gpu/)
    - [Performance](/configuring/extra/performance/)
    - [Tearing](/configuring/extra/tearing/)
    - [Xwayland](/configuring/extra/xwayland/)
    - [Systemd](/configuring/extra/systemd/)
  + [Lua code snippets](/configuring/code-snippets/)
* [Hypr Ecosystem](/hypr-ecosystem/)

  + [User apps and utilities](/hypr-ecosystem/user/)

    - [hyprpaper](/hypr-ecosystem/user/hyprpaper/)
    - [hyprpicker](/hypr-ecosystem/user/hyprpicker/)
    - [hyprlauncher](/hypr-ecosystem/user/hyprlauncher/)
    - [hypridle](/hypr-ecosystem/user/hypridle/)
    - [hyprlock](/hypr-ecosystem/user/hyprlock/)
    - [xdg-desktop-portal-hyprland](/hypr-ecosystem/user/xdg-desktop-portal-hyprland/)
    - [hyprsysteminfo](/hypr-ecosystem/user/hyprsysteminfo/)
    - [hyprsunset](/hypr-ecosystem/user/hyprsunset/)
    - [hyprpolkitagent](/hypr-ecosystem/user/hyprpolkitagent/)
    - [hyprland-qt-support](/hypr-ecosystem/user/hyprland-qt-support/)
    - [hyprqt6engine](/hypr-ecosystem/user/hyprqt6engine/)
    - [hyprpwcenter](/hypr-ecosystem/user/hyprpwcenter/)
    - [hyprshutdown](/hypr-ecosystem/user/hyprshutdown/)
    - [hyprtoolkit (user docs)](/hypr-ecosystem/user/hyprtoolkit/)
    - [hyprcursor](/hypr-ecosystem/user/hyprcursor/)
  + [Developer libs and toolkits](/hypr-ecosystem/dev/)

    - [aquamarine](/hypr-ecosystem/dev/aquamarine/)
    - [hyprgraphics](/hypr-ecosystem/dev/hyprgraphics/)
    - [hyprland-guiutils](/hypr-ecosystem/dev/hyprland-guiutils/)
    - [hyprlang](/hypr-ecosystem/dev/hyprlang/)
    - [hyprtoolkit (developer docs)](/hypr-ecosystem/dev/hyprtoolkit/)
    - [hyprutils](/hypr-ecosystem/dev/hyprutils/)
    - [hyprwayland-scanner](/hypr-ecosystem/dev/hyprwayland-scanner/)
* [Hyprland plugins](/hyprland-plugins/)

  + [Using plugins](/hyprland-plugins/using-plugins/)
  + [Development](/hyprland-plugins/development/)

    - [Getting started](/hyprland-plugins/development/getting-started/)
    - [Plugin guidelines](/hyprland-plugins/development/plugin-guidelines/)
    - [Advanced](/hyprland-plugins/development/advanced/)
* [Useful utilities](/useful-utilities/)

  + [Must-have](/useful-utilities/must-have/)
  + [Status bars](/useful-utilities/status-bars/)
  + [Wallpapers](/useful-utilities/wallpapers/)
  + [Screen sharing](/useful-utilities/screen-sharing/)
  + [Screenshots and recording](/useful-utilities/screenshots-and-recording/)
  + [App launchers](/useful-utilities/app-launchers/)
  + [App clients](/useful-utilities/app-clients/)
  + [Phone connect](/useful-utilities/phone-connect/)
  + [Color pickers](/useful-utilities/color-pickers/)
  + [Clipboard managers](/useful-utilities/clipboard-managers/)
  + [File managers](/useful-utilities/file-managers/)
  + [Other](/useful-utilities/other/)
  + [Hypr ecosystem](/useful-utilities/hypr-ecosystem/)
  + [UWSM](/useful-utilities/uwsm/)
* [Nix](/nix/)

  + [Hyprland on any distro using Nix](/nix/hyprland-on-any-distro-using-nix/)
  + [Hyprland on NixOS](/nix/installing-hyprland-on-nixos/)
  + [Configuring Hyprland with Hjem](/nix/configuring-hyprland-with-hjem/)
  + [Configuring Hyprland with Home Manager](/nix/configuring-hyprland-with-home-manager/)
  + [Cachix](/nix/cachix/)
  + [Advanced](/nix/advanced/)
  + [Contributing and Debugging](/nix/contributing-and-debugging/)
* [NVIDIA](/nvidia/)
* [IPC](/ipc/)
* [Crashes and Bugs](/crashes-and-bugs/)
* [FAQ](/faq/)
* [Community](/community/)
* [Contributing and debugging](/contributing-and-debugging/)

  + [Wiki writing guidelines](/contributing-and-debugging/wiki-guidelines/)
  + [Issue guidelines](/contributing-and-debugging/issue-guidelines/)
  + [PR guidelines](/contributing-and-debugging/pr-guidelines/)
  + [Tests](/contributing-and-debugging/tests/)
  + [Translations](/contributing-and-debugging/translations/)

LightDark
System

* Light
* Dark
* System

On this page

* [Install Hyprland](#install-hyprland)
* [NVIDIA?](#nvidia)
* [VM?](#vm)
* [Launching Hyprland](#launching-hyprland)
* [DE-like pre-configured setups](#de-like-pre-configured-setups)
* [In Hyprland with the default config](#in-hyprland-with-the-default-config)
* [Monitors config](#monitors-config)
* [Fully configure Hyprland](#fully-configure-hyprland)
* [Important software](#important-software)
* [Apps / X11 replacements](#apps--x11-replacements)
* [Force apps to use Wayland](#force-apps-to-use-wayland)
* [Themes](#themes)
* [Cursors](#cursors)

Our sponsors

[![Omacom Foundation](https://hypr.land/imgs/sponsors/omarchy.svg)](https://omarchy.org)

---

[Edit this page on GitHub →](https://github.com/hyprwm/hyprland-wiki/edit/main/content/getting-started/master-tutorial.md)

Scroll to top

[Getting Started](/getting-started/)

Master tutorial

# Master tutorial

If you are coming to Hyprland for the first time, this is the main tutorial to read.

This tutorial covers everything you need to get things going.
It links to other pages where necessary.

## Install Hyprland

See [Installation](../installation) and come back here once you have successfully installed Hyprland.

Install `kitty` (default terminal emulator).
This is available in most distros’ repositories.

## NVIDIA?

Note

If not using an NVIDIA card, skip this step.

Please take a look at the [NVIDIA page](../../nvidia) before launching.
It has information regarding the needed environment and tweaks.

## VM?

Note

If not using a VM, skip this step.

In a VM, make sure you have 3D acceleration enabled in your `virtio` config (or `virt-manager`), otherwise Hyprland ***will not work***.

You can also pass through a real GPU to make it work.

Please bear in mind that 3D acceleration in VMs may be pretty slow.

## Launching Hyprland

Hyprland can be executed by typing `start-hyprland` in your TTY.

Warning

Do **not** launch Hyprland with `root` permissions (don’t `sudo`).

You can see some launch flags by doing `start-hyprland -- -h`, these include setting the config path, ignoring a check for the above, etc.

Login managers are not officially supported, but here’s a short compatibility list:

* SDDM: Works flawlessly.
  Install SDDM version ⩾ 0.20.0 or the [latest git version](https://github.com/sddm/sddm)
  (or [sddm-git](https://aur.archlinux.org/packages/sddm-git) from the AUR)
  to prevent SDDM bug [1476](https://github.com/sddm/sddm/issues/1476) (90s shutdowns).
* plasma-login-manager: Works flawlessly, but depends on systemd.
* GDM: Works with the caveat of crashing Hyprland on the first launch.
* greetd: Works flawlessly, especially with [ReGreet](https://github.com/rharish101/ReGreet).
* ly: Works flawlessly.

## DE-like pre-configured setups

Do you want to just get Hyprland pre-configured like a DE, without making your own configuration from scratch?

Check out the [Preconfigured setups page](../preconfigured-setups) to see a few options.

These dotfiles should do everything for you, and have their own tutorials as well.

If you choose to use those, you can skip the next step.
However, it’s still recommended to read all the points below it.
They’ll give you recommended apps, replacements for old X11 software, information about configuring displays, etc.

## In Hyprland with the default config

You’re good to go with your adventure, technically.

Use SUPER + Q to launch kitty.
If you wish to choose the default terminal before you proceed, you can do so in `~/.config/hypr/hyprland.lua` ([example config](https://github.com/hyprwm/Hyprland/blob/main/example/hyprland.lua)).

If you want the best experience with less hassle googling, keep reading.

## Monitors config

See [Monitors page](../../configuring/core/monitors) to learn all about configuring your displays.

## Fully configure Hyprland

Head onto the [Configuring page](../../configuring) to learn all about configuring Hyprland to your liking.

## Important software

See the [Must-have software page](../../useful-utilities/must-have) for the crucial things to make Wayland/Hyprland/other apps work correctly.

## Apps / X11 replacements

See the [Useful utilities page](../../useful-utilities) about that.
You can also visit the [Awesome-Hyprland](https://github.com/hyprland-community/awesome-hyprland) repository for a more comprehensive list.

## Force apps to use Wayland

A lot of apps will use Wayland by default.
Chromium (and other browsers based on it), as well as Electron apps, don’t.
You need to pass `--enable-features=UseOzonePlatform --ozone-platform=wayland` to them or use `.conf` files where possible.
Chromium-based browsers also should have a toggle in `chrome://flags`.
Search for “ozone” and select Wayland.
If you are on NixOS, you can also set the environment variable `NIXOS_OZONE_WL=1` in your configuration.

For most Electron apps, you should put the above in `~/.config/electron-flags.conf`.
Note that VSCode is known **not** to work with it.

A few more environment variables for forcing Wayland mode are documented [here](../../configuring/core/environment-variables).

You can check whether an app is running in Xwayland or not with `hyprctl clients`.

## Themes

Since Hyprland is not a fully-fledged Desktop Environment, you will need to use tools such as `lxappearance` or `nwg-look` (recommended) for GTK, and `hyprqt6engine` for qt6 apps.

## Cursors

Cursors are a notorious pain to set up when you don’t know how.
See [this FAQ entry on changing your mouse cursor](../../faq#how-do-i-change-my-mouse-cursor).

Last updated on November 20, 2026

[Installation](/getting-started/installation/ "Installation")[Preconfigured setups](/getting-started/preconfigured-setups/ "Preconfigured setups")

ESC

No results found.
