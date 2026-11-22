---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/wiki/ryanoasis/nerd-fonts/ScriptOptions.md"
title: "ScriptOptions"
fetched_at: 2026-11-22T01:22:19+00:00
fetcher: "git clone (wiki oficial)"
site: "github.com/ryanoasis/nerd-fonts/wiki"
---
## Options of the `font-patcher` script

![](https://github.com/ryanoasis/nerd-fonts/raw/master/images/nerd-fonts-patcher-logo.png)

This explains the `font-patcher` command line options for version `v3.4.0-5 (4.20.3)`.

```
Nerd Fonts Patcher v3.5.0-16 (4.27.2) (ff 20230101)
usage: font-patcher [--careful] [--debug [{0,1,2,3}]] [--extension EXTENSION]
                    [--help] [--makegroups [{-1,0,1,2,3,4,5,6}]] [--mono]
                    [--outputdir OUTPUTDIR] [--quiet] [--single-width-glyphs]
                    [--variable-width-glyphs] [--version]
                    [--braille [{rectangle,circle,gapless}]] [--complete]
                    [--codicons] [--fontawesome] [--fontawesomeext] [--fontlogos]
                    [--material] [--octicons] [--pomicons] [--powerline]
                    [--powerlineextra] [--powersymbols] [--weather]
                    [--adjust-line-height] [--boxdrawing] [--cell CELLOPT]
                    [--configfile CONFIGFILE] [--custom CUSTOM] [--dry]
                    [--experimental EXPERIMENTAL] [--glyphdir GLYPHDIR]
                    [--has-no-italic] [--metrics {HHEA,TYPO,WIN}]
                    [--name FORCE_NAME] [--postprocess POSTPROCESS] [--removeligs]
                    [--xavgcharwidth [XAVGWIDTH]] [--progressbars | --no-progressbars]
                    font
```
Only the long form is listed here. Expand option to get full explanation.

#### positional arguments

<details><summary>
<code>  font                    </code><i>The path to the font to patch (e.g., Inconsolata.otf)</i>
</summary>
The to-be-patched font file, relative and absolute path is allowed. All font formats that <code>fontforge</code>
can open are allowed, but usually <code>.ttf</code> or <code>.otf</code> are best. Also <code>.ttc</code> is possible, but the size
savings that would be possible are not utilized.
</details>

#### options

<details><summary>
<code>  --help                  </code><i>show this help message and exit</i>
</summary>
The message is obviously not good and long enough, or you would not be looking here. Hope
you find something useful.
</details>

<details><summary>
<code>  --version               </code><i>show program's version number and exit</i>
</summary>
The detailed version is anyhow printed on every start of the <code>font-patcher</code> with Release and script versions,
so this is most useful for scripts that want to check the version rather than humans.
</details>

<details><summary>
<code>  --mono                  </code><i>Create monospaced font, existing and added glyphs are single-width (implies --single-width-glyphs)</i>
</summary>
Create a truly monospaced font (<code>Nerd Font Mono</code>)
That means that the added icons are also one (1) 'cell' wide which some people find too small.
On the other hand these fonts work with all terminals because there are no problematic glyph sizes, all fits into the cells.
<br/>
It also forces all preexisting glyphs to live in the 'standard cell', whether the preexisting glyphs fit into the cell or not.
Through this the chances are higher that the patched font will be detected as "monospaced font" by our system, and usually it is no
problem (when you patch a font that is supposed-to-be monospaced but fails the same-advance-width criterion.
<br/>
Without any option a <code>Nerd Font</code> is created: Here the symbols are typically a bit wider than one cell (1.5 widths) to make
them more readable. The 'advance width' is still one cell, so the next glyph will be printed on top of the
right half of the symbol - you need to add a blank after any icon. A lot of executables and terminals can work with this.
<br/>
See also <code>variable-width-glyphs</code>, <code>single-width-glyphs</code>
</details>

<details><summary>
<code>  --variable-width-glyphs </code><i>Do not adjust advance width (no "overhang") (Nerd Font Propo)</i>
</summary>
Create a proportional font (<code>Nerd Font Propo</code>
That means that the added icons are wider than one (1) 'cell' and really occupy that space -
their advance width is the same as the visual width. No need to add any blanks but still bigger
icons than a <code>Nerd Font Mono</code> font. This is most useful for GUI contexts instead terminal contexts.
<br/>
Without any option a <code>Nerd Font</code> is created: Here the symbols are typically a bit wider than one cell (1.5 widths) to make
them more readable. The 'advance width' is still one cell, so the next glyph will be printed on top of the
right half of the symbol - you need to add a blank after any icon. A lot of executables and terminals can work with this.
<br/>
See also <code>mono</code>
</details>

<details><summary>
<code>  --single-width-glyphs   </code><i>Whether to generate the glyphs as single-width not double-width (default is double-width) (Nerd Font Mono)</i>
</summary>
This creates a font alike <code>Nerd Font Mono</code> (the added icons are one (1) 'cell' wide, but it does not touch existing glyphs.
The font is not forced to be monospaced throughout. This is useful when you want to keep some un-proportional features from to-be-patched upstream in the created font (like certain types of ligatures), but still want to have the Nerd Font icons just one 'cell' wide.
<br/>
See also <code>mono</code>
</details>

<details><summary>
<code>  --debug [N]             </code><i>Verbose mode</i>
</summary>
The patcher can output diagnostics and details of what is does and sometimes what it guesses.
This can help in problematic cases or when you want to create an Issue report.
<br/>
Possible values are
<ul>
<li>0 = no messages (default)</li>
<li>1 = just to a logfile</li>
<li>2 = just to the console (this is also used if you just give <code>--debug</code> without number)</li>
<li>3 = log both to console and logfile</li>
</ul>
<br/>
The 'to file' option is useful when you patch more than one font and want to have the
diagnostics in one place afterwards. The file will be <code>font-patcher-log.txt</code> and be placed
where the script itself is. The lines in that file get the source font file name (which the
output to the console does not have).
</details>

<details><summary>
<code>  --quiet                 </code><i>Do not generate verbose output</i>
</summary>
Some standard output is suppressed. Usually best when you also redirect stderr to discard it (<code>... 2>/dev/null</code>).
</details>

<details><summary>
<code>  --careful               </code><i>Do not overwrite existing glyphs if detected</i>
</summary>
If a codepoint is already in use in the unpatched font it will not be replaced if you give this option.
Useful if you find that glyphs you like have been replaced after patching. On the other hand the icons
that we would have put there are then of course missing.
</details>

<details><summary>
<code>  --extension EXTENSION   </code><i>Change font file type to create (e.g., ttf, otf)</i>
</summary>
Specify the format of the generated patched font. Usually you should keep the original font's format.
</details>

<details><summary>
<code>  --outputdir OUTPUTDIR   </code><i>The directory to output the patched font file to</i>
</summary>
Normally the patched font ends up in the current working directory, but you can specify a different
relative or absolute path here. Make sure you can write to that directory.
</details>

<details><summary>
<code>  --makegroups [N]        </code><i>Use alternative method to name patched fonts</i>
</summary>
Sometimes the name of the patched font is rather long. With this option you can select a strategy to
shorten it. See the following table which component gets shorted:
<pre><code>
Original font name: Hugo Sans Mono ExtraCondensed Light Italic
                                                              NF  Family aggessive
-1  no renaming at all (keep old names and versions etc)     ---   ---   ---
 0  turned off, use old naming scheme                        [-]   [-]   [-]
 1  HugoSansMono Nerd Font ExtraCondensed Light Italic       [ ]   [ ]   [ ]
 2  HugoSansMono Nerd Font ExtCn Light Italic                [ ]   [X]   [ ]
 3  HugoSansMono Nerd Font XCn Lt It                         [ ]   [X]   [X]
 4  HugoSansMono NF ExtraCondensed Light Italic              [X]   [ ]   [ ]
 5  HugoSansMono NF ExtCn Light Italic                       [X]   [X]   [ ]
 6  HugoSansMono NF XCn Lt It                                [X]   [X]   [X]
</code></pre>
<i>Note: The 'old naming scheme' often creates broken font sets</i>
</details>

#### Symbol Fonts

<details><summary>
<code>  --complete              </code><i>Add all available Glyphs</i>
</summary>
Patch in all sets...
</details>

<details><summary>
<code>  --braille STYLE         </code><i>Add all Braille glyphs in your favorute style</i>
</summary>
Select between <code>rectangle</code>, <code>circle</code>, or <code>gapless</code>.<br/>
The <code>--complete</code> defaults to <code>rectangle</code> but you
can override this here.
</details>

<details><summary>
<code>  --codicons              </code><i>Add Codicons Glyphs</i>
</summary>
Patch in this set: <a href="https://github.com/microsoft/vscode-codicons">https://github.com/microsoft/vscode-codicons</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --fontawesome           </code><i>Add Font Awesome Glyphs</i>
</summary>
Patch in this set: <a href="http://fontawesome.io">http://fontawesome.io</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --fontawesomeext        </code><i>Add Font Awesome Extension Glyphs</i>
</summary>
Patch in this set: <a href="https://andrelzgava.github.io/font-awesome-extension">https://andrelzgava.github.io/font-awesome-extension</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --fontlogos             </code><i>Add Font Logos Glyphs</i>
</summary>
Patch in this set: <a href="https://github.com/Lukas-W/font-logos">https://github.com/Lukas-W/font-logos</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --material              </code><i>Add Material Design Icons</i>
</summary>
Patch in this set: <a href="https://github.com/templarian/MaterialDesign">https://github.com/templarian/MaterialDesign</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --octicons              </code><i>Add Octicons Glyphs</i>
</summary>
Patch in this set: <a href="https://octicons.github.com">https://octicons.github.com</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --powersymbols          </code><i>Add IEC Power Symbols</i>
</summary>
Patch in this set: <a href="https://unicodepowersymbol.com">https://unicodepowersymbol.com</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --pomicons              </code><i>Add Pomicon Glyphs</i>
</summary>
Patch in this set: <a href="https://github.com/gabrielelana/pomicons">https://github.com/gabrielelana/pomicons</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --powerline             </code><i>Add Powerline Glyphs</i>
</summary>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --powerlineextra        </code><i>Add Powerline Extra Glyphs</i>
</summary>
Patch in this set: <a href="https://github.com/ryanoasis/powerline-extra-symbols">https://github.com/ryanoasis/powerline-extra-symbols</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

<details><summary>
<code>  --weather               </code><i>Add Weather Icons</i>
</summary>
Patch in this set: <a href="https://github.com/erikflowers/weather-icons">https://github.com/erikflowers/weather-icons</a>
<br/>
See <a href="https://github.com/ryanoasis/nerd-fonts/wiki/Glyph-Sets-and-Code-Points#overview">Glyph Sets and Code Points Overview</a> for details.
</details>

#### Expert Options:

<details><summary>
<code>  --adjust-line-height    </code><i>Whether to adjust line heights (attempt to center powerline separators more evenly)</i>
</summary>
If the determined cell height is odd in design units it will be coerced to a even number by adding 1. Well, one design
unit is usually 1/500th to 1/2000th of the full height, so you will hardly ever see any difference.
Probably this option in completely useless and is only kept for historic reasons.
</details>

<details><summary>
<code>  --boxdrawing            </code><i>Force patching in (over existing) box drawing glyphs</i>
</summary>
The box drawing glyphs (<code>2500</code> - <code>259f</code> are <b>not</b> patched in if the original font already has all
of these. If only a subset exists the exiting glyphs are replaced by the Nerd Fonts Box set
to get the same style for all Box glyphs.
<br/>
In some cases (e.g. when the determined cell size differs from the originally intended one) it can
be better to do patch the Nerd Fonts Box set in, even if a complete set is already existing.
</details>

<details><summary>
<code>  --cell CELLOPT          </code><i>Adjust or query the cell size, e.g. use <code>0:1000:-200:800</code> or <code>"?"</code></i>
</summary>
With this option you can specify/force the size of the 'cell' in case the automatic detection is not optimal. Give 4 numbers separated by colons like <code>0:1000:-200:800</code> where the values are X-min, X-max, Y-min, Y-max in EM-units.
<br>
You can also query the autodetected cell size of a certain font by passing just a question mark as <code>CELLOPT</code>. If your shell tries to interpret the <code>?</code> you might need to quote or escape it.
</details>

<details><summary>
<code>  --configfile FILE       </code><i>Specify a file path for JSON configuration file (see sample: src/config.sample.json)</i>
</summary>
The patching process can be influenced by a configuration file. At the moment that is only used for <code>--removeligs</code>.
</details>

<details><summary>
<code>  --custom CUSTOM         </code><i>Specify a custom symbol font, all glyphs will be copied; absolute path suggested</i>
</summary>
If you have a font with some few glyphs that you want to patch in, this is the option for that.
Usually the custom symbol font needs to be specifically crafted for your purpose.
<br/>
The scaling and other details can not be influenced.
</details>

<details><summary>
<code>  --dry                   </code><i>Do neither patch nor store the font, to check naming</i>
</summary>
This generated most of the warning messages a real run would without producing any file.
</details>

<details><summary>
<code>  --experimental OPTION   </code><i>Enable an experimental / unstable feature</i>
</summary>
Some options are so special or obscure that we do not know yet if we want to keep them.
These are hidden here. Try <code>--experimental help</code> to see all currently available
experiments. The description points you to a pull request (PR) where that feature is
discussed.<br/>
Note that the options might be dropped without notice in the future.
</details>

<details><summary>
<code>  --glyphdir GLYPHDIR     </code><i>Path to glyphs to be used for patching</i>
</summary>
The icon set font files are expected to be in some specific directory relative to the script file.
When the files reside somewhere else you can specify the path to them here. This is very seldom useful.
</details>

<details><summary>
<code>  --has-no-italic         </code><i>Font family does not have Italic (but Oblique), to help create correct RIBBI set</i>
</summary>
The <code>font-patcher</code> tries to generate RIBBI sets of fonts. RIBBI means 'Regular Italic Bold Bold-Italic'. A lot
applications use/expect fonts to be such a set-of-four. But some fonts have (only) Oblique instead of Italic -
in that case you want a 'Regular Oblique Bold Bold-Oblique' set and need to specify this option.
</details>

<details><summary>
<code>  --metrics METRIC        </code><i>Select vertical metrics source (for problematic cases)</i>
</summary>
The baseline to baseline distance of a font can be specified in three different ways. Sometimes a source font
contradicts itself because the three metrics do not agree. The script tries then to come up with a reasonable
estimate. If that is wrong you can force another metric to be used. Use <code>--debug</code> to see the three values.
</details>

<details><summary>
<code>  --name MODE-OR-NAME     </code><i>Specify naming source ('full', 'postscript', 'filename', or concrete free name-string)</i>
</summary>
The <code>font-patcher</code> has to find out the name and the weight and style of the font. That can be challenging and the
script tries to guess which is best.
<br/>
If the naming of the patched font is unsatisfactory you can specify the naming source here (the FullName,
the PostscriptName, or try parsinging the filename).
<br/>
If all fails you can specify a free string here that is used as naming source and parsed. That name is best given in Postscript style with a dash, i.e. <code>FamilyName-StyleWeight</code> (e.g. <code>MysticFont-Regular</code>). To get complete control over the naming the usual "Nerd Font" suffix is not added to the name in the free string case.
</details>

<details><summary>
<code>  --postprocess SCRIPT    </code><i>Specify a Script for Post Processing</i>
</summary>
Sometimes you want to call some helper after patching. The helper is called in a subshell with the
generated patched font file's name as argument. That had been used in the past to automatically
hint the patched font, but that should not be necessary anymore.
</details>

<details><summary>
<code>  --removeligs            </code><i>Removes ligatures specificed in configuration file (needs --configfile)</i>
</summary>
This does not automatically remove all ligatures! Instead it removes some tables from the font, which need to
be specified in a config file. Removing tables can break the font in various ways, be careful.
<br/>
This is used for prepatched fonts that are problematic because codepoints we want to patch are used in some
ligatures.
</details>

<details><summary>
<code>  --xavgcharwidth [N]     </code><i>Adjust xAvgCharWidth (optional: concrete value)</i>
</summary>
In some very rare cases the <code>xAvgCharWidth</code> is important to keep. Patching in wider icons changes this value.
<ul>
<li>If just the option is specified (without numbger) the <code>xAvgCharWidth</code> is copied over from the source</li>
<li>If a number is added that number is used as <code>xAvgCharWidth</code></li>
<li>If the number added is zero we will calculate the old style <code>xAvgCharWidth</code>, which ignores our added icons</li>
</ul>
See for example <a href="https://github.com/ryanoasis/nerd-fonts/issues/522">Issue 522</a>.
</details>

<details><summary>
<code>  --progressbars          </code><i>Show percentage completion progress bars per Glyph Set (default)</i>
</summary>
Show one progress bar per glyph set, to shorten the wait time.
</details>

<details><summary>
<code>  --no-progressbars       </code><i>Don't show percentage completion progress bars per Glyph Set</i>
</summary>
Do <b>not</b> show the progress bar but instead details for each patched-in glyph like codepoint and name.
That is a lot output.
</details>
