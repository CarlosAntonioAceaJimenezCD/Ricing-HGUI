---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/dylanaraps/pywal/Using-`pywal`-as-a-module.md"
title: "Using `pywal` as a module"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/dylanaraps/pywal/wiki"
---
## Table of Contents

- **[Functions](#functions)**
    - [pywal.image.get()](#pywalimagegetimg-cache_dir)
    - [pywal.colors.get()](#pywalcolorsgetimg-cache_dir-color_count-notify)
    - [pywal.colors.file()](#pywalcolorsfileinput_file)
    - [pywal.sequences.send()](#pywalsequencessendcolors-cache_dir-to_send-vte_fix)
    - [pywal.export.every()](#pywalexporteverycolors-cache_dir)
    - [pywal.export.color()](#pywalexportcolorcolors-export_type-output_file)
    - [pywal.wallpaper.change()](#pywalwallpaperchangeimage)
    - [pywal.wallpaper.get()](#pywalwallpapergetcache_dir)
    - [pywal.reload.colors()](#pywalreloadcolorsvte-cache_dir)
    - [pywal.reload.env()](#pywalreloadenvxrdb_file)
    - [pywal.reload.i3()](#pywalreloadi3)
    - [pywal.reload.polybar()](#pywalreloadpolybar)
    - [pywal.reload.xrdb()](#pywalreloadxrdbxrdb_file)
- **[Color `dict` format.](#color-dict-format)**
- **[Examples](#examples)**
    - [Simple Example](#simple-example)
    - [More Complex Example (Custom cache location)](#more-complex-example-using-custom-cache-location)
    - [Example showing colors read from `json` file](#example-showing-colors-read-from-json-file)


## Functions


### `pywal.image.get(img, cache_dir)`

**Parameters:**

- **`image`**: 
    - Optional: `False`
    - Type: `string`
    - A path to an image or a directory.
    - When a directory is passed `wal` will select a random image from the directory.
- **`cache_dir`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal`
    - Only set this if you'd like to use a different cache location.

**Returns:**

This function validates image input and returns a string containing the full path to the image.


### `pywal.colors.get(img, cache_dir, color_count, notify)`

**Parameters:**

- **`image`**: 
    - Optional: `False`
    - Type: `string`
    - A path to an image or a directory.
- **`cache_dir`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal`
    - Only set this if you'd like to use a different cache location.
- **`color_count`**:
    - Optional: `True`
    - Type: `integer`
    - Default: `16`
    - How many colors to return.
- **`notify`**:
    - Optional: `True`
    - Type: `boolean`
    - Default: `False`
    - Whether or not to display notifications.

**Returns:**

This function generates a colorscheme using `imagemagick` and returns a `dict` containing the colors.

See: **[Color `dict` format.](#color-dict-format)**


### `pywal.colors.file(input_file)`

**Parameters:**

- **`input_file`**: 
    - Optional: `False`
    - Type: `string`
    - A path to a `json` file containing a valid scheme..
    - See this [wiki page](https://github.com/dylanaraps/pywal/wiki/Customization#scripting) for how the file is formatted.

**Returns:**

This function imports the colorscheme from a `json` file and returns a `dict` useable with the rest of the api.

See: **[Color `dict` format.](#color-dict-format)**


### `pywal.sequences.send(colors, cache_dir, to_send, vte_fix)`

**Parameters:**

- **`colors`**: 
    - Optional: `False`
    - Type: `dict`
    - Example: The output of `wal.create_palette()`
- **`cache_dir`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal`
    - Only set this if you'd like to use a different cache location.
- **`to_send`**:
    - Optional: `False`
    - Type: `boolean`
    - Set this to `False` to disable sending sequences to all open terminals.
- **`vte_fix`**:
    - Optional: `False`
    - Type: `boolean`
    - Set this to `True` if you're using a VTE based terminal.
        - xfce4-terminal, termite, gnome-terminal etc.

**Returns:**

N/A

**Purpose:**

This function uses a `dict` of colors to apply the colorscheme to every open terminal emulator.

### `pywal.export.every(colors, cache_dir)`

**Parameters:**

- **`colors`**: 
    - Optional: `False`
    - Type: `dict`
    - Example: The output of `wal.create_palette()`
- **`cache_dir`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal`
    - Only set this if you'd like to use a different cache location.

**Returns:**

N/A

**Purpose:**

This function takes template files from a directory, substitutes the markers and exports the file to the `cache_dir`.


### `pywal.export.color(colors, export_type, output_file)`

**Parameters:**

- **`colors`**: 
    - Optional: `False`
    - Type: `dict`
    - Example: The output of `wal.create_palette()`
- **`export_type`**: 
    - Optional: `False`
    - Type: `string`
    - Values: `css`, `dmenu`, `dwm`, `st`, `tabbed`, `gtk2`, `json`, `konsole`, `kitty`, `plain`, `putty`, `rofi`, `scss`, `shell`, `speedcrunch`, `sway`, `tty`, `waybar`, `xresources`, `xmonad`, `yaml`
    - Which template file to export.
    - Example: `pywal.export(colors, "css", "/path/to/save_file.css")`
- **`output_file`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal/{template_name}`
    - Only set this if you'd like to save the templates in a custom location with a different name.

**Returns:**

N/A

**Purpose:**

This function exports the colors in the specified format.

**Note:**

If you'd like to export in all formats use `pywal.export.every()`.


### `pywal.wallpaper.change(image)`

**Parameters:**

- **`image`**: 
    - Optional: `False`
    - Type: `string`
    - A path to an image or a directory.

**Returns:**

N/A

**Purpose:**

This function takes an image as input and sets the wallpaper.


### `pywal.wallpaper.get(cache_dir)`

**Parameters:**

- **`cache_dir`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal`
    - Only set this if you'd like to use a different cache location.

**Returns:**

This function returns a string with the full path to the current wallpaper.


### `pywal.reload.colors(vte, cache_dir)`

#### Deprecated in `1.0.0`+ will be removed in the future.

**Parameters:**

- **`vte`**:
    - Optional: `False`
    - Type: `boolean`
    - Set this to `True` if you're using a VTE based terminal.
        - xfce4-terminal, termite, gnome-terminal etc.
- **`cache_dir`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal`
    - Only set this if you'd like to use a different cache location.

**Returns:**

N/A

**Purpose:**

This function reapplies the colorscheme to the terminal. Same as `wal -r`.


### `pywal.reload.env(xrdb_file)`

**Parameters:**

- **`xrdb_file`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal/colors.Xresources`
    - Which file to read Xresources colors from.

**Returns:**

N/A

**Purpose:**

This function reloads various programs and imports the colors into the `xrdb`.


### `pywal.reload.i3()`

**Parameters:**

N/A

**Returns:**

N/A

**Purpose:**

This function reloads `i3`'s configuration.


### `pywal.reload.polybar()`

**Parameters:**

N/A

**Returns:**

N/A

**Purpose:**

This function reloads `polybar`'s configuration.


### `pywal.reload.xrdb(xrdb_file)`

**Parameters:**

- **`xrdb_file`**: 
    - Optional: `True`
    - Type: `string`
    - Default: `~/.cache/wal/colors.Xresources`
    - Which file to read Xresources colors from.

**Returns:**

N/A

**Purpose:**

This function loads an Xresources file into the db.


## Color `dict` format.

The `dict` of colors that most functions take as input looks like this:

```py
{'wallpaper': '/home/dylan/Pictures/Wallpapers/022.png', \
 'special': {'background': '#484C6A', 'foreground': '#C7D5E2', 'cursor': '#C7D5E2'}, \
 'colors': {'color0': '#484C6A', 'color1': '#CC95B4', 'color2': '#D09CB9', 'color3': '#C8A4BC', 'color4': '#D3A2BD', 'color5': '#D192C3', 'color6': '#D6A7C1', 'color7': '#C7D5E2', 'color8': '#999999', 'color9': '#CC95B4', 'color10': '#D09CB9', 'color11': '#C8A4BC', 'color12': '#D3A2BD', 'color13': '#D192C3', 'color14': '#D6A7C1', 'color15': '#C7D5E2'}}
```

It's a `dict` containing two additional nested `dicts`, one for `special` colors (background, foreground, cursor) and one for the colors `0-XXX`. It also contains a `key/value` for the wallpaper used to generate the scheme.

Here's how the format is represented in `json`:

```json
{
    "wallpaper": "{wallpaper}",

    "special": {
        "background": "{background}",
        "foreground": "{foreground}",
        "cursor": "{cursor}"
    },
    "colors": {
        "color0": "{color0}",
        "color1": "{color1}",
        "color2": "{color2}",
        "color3": "{color3}",
        "color4": "{color4}",
        "color5": "{color5}",
        "color6": "{color6}",
        "color7": "{color7}",
        "color8": "{color8}",
        "color9": "{color9}",
        "color10": "{color10}",
        "color11": "{color11}",
        "color12": "{color12}",
        "color13": "{color13}",
        "color14": "{color14}",
        "color15": "{color15}"
    }
}
```


## Examples


### Simple example.


```py
"""Simple script for wal api."""
import pywal


def main():
    """Main function."""
    # Validate image and pick a random image if a
    # directory is given below.
    image = pywal.image.get("/home/dylan/Pictures/Wallpapers/")

    # Return a dict with the palette.
    # Set quiet to 'True' to disable notifications.
    colors = pywal.colors.get(image)

    # Apply the palette to all open terminals.
    # Second argument is a boolean for VTE terminals.
    # Set it to true if the terminal you're using is
    # VTE based. (xfce4-terminal, termite, gnome-terminal.)
    pywal.sequences.send(colors, vte=False)

    # Export all template files.
    pywal.export.every(colors, cache_dir)

    # Export individual template files.
    pywal.export.color(colors, "xresources", "/home/dylan/.Xresources")
    pywal.export.color(colors, "shell", "/home/dylan/colors.sh")

    # Reload xrdb, i3 and polybar.
    pywal.reload.env()

    # Reload individual programs.
    pywal.reload.i3()
    pywal.reload.polybar()
    pywal.reload.xrdb()

    # Set the wallpaper.
    pywal.wallpaper.change(image)


main()
```


### More complex example (Using custom cache location).


```py
"""Test script for wal api.
   This script uses a custom cache location for the files."""
import os
import pywal


CACHE_DIR = os.path.join(os.environ["HOME"], "wal-test-dir")
COLOR_COUNT = 16


def main():
    """Main function."""
    # Validate image and pick a random image if a
    # directory is given below.
    #
    # CACHE_DIR is an optional argument and is used to check the current
    # wallpaper against the random selection. This prevents shuffling to
    # the identical image when a directory is passed as an argument.
    image = pywal.image.get("/home/dylan/Pictures/Wallpapers/", CACHE_DIR)

    # Return a dict with the palette.
    #
    # The last argument is 'quiet' mode. When set to true, no notifications
    # are displayed.
    colors = pywal.colors.get(image, CACHE_DIR, COLOR_COUNT)

    # Apply the palette to all open terminals.
    # Second argument is a boolean for VTE terminals.
    # Set it to true if the terminal you're using is
    # VTE based. (xfce4-terminal, termite, gnome-terminal.)
    pywal.sequences.send(colors, False, CACHE_DIR)

    # Export all template files.
    pywal.export.every(colors, CACHE_DIR)

    # Export individual template files.
    pywal.export.color(colors, "xresources", 
                       os.path.join(CACHE_DIR, "xresources"))
    pywal.export.color(colors, "shell", 
                       os.path.join(CACHE_DIR, "colors.bash"))

    # Reload xrdb, i3 and polybar.
    pywal.reload.env("/etc/foo/custom.Xresources")

    # Reload individual programs.
    pywal.reload.i3()
    pywal.reload.polybar()
    pywal.reload.xrdb("/etc/foo/custom.Xresources")

    # Set the wallpaper.
    pywal.wallpaper.change(image)


main()
```


### Example showing colors read from `json` file.

```py
"""Script showing how to import colors from a json file."""
import pywal


def main():
    """Main function."""
    # Read the colors from a `json` file.
    colors = pywal.colors.file("/home/dylan/test_file.json")
    image = colors["wallpaper"]

    # Apply the palette to all open terminals.
    # Second argument is a boolean for VTE terminals.
    # Set it to true if the terminal you're using is
    # VTE based. (xfce4-terminal, termite, gnome-terminal.)
    pywal.sequences.send(colors, vte=False)

    # Export all template files.
    pywal.export.every(colors)

    # Reload xrdb, i3 and polybar.
    pywal.reload.env()

    # Set the wallpaper.
    pywal.wallpaper.change(image)


main()
```