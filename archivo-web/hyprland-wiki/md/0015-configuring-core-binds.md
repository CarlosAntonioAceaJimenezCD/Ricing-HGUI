---
type: source
source_type: webpage
url: "https://wiki.hypr.land/configuring/core/binds/"
title: "Binds – Hyprland Wiki"
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

        + [Basics](#basics)
        + [Uncommon syms / binding with a keycode](#uncommon-syms--binding-with-a-keycode)
        + [Binding modkeys only](#binding-modkeys-only)
        + [Multiple binds to one key](#multiple-binds-to-one-key)
        + [Unbind](#unbind)
        + [XKB options](#xkb-options)
        + [Binding quirks](#binding-quirks)
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

* [Basics](#basics)
* [Uncommon syms / binding with a keycode](#uncommon-syms--binding-with-a-keycode)
* [Binding modkeys only](#binding-modkeys-only)
* [Multiple binds to one key](#multiple-binds-to-one-key)
* [Unbind](#unbind)
* [XKB options](#xkb-options)
* [Binding quirks](#binding-quirks)
* [Conditional bind resolution at bind time](#conditional-bind-resolution-at-bind-time)
* [Auto-consuming binds and return { ok = false }](#auto-consuming-binds-and-return--ok--false-)
* [Binding to keys handled by systemd-logind](#binding-to-keys-handled-by-systemd-logind)

Our sponsors

[![Omacom Foundation](https://hypr.land/imgs/sponsors/omarchy.svg)](https://omarchy.org)

---

[Edit this page on GitHub →](https://github.com/hyprwm/hyprland-wiki/edit/main/content/configuring/core/binds/_index.md)

Scroll to top

[Configuring](/configuring/)

[Core](/configuring/core/)

Binds

# Binds

Warning

**Keybind handlers must not block.**
Lua callbacks run on the compositor event loop.
Avoid `io.popen`, network I/O, clipboard tools (`wl-paste`, `xclip`), sleeps, and other long-running work inside bind functions.
Prefer `hl.dsp.exec_cmd(...)` for external commands so they run outside the bind callback.
If you must probe the system from Lua, bound the wait (for example with `timeout`).
A hung or slow call freezes input and the entire desktop until it returns.

Tip

If you are unsure of what your key’s name/keysym/keycode is, you can use [`wev`](https://github.com/jwrdegoede/wev) to find out.

## Basics

Basic syntax is:

```
hl.bind("keys", dispatcher or function(), { bind_flags })
```

The dispatcher list can be found in [Dispatchers](../dispatchers).
You can also supply a Lua function to your bind, if you prefer, and the bind will call it for you.

Bind flags are described [here](./flags).

**Examples**

```
-- bind SUPER + SHIFT + Q to open Firefox
hl.bind("SUPER + SHIFT + Q", hl.dsp.exec_cmd("firefox"))

-- bind to an anonymous function with logic inside
hl.bind("SUPER + SHIFT + X", function()
    -- more logic...
    hl.dispatch(hl.dsp.window.float())
end)
```

## Uncommon syms / binding with a keycode

See the [xkbcommon-keysyms.h header](https://github.com/xkbcommon/libxkbcommon/blob/master/include/xkbcommon/xkbcommon-keysyms.h) for all the keysyms.
The name you should use is the segment after `XKB_KEY_`.

To bind a keycode, use the `code:` prefix before the key.
For example:

```
hl.bind("SUPER + code:28", hl.dsp.exec_cmd("amongus"))
```

will bind `SUPER + T`, since `T` is keycode 28.

## Binding modkeys only

To bind only a modkey, use the appropriate keysym name.
Usually it is a `MOD` key, suffixed with `_L` or `_R`.
When a keysym is used, the order in which keys are pressed matters because keys are no longer treated as modifiers.

**Examples**

```
-- bind `amongus` to left alt
hl.bind("Alt_L", hl.dsp.exec_cmd("amongus"))

-- bind left super with left ctrl to open kitty
hl.bind("Super_L + Alt_L", hl.dsp.exec_cmd("kitty"))

-- bind left ctrl and right ctrl
hl.bind("Ctrl_L + Ctrl_R", hl.dsp.exec_cmd("kitty"))

-- bind super release to trigger only when not used as part of a key combo
hl.bind("Super_L", hl.dsp.exec_cmd("hyprlauncher -t"), { release = true })
```

## Multiple binds to one key

Warning

The keybinds will be executed top to bottom, in the order they were written.

You can trigger multiple actions with the same keybind by using a Lua lambda function, which can then execute multiple dispatch calls:

```
-- To switch between windows in a floating workspace:
hl.bind("SUPER + Tab", function()
    -- Change focus to another window
    hl.dispatch(hl.dsp.window.cycle_next())
    -- Bring it to the top
    hl.dispatch(hl.dsp.window.alter_zorder({ mode = "top" }))
end)
```

## Unbind

To unbind a key, use `hl.unbind("key")` or assign it to a variable and use the `:unbind()` or `:remove()` methods on it.
The key in `hl.unbind` is case-sensitive and must exactly match the case of the `hl.bind` you are unbinding.
Unbind will remove all occurrences of the key that were registered before it.

**Examples**

```
hl.bind("SUPER + TAB", hl.focus.workspace("e+1"))
hl.unbind("SUPER + Tab") -- this will NOT unbind
hl.unbind("SUPER + TAB") -- this will unbind

-- assign bind to "lft"
local moveLeft = hl.bind("SUPER + L", hl.dsp.window.move({ direction = "left" }) )

-- unbind "SUPER + L"
moveLeft:unbind()
-- or
moveLeft:remove()
```

## XKB options

To change the behavior of some keys, use `kb_options`.

To view all available options, run:

```
cat /usr/share/X11/xkb/rules/base.lst
```

**Examples**

To remap Caps Lock to Ctrl:

```
hl.config({
    input = {
        kb_options = "ctrl:nocaps"
    }
})
```

To swap Caps Lock and Escape:

```
hl.config({
    input =  {
        kb_options = "caps:swapescape"
    }
})
```

## Binding quirks

### Conditional bind resolution at bind time

When trying to create a bind with a condition inside it, you almost always want to wrap it in a function.
For example, this bind:

```
hl.bind("SUPER + L", hl.dsp.exec_cmd("foot", { float = not (hl.get_active_window().title == "foot") }) )
```

will be resolved to:

```
hl.bind("SUPER + L", hl.dsp.exec_cmd("foot", { float = false }) )
-- or, depending on your focus when config was reloaded
hl.bind("SUPER + L", hl.dsp.exec_cmd("foot", { float = true }) )
```

And it will stay like that until next config reload.
To make this act like you probably meant, the logic must be wrapped in a function:

```
hl.bind("SUPER + L", function()
    local is_foot = hl.get_active_window().title == "foot"
    hl.dispatch( hl.dsp.exec_cmd("foot", { float = not is_foot }) )
end)
```

Now the condition will be evaluated on each call of the bind, rather than only once at config load time.

### Auto-consuming binds and `return { ok = false }`

After executing a dispatcher, it can return an `ok` value to indicate whether it ran successfully.
When the `auto_consuming` flag is set, `hl.bind` checks that value to determine whether the keypress should be consumed or passed on.

**Example**

```
hl.bind("p", function()
    local window = hl.get_active_window()
    if window and window.title == "some cool app" then
        hl.dispatch(hl.dsp.exec_cmd("another_cool_app"))
    else
        return { ok = false }
    end
end, { auto_consuming = true })
```

This bind will spawn `another_cool_app` if the active window’s title is `"some cool app"`; otherwise it will pass `p` to the active window.

### Binding to keys handled by systemd-logind

Normally, systemd-logind will handle hardware events such as the power button or lid switch.
While this can be disabled globally by editing its config file, a better option is to block that handling specifically while Hyprland is running.

This can be accomplished using `systemd-inhibit`.
For example, you might launch Hyprland via `systemd-inhibit --what=handle-power-key Hyprland`, and then create a bind to the relevant key event (`XF86PowerOff` in this case).

Last updated on November 20, 2026

ESC

No results found.
