---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/ryanoasis/nerd-fonts/Font-Substitution-&-Fallback.md"
title: "Font Substitution & Fallback"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/ryanoasis/nerd-fonts/wiki"
---
<h1 align="center">
	<img src="https://raw.githubusercontent.com/ryanoasis/nerd-fonts/HEAD/images/nerd-fonts-logo.svg?sanitize=true" alt="Nerd Fonts" />
</h1>

In general Patched Fonts are not necessary required, because several systems support [font substitution](https://en.wikipedia.org/wiki/Font_substitution) and/or [Fallback fonts](https://en.wikipedia.org/wiki/Fallback_font)


## Windows

The EUDC feature of Windows can be used to define a fall-back font that will be used for Glyphs that are not found in the current font. This means that a single Nerd Font can be installed on a Windows machine, and the Nerd Font glyphs will then be shown for all other fonts in the system without need for patching other fonts.

Info on EUDC can be found here:
https://msdn.microsoft.com/en-us/library/windows/desktop/dd317836(v=vs.85).aspx

Example usage
```
Windows Registry Editor Version 5.00
;
; More info here: https://msdn.microsoft.com/en-us/library/windows/desktop/dd317836(v=vs.85).aspx
;
[HKEY_CURRENT_USER\EUDC\1252]
"SystemDefaultEUDCFont"="Hack Nerd Font Complete Windows Compatible.ttf"
```

Adapted from @sharkusk's issue, for complete context see: https://github.com/ryanoasis/nerd-fonts/issues/159

## Linux

Leveraging Fontconfig

see: https://github.com/ryanoasis/nerd-fonts/blob/-/10-nerd-font-symbols.conf
