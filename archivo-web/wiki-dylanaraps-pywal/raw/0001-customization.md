`wal` can be extended to support a wide range of programs and applications through the use of scripting or colorscheme files it generates. For example: The `colors.css` file allows you to use the generated colors in your `css` files to update your startpage's colors on the fly.

Another customization example is a custom script I've created called `wal-set` \[1\]. This script uses the exported `colors.sh` file to apply the colors to my `lemonbar`, `dunst` and `startpage`. The script is executed using `wal`'s `-o` flag (`wal -i img.png -o wal-set`).


\[1\] [wal-set](https://raw.githubusercontent.com/dylanaraps/bin/65c5c1acda3caf13dd7ff2fdbfc90b18b2adb40e/wal-set)

## Table of Contents

- **[Applications](#applications)**
    - [Steam](#steam)
    - [Discord](#discord)
    - [Zathura](#zathura)
    - [Telegram](#telegram)
    - [mocp](#mocp)
    - [Chromium](#chromium)
    - [Firefox (and Thunderbird)](#firefox)
- **[Window Managers](#window-managers)**
    - [i3](#i3)
    - [awesome](#awesomewm)
    - [bspwm](#bspwm)
    - [qtile](#qtile)
    - [sway](#sway)
    - [dwm](#dwm)
    - [yabai](#yabai)
- **[Application Launchers](#application-launchers)**
    - [rofi](#rofi)
    - [dmenu](#dmenu)
    - [Alfred](#alfred)
- **[Text Editors](#text-editors)**
    - [vim](#vim)
    - [emacs](#emacs)
    - [JetBrains IDEs](#jetbrains-ides)
    - [VS Code](#vs-code)
- **[Taskbars](#taskbars)**
    - [polybar](#polybar)
    - [lemonbar](#lemonbar)
- **[Terminal Emulators](#terminal-emulators)**
    - [konsole](#konsole)
    - [kitty](#kitty)
    - [st](#st)
    - [PuTTY](#putty)
    - [Terminal.sexy](#terminalsexy)
    - [Alacritty on MacOS](#alacritty-on-macos)
- **[Terminal Multiplexer/Workspace](#terminal-multiplexer-workspace)**
    - [Zellij](#zellij)
- **[Notification daemons](#notification-daemons)**
    - [mako](#mako)
- **[Web Files](#web-files)**
    - [CSS variables](#css-variables)
    - [SCSS variables](#scss-variables)
    - [Firefox reader mode](#firefox-reader-mode)
- **[Scripting Files](#scripting-files)**
    - [Shell Variables](#shell-variables)
    - [JSON file](#json-file)
    - [YAML file](#yaml-file)
- **[Peripheral](#peripheral)**
    - [Logitech keyboards](#logitech-keyboards)
    - [Razer](#razer)
    - [Asus ROG Laptops](#asusrog)
- **[Other Tools](#other-tools)**
    - [tabbed](#tabbed)
    - [lightdm](#lightdm)
    - [gnuplot](#gnuplot)

## Applications

### Steam

You can use `wal_steam` to theme Steam using the colors from `wal`.

https://github.com/kotajacob/wal_steam

### Discord

You can use either `pywal-discord` or `wal-discord` to theme Discord using the colors from `wal`.

There is also `discord-wal-theme` for a Vencord compatible template file (especially notable for Windows users).

https://github.com/FilipLitwora/pywal-discord

https://github.com/guglicap/wal-discord

https://github.com/Gremious/discord-wal-theme-template

### Zathura

You can use `Zathura-Pywal` to theme Zathura using the colors from `wal`.

https://github.com/GideonWolfe/Zathura-Pywal

### Telegram

You can use `wal-telegram` to theme Telegram using the colors from `wal`.

https://github.com/guillaumeboehm/wal-telegram

### `mocp`

Use the following theme file.

- Save the below file as `~/.moc/themes/wal`
- Add the following line to your `mocp` config.
    - `Theme = wal`

```
background           = default default
frame                = black   default
window_title         = green   default
directory            = red     default
selected_directory   = blue    default
playlist             = blue    default
selected_playlist    = magenta default
file                 = green   default
selected_file        = black   red
marked_file          = green   default bold
marked_selected_file = cyan    default bold
info                 = cyan    default
selected_info        = cyan    default
marked_info          = green   default bold
marked_selected_info = cyan    default bold
status               = magenta default
title                = green   default
state                = magenta default
current_time         = magenta default
time_left            = cyan    default
total_time           = cyan    default
time_total_frames    = magenta default
sound_parameters     = cyan    default
legend               = magenta default
disabled             = black   default
enabled              = yellow  default
empty_mixer_bar      = green   default
filled_mixer_bar     = black   green
empty_time_bar       = green   default
filled_time_bar      = black   green
entry                = yellow  default
entry_title          = red     default
error                = red     default
message              = yellow  default
plist_time           = magenta default
```

### Chromium

You can use `ChromiumPywal` to theme Chrome/Chromium using the colors from `wal`

https://github.com/metafates/ChromiumPywal


### Firefox

You can use `pywalfox` to theme Firefox and/or Thunderbird using the colors from `wal`.

https://github.com/Frewacom/pywalfox


## Window Managers

### i3

To use `wal` with i3 you have to make some modifications to your i3 config file.

i3 can read colors from `Xresources` into config variables! This allows us to change i3's colors dynamically. On run `wal` will detect that you're running i3 and reload your config for you. If you've set it up correctly i3 will then use your new colorscheme.

You can also set the colors of i3status and i3bar. The example below shows how to change the colors of i3status. For more information on i3status/i3bar see https://i3wm.org/docs/userguide.html#_colors

Example:

```sh
# Set colors from Xresources
# Change 'color7' and 'color2' to whatever colors you want i3 to use 
# from the generated scheme.
# NOTE: The '#f0f0f0' in the lines below is the color i3 will use if
# it fails to get colors from Xresources.
set_from_resource $fg i3wm.color7 #f0f0f0
set_from_resource $bg i3wm.color2 #f0f0f0

# class                 border  backgr. text indicator child_border
client.focused          $bg     $bg     $fg  $bg       $bg
client.focused_inactive $bg     $bg     $fg  $bg       $bg
client.unfocused        $bg     $bg     $fg  $bg       $bg
client.urgent           $bg     $bg     $fg  $bg       $bg
client.placeholder      $bg     $bg     $fg  $bg       $bg

client.background       $bg

# i3status
bar {
    status_command i3status
    colors {
        background $bg
        statusline $fg
        separator $fg
    }
}

# PROTIP: You can also dynamically set dmenu's colors this way:
bindsym $mod+d exec dmenu_run -nb "$fg" -nf "$bg" -sb "$bg" -sf "$fg"
```

### awesomewm

To use `wal` with awesome you have to use the Xresources theme.

The Xresources Theme comes with awesomewm pre-installed, and can be found in `/usr/share/awesome/themes` directory. It loads colors from `Xresources`. This allows us to change awesome's colors dynamically.

Unlike i3, wal does not automatically reload your awesome configuration for you, that you have to do yourself.

wal generates a colors.Xresources file. You have to link it to `~/.Xresources`.
```bash
ln -sf ~/.cache/wal/colors.Xresources ~/.Xresources
```

Then modify your `rc.lua` to use Xresources Theme

Replace this
```lua
beautiful.init(gears.filesystem.get_themes_dir() .. "default/theme.lua")
```
with this
```lua
beautiful.init(gears.filesystem.get_themes_dir() .. "xresources/theme.lua")
```

Now, Reload your configuration using `Ctrl-Mod-R`

### bspwm

The `bspwmrc` file is a shell script which makes using `wal`'s colors easy!

```sh
# source the colors.
. "${HOME}/.cache/wal/colors.sh"

# Set the border colors.
bspc config normal_border_color "$color1"
bspc config active_border_color "$color2"
bspc config focused_border_color "$color15"
# Use the line below if you are on bspwm >= 0.9.4
bspc config presel_feedback_color "$color1"
# Use the line below if you are on bspwm < 0.9.4
#bspc config presel_border_color "$color1"
```
### Qtile
to config.py add:
```
colors = []
cache='/home/username/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)

```
and then use 
```
colors[0]
```
format to customize colors
after changing wallpaper with ```wal -i /path/to/image``` reload qtile with super+ctrl+r (by default)
to apply colors.

### sway

sway can `include` arbitrary configuration files. In your `.config/sway/config` file, add before any color usage:

```
include "$HOME/.cache/wal/colors-sway"
```

And `wal` will set your wallpaper (`$wallpaper`) and colors (`$background`, `$foreground` and `$color0` through `$color15`). To use them:

```
output <name> background $wallpaper <mode>
client.focused $color0 $background $foreground $color7 $background
```

See `man 5 sway` on how to set wallpapers and colors.

### dwm

1. Delete all defined colors in your config.h
2. Delete the `static const char *colors[]` array.
3. In its place, include wal's exported colors via: 

    ```
    #include "/home/<USER>/.cache/wal/colors-wal-dwm.h"
    ```

(Replace \<USER\> with your username.)

**NOTE**: this `#include` must be on the same line as what was previously deleted.

This also assumes you have the "Urgent" color patch for dwm.

You can find the official patch [here](https://dwm.suckless.org/patches/urgentborder/dwm-6.2-urg-border.diff)

If you have not or do not wish to patch dwm, you will need to delete the lines of pywal's exported config which contain "urg". This config is located at `.cache/wal/colors-wal-dwm.h`. Note that whenever you restart/reconfigure `pywal`, you will need to delete these lines yet again. To solve this problem, we can use a [User Template](https://github.com/dylanaraps/pywal/wiki/User-Template-Files). See the command below.

Perform the following command to stop `pywal` from re-generating the default template: `cp .cache/wal/colors-wal-dwm.h .config/wal/templates`

**Q**: "I do not have a *colors[] array in my config.h?"
 
**A**: 6.1 and older dwm releases do not include the *colors[] array and the colors are named differently than in the `wal` output. Please use the current git version of dwm, which can be found at http://git.suckless.org/dwm

**Q**: "I get error when I try to (re)compile dwm while there is no `.cache/wal/colors-wal-dwm.h` (there is no `wal` theme set yet)"

**A**: Just set a theme, after that it will perfectly compile. If you want to be able to compile dwm even when there is no a `wal` theme set you can use the following block of code instead:

```
#define wal "/home/<USER>/.cache/wal/colors-wal-dwm.h"

#if __has_include(wal)
#include wal
#else
static const char col_gray3[]       = "#bbbbbb";
static const char col_gray4[]       = "#eeeeee";
static const char col_cyan[]        = "#005577";
static const char col_urgborder[]   = "#ff0000";
static const char *colors[][3]      = {
   /*               fg         bg         border   */
   [SchemeNorm] = { col_gray3, col_gray1, col_gray2 },
   [SchemeSel]  = { col_gray4, col_cyan,  col_cyan  },
   [SchemeUrg]  = { col_gray4, col_cyan,  col_urgborder  },
#endif
```

### yabai

Add the following lines to your yabai config file (usually in `~/.yabairc` or `~/.config/yabai/yabairc`), creating the file if it doesn't exist already: 

```
source ~/.cache/wal/colors.sh # pywal scheme - update if needed

# yabai template colours
CBACK=$(echo $background | sed 's/#//')
CFORE=$(echo $foreground | sed 's/#//')
CACTV=$(echo $color3 | sed 's/#//')
CNORM=$(echo $color1 | sed 's/#//')
CINSE=$(echo $foreground | sed 's/#//')

yabai -m config status_bar                   on
yabai -m config status_bar_background_color  0xff$CBACK
yabai -m config status_bar_foreground_color  0xff$CFORE

yabai -m config window_border                on
yabai -m config window_border_width          4
yabai -m config active_window_border_color   0xff$CACTV
yabai -m config normal_window_border_color   0xff$CNORM
yabai -m config insert_window_border_color   0xff$CINSE
```

Restart yabai (`brew services restart yabai` if installed through Homebrew) and enjoy the colours.

A simple script that uses osascript to retrieve your wallpaper and run pywal could be:

```
function pywal {
    # generate color scheme from current wallpaper
    current_wallpaper="$(osascript -e 'tell app "finder" to get posix path of (get desktop picture as alias)')"
    wal -i $current_wallpaper -n
}
```

Placing this into your `.zshrc`, `.bashrc`, or whatever rc file corresponding to your shell, will allow you to simply run `pywal` in a terminal and update your colours easily.

## Application Launchers

### rofi

Add one of the following lines to your `rofi` config file outside of the `configuration{...}` block located in `~/.config/rofi/config.rasi`. If the file doesn't exist, you can just create it.

```
/* Dark theme. */
@import "~/.cache/wal/colors-rofi-dark"

/* Light theme. */
@import "~/.cache/wal/colors-rofi-light"
```

**Defining your own custom theme.**

See: https://github.com/dylanaraps/pywal/wiki/User-Template-Files

### dmenu

You can use `dmenu`'s launch flags to style the colors dynamically.

As an alias in your `.bashrc`, `.zshrc` etc:

```sh
# Import the colors.
. "${HOME}/.cache/wal/colors.sh"

# Create the alias.
alias dmen='dmenu_run -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15"'
```

As a separate script (`dmen.sh`):

```sh
#!/bin/sh

# Import the colors
. "${HOME}/.cache/wal/colors.sh"

dmenu_run -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15"
```

Alternatively, you can modify dmenu's config.h file to apply the colors to all dmenu scripts:
1. Delete the ```static const char *colors[]``` array
2. In its place, include wal's exported colors via:
```
#include "/home/<USER>/.cache/wal/colors-wal-dmenu.h"
```

### Alfred

You can use `AlfredPywal` to generate pywal theme for Alfred 4

https://github.com/metafates/AlfredPywal

## Text Editors

### vim

I've created a vim colorscheme for use with with the colors `wal` generates and you can install it using any vim package manager. The colorscheme uses your terminal colors so it'll adapt to the colorscheme changes automatically.

Neovim users, make sure to remove `set termguicolors` as it messes up the colorscheme.

You can find the colorscheme here: https://github.com/dylanaraps/wal.vim

Example:

```vim
! Using plug
Plug 'dylanaraps/wal.vim'

colorscheme wal
```

### emacs

You have 2 options:

* Install [xresources-theme](https://github.com/cqql/xresources-theme) to make Emacs generate a theme using X environment's colors.
* Install [ewal](https://gitlab.com/jjzmajic/ewal), a theme agnostic colorscheme generator that uses `pywal` palettes as its input (and adds more shades to them, but only if you want them). It currently completely integrates with [spacemacs-theme](https://github.com/nashamri/spacemacs-theme) (more coming soon), so you don't loose out on any detail when changing colorschemes. You can also use its utility functions to configure your current theme to your liking with `pywal` colors.

Note: There's an ongoing discussion in [#43](https://github.com/dylanaraps/pywal/pull/43) about making Emacs change colors on the fly.

### JetBrains IDEs

Follow the instructions on this [repository](https://github.com/Mr-SD/intellijPywal) to integrate pywal with intellij idea or any other jetbrains IDE.

### VS Code

Install the [Wal Theme extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=dlasagno.wal-theme).  It will automatically update your theme whenever pywal generates a new color palette.

[Wal Theme Repository](https://github.com/dlasagno/vscode-wal-theme)


## Taskbars


### polybar

Polybar can read colors from `Xresources` to set the bar's colors. `wal` will also reload your config file for you  automatically if it detects that `polybar` is running.

Example:

```ini
[colors]
background = ${xrdb:color0:#222}
foreground = ${xrdb:color7:#222}
foreground-alt = ${xrdb:color7:#222}
primary = ${xrdb:color1:#222}
secondary = ${xrdb:color2:#222}
alert = ${xrdb:color3:#222}

[bar/bar]
; ...
background = ${colors.background}
foreground = ${colors.foreground}

; ...
```


### lemonbar

You can use `lemonbar`'s launch flags to style the colors dynamically. For a real world example you can take a look at my [bar script](https://github.com/dylanaraps/bin/blob/master/bar).

In your `lemonbar` script:

```sh
#!/bin/sh

# Import the colors
. "${HOME}/.cache/wal/colors.sh"

lemonbar -B "$color0" -F "$color8" # Other flags here.
```


## Terminal Emulators

### Konsole

`wal` generates a KDE colorscheme that can be imported into Konsole. The file is called `colors-konsole.colorscheme` and is located in the cache folder. This colorscheme can be symlinked into the Konsole theme folder using, for example,

`ln -s ~/.cache/wal/colors-konsole.colorscheme ~/.local/share/konsole`

Although the symlink does not need to be updated after running pywal, a restart (or theme switch) of Konsole is needed to pick up the new color scheme.

Plasma5 (outside Konsole) is not supported by `wal`.

### kitty

Open your kitty config file, usually `~/.config/kitty/kitty.conf`. Alternatively you can press Ctrl+Shift+F2 from within kitty to open the config in an editor. The colour config for kitty is exported by wal as `~/.cache/wal/colors-kitty.conf` and can be used by placing the following inside your kitty config file.

```
include ~/.cache/wal/colors-kitty.conf
```

If you have any existing colour definitions in your config file, make sure to paste the line after all of them or comment them out to avoid overriding the values in `colors-kitty.conf`

### st

1. Remove all color definitions in your `config.h`
2. Remove the `const char *colorname[]` array
3. Include wal's export colors via:

```
#include "/home/<USER>/.cache/wal/colors-wal-st.h"
```

(replace \<USER\> with your user name)

**NOTE**: this `#include` must be on the same line as what was previously deleted.
**NOTE**: there is a patch to st which loads a colorscheme from Xresources: https://st.suckless.org/patches/xresources/
**NOTE**: this `#include` would not work with [alpha](http://st.suckless.org/patches/alpha/) patch.
If you want to make it work with alpha patch, you have to change `colors-wal-st.h` such that `defaultbg` is set to `257`, `defaultfg` is set to `256`. This creates light theme. For dark theme, the color represented by `256` and `257` must be swapped with each other.

### PuTTY

`wal` also exports the colors so they can be used with PuTTY. After running `wal`, a file will be created (`$HOME/.cache/wal/colors-putty.reg`) that can be executed on a Windows machine to create a new PuTTY session with the generated colors. Once the file is executed, you can select `Wal` from the *Saved Sessions* list.


### Terminal.sexy

You can import `wal`'s colors into Terminal.sexy by copy-pasting the contents of the `colors.Xresources` file located in the cache directory.

### Alacritty on MacOS

On MacOS the colors do not get set in the `alacritty` config correctly. Luckily, a generous member of the community created a [script](https://github.com/egeesin/alacritty-color-export) to run to get this working. Just follow the instructions in the README. You may have to restart `alacritty` for the colors to correctly change.

## Terminal Emulators
### Zellij
You can use ZellijPywal to theme [Zellij](https://github.com/zellij-org/zellij) using the colors from wal

https://github.com/nicoandresr/ZellijPywal

## Notification Daemons
### mako

See mako [wiki page](https://github.com/emersion/mako/wiki/Pywal-integration-&-life-update)

## Web Files


### CSS variables

`wal` also exports the colors as CSS variables for use with Stylish or userChrome.css.

Example CSS:

```css
/* Import the CSS file.
   Change 'dylan' to your username. */
@import url('file:///home/dylan/.cache/wal/colors.css');

/* Use the variables */
#nav-bar {
  background-image: var(--wallpaper);
  color: var(--color7) !important;
}

h1 {
  background-color: var(--color3);
}
```


### SCSS variables

`wal` also exports the colorscheme as SCSS variables for use in webpages. I'm using this feature to update my startpage with the new colors dynamically.

Example:

```scss
// Example .scss file

// Import Colors
@import '/home/dylan/.cache/wal/colors.scss';

body {
  background: $background;
  color: $foreground;
}

main {
  background-image: url($wallpaper);
}

a {
  color: $color4;
}
```

### Firefox reader mode

Reader View is a Firefox feature that strips away clutter like buttons, ads and background images, and changes the page's text size, contrast and layout for better readability ([more information](https://support.mozilla.org/en-US/kb/firefox-reader-view-clutter-free-web-pages)).

You can customize this mode with wal css file:

1. type `about:support` in the address bar and copy the *Profile folder* path (should be something like `/home/username/.mozilla/firefox/885a2m8x.default`);
2. go to this directory and create `chrome` folder if not created yet;
3. in this folder, create/edit the file `userContent.css` by adding custom css attributes according to your preferences (see below);
4. restart Firefox.

Theses classes are added by Firefox on the `body` element:
- `loaded` when reader mode is enabled;
- `dark` when dark background is selected;
- `light` when light background is selected;
- `sepia` when sepia background is selected;
- `serif` when serif font is selected;
- `sans-serif` when sans-serif font is selected.

Use the selectors you want (`.body.loaded.dark`, `.body.loaded.sans-serif`, ...) or combine them (`.body.loaded.dark.sans-serif`, ...) and don't forget to add `!important` after each line.

userContent.css example:

```css
@import url('file:///home/your_user_name/.cache/wal/colors.css');

body.loaded.dark {
  color: var(--foreground) !important;
  background-color: var(--background) !important;
}

body.loaded.dark h1 {
  color: var(--color1) !important;
}

body.loaded.dark h2, body.loaded.dark h3, body.loaded.dark h4, body.loaded.dark h5, body.loaded.dark h6 {
  color: var(--color4) !important;
}

body.loaded.dark strong {
  color: var(--color5) !important;
}
```

## Scripting Files


### Shell Variables

`wal` also exports the colorscheme as a list of shell variables that you can source for use in scripts and the shell.

Example:

```sh
# Add this line to your .bashrc or a shell script.
. "~/.cache/wal/colors.sh"

```

In the shell:

```sh
# Once the file is sourced you can use the colors like this:

dylan ~ >echo "$background"
#282A23

dylan ~ >echo "$color0 $color5"
#282A23 #BCC3CE

dylan ~ >echo "$wallpaper"
/home/dylan/Pictures/Wallpapers/1.jpg

# lemonbar example
lemonbar -B "$color7" -F "$color0"
```

In a script:

```sh
#!/bin/sh

. "~/.cache/wal/colors.sh"

printf "%s\n" "$color0"
```


## JSON File

`wal` also exports the colors in `json`. This is helpful when you want use the colors in another script.

The file is called `colors.json` and is located in the cache directory. (`~/.cache/wal`). The file contains the wallpaper, hex colors for `background`, `foreground` and `cursor` as well as the colors `0-15`.

Example `colors.json` file:

```json
{
    "wallpaper": "/path/to/img.jpg",

    "special": {
        "background": "#4A3636",
        "foreground": "#F8F8F8",
        "cursor": "#F8F8F8"
    },
    "colors": {
        "color0": "#4A3636",
        "color1": "#EDD0B0",
        "color2": "#EDB7C8",
        "color3": "#E0D4DC",
        "color4": "#F4D3D0",
        "color5": "#F5E8D6",
        "color6": "#F5EDEA",
        "color7": "#F8F8F8",
        "color8": "#999999",
        "color9": "#EDD0B0",
        "color10": "#EDB7C8",
        "color11": "#E0D4DC",
        "color12": "#F4D3D0",
        "color13": "#F5E8D6",
        "color14": "#F5EDEA",
        "color15": "#F8F8F8"
    }
}
```


### YAML File


`wal` also exports the colors in `yml`. This is helpful when you want use the colors in another script.

The file is called `colors.yml` and is located in the cache directory. (`~/.cache/wal`). The file contains the wallpaper, hex colors for `background`, `foreground` and `cursor` as well as the colors `0-15`.

Example `colors.yml` file:


```yml
wallpaper: "/home/dylan/Pictures/Wallpapers/010.jpg"

special:
    background: "#2b454c"
    foreground: "#D2E2D0"
    cursor: "#D2E2D0"

colors:
    color0: "#2b454c"
    color": "#9AA2A7"
    color2: "#D4B2AF"
    color3: "#C2BFBF"
    color4: "#B5CBC9"
    color5: "#CFD1CA"
    color6: "#F1C9CB"
    color7: "#D2E2D0"
    color8: "#757575"
    color9: "#9AA2A7"
    color10: "#D4B2AF"
    color11: "#C2BFBF"
    color12: "#B5CBC9"
    color13: "#CFD1CA"
    color14: "#F1C9CB"
    color15: "#D2E2D0"
```

## Peripheral

### Logitech keyboards

You can use [g810-led utility](https://github.com/MatMoul/g810-led), to change RGB of Logitech G213, G410, G413, G512, G513, G610, G810, G910 and GPRO Keyboards

Basic script for pywal  [here](https://gist.github.com/mrt0rtikize/2b4964b3f2f62006c94744c92dbf97e5)

### Razer

For Razer peripherals you can use [razer-cli utility](https://github.com/LoLei/razer-cli#example-usage-with-pywal)

### Asus ROG Laptops

For ROG STRIX and TUF Laptops that have Aura RGB backlight and support ```asusctl```, you can use [wal-asusrog](https://github.com/Flexksx/wal-asusrog.git)


## Other Tools

### tabbed

1. Remove all defined colors in your `config.h`
2. In their place, include wal's exported colors via:

```
#include "/home/<USER>/.cache/wal/colors-wal-tabbed.h"
```

(Replace \<USER\> with your username.)

**NOTE**: this `#include` must be on the same line as what was previously deleted.

### Lightdm

You can use `slickgreeter-pywal` to change lightdm-slick-greeter's theme using the colors from `wal`.

https://github.com/Paul-Houser/slickgreeter-pywal

### Gnuplot

You can use `Gnuplot-Pywal` to theme Gnuplot using the colors from `wal`.

https://github.com/GideonWolfe/Gnuplot-Pywal