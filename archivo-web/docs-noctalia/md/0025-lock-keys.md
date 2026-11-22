---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/bar/widgets/lock-keys.mdx"
title: "lock keys"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: lock_keys
description: Shows Caps Lock, Num Lock, and Scroll Lock state.
sidebar:
  order: 13
---

Shows Caps Lock / Num Lock / Scroll Lock state from the active XKB keyboard state.

Configuring this widget keeps lock-key state polling active even when `[osd.kinds].lock_keys = false`.

| Setting            | Type   | Default   | Description                                         |
| ------------------ | ------ | --------- | --------------------------------------------------- |
| `display`          | string | `"short"` | `"short"` (`C N S`) or `"full"` (`Caps Num Scroll`) |
| `show_caps_lock`   | bool   | `true`    | Show the Caps Lock indicator                        |
| `show_num_lock`    | bool   | `true`    | Show the Num Lock indicator                         |
| `show_scroll_lock` | bool   | `false`   | Show the Scroll Lock indicator                      |
| `hide_when_off`    | bool   | `false`   | Hide each indicator when it is off                  |

```toml
[widget.lock_keys]
display          = "short"
show_caps_lock   = true
show_num_lock    = true
show_scroll_lock = false
hide_when_off    = false
```
