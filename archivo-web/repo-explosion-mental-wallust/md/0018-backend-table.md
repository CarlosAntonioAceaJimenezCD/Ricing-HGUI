---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/explosion-mental/wallust/master/docs/parameters/backend-table.md"
title: "backend table"
fetched_at: 2026-11-22T06:33:14+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/explosion-mental/wallust"
---
| Backends  | Description |
|-----------|-------------|
**Full** | Read and return the whole image pixels (more precision, slower)
**Resized** | Resizes the image before parsing, mantaining it's aspect ratio
**Wal** | Uses image magick `convert` to generate the colors, like pywal
**Thumb** | Faster algo hardcoded to 512x512 (no ratio respected)
**FastResize** | A much faster resize algo that uses SIMD. For some reason it fails on some images where `resized` doesn't, for this reason it doesn't *replace* but rather it's a new option.
**Kmeans** | Kmeans is an algo that divides and picks pixels all around the image, giving a more diverse look.
