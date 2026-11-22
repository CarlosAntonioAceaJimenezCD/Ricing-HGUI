---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/davatorium/rofi/Script-Launcher.md"
title: "`rofi` as a launcher for arbitrary shell scripts"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/davatorium/rofi/wiki"
---
# `rofi` as a launcher for arbitrary shell scripts

`rofi` can be used for running arbitrary shell scripts too. As an example, consider a scenario where you would like to get quick access to your passwords stored with a password manager (e.g., [gopass](https://github.com/gopasspw/gopass)) or you would like to quickly make screenshots with a tools like [scrot](https://github.com/dreamer/scrot). 

First, you can create a file that maps names to actual shell-scripts. You could achieve the same through aliases, but it is a bit more flexible using a simple `.csv` file (`cmd.csv`) for that.

``` 
Make Screenshot,$HOME/.config/rofi/sshot.sh
Get Password,$HOME/.config/rofi/pass.sh
```
The first column will be made visible in rofi and describes what the script does, and the second column provides the absolute path to the script to be executed.

Once configured, you can use the script below. The script uses the information from `cmd.csv` file to display a menu; the user selects the name from the first column and, based on the selection, the corresponding script is executed.

```
#!/bin/bash

WORKINGDIR="$HOME/.config/rofi/"
MAP="$WORKINGDIR/cmd.csv"

cat "$MAP" \
    | cut -d ',' -f 1 \
    | rofi -dmenu -p "Util " \
    | head -n 1 \
    | xargs -i --no-run-if-empty grep "{}" "$MAP" \
    | cut -d ',' -f 2 \
    | head -n 1 \
    | xargs -i --no-run-if-empty /bin/bash -c "{}"

exit 0

```







