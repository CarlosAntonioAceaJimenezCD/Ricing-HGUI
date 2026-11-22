---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/davatorium/rofi/dmenu_specs.md"
title: "dmenu_specs"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/davatorium/rofi/wiki"
---
#### What is dmenu?

* dmenu reads stdin, it splits the input based on a separator (newline character) and displays each item as a selectable entry. Confirming the selection will output that item to stdout.
* dmenu also has a input textbox, that is used to filter the input list.
* input can be arbitrary and will be shown on stdout the same way as regular entries.

#### rofi extends standard dmenu behavior in the following ways:
* it's possible to force output to match stdin. Entries that are not part of stdin are ignored
* each line can have multiple actions, depending on the key that was pressed. rofi will return a different exit code on each key (default: Alt-{1-9} > exit codes 10-18)
* filtering is case insensitive by default.
* rofi can select a certain line number on startup.
* rofi can filter the list with the `-filter` argument. This will basically put text into input bar and filter the list accordingly
* entries can be colored line by line, it's possible to color ranges and single lines. (x-y and x,y,z)
* formatting of stdout with -format parameter
 * `-format i` will show line number, starting at 0
 * `-format s` will show line content  
 * `-format e` will show the line content, shell quoted.
 * `-format f` will show last used filter
 * `-format F` will show last used filter, shell quoted

##### Example:
```
echo -e "foo\nbar" | rofi -dmenu -format i:s
1:bar
```

#### Icons

You can get icon with a row by passing extra information in the line like:
```bash
echo -en "aap\0icon\x1ffolder\n"
```
Here:
* `\0` indicates end of entry.
* `\x1f` is the field separator.
* `\n` is the entry separator.


Currently only 'icon' is supported.

#### Proposed extended features:
* allow to separate input into a visible output and a hidden string, which matches output.
* allow to output all filtered results to stdout
* mark lines to be printed on stdout
* make certain lines not selectable (think of help text at the top) - this could work similar to -u and -a options