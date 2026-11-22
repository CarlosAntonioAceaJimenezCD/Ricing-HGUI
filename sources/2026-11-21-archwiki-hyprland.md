---
type: source
source_type: webpage
url: "https://wiki.archlinux.org/title/Hyprland"
title: "ArchWiki · Hyprland"
fetched_at: 2026-11-22T00:51:12+00:00
fetcher: curl + markitdown
author: "Arch Linux Wiki"
---

* [Home](https://archlinux.org/)
* [Packages](https://archlinux.org/packages/)
* [Forums](https://bbs.archlinux.org/)
* [Wiki](https://wiki.archlinux.org/)
* [GitLab](https://gitlab.archlinux.org/archlinux)
* [Security](https://security.archlinux.org/)
* [AUR](https://aur.archlinux.org/)
* [Download](https://archlinux.org/download/)

[Jump to content](#bodyContent)

[ ]

Main menu

Main menu

move to sidebar
hide

Navigation

* [Main page](/title/Main_page "Visit the main page [z]")
* [Table of contents](/title/Table_of_contents)
* [Getting involved](/title/Getting_involved "Various ways Archers can contribute to the community")
* [Wiki news](/title/ArchWiki%3ANews "The latest lowdown on the wiki")
* [Random page](/title/Special%3ARandom "Load a random page [x]")

Interaction

* [Help](/title/Category%3AHelp "Wiki navigation, reading, and editing help")
* [Contributing](/title/ArchWiki%3AContributing)
* [Recent changes](/title/Special%3ARecentChanges "A list of recent changes in the wiki [r]")
* [Recent talks](https://wiki.archlinux.org/index.php?title=Special:RecentChanges&namespace=all-discussions)
* [New pages](/title/Special%3ANewPages)
* [Statistics](/title/ArchWiki%3AStatistics)
* [Requests](/title/ArchWiki_talk%3ARequests)

[**ArchWiki**](/title/Main_page)

[Search](/title/Special%3ASearch "Search ArchWiki [f]")

Search

[ ]

Appearance

* [Create account](/index.php?title=Special:CreateAccount&returnto=Hyprland "You are encouraged to create an account and log in; however, it is not mandatory")
* [Log in](/index.php?title=Special:UserLogin&returnto=Hyprland "You are encouraged to log in; however, it is not mandatory [o]")

[ ]

Personal tools

* [Create account](/index.php?title=Special:CreateAccount&returnto=Hyprland "You are encouraged to create an account and log in; however, it is not mandatory")
* [Log in](/index.php?title=Special:UserLogin&returnto=Hyprland "You are encouraged to log in; however, it is not mandatory [o]")

## Contents

move to sidebar
hide

* Beginning
* [1
  Installation](#Installation)
* [2
  Configuration](#Configuration)

  Toggle Configuration subsection
  + [2.1
    Keyboard](#Keyboard)
    - [2.1.1
      Keymap](#Keymap)
    - [2.1.2
      Typematic delay and rate](#Typematic_delay_and_rate)
    - [2.1.3
      Keyboard backlight](#Keyboard_backlight)
    - [2.1.4
      Media keys](#Media_keys)
  + [2.2
    Touchpad gestures](#Touchpad_gestures)
  + [2.3
    Display settings](#Display_settings)
    - [2.3.1
      Screen sharing](#Screen_sharing)
    - [2.3.2
      Setting screen resolution](#Setting_screen_resolution)
    - [2.3.3
      Settings GUI](#Settings_GUI)
    - [2.3.4
      Screen backlight](#Screen_backlight)
* [3
  Usage](#Usage)

  Toggle Usage subsection
  + [3.1
    Starting](#Starting)
    - [3.1.1
      Universal Wayland Session Manager](#Universal_Wayland_Session_Manager)
    - [3.1.2
      Terminal](#Terminal)
    - [3.1.3
      Display managers](#Display_managers)
    - [3.1.4
      Auto login](#Auto_login)
  + [3.2
    hyprctl and IPC](#hyprctl_and_IPC)
  + [3.3
    Autostart](#Autostart)
  + [3.4
    Setting environment variables](#Setting_environment_variables)
* [4
  Hypr-Ecosystem](#Hypr-Ecosystem)

  Toggle Hypr-Ecosystem subsection
  + [4.1
    Hyprpaper](#Hyprpaper)
  + [4.2
    Hyprpicker](#Hyprpicker)
  + [4.3
    Hypridle](#Hypridle)
  + [4.4
    Hyprlock](#Hyprlock)
  + [4.5
    Hyprcursor](#Hyprcursor)
    - [4.5.1
      Hyprcursor themes](#Hyprcursor_themes)
  + [4.6
    XDG-Desktop-Portal-Hyprland](#XDG-Desktop-Portal-Hyprland)
  + [4.7
    Hyprpolkitagent](#Hyprpolkitagent)
  + [4.8
    Hyprsunset](#Hyprsunset)
  + [4.9
    Hyprsysteminfo](#Hyprsysteminfo)
* [5
  Tips and tricks](#Tips_and_tricks)

  Toggle Tips and tricks subsection
  + [5.1
    File manager](#File_manager)
  + [5.2
    Application launcher](#Application_launcher)
  + [5.3
    Idle](#Idle)
    - [5.3.1
      Automatic screen locking and suspend](#Automatic_screen_locking_and_suspend)
    - [5.3.2
      Turning off the screen using DPMS after a timeout period](#Turning_off_the_screen_using_DPMS_after_a_timeout_period)
  + [5.4
    Status bar](#Status_bar)
    - [5.4.1
      Workspace overview](#Workspace_overview)
  + [5.5
    Polkit authentication](#Polkit_authentication)
  + [5.6
    Desktop wallpaper](#Desktop_wallpaper)
    - [5.6.1
      Using a script to randomize the wallpaper](#Using_a_script_to_randomize_the_wallpaper)
  + [5.7
    On-screen notifications](#On-screen_notifications)
    - [5.7.1
      Mako](#Mako)
      * [5.7.1.1
        Keyboard backlight notifications](#Keyboard_backlight_notifications)
      * [5.7.1.2
        Media key notifications](#Media_key_notifications)
      * [5.7.1.3
        Screen backlight notifications](#Screen_backlight_notifications)
      * [5.7.1.4
        Keyboard language notifications](#Keyboard_language_notifications)
  + [5.8
    Power control](#Power_control)
  + [5.9
    Clipboard](#Clipboard)
  + [5.10
    Enable/disable devices](#Enable/disable_devices)
  + [5.11
    Separate dconf profile](#Separate_dconf_profile)
  + [5.12
    KDE Plasma applications not following Qt theming](#KDE_Plasma_applications_not_following_Qt_theming)
* [6
  Troubleshooting](#Troubleshooting)

  Toggle Troubleshooting subsection
  + [6.1
    Jetbrains apps focus issues](#Jetbrains_apps_focus_issues)
  + [6.2
    Squares instead of text after fresh install](#Squares_instead_of_text_after_fresh_install)
* [7
  See also](#See_also)

[ ]

Toggle the table of contents

# Hyprland

[ ]

4 languages

* [日本語](https://wiki.archlinux.jp/index.php/Hyprland "Hyprland – 日本語")
* [Português](https://wiki.archlinux.org/title/Hyprland_%28Portugu%C3%AAs%29 "Hyprland – português")
* [Русский](https://wiki.archlinux.org/title/Hyprland_%28%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%29 "Hyprland – русский")
* [中文（简体）](https://wiki.archlinuxcn.org/wiki/Hyprland "Hyprland – 中文（简体）")

* [Page](/title/Hyprland "View the content page [c]")
* [Discussion](/title/Talk%3AHyprland "Discussion about the content page [t]")

[ ]
English

* [Read](/title/Hyprland)
* [View source](/index.php?title=Hyprland&action=edit "This page is protected.
  You can view its source [e]")
* [View history](/index.php?title=Hyprland&action=history "Past revisions of this page [h]")

[ ]
Tools

Tools

move to sidebar
hide

Actions

* [Read](/title/Hyprland)
* [View source](/index.php?title=Hyprland&action=edit)
* [View history](/index.php?title=Hyprland&action=history)

General

* [What links here](/title/Special%3AWhatLinksHere/Hyprland "A list of all wiki pages that link here [j]")
* [Related changes](/title/Special%3ARecentChangesLinked/Hyprland "Recent changes in pages linked from this page [k]")
* Printable version
* [Permanent link](/index.php?title=Hyprland&oldid=887257 "Permanent link to this revision of this page")
* [Page information](/index.php?title=Hyprland&action=info "More information about this page")

Appearance

move to sidebar
hide

From ArchWiki

Related articles

* [Window manager](/title/Window_manager "Window manager")
* [Wayland](/title/Wayland "Wayland")

[Hyprland](https://hypr.land/) is an independent tiling [Wayland compositor](/title/Wayland#Compositors "Wayland"). Noteworthy features of Hyprland include dynamic tiling, tabbed windows, a clean and readable C++ code-base, and a custom renderer that provides window animations, rounded corners, and Dual-Kawase Blur on transparent windows. General usage and configuration is thoroughly documented at [Hyprland wiki](https://wiki.hypr.land/).

## Installation

[Install](/title/Install "Install") the [hyprland](https://archlinux.org/packages/?name=hyprland) package.

**Note**

* Using an [NVIDIA](/title/NVIDIA "NVIDIA") GPU with Hyprland is unsupported, but may work. Users should follow the NVIDIA specific page on the [upstream Wiki](https://wiki.hypr.land/Nvidia/) before trying to launch Hyprland. Failure to do so will likely result in many bugs including not being able to log in, flashing windows and high CPU usage.

* Make sure to install the [Polkit](/title/Polkit "Polkit") package, or [start](/title/Start "Start") and [enable](/title/Enable "Enable") `seatd.service`. As the lack thereof will cause Hyprland to fail to start.
* For Vmware/VirtualBox users, it may be necessary to enable 3D acceleration in order to run Hyprland properly.

## Configuration

**Note** Most of the configuration options listed below (and many more) are explained in detail on the [upstream Wiki](https://wiki.hypr.land/Configuring/). Since version 0.55, Hyprland has transitioned to Lua for its configuration, deprecating the older custom syntax.

Configuration is done through a single Lua file, typically located at `~/.config/hypr/hyprland.lua`. If the file does not exist, *hyprland* will automatically generate an example configuration. You can also split your configuration into multiple files and load them using the Lua `require()` function. The default generated configuration can also be found at `/usr/share/hypr/hyprland.lua`.

The `hyprland.lua` file contains directives to configure devices like keyboards and monitors, as well as layout, decoration, and animation settings. You can define window rules, key bindings, and commands to execute at startup.

The configuration is reloaded automatically the moment you save the file. Alternatively, you can reload it manually by executing `hyprctl reload`. For some settings, you may have to restart your Hyprland session.

Settings can also be changed on the fly with *hyprctl* but they will not be saved.

### Keyboard

#### Keymap

By default, Hyprland will use the `us` layout; you can configure a different layout using the `hl.config()` function:

```
~/.config/hypr/hyprland.lua
```

```
-- German Colemak layout
hl.config({
    input = {
        kb_layout = "de",
        kb_variant = "colemak",
    }
})
```

See the [upstream's Wiki](https://wiki.hypr.land/Configuring/Basics/Variables/#input) for all available options.

**Note** Hyprland will override [locale](/title/Locale "Locale") definitions so its necessary to change keymap if you do not use a `us` layout keyboard.

#### Typematic delay and rate

While Xorg users will be used to having this setting [defined at the server level](/title/Xorg/Keyboard_configuration#Adjusting_typematic_delay_and_rate "Xorg/Keyboard configuration"), on Wayland each compositor handles it on its own:

```
~/.config/hypr/hyprland.lua
```

```
-- Repeat rate and delay
hl.config({
    input = {
        repeat_rate = 25,
        repeat_delay = 600,
    }
})
```

#### Keyboard backlight

Using keyboard brightness controls in Hyprland is possible. [Install](/title/Install "Install") [brightnessctl](https://archlinux.org/packages/?name=brightnessctl) then add the related binds (replace `keyboard_brightness_*` with `SUPER`, `FX` or `XF86KbdBrightness` depending on how your hardware exposes the [keyboard backlight](/title/Keyboard_backlight "Keyboard backlight")):

```
~/.config/hypr/hyprland.lua
```

```
-- Keyboard backlight
hl.bind("keyboard_brightness_up_shortcut", hl.dsp.exec_cmd("brightnessctl -d *::kbd_backlight set +33%"))
hl.bind("keyboard_brightness_down_shortcut", hl.dsp.exec_cmd("brightnessctl -d *::kbd_backlight set 33%-"))
```

It is also possible to have [on-screen notifications](#On_screen_notifications) that fire when changes are made.

#### Media keys

Using keyboard media controls in Hyprland is possible by making use of `XF86Audio` keysyms and an external application like [pavucontrol](https://archlinux.org/packages/?name=pavucontrol) or [pamixer](https://archlinux.org/packages/?name=pamixer) and [playerctl](/title/Playerctl "Playerctl"):

```
~/.config/hypr/hyprland.lua
```

```
-- Volume and Media Control
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("pamixer -i 5"), { repeating = true })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("pamixer -d 5"), { repeating = true })
hl.bind("XF86AudioMicMute", hl.dsp.exec_cmd("pamixer --default-source -m"))
hl.bind("XF86AudioMute", hl.dsp.exec_cmd("pamixer -t"))
hl.bind("XF86AudioPlay", hl.dsp.exec_cmd("playerctl play-pause"))
hl.bind("XF86AudioPause", hl.dsp.exec_cmd("playerctl play-pause"))
hl.bind("XF86AudioNext", hl.dsp.exec_cmd("playerctl next"))
hl.bind("XF86AudioPrev", hl.dsp.exec_cmd("playerctl previous"))
```

It is also possible to have [on-screen notifications](#On_screen_notifications) that fire when changes are made.

### Touchpad gestures

Being a [Wayland](/title/Wayland "Wayland") compositor, Hyprland has full support for touchpad gestures though they are disabled by default. To enable them, make the following edit using the `hl.gesture()` function:

```
~/.config/hypr/hyprland.lua
```

```
-- Enable touchpad gestures
hl.gesture({
    fingers = 3,
    direction = "horizontal",
    action = "workspace"
})
```

See the [upstream Wiki](https://wiki.hypr.land/Configuring/Advanced-and-Cool/Gestures/) for all available options.

### Display settings

#### Screen sharing

See [Screencast](/title/Screencast "Screencast").

Being a wlroots-compatible compositor, Hyprland can utilize [xdg-desktop-portal-wlr](https://archlinux.org/packages/?name=xdg-desktop-portal-wlr) to enable screen capture in a range of applications by way of [xdg-desktop-portal](/title/Xdg-desktop-portal "Xdg-desktop-portal").

Hyprland also maintains [xdg-desktop-portal-hyprland](https://archlinux.org/packages/?name=xdg-desktop-portal-hyprland), which supports screen sharing (including region sharing and window sharing), global shortcuts, and has a graphical picker utility. Usage of the portal is further documented in the [Hyprland wiki](https://wiki.hypr.land/Hypr-Ecosystem/xdg-desktop-portal-hyprland/).

It is worth noting that *xdg-desktop-portal-hyprland* does not include a file picker, for which users can additionally install [xdg-desktop-portal-gtk](https://archlinux.org/packages/?name=xdg-desktop-portal-gtk).

#### Setting screen resolution

Hyprland will try to detect your screen resolution automatically and then select either 1x, 1.5x, or 2x screen scaling. However, in some cases it will fail and default to a fail-safe, usually if there are multiple screens present or if you have a hybrid laptop. If everything on your screen is huge then you need to configure your default monitor and resolution.

First find your default monitor using *hyprctl*:

```
$ hyprctl monitors
```

```
Monitor eDP-1 (ID 0):
        1920x1080@144.003006 at 0x0
        description: Chimei Innolux Corporation 0x153C (eDP-1)
        ...
```

Then add your monitor to the configuration using the `hl.monitor()` function:

```
~/.config/hypr/hyprland.lua
```

```
-- Monitor details
hl.monitor({
    output = "eDP-1",
    mode = "1920x1080@144",
    position = "0x0",
    scale = 1,
})
```

`0x0` is a position offset used for multi screen setups and the final `1` is the screen scaling factor.

See the [upstream Hyprland Monitors Wiki](https://wiki.hypr.land/Configuring/Basics/Monitors/) for more details.

#### Settings GUI

There is the [nwg-displays](https://archlinux.org/packages/?name=nwg-displays) package, a GUI application for monitor arrangement, that supports Hyprland. It is part of the [nwg-shell](/title/Nwg-shell "Nwg-shell") (but works standalone), see [nwg-displays github](https://github.com/nwg-piotr/nwg-displays) for more details.

#### Screen backlight

[Install](/title/Install "Install") [brightnessctl](https://archlinux.org/packages/?name=brightnessctl) then add the following binds:

```
~/.config/hypr/hyprland.lua
```

```
-- Screen brightness
hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("brightnessctl s +5%"))
hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("brightnessctl s 5%-"))
```

It is also possible to have [on-screen notifications](#On_screen_notifications) that fire when changes are made.

## Usage

### Starting

#### Universal Wayland Session Manager

[Universal Wayland Session Manager](/title/Universal_Wayland_Session_Manager "Universal Wayland Session Manager") wraps the compositor and accordingly configured applications and daemons through systemd unit files, allowing you to control them with *systemctl*.

Hyprland can be started via a [Display manager](/title/Display_manager "Display manager") with *uwsm* by selecting *hyprland (uwsm-managed)*.

You can start Hyprland with uwsm both in a [getty](/title/Getty "Getty") via the following script in your [login shell](/title/Login_shell "Login shell"):

```
if uwsm check may-start && uwsm select; then
  exec systemd-cat -t uwsm_start uwsm start default
fi
```

**Note**

* `uwsm check may-start` checks whether it is OK to launch a wayland session, in particular if it is running from a [login shell](/title/Login_shell "Login shell"). However, you should still avoid using it inside `.bashrc` or other files which are sourced even by nonlogin shells. **Ensure this snippet is placed at the bottom of your profile file**, as executing it will block the rest of the file from running.
* Hyprland no longer [recommends](https://github.com/hyprwm/hyprland-wiki/commit/7611480bc4c6a5cae1734cd7d6ea480b55e4c368) starting your session with *uwsm* as it is considered experimental and intended for advanced users who understand its implications and [quirks](https://github.com/hyprwm/Hyprland/discussions/11255#discussioncomment-13938618).

**Tip** If you want to bypass compositor selection menu and launch Hyprland directly, use this code in your [login shell](/title/Login_shell "Login shell"), instead:

```
if uwsm check may-start; then
  exec uwsm start hyprland.desktop
fi
```

**Warning** If you choose to start Hyprland via *uwsm* then you should accordingly adjust your configuration. In particular:

* **you must avoid using the `hl.dsp.exit()` dispatcher or terminate the Hyprland process directly since this would interfere with the normal shutdown process**. Use instead `uwsm stop` or `loginctl terminate-user ""` to terminate Hyprland and exit user session, for example:

```
~/.config/hypr/hyprland.lua
```

```
hl.bind("SUPER + M", hl.dsp.exec_cmd("uwsm stop"))
```

* Do not put environment variables in `hyprland.lua`, but use instead *uwsm* files `~/.config/uwsm/env` for variables common to all graphical sessions managed by uwsm (GTK, Qt, xcursor, ...) and `~/.config/uwsm/env-hyprland` for Hyprland exclusive environment variables (`HYPR*` and `AQ_*` variables for example). The format of these files is `export KEY=VALUE` on each line without comments. It is strongly suggested, if you use multiple GPUs, to put the environment variable `AQ_DRM_DEVICES` inside `env-hyprland` in order to avoid conflicts with other compositors.

Read the [related page in Hyprland's wiki](https://wiki.hypr.land/Useful-Utilities/Systemd-start/) for additional information about configuration with uwsm.

#### Terminal

You can start Hyprland from a [getty](/title/Getty "Getty") with the following command:

```
$ start-hyprland
```

**Note** Hyprland no longer [recommends](https://hypr.land/news/update53/) starting your session with `Hyprland` as the new wrapper provides crash recovery and safe mode.

#### Display managers

While launching from a [display manager](/title/Display_manager "Display manager") is not officially supported, users have reported success launching from [GDM](/title/GDM "GDM"), [SDDM](/title/SDDM "SDDM"), and others. The [upstream wiki](https://wiki.hypr.land/Getting-Started/Master-Tutorial/#launching-hyprland) maintains a compatibility list with display managers. The [hyprland](https://archlinux.org/packages/?name=hyprland) package contains two [desktop entries](/title/Desktop_entries "Desktop entries"), and all Hyprland AUR packages will generate one automatically.

Both methods provide identical results, plus or minus a few environment variables and services.

#### Auto login

Users can automatically login by using a [display manager](/title/Display_manager "Display manager") or adapting the method described in [Xinit#Autostart X at login](/title/Xinit#Autostart_X_at_login "Xinit").

### hyprctl and IPC

*hyprctl* is a command line utility that comes installed with Hyprland to communicate with the display server. It allows you to dispatch commands to the server (equivalent to commands in the configuration file, but with a slightly different syntax), set keywords, send queries and request information. See the [full documentation](https://wiki.hypr.land/Configuring/Using-hyprctl/).

Hyprland also exposes [2 UNIX Sockets](https://wiki.hypr.land/IPC/) for controlling and getting information about Hyprland via code or command-line utilities. These sockets broadcast events on focus change (windows, workspaces, monitors), creation of windows/workspace, and so on.

Both *hyprctl* and the IPC sockets can be effectively used in scripts to control Hyprland for complex tasks.

### Autostart

In the Lua configuration, autostarting applications is done by executing commands inside the `hyprland.start` event listener.

**Note** As mentioned in <#Configuration>, Hyprland automatically parses `hyprland.lua` **each time a change to the file is saved**. Using the `hl.on("hyprland.start", ...)` event ensures that your startup applications and daemons are launched only once at boot, preventing race conditions or multiple instances running simultaneously on reload.

**Tip** If you started Hyprland via Universal Wayland Session Manager (uwsm) and the application you want to run at startup provides a systemd unit then you can [enable](/title/Enable "Enable") it to automatically start it when Hyprland is ready. Otherwise, you can pass that application to `uwsm app` as argument in order to be managed by *uwsm*. For example:

```
~/.config/hypr/hyprland.lua
```

```
hl.on("hyprland.start", function ()
    hl.exec_cmd("uwsm app -- mycommand --arg1 --arg2")
end)
hl.bind("SUPER + E", hl.dsp.exec_cmd("uwsm app -- pcmanfm-qt.desktop"))
```

### Setting environment variables

It is possible to set [environment variables](/title/Environment_variables "Environment variables") directly in `hyprland.lua` through the `hl.env()` function, which has a different syntax than the *env* UNIX command used by shells.

The differences are explained on the [upstream Wiki](https://wiki.hypr.land/Configuring/Advanced-and-Cool/Environment-variables/).

KDE Frameworks applications such as Dolphin or digiKam may show an empty
*Open With* menu if `XDG_MENU_PREFIX` is unset. Set it to match an
installed menu file in `/etc/xdg/menus/`, for example:

```
~/.config/hypr/hyprland.lua
```

```
hl.env("XDG_MENU_PREFIX", "gnome-")
```

Use `plasma-` for `plasma-applications.menu` or `xfce-` for
`xfce-applications.menu`. Then rebuild the KDE service cache:

```
$ kbuildsycoca6 --noincremental
```

## Hypr-Ecosystem

**Warning** Some of the tools outlined in the following section are still work in progress. As such, bugs are to be expected. For this reason full instructions and examples will be omitted until they mature enough to be stable. Detailed instructions on their use is outlined on the [upstream Wiki](https://wiki.hypr.land/Hypr-Ecosystem/).

The Hyprland development team are building an ecosystem of applications tailored to be specifically used with Hyprland; these tools will include dispatchers allowing for them to be controlled with `hyprctl` rather than relying on scripts.

Currently the ecosystem consists of:

### Hyprpaper

Hyprpaper is a wallpaper utility; it can be installed with the [hyprpaper](https://archlinux.org/packages/?name=hyprpaper) package.

### Hyprpicker

Hyprpicker is a utility to grab a colour from a desktop; it can be installed with the [hyprpicker](https://archlinux.org/packages/?name=hyprpicker) package. It does not require any configuration.

### Hypridle

Hypridle is an idle management daemon; it can be installed with the [hypridle](https://archlinux.org/packages/?name=hypridle) package.

### Hyprlock

[Hyprlock](/title/Hyprlock "Hyprlock") is a screen lock manager; it can be installed with the [hyprlock](https://archlinux.org/packages/?name=hyprlock) package.

### Hyprcursor

Hyprcursor is a new format for handling screen cursors that offers many improvements over the traditional way; it can be installed with the [hyprcursor](https://archlinux.org/packages/?name=hyprcursor) package.

#### Hyprcursor themes

**Tip** If you install hyprcursor and do not install a theme alongside it then it will fall back to your legacy cursor setting.

Cursor themes can be installed from the [AUR](/title/AUR "AUR"), for example:

* [sweet-cursors-hyprcursor-git](https://aur.archlinux.org/packages/sweet-cursors-hyprcursor-git/)AUR
* [nordzy-hyprcursors](https://aur.archlinux.org/packages/nordzy-hyprcursors/)AUR
* [xcursor-pro-hyprcursor](https://aur.archlinux.org/packages/xcursor-pro-hyprcursor/)AUR
* [hyprcursor-dracula-kde-git](https://aur.archlinux.org/packages/hyprcursor-dracula-kde-git/)AUR

Instructions for porting existing themes to Hyprcursor are available on the [upstream GitHub repository](https://github.com/hyprwm/hyprcursor/tree/main/docs).

### XDG-Desktop-Portal-Hyprland

Hyprland's own implementation of [XDG Desktop Portal](/title/XDG_Desktop_Portal "XDG Desktop Portal"). Compatible with other wlroots-based compositors, but provides extra functionality when used on Hyprland. Available through the [xdg-desktop-portal-hyprland](https://archlinux.org/packages/?name=xdg-desktop-portal-hyprland) package.

### Hyprpolkitagent

Hyprpolkitagent is a [polkit](/title/Polkit "Polkit") authentication daemon. It can be installed with the [hyprpolkitagent](https://archlinux.org/packages/?name=hyprpolkitagent) package.

### Hyprsunset

Hyprsunset is a small utility to provide a blue light filter for your system. It can be installed with the [hyprsunset](https://archlinux.org/packages/?name=hyprsunset) package.

### Hyprsysteminfo

Hyprsysteminfo is a system information fetching program like [neofetch](https://aur.archlinux.org/packages/neofetch/)AUR or [fastfetch](https://archlinux.org/packages/?name=fastfetch). It can be installed with the [hyprsysteminfo](https://aur.archlinux.org/packages/hyprsysteminfo/)AUR AUR package.

## Tips and tricks

**Note**

* For all below sections there will usually be more than one way of achieving a similar result; everything provided here is a basic example.
* For a comprehensive list of alternatives refer to the [List of applications](/title/List_of_applications "List of applications"), a Hyprland specific list can be found on the [upstream Wiki](https://wiki.hypr.land/Useful-Utilities/).

### File manager

Hyprland requires a wayland-compatible external application if graphical file management is desired. Using [thunar](https://archlinux.org/packages/?name=thunar) as an example, we simply need to assign it a keybind as follows:

```
~/.config/hypr/hyprland.lua
```

```
...
hl.bind("SUPER + E", hl.dsp.exec_cmd("thunar"))
...
```

### Application launcher

Hyprland requires a wayland-compatible external application to launch applications. Using [wofi](https://archlinux.org/packages/?name=wofi) as an example, we simply need to assign it a keybind as follows:

```
~/.config/hypr/hyprland.lua
```

```
...
hl.bind("SUPER + F", hl.dsp.exec_cmd("wofi --show drun"))
...
```

### Idle

Hyprland requires a wayland-compatible external idle management daemon. The most common setup is [hypridle](https://archlinux.org/packages/?name=hypridle) and [hyprlock](https://archlinux.org/packages/?name=hyprlock). You can lock your screen manually using a bind as follows:

```
~/.config/hypr/hyprland.lua
```

```
...
hl.bind("SUPER + L", hl.dsp.exec_cmd("hyprlock"))
...
```

#### Automatic screen locking and suspend

Create the following file:

```
~/.config/hypr/hypridle.conf
```

```
general {
    lock_cmd = pidof hyprlock || hyprlock
}

listener {
    timeout = 300
    on-timeout = loginctl lock-session
}

listener {
    timeout = 600
    on-timeout = systemctl suspend
}
```

**Tip** You can adjust the timeout periods by editing the numerical values, in seconds. 300 is 5 minutes, 600 is 10 minutes etc.

Then run it:

```
~/.config/hypr/hyprland.lua
```

```
-- enable hypridle at start
hl.on("hyprland.start", function()
    ...
    hl.exec_cmd("hypridle")
    ...
end)
```

#### Turning off the screen using DPMS after a timeout period

Hyprland has a built-in dispatcher to handle DPMS requests; however, using it as a direct keybind is not recommended, doing so will result in you not being able to turn the screen back on and will require you to reboot.

Edit the file from above and change it to read:

```
~/.config/hypr/hypridle.conf
```

```
general {
    lock_cmd = pidof hyprlock || hyprlock
}

listener {
    timeout = 300
    on-timeout = loginctl lock-session
}

listener {
    timeout = 600
    on-timeout = hyprctl dispatch dpms off
    on-resume = hyprctl dispatch dpms on
}

listener {
    timeout = 900
    on-timeout = systemctl suspend
}
```

### Status bar

Hyprland requires a wayland-compatible external application to display a status bar. Using [waybar](https://archlinux.org/packages/?name=waybar) as an example, we simply need to call it as follows:

```
~/.config/hypr/hyprland.lua
```

```
-- enable status bar at start
hl.on("hyprland.start", function()
    ...
    hl.exec_cmd("waybar")
    ...
end)
```

#### Workspace overview

[waybar](https://archlinux.org/packages/?name=waybar) has a built-in, fully customisable module that supports Hyprland workspace switching natively.

See the waybar Wiki [[1]](https://github.com/Alexays/Waybar/wiki/Module%3A-Workspaces) for details.

### Polkit authentication

[Polkit](/title/Polkit "Polkit") authentication requires the use of an external [authentication agent](/title/Polkit#Authentication_agents "Polkit"). Hyprland recommends using [hyprpolkitagent](https://archlinux.org/packages/?name=hyprpolkitagent) but any should work.

Call it as follows:

```
~/.config/hypr/hyprland.lua
```

```
-- enable polkit authentication agent at start
hl.on("hyprland.start", function()
    ...
    hl.exec_cmd("systemctl --user start hyprpolkitagent")
    ...
end)
```

### Desktop wallpaper

Hyprland requires a Wayland-compatible external application to manage desktop wallpapers. Using [hyprpaper](https://archlinux.org/packages/?name=hyprpaper) as an example, we simply need to call it as follows:

```
~/.config/hypr/hyprland.lua
```

```
-- enable hyprpaper at start
hl.on("hyprland.start", function()
    ...
    hl.exec_cmd("hyprpaper")
    ...
end)
```

Additionally since [hyprpaper](https://archlinux.org/packages/?name=hyprpaper) requires a configuration file to start; make the file as follows:

```
~/.config/hypr/hyprpaper.conf
```

```
wallpaper {
    monitor = monitor
    path = /home/me/amongus.png
    fit_mode = cover
}
```

Replace *monitor* with the monitor you would like the wallpaper to be set on, you can grab a list via `hyprctl monitors`. `monitor` can also be left blank to apply the rule to all monitors.

#### Using a script to randomize the wallpaper

Create the following script and make sure it is [executable](/title/Executable "Executable"):

```
~/.config/hypr/scripts/hyprpaper-random
```

```
#!/usr/bin/env bash

WALLPAPER_DIR="$HOME/.config/hypr/wallpapers/"
CURRENT_WALL=$(hyprctl hyprpaper listloaded)

# Get a random wallpaper that is not the current one
WALLPAPER=$(find "$WALLPAPER_DIR" -type f ! -name "$(basename "$CURRENT_WALL")" | shuf -n 1)

# Apply the selected wallpaper
hyprctl hyprpaper reload ,"$WALLPAPER"
```

Next create a new *directory* to store wallpapers, something like `~/.config/hypr/wallpapers` should work fine, and populate it with any images you want.

Finally call the script when the *specified* bind is pressed:

```
~/.config/hypr/hyprland.lua
```

```
...
hl.bind("SUPER + R", hl.dsp.exec_cmd("~/.config/hypr/scripts/hyprpaper-random"))
...
```

### On-screen notifications

On-screen notifications for actions like brightness and volume changes are possible by using external notification daemons. This is a very complex topic, and covering it completely is beyond the scope of this page. Rather, this section will focus on [mako](https://archlinux.org/packages/?name=mako) so go ahead and [install](/title/Install "Install") it.

See [Desktop notifications](/title/Desktop_notifications "Desktop notifications") for further instructions and [Desktop notifications#Standalone](/title/Desktop_notifications#Standalone "Desktop notifications") for a list of alternatives.

**Note**

* All scripts offered here are examples and will very likely need to be adjusted for your setup.
* All scripts in this section must be [executable](/title/Executable "Executable").

#### Mako

![](/images/5/53/Tango-edit-clear.svg)**This article or section needs language, wiki syntax or style improvements. See [Help:Style](/title/Help%3AStyle "Help:Style") for reference.**

**Reason:** This section goes beyond the scope of this page and probably deserves its own dedicated page. (Discuss in [Talk:Hyprland](https://wiki.archlinux.org/title/Talk%3AHyprland))

Mako is a lightweight notification daemon, you can read [mako(5)](https://man.archlinux.org/man/mako.5) for details. Its configuration file is `~/.config/mako/config`, icons used for OSD are stored at `~/.config/mako/icons/` and should be in PNG format.

For the rest of this section all the images used by the scripts are available from [this GitHub folder](https://github.com/SolDoesTech/HyprV4/tree/main/HyprV/mako/icons).

##### Keyboard backlight notifications

First create the following script:

```
~/.config/hypr/scripts/kbbacklight
```

```
#!/usr/bin/env bash

iDIR="$HOME/.config/mako/icons"

# Get brightness
get_backlight() {
	LIGHT="$(cat /sys/class/leds/*::kbd_backlight/brightness)"
	echo "${LIGHT}"
}

# Get icons
get_icon() {
	current="$(cat /sys/class/leds/*::kbd_backlight/brightness)"

	if [[ ("$current" -ge "0") && ("$current" -le "1") ]]; then
		icon="$iDIR/brightness-20.png"
	elif [[ ("$current" -ge "1") && ("$current" -le "2") ]]; then
		icon="$iDIR/brightness-60.png"
	elif [[ ("$current" -ge "2") && ("$current" -le "3") ]]; then
		icon="$iDIR/brightness-100.png"
	fi
}

# Notify
notify_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$icon" "Keyboard Brightness : $(brightnessctl -d '*::kbd_backlight' g)"
}

# Increase brightness
inc_backlight() {
	brightnessctl -d *::kbd_backlight set 33%+ && get_icon && notify_user
}

# Decrease brightness
dec_backlight() {
	brightnessctl -d *::kbd_backlight set 33%- && get_icon && notify_user
}

# Zero brightness
zero_backlight() {
	brightnessctl -d *::kbd_backlight s 0%
}

# Full brightness
full_backlight() {
	brightnessctl -d *::kbd_backlight s 100%
}

# Execute accordingly
if [[ "$1" == "--get" ]]; then
	brightnessctl -d '*::kbd_backlight' g
elif [[ "$1" == "--inc" ]]; then
	inc_backlight
elif [[ "$1" == "--dec" ]]; then
	dec_backlight
elif [[ "$1" == "--zero" ]]; then
	zero_backlight
elif [[ "$1" == "--full" ]]; then
	full_backlight

else
	get_backlight
fi
```

Then add a new bind or edit any [existing one](#Keyboard_backlight):

```
~/.config/hypr/hyprland.lua
```

```
-- Keyboard brightness
hl.bind("keyboard_brightness_up_shortcut", hl.dsp.exec_cmd("~/.config/hypr/scripts/kbbacklight --inc"))
hl.bind("keyboard_brightness_down_shortcut", hl.dsp.exec_cmd("~/.config/hypr/scripts/kbbacklight --dec"))
```

##### Media key notifications

First create the following script:

```
~/.config/hypr/scripts/volume
```

```
#!/usr/bin/env bash

iDIR="$HOME/.config/mako/icons"

# Get Volume
get_volume() {
	volume=$(pamixer --get-volume)
	echo "$volume"
}

# Get icons
get_icon() {
	current=$(get_volume)
	if [[ "$current" -eq "0" ]]; then
		echo "$iDIR/volume-mute.png"
	elif [[ ("$current" -ge "0") && ("$current" -le "30") ]]; then
		echo "$iDIR/volume-low.png"
	elif [[ ("$current" -ge "30") && ("$current" -le "60") ]]; then
		echo "$iDIR/volume-mid.png"
	elif [[ ("$current" -ge "60") && ("$current" -le "100") ]]; then
		echo "$iDIR/volume-high.png"
	fi
}

# Notify
notify_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$(get_icon)" "Volume : $(get_volume) %"
}

# Increase Volume
inc_volume() {
	pamixer -i 5 && notify_user
}

# Decrease Volume
dec_volume() {
	pamixer -d 5 && notify_user
}

# Toggle Mute
toggle_mute() {
	if [ "$(pamixer --get-mute)" == "false" ]; then
		pamixer -m && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$iDIR/volume-mute.png" "Volume Switched OFF"
	elif [ "$(pamixer --get-mute)" == "true" ]; then
		pamixer -u && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$(get_icon)" "Volume Switched ON"
	fi
}

# Toggle Mic
toggle_mic() {
	if [ "$(pamixer --default-source --get-mute)" == "false" ]; then
		pamixer --default-source -m && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$iDIR/microphone-mute.png" "Microphone Switched OFF"
	elif [ "$(pamixer --default-source --get-mute)" == "true" ]; then
		pamixer -u --default-source u && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$iDIR/microphone.png" "Microphone Switched ON"
	fi
}
# Get icons
get_mic_icon() {
	current=$(pamixer --default-source --get-volume)
	if [[ "$current" -eq "0" ]]; then
		echo "$iDIR/microphone.png"
	elif [[ ("$current" -ge "0") && ("$current" -le "30") ]]; then
		echo "$iDIR/microphone.png"
	elif [[ ("$current" -ge "30") && ("$current" -le "60") ]]; then
		echo "$iDIR/microphone.png"
	elif [[ ("$current" -ge "60") && ("$current" -le "100") ]]; then
		echo "$iDIR/microphone.png"
	fi
}
# Notify
notify_mic_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$(get_mic_icon)" "Mic-Level : $(pamixer --default-source --get-volume) %"
}

# Increase MIC Volume
inc_mic_volume() {
	pamixer --default-source -i 5 && notify_mic_user
}

# Decrease MIC Volume
dec_mic_volume() {
	pamixer --default-source -d 5 && notify_mic_user
}

# Execute accordingly
if [[ "$1" == "--get" ]]; then
	get_volume
elif [[ "$1" == "--inc" ]]; then
	inc_volume
elif [[ "$1" == "--dec" ]]; then
	dec_volume
elif [[ "$1" == "--toggle" ]]; then
	toggle_mute
elif [[ "$1" == "--toggle-mic" ]]; then
	toggle_mic
elif [[ "$1" == "--get-icon" ]]; then
	get_icon
elif [[ "$1" == "--get-mic-icon" ]]; then
	get_mic_icon
elif [[ "$1" == "--mic-inc" ]]; then
	inc_mic_volume
elif [[ "$1" == "--mic-dec" ]]; then
	dec_mic_volume
else
	get_volume
fi
```

Then add the following (or edit any existing binds):

```
~/.config/hypr/hyprland.lua
```

```
-- Volume
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("~/.config/hypr/scripts/volume --inc"))
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("~/.config/hypr/scripts/volume --dec"))
hl.bind("XF86AudioMicMute", hl.dsp.exec_cmd("~/.config/hypr/scripts/volume --toggle-mic"))
hl.bind("XF86AudioMute", hl.dsp.exec_cmd("~/.config/hypr/scripts/volume --toggle"))
```

##### Screen backlight notifications

First create the following script:

```
~/.config/hypr/scripts/backlight
```

```
#!/usr/bin/env bash

iDIR="$HOME/.config/mako/icons"

# Get brightness
get_backlight() {
	LIGHT=$(printf "%.0f\n" $(brightnessctl g))
	echo "${LIGHT}"
}

# Get icons
get_icon() {
	current="$(get_backlight)"
	if [[ ("$current" -ge "0") && ("$current" -le "19200") ]]; then
		icon="$iDIR/brightness-20.png"
	elif [[ ("$current" -ge "19200") && ("$current" -le "38400") ]]; then
		icon="$iDIR/brightness-40.png"
	elif [[ ("$current" -ge "38400") && ("$current" -le "57600") ]]; then
		icon="$iDIR/brightness-60.png"
	elif [[ ("$current" -ge "57600") && ("$current" -le "76800") ]]; then
		icon="$iDIR/brightness-80.png"
	elif [[ ("$current" -ge "76800") && ("$current" -le "96000") ]]; then
		icon="$iDIR/brightness-100.png"
	fi
}

# Notify
notify_user() {
	notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$icon" "Brightness : $(get_backlight)"
}

# Increase brightness
inc_backlight() {
	brightnessctl s +5% && get_icon && notify_user
}

# Decrease brightness
dec_backlight() {
	brightnessctl s 5%- && get_icon && notify_user
}

# Execute accordingly
if [[ "$1" == "--get" ]]; then
	get_backlight
elif [[ "$1" == "--inc" ]]; then
	inc_backlight
elif [[ "$1" == "--dec" ]]; then
	dec_backlight
else
	get_backlight
fi
```

Then add the following (or edit any existing binds):

```
~/.config/hypr/hyprland.lua
```

```
-- Screen brightness
hl.bind("XF86MonBrightnessUp", hl.dsp.exec_cmd("~/.config/hypr/scripts/backlight --inc"))
hl.bind("XF86MonBrightnessDown", hl.dsp.exec_cmd("~/.config/hypr/scripts/backlight --dec"))
```

##### Keyboard language notifications

To run this script, you need a command-line JSON processor [gojq](https://aur.archlinux.org/packages/gojq/)AUR.

First create the following script:

```
~/.config/hypr/scripts/lang
```

```
#!/usr/bin/env bash

icon="$HOME/.config/mako/icons/language.png"

# Get language
get_lang() {
	lang=$(hyprctl devices -j | gojq -r '.keyboards[] | select(.name == "at-translated-set-2-keyboard") | .active_keymap' | cut -c 1-2 | tr 'A-Z' 'a-z')
	case $lang in
		en)
			lang="English language"
			;;
		ru)
			lang="Русский язык"
			;;
		uk)
			lang="Українська мова"
			;;
	esac
	echo $lang
}

# Notify
notify-send -h string:x-canonical-private-synchronous:sys-notify -u low -i "$icon" "$(get_lang)"
```

Then add the following (or edit any existing binds):

```
~/.config/hypr/hyprland.lua
```

```
hl.device({
  name = "at-translated-set-2-keyboard",
  kb_layout = "us,ru,ua",
  kb_variant = "lang",
  kb_options = "grp:win_space_toggle",
})

-- Language
hl.bind("SUPER + SPACE", hl.dsp.exec_cmd("~/.config/hypr/scripts/lang"))
```

### Power control

Hyprland requires a wayland-compatible external application for power control. Using [nwg-bar](https://archlinux.org/packages/?name=nwg-bar) as an example, we simply need to bind it as follows:

```
~/.config/hypr/hyprland.lua
```

```
...
hl.bind("SUPER + ESCAPE", hl.dsp.exec_cmd("nwg-bar"))
...
```

### Clipboard

[Wayland](/title/Wayland "Wayland") clipboard behaviour deletes data when closing the application we copied it from. Other desktop environments work around this by using dedicated clipboard managers, and on Hyprland there are multiple compatible choices. See the [upstream Wiki](https://wiki.hypr.land/Useful-Utilities/Clipboard-Managers/) for more information.

This section will cover [cliphist](https://archlinux.org/packages/?name=cliphist) as it supports copying images as well as text. Start by adding the following:

```
~/.config/hypr/hyprland.lua
```

```
hl.on("hyprland.start", function()
    ...
    hl.exec_cmd("wl-paste --type text --watch cliphist store")
    hl.exec_cmd("wl-paste --type image --watch cliphist store")
    ...
end)
```

Then create a bind to call the history in your chosen [application launcher](#Application_launcher):

```
~/.config/hypr/hyprland.lua
```

```
...
hl.bind("SUPER + V", hl.dsp.exec_cmd("cliphist list | wofi --dmenu | cliphist decode | wl-copy"))
...
```

Now pressing `Super+v` will open up a `wofi` window with a clipboard history list.

### Enable/disable devices

To enable/disable devices (e.g., touchpad), first use:

```
$ hyprctl devices
```

to get the name of your device.

Put these lines of code into your configuration file (replace <device\_name> with the name of your device queried above) to turn the device on/off:

```
~/.config/hypr/hyprland.lua
```

```
hl.device({
  name = "<device_name>"
  enabled = {true/false}
})
```

To dynamically switch the device on/off, use hyprctl:

```
$ hyprctl eval "hl.device({ name = '<device-name>', enabled = {true/false) })"
```

You can also create a keybinding, e.g.,

```
~/.config/hypr/hyprland.lua
```

```
...
hl.bind("SUPER + T", hl.dsp.exec_cmd([[hyprctl eval "hl.device({ name = 'logitech-g502-hero-gaming-mouse', enabled = false})"]]))

hl.bind("SUPER + SHIFT + T", hl.dsp.exec_cmd([[hyprctl eval "hl.device({ name = 'logitech-g502-hero-gaming-mouse', enabled = true})"]]))
...
```

### Separate dconf profile

In case you do not want to poison settings for other GTK-based DEs, you can use a separate `dconf` profile. For example:

Declare new global dconf profile:

```
/etc/dconf/profile/hyprland
```

```
user-db:hyprland
```

```
~/.config/hypr/hyprland.lua
```

```
...
hl.env("DCONF_PROFILE", "hyprland")
...
```

Now you can use *gsettings* and it should not affect other desktop environments.

### KDE Plasma applications not following Qt theming

Even with a Qt theme set, some plasma applications might not follow it. This can be solved by installing [qt6ct-kde](https://aur.archlinux.org/packages/qt6ct-kde/)AUR and choosing a KColorScheme or by adding this configuration line in kdeglobals:

```
~/.config/kdeglobals
```

```
[UiSettings]
ColorScheme=NameOfTheProfile
```

## Troubleshooting

### Jetbrains apps focus issues

JetBrains apps (Pycharm, Intellij) can have strange focus problems such as:

* Unable to drag tab from the tab bar [[2]](https://github.com/hyprwm/Hyprland/issues/1120) to either a split, or another tab stack without focus being stolen and the tab being dropped as soon as you drag it past the current tab bar.

* An autocomplete popup window steals focus until the mouse is moved.

To mitigate the issue, add this to *hyprland*'s configuration file:

```
~/.config/hypr/hyprland.lua
```

```
hl.window_rule({
     match = { xwayland = true },
     no_initial_focus = true,
 })
```

### Squares instead of text after fresh install

Hyprland uses `sans-serif` style font [[3]](https://wiki.hypr.land/useful-utilities/must-have/#fonts). Install font such as [noto-fonts](https://archlinux.org/packages/?name=noto-fonts). Missing glyphs for additional icons could be supplied with [ttf-nerd-fonts-symbols](https://archlinux.org/packages/?name=ttf-nerd-fonts-symbols)

## See also

* [Hyprland Website](https://hypr.land/)
* [The official documentation](https://wiki.hypr.land/)
* [Hyprland Github Page](https://github.com/hyprwm/Hyprland/)
* [Community-maintained list of tools, plugins and extensions](https://github.com/hyprland-community/awesome-hyprland)
* [SolDoesTech Github Repo - Notification scripts creator](https://github.com/SolDoesTech/HyprV4)

Retrieved from "<https://wiki.archlinux.org/index.php?title=Hyprland&oldid=887257>"

[Category](/title/Special%3ACategories "Special:Categories"):

* [Wayland compositors](/title/Category%3AWayland_compositors "Category:Wayland compositors")

Hidden category:

* [Pages or sections flagged with Template:Style](/title/Category%3APages_or_sections_flagged_with_Template%3AStyle "Category:Pages or sections flagged with Template:Style")

* This page was last edited on 8 October 2026, at 10:11.
* Content is available under [GNU Free Documentation License 1.3 or later](https://www.gnu.org/copyleft/fdl.html) unless otherwise noted.

* [Privacy policy](https://terms.archlinux.org/docs/privacy-policy/)
* [About ArchWiki](/title/ArchWiki%3AAbout)
* [Disclaimers](/title/ArchWiki%3AGeneral_disclaimer)
* [Code of conduct](https://terms.archlinux.org/docs/code-of-conduct/ "archlinux-service-agreements:code-of-conduct")
* [Terms of service](https://terms.archlinux.org/docs/terms-of-service/ "archlinux-service-agreements:terms-of-service")

* [![GNU Free Documentation License 1.3 or later](/resources/assets/licenses/gnu-fdl.png)](https://www.gnu.org/copyleft/fdl.html)
* ![](/resources/assets/mediawiki_compact.svg)

Search

Search

[ ]

Toggle the table of contents

Hyprland

Add topic
