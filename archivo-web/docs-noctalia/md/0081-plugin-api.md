---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/plugins/development/plugin-api.mdx"
title: "plugin api"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: Plugin API Versions
description: See which plugin capabilities each API level introduced and which Noctalia version first shipped them.
sidebar:
  label: Plugin API Versions
  order: 6
---

import PluginApiTable from '../../../../../components/PluginApiTable.astro';
import PluginApiRange from '../../../../../components/PluginApiRange.astro';

Every plugin declares the oldest API level it requires with `plugin_api` in `plugin.toml`. API levels are cumulative: use the oldest level that includes every capability your plugin needs to keep it compatible with as many Noctalia versions as possible.

<PluginApiTable />

Noctalia currently supports plugin API levels <PluginApiRange />. A plugin version declaring a level outside that range cannot run.

Raising a plugin's level therefore drops it from every Noctalia below it. A source repo can keep those users covered by publishing older revisions in its catalog: Noctalia then installs the newest revision of the plugin its own API range allows, labels it in the store as an older version, and moves the user up to the newest one once they upgrade Noctalia. See [keeping older Noctalia versions supported](/noctalia/plugins/development/workflow/#keeping-older-noctalia-versions-supported).
