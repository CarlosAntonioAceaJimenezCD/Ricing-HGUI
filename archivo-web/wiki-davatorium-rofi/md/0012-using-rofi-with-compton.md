---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/davatorium/rofi/Using-rofi-with-compton.md"
title: "Using rofi with compton"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/davatorium/rofi/wiki"
---
### Dimming inactive windows

If you're using the option *--inactive-dim* to let compton dim inactive windows, rofi gets permanently dimmed because it's not a regular X11 window and thus never has the focus. You can avoid this by adding rofi to the list of windows which are considered to be always focused. This is done with the option *--focus-exclude*:

`compton --inactive-dim 0.3 --focus-exclude 'class_g = "Rofi"'`