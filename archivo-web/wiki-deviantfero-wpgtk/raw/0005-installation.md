## Table of Contents

- **[Requirements](#requirements)**
    - [Dependencies](#dependencies)
- **[Installation](#installation)**
    - [Pip](#pip)
    - [Official Packages](#official-packages)
    - [Git](#git)
    - [Default Templates](#default-templates)


## Requirements

### Dependencies
* python 3.5+
* feh, or any other wallpaper setting software (optional)
* python-gobject
* Pillow (python)
* pywal (depends on imagemagick)
* xsettingsd (optional, live GTK+ reload)
* gtk-engine-murrine (optional, better looking GTK+ theme)

## Installation

### Pip
```c
sudo pip3 install wpgtk
```
### Official Packages

For an up to date list of available releases in all repositories, check [repology.](https://repology.org/project/wpgtk/versions)


| OS            | Package                                                  |
| ------------- | -------------                                            |
| Arch Linux    | `wpgtk-git`  via the AUR                                 |
| Arch Linux    | `wpgtk`  via the AUR                                     |
| Void Linux    | `wpgtk`                                                  |
| NixOS         | `wpgtk`, check the [wiki](https://nixos.wiki/wiki/Wpgtk) |


### Git
```
git clone https://github.com/deviantfero/wpgtk
cd wpgtk
sudo pip install .
```

### Default Templates
`wpgtk` works with every text file you can give to it, but to make the process easier
a script is included that will let you install default templates for most common software.
This script is called `wpg-install.sh`, and is available after the installation of `wpgtk`

```
Usage :  /usr/bin/wpg-install.sh [options] [--]

  Options:
  -h   Display this message
  -v   Display script version
  -o   Install openbox templates
  -t   Install tint2 template
  -g   Install gtk template
  -G   Install linea nord gtk template
  -i   Install icon-set
  -r   Install rofi template
  -I   Install i3 template
  -p   Install polybar template
  -b   Install bspwm template
  -d   Install dunst template
  -B   Install bpytop template
  -q   Install qtile template
  -H   Specify hash of wpgtk-templates repository to use
```

You can combine flags in this script to install several templates at the same time. These templates will be installed in their respective folders, and will work with `wpg` without any modifications; your original config files will be backed up as `filename.bak`.
