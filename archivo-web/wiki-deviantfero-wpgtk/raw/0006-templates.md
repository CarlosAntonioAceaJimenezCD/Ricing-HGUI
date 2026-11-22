## Table of Contents

- **[What are Templates](#what-are-templates)**
- **[Default Keywords](#default-keywords)**
- **[Adding a Template](#adding-a-template)**
  - [CLI](#cli)
  - [GUI](#gui)
- **[Removing a Template](#removing-a-template)**
  - [CLI](#cli-1)
  - [GUI](#gui-1)
- **[Restore a Template](#restore-a-template)**
- **[Ignore a Template](#ignore-a-template)**


## What are Templates

In `wpgtk` templates are text files with `.base` extensions which get read,
parsed and have special keywords in them replaced, then copied over to a file
that is symlinked to the original config files, this way it is ensured that
the original files only receive already processed information and are updated 
on the fly, the base files created are stored under `$HOME/.config/wpg/templates`.

A typical template will look like this `rofi.base`

```
rofi.font:                           go mono 10
rofi.color-normal:                   {color0}, {color15}, {color0}, {active}, {color15}
rofi.color-urgent:                   {color0}, #d6b48d, #22231D, #d6b48d, {color15}
rofi.color-active:                   {color0}, {color14}, {color0}, {color14}, {color0}
rofi.color-window:                   {color0}, {active}, {inactive}
```

You can install a set of default templates with a script included with `wpgtk`
just follow this [steps](https://github.com/deviantfero/wpgtk/wiki/Installation#default-templates)

## Default Keywords

Here are the default keywords included with `wpgtk`:

```
{color0}
{color1}
...
{color15}
{active}
{inactive}
```

From version `6.0.0` onwards there are some breaking changes these from the fact that the template format will change, I provide an example below:

```
#<COLOR8>   became {color8}
#<COLORACT> became {active}
#<COLORIN>  became {inactive}

if you have normal braces {{
   you will need to escape them like this
}}

but this means you can do things like: 
{color8}                -> #ffffff
{color8.octal}          -> #77777777
{active.rgb}            -> 255, 255, 255
{userdefinedcolor.rgb}  -> 0, 0, 0
#BA{color8.strip}       -> #BAffffff
```

## Adding a Template

This will create a backup in the location specified under `filename.bak`
to avoid losing any precious data if you regret adding the file later, 
it also creates a copy of that file under `$HOME/.config/wpg/templates`
with the `.base` extension, in which you can edit and place keywords
for `wpgtk` to replace.

### CLI

```
wpg -ta ./path/to/file
```

### GUI

![img-1](https://i.imgur.com/xrjA5QZ.png)

Using the `Add` button under the Templates tab

## Remove a Template

This will remove the `.base` file from your `templates` folder, it will not
restore your backup, you'll have to do that yourself if you wish to, the config
file that remains will have the latest color-scheme applied.

### CLI
```
wpg -td basefilename.base
# you can get a list of these names with
wpg -tl
```

### GUI

After selecting the Template you wish to remove, click the `Remove` button under the Templates tab 

![img-1](https://i.imgur.com/xrjA5QZ.png)

## Restore a Template

If you're coming from a fresh install and keep your `.base` files elsewhere
you are probably gonna want them back without going through the hassle of re-adding them
so here's an easy way to re-attach this base files to their respective configuration files

```
wpg --link ./path/to/basefile.base ./path/to/config_file
```
**Note:** The `.base` file should **not** be located inside the templates directory.  
It will be automatically copied or linked

## Ignore a Template

If you don't want to delete a template but don't want to apply a new color-scheme to it
simply add a comment in the first line of the `.base` that says `wpgtk-ignore`, this way
the template remains in your added templates but is ignored in each color-scheme change,
when adding that keyword, use a format that is ignored by that configuration or text file.

## Update a Template

**_WARNING_**: don't run this on already updated files, or files that are not templates, this will change the content of the files, this flag will ignore files that don't end with `.base`.

If you're coming from a version below `6.0.0`, you might want to upgrade your custom templates to the new
format, you can do so via the flag `--update`, this flag supports blobs so you can update multiple templates at once, you can use it like this:

```sh
wpg --update /path/to/basefile.base   # for one file
wpg --update /path/to/multiple/*.base # for multiple files
```

This will replace the braces with double braces to escape them, and then change the old keyword system by the new one.

**_BEWARE_**: this will not update your own custom keywords, please surround them with `{}` instead of `<>` yourself.

If you have any default template I recommend just re-installing it via `wpg-install.sh`.