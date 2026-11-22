#### The problem

When using custom keymaps with custom modifier keys, rofi will not be able to use these modifiers.  
The following writeup was done by [mardukbp](https://github.com/mardukbp).

Relevant bug report: https://github.com/DaveDavenport/rofi/issues/307

#### xmodmap

In the following I will assume that the current keymap is vanilla `us`: `setxkbmap us -option`.

The current keymap can be exported to a file with `xmodmap -pke > xmodmaprc`. This file contains a dictionary mapping keycodes to keys. If one wants to e.g. use `Alt_L` as `Shift_L`, it is only a matter of changing the line corresponding to keycode 64 and then calling `xmodmap xmodmaprc`.

Now issuing `xmodmap` shows that no keycode is bound to `Alt_L` and `rofi` will obviously complain. How does one make `rofi` happy? Add the following lines at the BOTTOM of `xmodmaprc`:

```
clear mod1
add mod1 = Alt_L Alt_R Meta_L
```

Adding lines beginning with `clear` and `add` at the top of the file when a lot of keys have been remapped leads to anger->hate->suffering (that's what happened to me!).

Now running `xmodmap xmodmaprc && xmodmap` will show that there is an `Alt_L` bound to keycode 204 (0xcc), that is `Alt_R + Alt_L = Alt_L`, and `rofi` will not complain anymore. However, `xmodmap` will only report two Shift keys when in reality there are now three. Adding the following lines to the bottom of `xmodmaprc` takes care of this:

```
clear shift
add shift = Shift_L Shift_R
```

#### Bottom line

Whenever one rebinds the keycodes of modifier keys in `xmodmaprc` one also has to update the modifier map. This is done using the commands `clear` and `add` as explained above.