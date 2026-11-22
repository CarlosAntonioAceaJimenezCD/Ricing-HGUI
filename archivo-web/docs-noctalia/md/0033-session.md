---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/bar/widgets/session.mdx"
title: "session"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: session
description: Opens the session menu panel from the bar.
sidebar:
  order: 21
---

Shows a power glyph and opens the session menu panel on click.

| Setting                 | Type   | Default      | Description                                                                         |
| ----------------------- | ------ | ------------ | ----------------------------------------------------------------------------------- |
| `glyph`                 | string | `"shutdown"` | Bar glyph name: Noctalia alias, Tabler icon name, or `U+` / `0x` codepoint          |
| `custom_image`          | string | `""`         | Path to a custom image displayed instead of the glyph. Leave empty to use the glyph |
| `custom_image_colorize` | bool   | `false`      | When `true`, tint the custom image with the widget icon color                       |

```toml
[widget.session]
glyph = "lock"
```
