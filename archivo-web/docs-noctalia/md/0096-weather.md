---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/noctalia-dev/noctalia/main/docs/user/services/weather.mdx"
title: "weather"
fetched_at: 2026-11-22T01:22:58+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/noctalia-dev/noctalia"
---
---
title: Weather
description: Weather service configuration and location requirements.
sidebar:
  order: 11
---

```toml
[weather]
enabled         = true
refresh_minutes = 30
unit            = "metric"      # metric | imperial
effects         = true          # visual weather effects
```

Weather consumes the coordinates resolved by [`[location]`](/noctalia/services/location/) - set `auto_locate` or `address` there. When a location is available, Noctalia fetches current weather plus a 6-day forecast. Configure under **Settings → Location → Weather**.

Weather data is provided by [Open-Meteo](https://open-meteo.com/). See the [Open-Meteo privacy policy](https://open-meteo.com/en/terms#privacy) for how requests to that service are handled.

Enabling weather adds a `Weather` tab to the control center. The bar `weather` widget type also requires weather to be enabled.
