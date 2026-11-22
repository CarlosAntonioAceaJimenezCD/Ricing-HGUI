`wpgtk` loads it's configuration from `$HOME/.config/wpg/wpg.conf` this are the default values
the `keywords` section is explained [here](https://github.com/deviantfero/wpgtk/wiki/Custom-Keywords).

```python
[settings]
set_wallpaper = true # set wallpaper or not in each color-scheme change
gtk = true           # live reload GTK+ or not
active = 0           # color to use as "active" and "inactive" shades
light_theme = false  # whether to use a light theme or not
editor = gvim        # editor to use on templates
execute_cmd = false  # execute command after applying theme
command = urxvt -e echo hi # command to execute 
backend = wal        # colorscheme generation backend
alpha = 100          # transparency value
smart_sort = true    # sort color-schemes according to xterm standard
auto_adjust = false  # auto-adjust color-schemes when adding them

[keywords]
# custom-key = value
```

To adjust your settings you can either edit the file directly or use the `Options` tab
in `wpg` GUI mode, an advantage to doing this is that you can change the settings without
actually saving theme for a one-time configuration.

<p align="center">
  <img src="https://i.imgur.com/rcYOlp8.png" alt="config-tab"/>
</p>