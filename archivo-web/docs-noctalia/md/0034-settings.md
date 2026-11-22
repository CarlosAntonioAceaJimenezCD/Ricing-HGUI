---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/bar/widgets/settings.mdx"
title: "settings"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: settings
description: Opens the Noctalia Settings window from the bar.
sidebar:
  order: 22
---

Shows a glyph/image and opens the Settings window on click.

| Setting                 | Type   | Default      | Description                                                                         |
| ----------------------- | ------ | ------------ | ----------------------------------------------------------------------------------- |
| `glyph`                 | string | `"settings"` | Bar glyph name: Noctalia alias, Tabler icon name, or `U+` / `0x` codepoint          |
| `custom_image`          | string | `""`         | Path to a custom image displayed instead of the glyph. Leave empty to use the glyph |
| `custom_image_colorize` | bool   | `false`      | When `true`, tint the custom image with the widget icon color                       |

```toml
[widget.settings]
custom_image = "/path/to/settings.png"
custom_image_colorize = true
```
