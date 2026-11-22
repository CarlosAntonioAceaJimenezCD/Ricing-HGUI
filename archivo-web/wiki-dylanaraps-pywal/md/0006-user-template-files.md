---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/dylanaraps/pywal/User-Template-Files.md"
title: "User Template Files"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/dylanaraps/pywal/wiki"
---
As of version `1.0.0` `pywal` now supports user defined template files. What this means is that similar to the export files in the `~/.cache/wal/` directory you can now create your own files which will be processed by `pywal` and spit out in this directory.

The user defined files are read from `~/.config/wal/templates/` and are exported to `~/.cache/wal/` under the same name. Using this feature you can also overwrite the default export files, here's an example using `rofi`.

The default `rofi` configuration in `pywal` has both a light and dark variation. You can modify either one of these themes by adding your own under the aforementioned directory. To demonstrate, the steps to customize the dark version of the theme are:

1. Find the default template file. 
   - https://github.com/dylanaraps/pywal/tree/master/pywal/templates
   - For `rofi` it's called `colors-rofi-dark.rasi` (`colors-rofi-light.rasi` for the light version).
1. Create a file called `colors-rofi-dark.rasi` in `~/.config/wal/templates`.
2. Define your own colors for `rofi` using the values you want based on the original template.

```rasi
// Example snippet.
* {{
    active-background: {color2};
    active-foreground: {foreground};
    normal-background: {background};
    normal-foreground: {foreground};
    urgent-background: {color1};
    urgent-foreground: {foreground};
    // ...
}}
```

3. Rerun `wal` to apply the new settings.


### Available variables and syntax.

`pywal`'s templating works by using Python's string formatting so it's builtin, quick and simple. Variables must be surrounded by `{`/`}` to be recognized and any existing curly-braces need to be escaped. To escape curly-braces you just double them, so `{` becomes `{{` and so on.

**Variables**

- `{color0}` --> `{color15}`: Colors 0-15.
- `{background}`: Background color.
- `{foreground}`: Foreground color.
- `{cursor}`: Cursor color.
- `{alpha}`: Transparency, if provided via the `-a` flag. Default 0.
- `{wallpaper}`: The full path to the current wallpaper.

**Modifiers**

Note: These apply to all variables minus `wallpaper`.

- `{var}`: Output the color in `hex`.
- `{var.rgb}`: Output the color in `rgb`.
- `{var.rgba}`: Output the color in `rgba`.
- `{var.xrgba}`: Output the color in `xrgb`.
- `{var.strip}`: Output the color in `hex` (without a `#`).
- `{var.red}`: Output the red value as float.
- `{var.green}`: Output the green value as float.
- `{var.blue}`: Output the blue value as float.