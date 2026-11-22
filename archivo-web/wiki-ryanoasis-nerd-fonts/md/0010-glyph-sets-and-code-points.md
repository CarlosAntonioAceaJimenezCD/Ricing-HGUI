---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/ryanoasis/nerd-fonts/Glyph-Sets-and-Code-Points.md"
title: "Glyph Sets"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/ryanoasis/nerd-fonts/wiki"
---
<h1 align="center">
	<img src="https://raw.githubusercontent.com/ryanoasis/nerd-fonts/HEAD/images/nerd-fonts-logo.svg?sanitize=true" alt="Nerd Fonts" />
</h1>

:mag: :mag: You can search for glyphs easily on [NerdFonts.com][nf] via [Cheat Sheet][Cheat Sheet]

---


# Glyph Sets

_As of v3.5.0_

### Seti-UI + Custom
Based off of [Seti-UI] Icomoon with extra custom glyphs. ([on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-custom-))<br>
Code Point Ranges: `e5fa`-`e6bb`

### Devicons
An iconic font made for developers, code jedis, ninjas, HTTPsters, evangelists and nerds(sic). ([repo][vorillaz-devicons] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-dev-))<br>
Code Point Ranges: `e700`-`e958`

### Font Awesome
The iconic font and CSS toolkit. ([repo][font-awesome] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-fa-))<br>
Code Point Ranges: `ed00`-`f2ff` (with two gaps)

### Font Awesome Extension
Simple Font Awesome Extension. ([repo][font-awesome-extension] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-fae-))<br>
Code Point Ranges: `e200`-`e2a9`

### Material Design Icons
6000+ Material Design Icons from the Community. ([repo][font-material-design-icons] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-md-))<br>
Code Point Ranges: `f0001`-`f1af0`

### Weather
215 Weather Themed Icons and CSS. ([repo][font-weather] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-weather-))<br>
Code Point Ranges: `e300`-`e3e3`

### Octicons
GitHub's icons. ([repo][octicons] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-oct-))<br>
Code Point Ranges: `f400`-`f533`,`2665`,`26A1`

### Powerline Symbols
Powerline glyphs. ([on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-pl-))<br>
Code Point Ranges: `e0a0`-`e0a2`,`e0b0`-`e0b3`

### Powerline Extra Symbols
Provides extra Powerline separator glyphs and a column number glyph (CN). ([repo][ryanoasis-powerline-extra-symbols] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-ple-))<br>
Code Point Ranges: `e0a3`,`e0b4`-`e0c8`,`e0ca`,`e0cc`-`e0d7`, `2630`

### IEC Power Symbols
Adding new characters into Unicode ([website][website-iecpower] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-iec-))<br>
Code Point Ranges: `23fb`-`23fe`,`2b58`

### Font Logos
Font-logos is an icon font containing logos of popular linux distributions and other open source software. ([repo][font-linux] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-linux-))<br>
Code Point Ranges: `f300`-`f385`

