### Dimming inactive windows

If you're using the option *--inactive-dim* to let compton dim inactive windows, rofi gets permanently dimmed because it's not a regular X11 window and thus never has the focus. You can avoid this by adding rofi to the list of windows which are considered to be always focused. This is done with the option *--focus-exclude*:

`compton --inactive-dim 0.3 --focus-exclude 'class_g = "Rofi"'`