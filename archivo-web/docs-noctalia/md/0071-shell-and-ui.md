---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/ipc/shell-and-ui.mdx"
title: "shell and ui"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: IPC Command Sections
description: Compatibility hub for the split v5 IPC command references.
sidebar:
  hidden: true
---

import { LinkCard, CardGrid } from '@astrojs/starlight/components';

The old combined command list has been split into focused pages:

<CardGrid>
  <LinkCard title="Shell" description="Status, config reload, settings, window switcher, and session actions." href="/noctalia/ipc/shell/" />

  <LinkCard title="Surfaces" description="Bar, panels, dock, desktop widgets, and lockscreen widgets." href="/noctalia/ipc/surfaces/" />

  <LinkCard title="Media & UI" description="Notifications, clipboard, media controls, wallpaper, theme, and screenshots." href="/noctalia/ipc/media-and-ui/" />

  <LinkCard title="Plugins" description="Plugin event dispatch and plugin/source management." href="/noctalia/ipc/plugins/" />
</CardGrid>
