---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/davatorium/rofi/mode-Specs.md"
title: "Basic flow"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/davatorium/rofi/wiki"
---
Apart from [dmenu mode](https://github.com/davatorium/rofi/wiki/dmenu_specs), rofi can be told to call a custom script.

# Basic flow
If you start `rofi -modi yourscript:yourscript.sh -show yourscript`, this happens:
1. Rofi calls `yourscript.sh` without parameters.
2. Your script needs to write its choices to `stdout`, separated by line breaks (`\n`).
3. Rofi shows these entries and allows the user to choose one.
4. Your script is called again with the chosen entry as its parameter.

# Pass extra properties in script mode

Please see the [rofi-script](https://github.com/davatorium/rofi/blob/next/doc/rofi-script.5.markdown) manpage.
