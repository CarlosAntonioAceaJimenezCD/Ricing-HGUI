---
type: source
source_type: doc
url: "https://raw.githubusercontent.com/end-4/dots-hyprland/main/sdata/dist-fedora/README.md"
title: "Install scripts for Fedora Linux"
fetched_at: 2026-11-22T01:22:59+00:00
fetcher: "git clone (repositorio oficial)"
site: "github.com/end-4/dots-hyprland"
---
# Install scripts for Fedora Linux

Note:
- The scripts here are **not** meant to be executed directly.
- This folder should reflect the equivalents of `/sdata/dist-arch/` but under Fedora.
  - **When `/sdata/dist-arch/` is newer than this folder, an update on this folder is very likely needed.**
  - Useful link: [Commit history on sdata/dist-arch/](https://github.com/end-4/dots-hyprland/commits/main/sdata/dist-arch)
- See also [Install scripts | illogical-impulse](https://ii.clsty.link/en/dev/inst-script/)

## Contributors
- Author: [ririko6z](https://github.com/ririko6z)

## Tested
- It has been tested on Fedora Everything 44 on the `x86_64` platform.

## Post installation
- Fix the issue of the right column crashing when clicking the `Details` button in Wi-Fi mode. Edit this file: `~/.config/illogical-impulse/config.json`
- Replace `pacman` with `dnf` in update app.
```diff
@@ 44,3 44,3 @@
-  "apps": {
-    "bluetooth": "kcmshell6 kcm_bluetooth",
-    "network": "kitty -1 fish -c nmtui",
-    "update": "kitty -1 --hold=yes fish -i -c 'pkexec pacman -Syu'",

+  "apps": {
+    "bluetooth": "kcmshell6 kcm_bluetooth",
+    "network": "plasmawindowed org.kde.plasma.networkmanagement",
+    "update": "kitty -1 --hold=yes fish -i -c 'sudo dnf update -y'",
```
