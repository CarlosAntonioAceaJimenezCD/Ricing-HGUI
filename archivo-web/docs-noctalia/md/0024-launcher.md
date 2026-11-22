---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/bar/widgets/launcher.mdx"
title: "launcher"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: launcher
description: Opens the launcher panel from the bar.
sidebar:
  order: 12
---

Opens the launcher panel on click. Its width, toolbar, default view, shortcuts, categories, and app grid follow the options under `shell.launcher`.

| Setting                 | Type   | Default    | Description                                                                                       |
| ----------------------- | ------ | ---------- | ------------------------------------------------------------------------------------------------- |
| `glyph`                 | string | `"search"` | Bar glyph name: Noctalia alias, Tabler icon name, or `U+` / `0x` codepoint                        |
| `custom_image`          | string | `""`       | Path to a custom image displayed instead of the glyph. Leave empty to use the glyph               |
| `custom_image_colorize` | bool   | `false`    | When `true`, tint the custom image with the widget **Color** setting (same as the glyph fallback) |

```toml
[widget.launcher]
glyph = "menu-2"
custom_image_colorize = true
```
