---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/explosion-mental/wallust/master/tests/README.md"
title: "Tests"
fetched_at: 2026-11-22T06:33:14+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/explosion-mental/wallust"
---
# Tests

The major testing occurs with the `pywal template engine` in `template-pywal`.
Definitions of colors and other variables are inside `template/mod.rs`


The file `template-pywal`, test against the [original pywal templates](https://github.com/dylanaraps/pywal/tree/master/pywal/templates),
to avoid breaking the engine, constantly testing is needed.
