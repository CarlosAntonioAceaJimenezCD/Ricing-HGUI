---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/explosion-mental/wallust/master/docs/parameters/fallback_generator.md"
title: "Fallback Generator"
fetched_at: 2026-11-22T06:33:14+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/explosion-mental/wallust"
---
# Fallback Generator

This field chooses a method to use when the gathered colors aren't enough:

| Name | Description |
|------|-------------|
**interpolation** | (default) Tries to pick two colors and built gradients over them
**complementary** | Uses the complementary colors of two colors, or more (if needed), colors.

<hr>

To edit this value:
- **Config file**: `fallback_generator = "complementary"`
- **Cli**: `wallust run image.png --fallback-generator complementary`
