---
type: source
source_type: webpage
url: "https://wiki.hypr.land/crashes-and-bugs/"
title: "Crashes and Bugs – Hyprland Wiki"
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
    - [Configuring Hyprland with Home Manager](/nix/configuring-hyprland-with-home-manager/)
    - [Cachix](/nix/cachix/)
    - [Advanced](/nix/advanced/)
    - [Contributing and Debugging](/nix/contributing-and-debugging/)
  + [NVIDIA](/nvidia/)
  + [IPC](/ipc/)
  + [Crashes and Bugs](/crashes-and-bugs/)

    - [Getting the log](#getting-the-log)
    - [Obtaining the Hyprland Crash Report](#obtaining-the-hyprland-crash-report)
    - [Crashes at launch](#crashes-at-launch)
    - [Crashes not at launch](#crashes-not-at-launch)
    - [Obtaining a debug stacktrace](#obtaining-a-debug-stacktrace)
    - [Obtaining a trace log](#obtaining-a-trace-log)
    - [Bugs](#bugs)
    - [Bisecting an issue](#bisecting-an-issue)
    - [Building the Wayland stack with ASan](#building-the-wayland-stack-with-asan)
    - [Debugging DRM issues](#debugging-drm-issues)
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

* [Getting the log](#getting-the-log)
* [Obtaining the Hyprland Crash Report](#obtaining-the-hyprland-crash-report)
* [Crashes at launch](#crashes-at-launch)
* [Crashes not at launch](#crashes-not-at-launch)
* [Obtaining a debug stacktrace](#obtaining-a-debug-stacktrace)
* [Obtaining a trace log](#obtaining-a-trace-log)
* [Bugs](#bugs)
* [Bisecting an issue](#bisecting-an-issue)
* [Building the Wayland stack with ASan](#building-the-wayland-stack-with-asan)
* [Debugging DRM issues](#debugging-drm-issues)

Our sponsors

[![Omacom Foundation](https://hypr.land/imgs/sponsors/omarchy.svg)](https://omarchy.org)

---

[Edit this page on GitHub →](https://github.com/hyprwm/hyprland-wiki/edit/main/content/crashes-and-bugs/_index.md)

Scroll to top

Crashes and Bugs

# Crashes and Bugs

## Getting the log

First, make sure logging is enabled by [setting](../configuring/core/config-options#syntax) `debug.disable_logs` to `false`.
If you also need OpenGL messages, set `debug.gl_debugging` to `true`.

Remember to unset these when done logging, as they negatively impact performance.

Tip

Debug logging can be toggled dynamically, using `hyprctl eval` to change the option at runtime.
If you don’t need to see startup logs, consider setting debug options this way (rather than in your config file), so that you can simply reload your config to disable logging when you finish.

If you are in a TTY, and the Hyprland session that crashed was the last one you launched, the log can be printed with

```
cat $XDG_RUNTIME_DIR/hypr/$(ls -t $XDG_RUNTIME_DIR/hypr/ | head -n 1)/hyprland.log
```

If you are in a Hyprland session, and you want the log of the last session, use

```
cat $XDG_RUNTIME_DIR/hypr/$(ls -t $XDG_RUNTIME_DIR/hypr/ | head -n 2 | tail -n 1)/hyprland.log
```

## Obtaining the Hyprland Crash Report

If you have `$XDG_CACHE_HOME` set, the crash report directory is `$XDG_CACHE_HOME/hyprland`.
If not, it’s `$HOME/.cache/hyprland`.

Go to the crash report directory and you should find a file named `hyprlandCrashReport[XXXX].txt` where `[XXXX]` is the PID of the process that crashed.

Attach that file to your issue.

## Crashes at launch

Diagnose the issue by what is in the log:

* `backend failed to start`: launch in the TTY and refer to the logs shown in RED.
* `Monitor X has NO PREFERRED MODE, and an INVALID one was requested`: your monitor is broken.
* Other: see the coredump. Use `coredumpctl`, find the latest one’s PID and do `coredumpctl info PID`.
* failing on a driver (e.g. `radeon`): report an issue.
* failing on `Hyprland`: report an issue.

## Crashes not at launch

Report an issue on GitHub or on the Discord server.

## Obtaining a debug stacktrace

> Systemd-only.

1. Build Hyprland in debug (`make debug`).
2. Start Hyprland and get it to crash.
3. In a TTY or terminal, do `coredumpctl debug Hyprland`.
   * If GDB asks you for symbols, say `y`.
   * If it asks about paging, say `c`.
4. Once you get to `(gdb)`, start file logging with `set logging enabled`.
   * For a specific file, use `set logging file output.log`.
5. Run `bt -full`, then `exit` once finished, and attach the output.

## Obtaining a trace log

Launch Hyprland with `HYPRLAND_TRACE=1 AQ_TRACE=1` environment variables set.

These variables will enable *very* verbose logging and it’s not recommended to enable them unless debugging, as they might cause slowdowns and *massive* log files.

Try to reproduce your issue as fast as possible so we don’t have to sift through 1 million lines of logs.

## Bugs

First of all, ***READ THE [FAQ PAGE](../faq)***.

If your bug is not listed there, you can ask on the Discord server or open a [discussion on GitHub](https://github.com/hyprwm/Hyprland/discussions).

## Bisecting an issue

“Bisecting” is finding the first *git* commit that introduced a specific bug or regression using binary search.
This is done in `git` using the `git bisect` command.

First, clone the Hyprland repo if you haven’t already:

```
git clone --recursive https://github.com/hyprwm/Hyprland
cd Hyprland
```

Start the bisect process:

```
git bisect start
```

Enter the first known good commit hash that did not contain the issue:

```
git bisect good [good commit]
```

Then, enter the known bad commit hash that does contain the issue. You can simply use HEAD:

```
git bisect bad HEAD
```

`git` will now checkout a commit in the middle of the specified range.
Now, reset and build Hyprland:

```
git reset --hard --recurse-submodules
make all
```

…and run the built executable from the TTY `./build/Hyprland`.

Try to reproduce your issue.
If you can’t (i.e. the bug is not present), go back to the Hyprland repo and run `git bisect good`.
If you can reproduce it, run `git bisect bad`.
`git` will then checkout another commit and continue the binary search.
If there’s a build error, run `git bisect skip`.

Reset, build and install Hyprland again and repeat this step until `git` identifies the commit that introduced the bug:

```
[commit hash] is the first bad commit
```

## Building the Wayland stack with ASan

If requested, this is the deepest level of memory issue debugging possible.

*Do this in the TTY, with no Hyprland instances running.*

Clone Hyprland: `git clone --recursive https://github.com/hyprwm/Hyprland`

`make asan`

Reproduce your crash.
Hyprland will exit back to the TTY.

Now, in either `cwd`, `~` or `./build`, search for file(s) named `asan.log.XXXXX` where XXXXX is a number.

Zip all of them up and attach to your issue.

## Debugging DRM issues

DRM (Direct Rendering Manager) is the underlying kernel architecture to take a GPU buffer (something we can render to) and put it on your screen (via the GPU) instead of a window.

Freezes, glitches, and others, can be caused by issues with Hyprland’s communication with DRM, the driver or kernel.
In those cases, a DRM log is helpful.

Warning

Please note, these logs are EXTREMELY verbose.
Please reproduce your bug(s) ASAP to avoid getting a 1GB log.

```
echo 0x19F | sudo tee /sys/module/drm/parameters/debug  # enables verbose drm logging
sudo dmesg -C                                           # clears kernel debug logs
dmesg -w > ~/dmesg.log &                                # writes kernel logs in the background to a file at ~/dmesg.log
Hyprland

# ... repro the issue, then quit Hyprland

fg # after this, use CTRL+C to stop writing the logs
echo 0 | sudo tee /sys/module/drm/parameters/debug # disables drm logging, don't forget this to avoid slowdowns
```

After this, *attach* the `dmesg.log` file.

Last updated on November 20, 2026

ESC

No results found.
