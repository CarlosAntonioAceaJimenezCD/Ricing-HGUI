## Table of Contents

- [How to use `wal`](#how-to-use-wal)
- [Applying the theme to new terminals](#applying-the-theme-to-new-terminals)
- [Making the colorscheme persist on reboot](#making-the-colorscheme-persist-on-reboot)
- [Using a custom wallpaper setter](#using-a-custom-wallpaper-setter)
- [Further Reading: --> Customization](https://github.com/dylanaraps/pywal/wiki/Customization)


## How to use `wal`

Run `wal` and point it to either a directory (`wal -i "path/to/dir"`) or an image (`wal -i "/path/to/img.jpg"`) and that's all. `wal` will change your wallpaper for you and also set your terminal colors.

```sh
usage: wal [-h] [-a "alpha"] [-b background] [--backend [backend]]
           [--theme [/path/to/file or theme_name]] [--iterative]
           [--saturate 0.0-1.0] [--preview] [--vte] [-c]
           [-i "/path/to/img.jpg"] [-l] [-n] [-o "script_name"] [-q] [-r] [-R]
           [-s] [-t] [-v] [-e]

wal - Generate colorschemes on the fly

optional arguments:
  -h, --help            show this help message and exit
  -a "alpha"            Set terminal background transparency. *Only works in
                        URxvt*
  -b background         Custom background color to use.
  --backend [backend]   Which color backend to use. Use 'wal --backend' to
                        list backends.
  --theme [/path/to/file or theme_name], -f [/path/to/file or theme_name]
                        Which colorscheme file to use. Use 'wal --theme' to
                        list builtin themes.
  --iterative           When pywal is given a directory as input and this flag
                        is used: Go through the images in order instead of
                        shuffled.
  --saturate 0.0-1.0    Set the color saturation.
  --preview             Print the current color palette.
  --vte                 Fix text-artifacts printed in VTE terminals.
  -c                    Delete all cached colorschemes.
  -i "/path/to/img.jpg" Which image or directory to use.
  -l                    Generate a light colorscheme.
  -n                    Skip setting the wallpaper.
  -o "script_name"      External script to run after "wal".
  -q                    Quiet mode, do not print anything.
  -r                    'wal -r' is deprecated: Use (cat
                        ~/.cache/wal/sequences &) instead.
  -R                    Restore previous colorscheme.
  -s                    Skip changing colors in terminals.
  -t                    Skip changing colors in tty.
  -v                    Print "wal" version.
  -e                    Skip reloading gtk/xrdb/i3/sway/polybar
```


## Applying the theme to new terminals

`wal` only applies the new colors to the currently open terminals. Any new terminal windows you open won't use the new theme unless you add a single line to your shell's start up file.

Add this line to your shell startup file. (`.bashrc`, `.zshrc`, `.mkshrc` etc.)

```sh
# Import colorscheme from 'wal' asynchronously
# &   # Run the process in the background.
# ( ) # Hide shell job control messages.
# Not supported in the "fish" shell.
(cat ~/.cache/wal/sequences &)

# Alternative (blocks terminal for 0-3ms)
cat ~/.cache/wal/sequences

# To add support for TTYs this line can be optionally added.
source ~/.cache/wal/colors-tty.sh
```

## Making the colorscheme persist on reboot

On reboot your new colorscheme won't be set or in use. To fix this you have to add a line to your `.xinitrc` or whatever file starts programs on your system. This `wal` command will set your wallpaper to the wallpaper that was set last boot and also apply the colorscheme again.

Without this you'll be themeless until you run `wal` again.

```sh
# Add this to your .xinitrc or whatever file starts programs on startup.
# -R restores the last colorscheme that was in use.
wal -R
```


## Using a custom wallpaper setter

`wal` will detect which wallpaper setter you have installed and use it with the `fill` mode to set the wallpaper. If you'd like to override this and use either your own setter, a different mode or some different commandline flags you can do the following:

```sh
# -n tells `wal` to skip setting the wallpaper.
wal -i img.jpg -n

# Using feh to tile the wallpaper now.
# We grab the wallpaper location from wal's cache so 
# that this works even when a directory is passed.
feh --bg-tile "$(< "${HOME}/.cache/wal/wal")"  


# You can create a function for this in your shellrc (.bashrc, .zshrc).
wal-tile() {
    wal -n -i "$@"
    feh --bg-tile "$(< "${HOME}/.cache/wal/wal")"
}

# Usage:
wal-tile "~/Pictures/wall.jpg"
wal-tile "~/Pictures/tiles"
```