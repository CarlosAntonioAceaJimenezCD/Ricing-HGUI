<h1 align="center">
	<img src="https://raw.githubusercontent.com/ryanoasis/nerd-fonts/HEAD/images/nerd-fonts-logo.svg?sanitize=true" alt="Nerd Fonts" />
</h1>


0. [What does it look like?](#what-does-it-look-like)
0. [How do I report issues?](#how-do-i-report-issues)
0. [What are all these variations?](#which-font)
0. [Which font do I want?](#which-font)
   - [TL;DR](#tldr)
   - [Explanation](#explanation)
0. [How do I use glyphs in my terminal](#how-do-i-use-glyphs-in-my-terminal)
0. [Why do the glyphs look small, squished, or not full width?](#why-do-the-glyphs-look-small-squished-or-not-full-width)
0. [Why do some of the fonts names appear incorrect or appear to have typos?](#why-do-some-of-the-fonts-names-appear-incorrect-or-appear-to-have-typos)
0. [What do these acronym variations in the font name mean: `LG`, `L`, `M`, `S`, `DZ`, `SZ`?](#what-do-these-acronym-variations-in-the-font-name-mean-lg-l-m-s-dz-sz)
0. [Why isn't my favorite font included (already patched)?](#why-isnt-my-favorite-font-included)
0. [Font patching debugging](#font-patching-debugging)
0. [Symbols not shown when I use `less`](#less-settings)

---

## What does it look like?

see [Screenshots](wiki/screenshots)

## How do I report issues? 

see: [Reporting Issues](wiki/reporting-issues)

## Which font?

### TL;DR

* Pick your font family:

  *  If you are limited to monospaced fonts (because of your terminal, etc) then pick a font with Nerd Font Mono (or NFM).
  *  If you want to have bigger icons (usually around 1.5 normal letters wide) pick a font without Mono i.e. Nerd Font (or NF). Most terminals support this, but ymmv.
  *  If you work in a proportional context (GUI elements or edit a presentation etc) pick a font with Nerd Font Propo (or NFP).

### Explanation

Once you narrow down your font choice of family (`Droid Sans`, `Inconsolata`, etc) and style (`bold`, `italic`, etc) you have 2 main choices:

#### `Option 1: Download already patched font`

For a stable version download a font package from the [release page](https://github.com/ryanoasis/nerd-fonts/releases)

#### `Option 2: Patch your own font`

Patch your own variations with the various options provided by the font patcher (e.g. not include all symbols for smaller font size)

This is the option you want if the font you use is _not_ already included or you want maximum control of what's included

## How do I use glyphs in my terminal?

```sh
echo $'\ue62b'
echo "5 digit codes: \Uf0004"
printf "or use printf instead of echo"
```

If `echo` or `printf` can do `\u` or `\U` depends on your concrete shell.

On linux you can enter unicodes directly with the key sequence `ctrl`-`shift`-`u` `f` `0` `0` `0` `4` `enter` (example for `f0004`).

## Why do the glyphs look small, squished, or not full width?

Make sure your terminal supports double-width (aka full width ambiguous characters). Some terminal emulators (such as URxvt) do not work well or at all with such characters. If this is the case you will have to use the single-width (monospace) version of a given font _or_ use a different terminal emulator.

For URxvt specific help or things to try see the wiki page [Terminal Emulators URxvt](https://github.com/ryanoasis/nerd-fonts/wiki/Terminal-Emulators#urxvt)

Issue references: [#155][issue-155], [#37][issue-37]

## Why do some of the fonts names appear incorrect or appear to have typos?

Some of the patched fonts are _intentionally_ renamed due to license restrictions to comply with SIL Open Font License (OFL). In particular the [Reserved Font Names (RFNs)](http://scripts.sil.org/cms/scripts/page.php?item_id=OFL_web_fonts_and_RFNs#14cbfd4a)

## What do these acronym variations in the font name mean: `LG`, `L`, `M`, `S`, `DZ`, `SZ`?

- LG - Line Gap
- L - Large
- M - Medium
- S - Small
- DZ - Dotted Zero
- SZ - Slashed Zero

This particularly applies to Meslo at the moment:

> Meslo has changed it’s name to Meslo LG which now includes three variants: 
small, medium and large.
>
> LG stands for Line Gap, so there’s one variant for smaller vertical line spacing, 
more towards Apple’s Menlo, a normal line gap (which equals Meslo v0.1) and 
a large gap, which is more than twice the space of Apple’s Menlo.
>
> In addition to Regular, there’s Italic, Bold and Bold Italic font styles 
included for each LG variant.

source: https://github.com/andreberg/Meslo-Font


## Why isn't my favorite font included?

It is most likely due to the font not being free _or_ due to licensing reasons which prevent distributing or distributing modified versions. 

E.g.

* [Input Mono][input-mono] (license restriction)
  * Possibly coming with external hosting :)
* [PragmataPro][pragmatapro] (not free)
* [Consolas][consolas] (proprietary)


Most fonts you can freely modify on your own so feel free to try patching them on your own :)



## Font patching debugging

### Issue

The font you patched is looking having some issues.

### Solution

1. You did take a backup of your old patched font before patching it again, didn't you?
1. Look at the output of `font-patcher` after adding `--debug 2`. Is there anything there that hints to the issue you are experiencing?
1. Copy and paste (as text) the strange icon into a [unicode to codepoint converter](https://onlinetools.com/unicode/convert-unicode-to-code-points). Then, search which font provides the glyph for that codepoint `fc-list :charset=xxxx` with `xxxx` being the 4 digit hexadecimal codepoint you found from the above. This will tell you where the glyph is coming from.
1. [nerdfix](https://github.com/loichyan/nerdfix) might be helpful. Although, fixing upstream is always better.
1. Make sure that whatever is using the glyph has updated to the same version of Nerd Fonts that you are using. If not, they might be using deprecated glyph.

## `less` settings

### Issue

You are using the pager `less` (version 633 or above) and notice that Private Use Area (PUA) characters from Nerd Fonts are not displaying.

### Solution

You can use the `LESSUTFCHARDEF` environment variable to specify the code points for PUA characters. This can be done as follows:

```bash
LESSUTFCHARDEF=e000-f8ff:p,f0001-fffff:p
```

Depending on your terminal settings some icons may be shown using 2 "cells" and for these you need to add ranges with `:w` inplace of `:p` in `LESSUTFCHARDEF`.

```bash
LESSUTFCHARDEF=e000-e09f:w,e0a0-e0bf:p,e0c0-f8ff:w,f0001-fffff:w
```

[vim-devicons]:https://github.com/ryanoasis/vim-devicons
[vorillaz-devicons]:http://vorillaz.github.io/devicons/
[font-awesome]:https://github.com/FortAwesome/Font-Awesome
[octicons]:https://github.com/github/octicons
[gabrielelana-pomicons]:https://github.com/gabrielelana/pomicons
[Seti-UI]:https://atom.io/themes/seti-ui
[ryanoasis-powerline-extra-symbols]:https://github.com/ryanoasis/powerline-extra-symbols
[consolas]:https://www.microsoft.com/typography/fonts/family.aspx?FID=300
[input-mono]:http://input.fontbureau.com/download/
[pragmatapro]:http://www.fsd.it/shop/fonts/pragmatapro/

[issue-155]:https://github.com/ryanoasis/nerd-fonts/issues/155
[issue-129]:https://github.com/ryanoasis/nerd-fonts/issues/129
[issue-129-1]:https://github.com/ryanoasis/nerd-fonts/issues/129#issuecomment-279142777
[issue-129-a]:https://github.com/fontforge/fontforge/issues/2992#issuecomment-272713810
[issue-129-b]:https://github.com/fontforge/fontforge/issues/2992#issuecomment-274091254
[issue-129-c]:https://github.com/fontforge/fontforge/pull/3046
[issue-37]:https://github.com/ryanoasis/nerd-fonts/issues/37
[issue-8]:https://github.com/ryanoasis/nerd-fonts/issues/8
[issue-8-1]:https://github.com/ryanoasis/nerd-fonts/issues/8#issuecomment-106804334