### Pomicons
11 symbols for the ["Pomodoro Technique"®](https://cirillocompany.de/pages/pomodoro-technique). ([repo][gabrielelana-pomicons] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-pom-))<br>
Code Point Ranges: `e000`-`e00a`

### Codicons
The icon font for Visual Studio Code. ([repo][vscode-codicons] | [on cheat sheet](https://nerdfonts.com/cheat-sheet?q=nf-code-))<br>
Code Point Ranges: `ea60`-`ec84`

### Additional sets
These sets are automatically selected, sometimes.
* Heavy Angle Brackets (`276c`-`2771`)
* Box Drawing (`2500`-`259f`)
* Progress (`ee00` - `ee0b`)
* Braille (`2800` - `28ff`)

# Overview

The following table shows how the glyph sets are relocated to different code points.
It is sorted by Nerd Font (target) code point.

For comparison the [Private Use Areas](https://en.wikipedia.org/wiki/Unicode_block) are `e000` - `f8ff`, `f0000` - `fffff`, and `100000` - `10ffff`.

| Glyph Set | original if different | location in Nerd Font | rough area |
|---|---|---|---|
| IEC Power Symbols | - | `23fb` - `23fe` | `23` |
| Box Drawing | - | `2500` - `259f` | `25` |
| Powerline Extra | - | `2630` | `26` |
| Octicons | - | `2665` | `26` |
| Octicons | - | `26a1` | `26` |
| Heavy Angle Brackets | - | `276c` - `2771` | `27` |
| Braille | - | `2800` - `28ff` | `28` |
| IEC Power Symbols | - | `2b58` | `2b` |
| Pomicons | - | `e000` - `e00a` | `e0` |
| Powerline | - | `e0a0` - `e0a2` | `e0` |
| Powerline Extra | - | `e0a3` | `e0` |
| Powerline | - | `e0b0` - `e0b3` | `e0` |
| Powerline Extra | - | `e0b4` - `e0c8` | `e0` |
| Powerline Extra | - | `e0ca` | `e0` |
| Powerline Extra | - | `e0cc` - `e0d7` | `e0` |
| Font Awesome Extension | `e000` - `e0a9` | `e200` - `e2a9` | `e2` |
| Weather Icons | `f000` - `f0eb` `*` | `e300` - `e3e3` | `e3` |
| Seti-UI + Custom | - | `e5fa` - `e6bb` | `e6` |
| Devicons | relocated | `e700` - `e958` | `e7` - `e8` |
| Codicons | - | `ea60` - `ec84` | `ea` - `ec` |
| Font Awesome | relocated | `ed00` - `efce` `**` | `ed` - `ef` |
| Progress | - | `ee00` - `ee0b` | `ee` |
| Font Awesome | relocated | `f000` - `f2ff` | `f0` - `f2` |
| Font Logos | - | `f300` - `f384` | `f3` |
| Octicons | `f000` - `f305` `*` | `f400` - `f533` | `f4` - `f5` |
| ~Material Design~ | `f001` - `f847` | `f500` - `fd46` | `f5` - `fd` |
| Material Design | - | `f0001`-`f1af0` | `f00` - `f10` |


_`*`: Original has unused codepoints in the range that we remove._

_`**`: Codepoints `EE00` to `EE0B` are not used, they are occupied by the progress indicators._

> [!TIP]
> `less` users: read [this message](https://github.com/ryanoasis/nerd-fonts/wiki/FAQ-and-Troubleshooting#less-settings) about codepoints and the `LESSUTFCHARDEF` variable.
(And update `LESSUTFCHARDEF`'s value when the codepoints change.)

<!--
Repo References
-->

[vim-devicons]:https://github.com/ryanoasis/vim-devicons "VimDevIcons Vim Plugin (external link) ➶"
[vorillaz-devicons]:https://vorillaz.github.io/devicons/
[font-awesome]:https://github.com/FortAwesome/Font-Awesome
[font-awesome-extension]:https://github.com/AndreLZGava/font-awesome-extension
[font-material-design-icons]:https://github.com/Templarian/MaterialDesign
[font-weather]:https://github.com/erikflowers/weather-icons
[octicons]:https://github.com/primer/octicons
[font-linux]:https://github.com/Lukas-W/font-logos
[gabrielelana-pomicons]:https://github.com/gabrielelana/pomicons
[vscode-codicons]:https://github.com/microsoft/vscode-codicons
[Seti-UI]:https://atom.io/themes/seti-ui
[ryanoasis-powerline-extra-symbols]:https://github.com/ryanoasis/powerline-extra-symbols
[wiki]:https://github.com/ryanoasis/nerd-fonts/wiki
[wiki-project-purpose]:https://github.com/ryanoasis/nerd-fonts/wiki/Project-Purpose
[repo]:https://github.com/ryanoasis/nerd-fonts
[gitter]:https://gitter.im/ryanoasis/nerd-fonts
[code-climate]:https://codeclimate.com/github/ryanoasis/nerd-fonts

<!--
Website References
-->

[website-iecpower]:https://unicodepowersymbol.com/
[nf]:https://nerdfonts.com
[Cheat Sheet]:https://nerdfonts.com/cheat-sheet
[stickers]:https://www.redbubble.com/people/ryanoasis/works/30764810-nerd-fonts-iconic-font-aggregator