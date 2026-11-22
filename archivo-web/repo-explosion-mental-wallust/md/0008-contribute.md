---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/explosion-mental/wallust/master/docs/contribute.md"
title: "Contribute!"
fetched_at: 2026-11-22T06:33:14+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/explosion-mental/wallust"
---
# Contribute!
Show some of your taste by adding a [backend](./src/backends/mod.rs),
[colorspace](./src/colorspaces/mod.rs), [scheme palettes](./src/palettes/mod.rs),
and/or a [custom theme](https://codeberg.org/explosion-mental/wallust-themes).

Having design ideas or suggestios is also very welcome.


## Ideas
Some food for thought.

- `wallust init`, which will scan your system for common aplication in which
 there is an avaliable theme template at
 [wallust-templates](https://codeberg.org/explosion-mental/wallust-templates).
 If so, it will automatically fetch those templates, add it in your toml
 config and configure accorndingly. Make it interactive.

- Allow to have more than 6 (MIN_COLS) passed to `palettes`. This requires some
 comunication to be exchanged between `ColorSpace <-> Palette` modules.

- Learn more from "Material You" implementations, what I've seen is that it
  looses some colors and hues to mantain contrast.

- Pulish code on colorspaces

For more, grep the src for TODO `rg TODO`
