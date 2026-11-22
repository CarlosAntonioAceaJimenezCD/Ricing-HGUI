---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/davatorium/rofi/Themes.md"
title: "Themes"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/davatorium/rofi/wiki"
---
| ❗ **This is brief description of the features. See [theme manpages](https://github.com/davatorium/rofi/blob/next/doc/rofi-theme.5.markdown) to see the full documentation.**   |
| --- |

The official repository for themes can be found [here](https://github.com/DaveDavenport/rofi-themes).

Rofi themes use the `.rasi` file extension. The format is similar to `.css`. You can find documentation on the `.rasi` format [here](https://github.com/davatorium/rofi/blob/next/doc/rofi-theme.5.markdown).

## Getting Started with themes

To see the default theme, run the following command:

`rofi -no-config -dump-theme`

This can also be used as a base for further customization

`rofi -no-config -dump-theme > ~/.config/rofi/<your-theme-name>.rasi`

Later on you can modify and use this with 

`rofi -show <modi> -theme <your-theme-name>` 

or adding `@theme <your-theme-name>` to your configuration file.

_if the theme file is in some other directory other than the following, then use the full path when specifying it_:

* `/usr/local/share/rofi/themes`
* `$HOME/.local/share/rofi/themes`
* `$HOME/.config/rofi/themes`

Generate a default configuration file
```
mkdir -p ~/.config/rofi
rofi -dump-config > ~/.config/rofi/config.rasi
```

This creates a file called `config.rasi` in the `~/.config/rofi/` folder. You can modify this file to set configuration settings and modify themes. `config.rasi` is the file rofi looks to by default.

## Editing Themes + Live Reload

It is possible to live reload rofi as you edit and save your the theme you're working on.

### Dependencies
- [Entr](http://eradman.com/entrproject/)

Take the following script called `run_rofi.sh`:

```
#!/usr/bin/env bash
options="one
two
three"
theme=${1:-$HOME/.config/rofi/config.rasi}
selection=$(echo -e "${options}" | rofi -dmenu -config $theme)
case "${selection}" in
  "one")
    notify-send "run_rofi.sh" "one";;
  "two")
    notify-send "run_rofi.sh" "two";;
  "three")
    notify-send "run_rofi.sh" "three";;
esac
```

You can run the following:

```
cd ~/.config/rofi
ls | entr -r $HOME/.config/rofi/run_rofi.sh
```
Which  effectively re-runs `run_rofi.sh` whenever a file in `~/.config/rofi` is modified.

You will notice that this places rofi in the foreground whenever you save a file, forcing you to press Escape to close it to get back to your editor. An alternative is to pass the `-normal-window` flag to rofi, which in this case is called in `run_rofi.sh`. This will place rofi in a normal window. It still steals focus from your editor, but you can alt+tab back to your editor, or if you use a tiling window manager, move focus to the adjacent window (your editor) via your normal key commands (for me, in i3, it is `$mod+j`). This will leave rofi open and may be preferable. 

If anyone finds out a way to run rofi without it taking cursor focus, please document it here!

## Overriding Default Theme `~/.config/rofi/config.rasi`

If you have your own custom theme other than what's defined in `config.rasi` you can use the `-theme {name}` flag when running rofi. The {name} handed to the themes folder is the name of the `.rasi` file in `~/.config/rofi/` that you want to use instead.

Example: 

Running rofi with a custom theme file `~/.config/rofi/mytheme.rasi`. 
```
rofi -show drun -theme mytheme
```

Example:

Reference the theme by name in your `config.rasi`.
```
configuration {
...

...
}
@theme "mytheme"
```

## Icons

Icon themes must be located in `~/.local/share/icons/` or `~/.icons/`. Also `-drun` needs to be used instead of `-run`.

Set icons via rofi commands:

```
rofi -show drun -show-icons -icon-theme MY_ICON_THEME
```

Set icons via .rasi:

```css
configuration {
    icon-theme: "MY_ICON_THEME";
}
element {
    children: [ element-icon, element-text ];
}
```

## How to enable `.rasi` syntax highlighting

### Vim:

Add the following to the _bottom_ of your `.rasi` file.
Usually these syntax highlighting indicators are put at the beginning of the file, but rofi will fail to load the theme if it's not at the bottom of the file.

 `/* vim:ft=css`

Or in your vimrc:

```
au BufNewFile,BufRead /*.rasi setf css
```

### Emacs: 

This should go at the _beginning_ of the file.

`/*-*- mode: css; -*-*/`

## Examples

* https://github.com/Murzchnvok/rofi-collection

* https://github.com/MonsieurBedard/rofi-breeze-theme

* https://github.com/lr-tech/rofi-themes-collection
