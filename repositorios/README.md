# Repositorios de referencia

Esta carpeta contiene clones **shallow** de proyectos usados como evidencia y
como código de ejemplo. Se excluyen de Git (ver `../.gitignore`) para no inflar
el repositorio; puedes recuperarlos cuando quieras con:

```bash
git clone --depth 1 --single-branch https://github.com/noctalia-dev/noctalia.git noctalia
git clone --depth 1 --single-branch https://github.com/end-4/dots-hyprland.git dots-hyprland
git clone --depth 1 --single-branch https://github.com/JaKooLit/Hyprland-Dots.git Hyprland-Dots
git clone --depth 1 --single-branch https://github.com/BlueManCZ/hyprmod.git hyprmod
```

| Repo | Para qué sirve en esta investigación |
|---|---|
| `noctalia` | Documentación `docs/user/theming/*`, plantillas de tema, integración Hyprland |
| `dots-hyprland` | Rice de referencia (end-4), patrones de dotfiles |
| `Hyprland-Dots` | Rice de referencia (JaKooLit), instalador y estructura |
| `hyprmod` | **código real** de una settings GUI GTK4/libadwaita para Hyprland |

> Cada repositorio conserva su propia licencia. `hyprmod` es GPL-3.0: úsalo como
> referencia de arquitectura, no como código a copiar sin atribución.
