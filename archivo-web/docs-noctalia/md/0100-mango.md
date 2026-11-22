---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/templates/official/mango.mdx"
title: "mango"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: Mango
description: Theme Mango window borders and overview colors with Noctalia.
sidebar:
  order: 10
---

**This template is only compatible with Mango version 0.18.0 or higher.**

The built-in Mango template generates border colors for regular, active, split, and urgent windows, and colors for jump label, and group bar borders, as well as the scratchpad background, root window background, and drop shadow of dragged windows.

## Setup

Enable **Mango** under **Settings → Templates → Compositors**.

Noctalia writes the rendered template to `~/.config/mango/noctalia.conf` and appends the line `source=~/.config/mango/noctalia.conf` to `~/.config/mango/config.conf` when that config already exists and is writable. These paths honor `$XDG_CONFIG_HOME`. If the Mango setting `auto_reload_config` is enabled, Mango reloads both files automatically when they change.

If the primary user config is absent, Noctalia leaves it absent and warns that manual setup is required. Add the source line to the config Mango actually loads. Use the resolved absolute path to `noctalia.conf` when editing a system or custom config, and edit the managing source for declarative configs. See [Compositor Configuration](/noctalia/theming/app-theming/#compositor-configuration) for setup and recovery instructions.
