---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/bar/widgets/control-center.mdx"
title: "control center"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: control-center
description: Opens the control center panel from the bar.
sidebar:
  order: 9
---

Opens the control center panel on click.

| Setting                 | Type   | Default      | Description                                                                                       |
| ----------------------- | ------ | ------------ | ------------------------------------------------------------------------------------------------- |
| `glyph`                 | string | `"noctalia"` | Bar glyph name: Noctalia alias, Tabler icon name, or `U+` / `0x` codepoint                        |
| `custom_image`          | string | `""`         | Path to a custom image displayed instead of the glyph. Leave empty to use the glyph               |
| `custom_image_colorize` | bool   | `false`      | When `true`, tint the custom image with the widget **Color** setting (same as the glyph fallback) |

```toml
[widget.control-center]
custom_image = "/path/to/image.png"
custom_image_colorize = true
```
