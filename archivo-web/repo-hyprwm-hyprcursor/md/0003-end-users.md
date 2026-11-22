---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/hyprwm/hyprcursor/main/docs/END_USERS.md"
title: "END_USERS"
fetched_at: 2026-11-22T06:33:14+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/hyprwm/hyprcursor"
---
## Using a hyprcursor theme

Download a hyprcursor theme and extract it to a new directory in `~/.local/share/icons`.

Make sure the first directory contains a manifest, for example:

```s
~/.local/share/icons/myCursorTheme/manifest.hl
```

## Overriding a theme

Set the `HYPRCURSOR_THEME` env to your theme directory,
so for example to get the above to always load, use `export HYPRCURSOR_THEME = myCursorTheme`.