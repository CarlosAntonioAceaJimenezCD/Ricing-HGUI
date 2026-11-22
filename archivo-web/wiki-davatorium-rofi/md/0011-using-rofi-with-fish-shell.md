---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/davatorium/rofi/Using-Rofi-with-Fish-Shell.md"
title: "Using Rofi with Fish Shell"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/davatorium/rofi/wiki"
---
For all you fish shell users, all 9 of you! It would be nice if Rofi worked well with your shell. This functionality can be yours for the low price of 2 lines added to `~/.Xresources`

    rofi.run-command: fish -c '{cmd}'

This will tell rofi to run commands via fish.

    rofi.run-list-command: 'fish -c functions'

The functions shell command outputs a comma separated list of defined fish shell functions that serve as candidates for completion by Rofi.  This also prevents rofi from giving you an error regarding <insert-shell-function> not being an existing command when triggering kb-accept-custom, which is by default bound to Shift+Return and Ctrl+Return.
**Attention: This creates some delay if your fish shell takes some time to start (e.g. with oh-my-fish)**

After adding these lines don't forget to run:

    xrdb ~/.Xresources

in order for your changes to take effect immediately.