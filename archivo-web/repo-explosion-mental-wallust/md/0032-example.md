---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/explosion-mental/wallust/master/docs/templates/example.md"
title: "Example"
fetched_at: 2026-11-22T06:33:14+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/explosion-mental/wallust"
---
# Example

```
# zathurarc config sample
...

# colors
set default-bg     "{{background}}"

# complementary foreground, but keep it light
set default-fg     "{{foreground | complementary | lighten(0.5)}}"

# make it a bit lighter than background
set statusbar-bg   "{{background | lighten(0.3)}}"

# make it darken by blending to a darken color
set statusbar-fg   "{{foreground | blend("#eeeeee")}}"

# use it's complementary
set inputbar-bg    "{{background | complementary}}"
```

Then you can add this file to `~/.config/wallust/templates`
and use the config file to **template** it. For example,
`zathura.template = 'zathurarc'`, and then define a
**target** field, see [config](../config/README.md).
