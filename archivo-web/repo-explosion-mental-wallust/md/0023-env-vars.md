---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/explosion-mental/wallust/master/docs/parameters/env_vars.md"
title: "Enviromental Variables in templates/targets paths"
fetched_at: 2026-11-22T06:33:14+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/explosion-mental/wallust"
---
# Enviromental Variables in templates/targets paths

Allows you to have shell variables in your paths. For example:

```toml
# using XDG var
pywal = { src = "pywal", dst = "${XDG_HOME_CONFIG}/templates/pywal-result/", pywal = true }
```


To avoid possible security issues, this flag is **disabled** by default.

<hr>

To edit this value:
- **Config file**: `env_vars = true`
