---
type: source
source_type: webpage
url: "https://wiki.hypr.land/nix/configuring-hyprland-with-hjem/"
title: "Configuring Hyprland with Hjem – Hyprland Wiki"
fetched_at: 2026-11-22T01:14:36+00:00
fetcher: "curl + markitdown"
site: "wiki.hypr.land"
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

      * [Writing your hyprland.lua directly inside your Nix config](#writing-your-hyprlandlua-directly-inside-your-nix-config)
      * [Sourcing a hyprland.lua file at your Nix config](#sourcing-a-hyprlandlua-file-at-your-nix-config)
      * [Hjem-impure](#hjem-impure)
      * [FindFiles](#findfiles)
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

* [Writing your hyprland.lua directly inside your Nix config](#writing-your-hyprlandlua-directly-inside-your-nix-config)
* [Sourcing a hyprland.lua file at your Nix config](#sourcing-a-hyprlandlua-file-at-your-nix-config)
* [Hjem-impure](#hjem-impure)
* [FindFiles](#findfiles)

Our sponsors

[![Omacom Foundation](https://hypr.land/imgs/sponsors/omarchy.svg)](https://omarchy.org)

---

[Edit this page on GitHub →](https://github.com/hyprwm/hyprland-wiki/edit/main/content/nix/configuring-hyprland-with-hjem.md)

Scroll to top

[Nix](/nix/)

Configuring Hyprland with Hjem

# Configuring Hyprland with Hjem

Hjem (“home” in Danish) is a module system that implements a simple and streamlined way to manage files in your `$HOME`, such as but not limited to files in your `~/.config`.
Hjem aims to serve as an alternative and easy-to-grasp utility for managing your `$HOME` purely and safely.

You can read the wonderful [Hjem documentation](https://hjem.feel-co.org/) to learn how to install and use it.

## Writing your hyprland.lua directly inside your Nix config

Here follows an example of how to write your `hyprland.lua` contents directly inside your Nix config using Hjem, which will allow you to use Nix string interpolation.

hyprland.nix

```
{
    hjem.users.youruser.xdg.config.files."hypr/hyprland.lua".text = /* lua */ ''
      # Your hyprland.lua content goes here.
      # You can use string interpolation for Nix to evaluate variables at build time.
      # A snippet of a hyprland.lua config using string interpolation for some variables to be interpreted by Nix:
          local monitor1 = "${config.custom.host.monitors."1"}"
          local monitor2 = "${config.custom.host.monitors."2"}"
          hl.monitor({
              output   = monitor2,
              ${lib.optionalString (hostName == "deck") "transform = 3"}
          })
    ''
}
```

## Sourcing a hyprland.lua file at your Nix config

Instead of writing your `hyprland.lua` contents directly inside your Nix config, you also have the possibility of sourcing an already existing `hyprland.lua` file using Hjem, to link it into its place at `~/.config/hypr/`.
If using version control, make sure this `hyprland.lua` is in the same repository as your config.
However, you can’t use Nix string interpolation this way.

hyprland.nix

```
{
    hjem.users.youruser.xdg.config.files."hypr/hyprland.lua".source = ./relative/path/to/file;
}
```

If you have already split your `hyprland.lua` into multiple files, you may source them the same way.

hyprland.nix

```
{
    hjem.users.youruser.xdg.config.files = {
        "hypr/hyprland.lua".source = ./relative/path/to/hyprland.lua;
        "hypr/rules.lua".source = ./relative/path/to/rules.lua;
        "hypr/keybinds.lua".source = ./relative/path/to/keybinds.lua;
        "hypr/animations.lua".source = ./relative/path/to/animations.lua;
    };
}
```

For multi-file examples such as the one above, you may prefer to just link a whole directory.
While you can do that in Hjem, it comes with the caveat that it makes the whole directory read-only.
This can be undesirable as it blocks any new files from being made inside that directory, breaking certain apps.
If you would like to recursively link only the files from inside a directory, [FindFiles](#findfiles) will interest you.

## Hjem-impure

Your `hyprland.lua` file will most likely change frequently.
What if you want to try a new change in your Hyprland config without having to build switch your NixOS config?
After `hyprland.lua` is deployed by Hjem, it will write a link into `~/.config/hyprland.lua` from the Nix store.
This file is read-only by default, but we can easily get to rewrite it by using a tool called [`hjem-impure`](https://github.com/Rexcrazy804/hjem-impure).

Executing `hjem-impure` replaces every Hjem symlink with writable normal files and directories.
So after that, you can write into your `~/.config/hyprland.lua` file deployed by Hjem.
**This enables experimentation.**
What this means is that, after a NixOS build switch or after a system reboot, the changes that you made in `~/.config/hyprland.lua` **will be gone**.
So after you are happy with your changes, write them into your Nix config for them to be persisted.

## FindFiles

[FindFiles](https://github.com/Michael-C-Buckley/findFiles.nix) is a small Nix library that allows you to easily link whole directories from inside your configuration to the correct locations.
It combines with a home management tool such as Hjem, which manages the linking itself, but it recursively finds files inside a directory.
This way you are linking every file in a folder instead of the folder itself all with one line of code.
Normal directory linking with Hjem links the whole folder, meaning the folder becomes read-only.
It works well with Hjem-impure if you desire hot reloading.
An example of what you can do with FindFiles:

* Have a config directory inside your repository and have it overlay on your entire `~/.config`.
* Have a Hyprland directory that gets auto-placed at `~/.config/hypr/`.

Last updated on November 20, 2026

[Hyprland on NixOS](/nix/installing-hyprland-on-nixos/ "Hyprland on NixOS")[Configuring Hyprland with Home Manager](/nix/configuring-hyprland-with-home-manager/ "Configuring Hyprland with Home Manager")

ESC

No results found.
