---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/dylanaraps/pywal/What's-different-in-pywal?.md"
title: "What's different in pywal?"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/dylanaraps/pywal/wiki"
---
This Wiki page will list the differences between both `pywal` and `wal` to clear some confusion between the versions.

**OS**

- Supports macOS (iTerm2 only)


**General**

- Faster.
- Installable.


**Code-wise**

- Written in **Python 3**.
- Has tests!
- Split into multiple smaller files.
    - Easier to maintain.
- No global variables.
- Functions are general and have a clear purpose.
- Uses template files for export formats.
    - Cleaner and faster than generating them with loops.


**Args**

- Added `-b` to set a custom background color.
    - Example `wal -i img.jpg -b "#222222"`
- Added `-R` to restore the previous colorscheme.
- Removed `-x`.
    - This arg is no longer needed as colorscheme files now map to `0-15` by default.
- Relative paths now work in arguments. (`wal -i .`, `wal -i ../img.png`)
- Removed `-t`
- Removed `-r`


**Dependencies**

- Removed `xprop` dependency.



**Export formats**

- Exports colors in `json`.
- Exports colors in `yaml`.
- Exports colors as Konsole colorschemes.
- Exports `xclock` colors.


**Other**

- Vim colorscheme moved to own repo.
    - https://github.com/dylanaraps/wal.vim
- Wallpaper is now exported in the export files.
