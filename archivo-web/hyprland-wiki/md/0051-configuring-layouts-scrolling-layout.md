---
type: source
source_type: webpage
url: "https://wiki.hypr.land/configuring/layouts/scrolling-layout/"
title: "Scrolling layout – Hyprland Wiki"
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

        + [Config](#config)
        + [Workspace rules](#workspace-rules)
        + [Layout messages](#layout-messages)
        + [Convenience functions](#convenience-functions)
        + [Window rules](#window-rules)
        + [Layout-Handled Fullscreen](#layout-handled-fullscreen)
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

* [Config](#config)
* [Workspace rules](#workspace-rules)
* [Layout messages](#layout-messages)
* [Convenience functions](#convenience-functions)
* [Window rules](#window-rules)
* [Layout-Handled Fullscreen](#layout-handled-fullscreen)

Our sponsors

[![Omacom Foundation](https://hypr.land/imgs/sponsors/omarchy.svg)](https://omarchy.org)

---

[Edit this page on GitHub →](https://github.com/hyprwm/hyprland-wiki/edit/main/content/configuring/layouts/scrolling-layout.md)

Scroll to top

[Configuring](/configuring/)

[Layouts](/configuring/layouts/)

Scrolling layout

# Scrolling layout

Scrolling is a layout where windows are positioned on an infinitely growing tape.

[
](https://dl.hypr.land/wiki/demo_scrolling.mp4)

## Config

Category: `scrolling`

| Name | Description | Type | Default | Limits |
| --- | --- | --- | --- | --- |
| fullscreen\_on\_one\_column | When enabled, a single column on a workspace will always span the entire screen | bool | `true` |  |
| column\_width | The default width of a column | float | `0.5` | [0.1 - 1.0] |
| focus\_fit\_method | When a column is focused, what method should be used to bring it into view. 0 - center, 1 - fit, 2 - clamped\_center | int | `1` | [0 - 2] |
| follow\_focus | Behaviour of the scrolling tape when a window is in focus. 0: Focus doesn’t cause tape move. 1: Focus may cause tape move, mouse click always moves the tape. 2: Focus may cause tape move. | int | `1` | [0 - 2] |
| follow\_min\_visible | When a window is focused, require that at least a given fraction of it is visible for focus to follow. Hard input (e.g., binds, clicks) will always follow | float | `0.4` | [0.0 - 1.0] |
| explicit\_column\_widths | A comma-separated list of preconfigured widths for `colresize +conf/-conf` | string | `"0.333, 0.5, 0.667, 1.0"` |  |
| wrap\_focus | When enabled, causes `hl.dsp.layout("focus l/r")` to wrap around at the beginning and end | bool | `true` |  |
| wrap\_swapcol | When enabled, causes `hl.dsp.layout("swapcol l/r")` to wrap around at the beginning and end | bool | `true` |  |
| direction | Direction in which new windows appear and the layout scrolls. `"left"`/`"right"`/`"down"`/`"up"` | string | `"right"` |  |

## Workspace rules

| name | description | type |
| --- | --- | --- |
| direction | Same as the `scrolling.direction` config option, but per workspace | string |

For example:

```
hl.workspace_rule({ workspace = "2", layout_opts = { direction = "right" } })
```

## Layout messages

Dispatcher `hl.dsp.layout()` arguments:

| Name | Description | Params |
| --- | --- | --- |
| center | Centers the currently focused column | none |
| colresize | Resize the current column, to either a value or by a relative value (e.g., `0.5`, `+0.2`, `-0.2`), or cycle the preconfigured ones with `+conf` or `-conf`. Can also be `all (number)` for resizing all columns to a specific width | relative float/relative `conf` |
| consume | Moves the current window into the previous column | none |
| consume\_or\_expel | Expel if not alone, consume if alone in a column | `prev` or `next` |
| expel | Moves the current window to its own new column (in the backward direction if window is in the top half of the screen, otherwise in the forward direction) | none |
| fit | Executes a fit operation based on the argument. Available: `active`, `visible`, `all`, `toend`, `tobeg`, `expand`. `expand` will expand the current window to take up the remaining free space on the monitor | fit mode |
| fit\_into\_view | Fits the currently active column fully into view | none |
| focus | Moves the focus and centers the layout, while also wrapping instead of moving to neighboring monitors | direction |
| inhibit\_scroll | Prevents the scrolling view from moving for the currently active workspace. The switch is independent for each workspace | left empty for toggle, or `bool` for explicitly enabling/disabling |
| move | Move the layout horizontally, by either a relative logical px (`-200`, `+200`) or columns (`+col`, `-col`) | move data |
| promote | Moves a window to its own new column (in the forward direction) | none |
| swapcol | Swaps the current column with its neighbor to the left (`l`) or right (`r`). The swap wraps around (e.g., swapping the first column left moves it to the end) | `l` or `r` |

Example key bindings for your Hyprland config:

```
hl.bind(mainMod .. " + period", hl.dsp.layout("move +col"))
hl.bind(mainMod .. " + comma", hl.dsp.layout("swapcol l"))
```

## Convenience functions

* `hl.get_scrolling_offset()`
* `hl.set_scrolling_offset(double)`

Use the LSP (or examine the stubs yourself) for the return values. See [here](../../core#editor-autocompletion) to set up the LSP in your code editor.

## Window rules

With the static rule scrolling\_width you can set a starting column width for a window.

```
hl.window_rule({ name = "kitty_starting_width", match = { class = "kitty" }, scrolling_width = 0.5})
```

## Layout-Handled Fullscreen

Scrolling has an optional layout-handled fullscreen behavior, which uses its own fullscreen handler.
This custom fullscreen behavior allows you to scroll away from your fullscreen windows without them being un-fullscreened.

You can use it by using `layout_aware = true` (or not specifying `layout_aware` option at all) in your fullscreen dispatches when on a scrolling layout workspace.
It also works with existing window/workspace fullscreen-related selectors.

Note

When a fullscreen window has focus, the `hl.dsp.focus({ direction })` dispatcher will by default look for other monitors in the specified direction, rather than changing windows on the current monitor.
If you want to take advantage of the layout-handled ability to scroll away from a fullscreen window, either set `binds.movefocus_cycles_fullscreen = true` to restore the focus dispatcher’s window-seeking behavior, or use the scrolling layout’s `focus` layout message instead.

Learn more about Fullscreen Handlers [here](../../core/dispatchers#fullscreen-handlers).

Last updated on November 20, 2026

[Dwindle layout](/configuring/layouts/dwindle-layout/ "Dwindle layout")[Master layout](/configuring/layouts/master-layout/ "Master layout")

ESC

No results found.
