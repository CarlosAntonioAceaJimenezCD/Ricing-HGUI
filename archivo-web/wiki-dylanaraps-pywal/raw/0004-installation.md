## Table of Contents

- **[Requirements](#requirements)**
    - [Dependencies](#dependencies)
    - [Terminal Emulator](#terminal-emulator)
- **[Installation](#installation)**
    - [Pip install](#pip-install)
    - [Manual/Git install](#manualgit-install)
    - [OS/Distro Packages](#osdistro-packages)
        - [Arch Linux](#arch-linux)
        - [Nixpkgs/NixOS](#nixpkgs-nixos)
        - [Void Linux](#void-linux)
        - [Source Mage GNU/Linux](#source-mage-gnu-linux)
        - [MacOS](#MacOS)


## Requirements

### Dependencies

- `linux` or `bsd` or `macOS (iTerm2)` or `windows (no terminal support)`
- `python 3.5+`
- `imagemagick`
    - Colorscheme generation.
- `pidof` (`procps`)
    - Detection of running programs.
- `xfce`, `gnome`, `cinnamon`, `mate`
    - Desktop wallpaper setting.
- `feh`, `nitrogen`, `bgs`, `hsetroot`, `habak`, `display`
    - Universal wallpaper setting.


### Terminal Emulator

To use `wal` your terminal emulator must support a special type of escape sequence. The command below can be used as a test to see if `wal` will work with your setup.

Run the command below, does the background color of your terminal become red?

```sh
printf "%b" "\033]11;#ff0000\007"
```
**Note:** Before the test, clean your current memory's Xresources with `xrdb -remove *`. The **.Xresources** file overrides the `printf "%b" "\033]11;#ff0000\007"` command.

If your terminal's background color is now red, your terminal should work with `wal`.


**Terminals that DON'T work with `wal`.**

- Konsole. [#24](https://github.com/dylanaraps/pywal/issues/24)
- Hyper. https://github.com/vercel/hyper/issues/2038
- Terminal.app.
- Terminology. [#50](https://github.com/dylanaraps/pywal/issues/50)
- st.


## Installation

### Pip install

**System-wide install (*`sudo`*)**

```sh
sudo pip3 install pywal
```

**User install (*No `sudo`*)**

```sh
pip3 install --user pywal

# Add local 'pip' to PATH:
# (In your .bashrc, .zshrc etc)
export PATH="${PATH}:${HOME}/.local/bin/"
```


### Manual/Git install

```sh
git clone https://github.com/dylanaraps/pywal
cd pywal
pip3 install --user .

# Add local 'pip' to PATH:
# (In your .bashrc, .zshrc etc)
export PATH="${PATH}:${HOME}/.local/bin/"
```


### OS/Distro Packages

#### <a name="arch-linux"></a> Arch Linux

`pywal` is available in the Arch Linux repos as `python-pywal`.

#### <a name="nixpkgs-nixos"></a> Nixpkgs/NixOS

`pywal` is availalble in Nixpkgs as `pywal`

#### <a name="void-linux"></a> Void Linux

`pywal` is availalble in the main Void Linux repo as `pywal`

#### <a name="source-mage-gnu-linux"></a> Source Mage GNU/Linux

`pywal` is available in test grimoire as `pywal`

#### <a name="MacOS"></a> MacOS
`pywal` should be installed on MacOS with the following command

```sh
# Downloads the master release, the pip release is not functional out-of-the box for MacOS
pip install --user https://github.com/dylanaraps/pywal/archive/master.zip

#Prints your pywal installation path
pip show pywal | grep "Location"

```

Then, paste the path from above in place of the word replace below into a line of your .bashrc/.zshrc/other:

```sh
export PATH="${PATH}:REPLACE"
```

## Backends

If you want to enable alternative backends, install the supported backend via pip. To install `colorz` for example:

```
pip3 install --user colorz
```