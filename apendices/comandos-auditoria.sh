#!/usr/bin/env bash
# Comandos usados para auditar el sistema y reproducir el perfil.
# Ejecutar con: bash apendices/comandos-auditoria.sh
set -uo pipefail

echo "=== Sistema ==="
cat /etc/os-release
uname -a
echo "SHELL=$XDG_CURRENT_DESKTOP / $XDG_SESSION_TYPE / $WAYLAND_DISPLAY"

echo "=== Compositor ==="
hyprland --version
hyprctl monitors
hyprctl devices

echo "=== GPU / pantalla ==="
lspci | grep -iE 'vga|3d|display'

echo "=== Paquetes ==="
pacman -Q | sort
pacman -Qm            # AUR/foreign
flatpak list          # si aplica

echo "=== Config Hyprland ==="
find ~/.config/hypr -maxdepth 3 -type f -print
for f in ~/.config/hypr/hyprland.lua ~/.config/hypr/config/*.lua; do
  echo "----- $f"; cat "$f"
done

echo "=== Shell / tema ==="
cat ~/.config/noctalia/config.toml
cat ~/.config/gtk-3.0/settings.ini
cat ~/.config/gtk-3.0/noctalia.css
cat ~/.config/xsettingsd/xsettingsd.conf
cat ~/.local/share/color-schemes/noctalia.colors

echo "=== Terminales ==="
cat ~/.config/kitty/kitty.conf
cat ~/.config/kitty/themes/noctalia.conf
cat ~/.config/alacritty/alacritty.toml
cat ~/.config/alacritty/themes/noctalia.toml

echo "=== Fuentes / iconos ==="
fc-list : family | sort -u
find /usr/share/icons ~/.icons ~/.local/share/icons -maxdepth 2 -iname index.theme -print

echo "=== Servicios de usuario ==="
systemctl --user list-units --type=service --state=running
