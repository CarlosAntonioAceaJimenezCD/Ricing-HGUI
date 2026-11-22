---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/ryanoasis/nerd-fonts/Codepoint-Conflicts.md"
title: "Codepoint Conflicts"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/ryanoasis/nerd-fonts/wiki"
---
<h1 align="center">
	<img src="https://raw.githubusercontent.com/ryanoasis/nerd-fonts/HEAD/images/nerd-fonts-logo.svg?sanitize=true" alt="Nerd Fonts" />
</h1>

## Everyone wants to be at `u_F000`

* Because some iconic fonts have overlapping codepoints one of them has to "win". We move the sets as this:

| Set | Original | Nerd Fonts | gaps filled? |
|---|---|---|---|
| Devicons | `E600` | `E700` | yes |
| Font Awesome Ext | `E000` | `E200` | yes |
| Material Design | `F000` | `F500` | yes |
| Weather | `F000` | `E300` | yes |
| Octicons | `F000` | `F400` | yes |

In contrast these keep their original codepoints:
| Set | Original | Nerd Fonts | gaps filled? |
|---|---|---|---|
| Pomicons | `E000` | `E000` | no |
| Font Awesome | `F000` | `F000` | no |
| Font Logos | `F300` | `F300` | no |
| Codicons | `EA60` | `EA60` | no |
