---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/bar/widgets/caffeine.mdx"
title: "caffeine"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: caffeine
description: Shows and controls the compositor idle inhibitor.
sidebar:
  order: 6
---

Shows a coffee glyph and toggles the compositor idle inhibitor on click. Uses the standard Wayland `zwp_idle_inhibit_manager_v1` protocol.

No configurable settings.

**Command-line controls:**

```sh
noctalia msg caffeine-enable
noctalia msg caffeine-disable
noctalia msg caffeine-toggle
```
