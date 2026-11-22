#!/usr/bin/env python3
"""Genera sources/*.md a partir de los artefactos descargados en .staging/.

El cuerpo de cada archivo sale de una herramienta de conversion (html2md.py,
jq o pass-through para markdown); nunca se escribe a mano. La frontmatter
registra la URL original, el titulo, la fecha de descarga y el conversor.
"""
from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / ".staging"
SOURCES = ROOT / "sources"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from html2md import convert as html2md  # noqa: E402

NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

# (archivo staged, slug, titulo, url, source_type, extras)
MANIFEST = [
    ("hypr-master-tutorial.html", "hyprland-master-tutorial", "Hyprland · Master Tutorial", "https://wiki.hypr.land/getting-started/master-tutorial/", "webpage", {}),
    ("hypr-config-options.html", "hyprland-config-options", "Hyprland · Config Options", "https://wiki.hypr.land/configuring/core/config-options/", "webpage", {}),
    ("hypr-lua-utilities.html", "hyprland-lua-utilities", "Hyprland · Lua Utilities", "https://wiki.hypr.land/configuring/core/advanced-configuration/lua-utilities/", "webpage", {}),
    ("hypr-events.html", "hyprland-events", "Hyprland · Events", "https://wiki.hypr.land/configuring/core/advanced-configuration/events/", "webpage", {}),
    ("hypr-window-rules.html", "hyprland-window-rules", "Hyprland · Window Rules", "https://wiki.hypr.land/configuring/core/rules/window-rules/", "webpage", {}),
    ("hypr-binds.html", "hyprland-binds", "Hyprland · Binds", "https://wiki.hypr.land/configuring/core/binds/", "webpage", {}),
    ("hypr-performance.html", "hyprland-performance", "Hyprland · Performance", "https://wiki.hypr.land/configuring/extra/performance/", "webpage", {}),
    ("hypr-colors.html", "hyprland-colors", "Hyprland · Monitor Colors", "https://wiki.hypr.land/configuring/core/monitors/colors/", "webpage", {}),
    ("hypr-must-have.html", "hyprland-must-have", "Hyprland · Must-have utilities", "https://wiki.hypr.land/useful-utilities/must-have/", "webpage", {}),
    ("hypr-status-bars.html", "hyprland-status-bars", "Hyprland · Status Bars", "https://wiki.hypr.land/useful-utilities/status-bars/", "webpage", {}),
    ("hypr-wallpapers.html", "hyprland-wallpapers", "Hyprland · Wallpapers", "https://wiki.hypr.land/useful-utilities/wallpapers/", "webpage", {}),
    ("hypr-ecosystem-user.html", "hyprland-ecosystem-user", "Hyprland · User ecosystem (hyprpaper, hyprlock, hypridle, hyprpicker…)", "https://wiki.hypr.land/hypr-ecosystem/user/", "webpage", {}),
    ("hypr-preconfigured.html", "hyprland-preconfigured-setups", "Hyprland · Preconfigured setups", "https://wiki.hypr.land/getting-started/preconfigured-setups/", "webpage", {}),
    ("hypr-animations.html", "hyprland-animations", "Hyprland · Animations", "https://wiki.hypr.land/configuring/core/animations/", "webpage", {}),
    ("hypr-release.json", "hyprland-releases", "Hyprland · GitHub Releases (v0.56.1 – v0.57.2)", "https://github.com/hyprwm/Hyprland/releases", "report", {"author": "hyprwm", "fetcher": "curl + jq"}),
    ("noctalia-readme.md", "noctalia-readme", "Noctalia · README", "https://github.com/noctalia-dev/noctalia/blob/main/README.md", "doc", {"author": "noctalia-dev"}),
    ("noctalia-repo.json", "noctalia-repo-metadata", "Noctalia · Repositorio GitHub (metadatos)", "https://api.github.com/repos/noctalia-dev/noctalia", "report", {"fetcher": "curl + jq"}),
    ("noct-theming-index.mdx", "noctalia-theming-index", "Noctalia · Theming overview", "https://github.com/noctalia-dev/noctalia/blob/main/docs/user/theming/index.mdx", "doc", {"author": "noctalia-dev"}),
    ("noct-theming-palette.mdx", "noctalia-theming-palette", "Noctalia · Palette generation (Material You)", "https://github.com/noctalia-dev/noctalia/blob/main/docs/user/theming/palette.mdx", "doc", {"author": "noctalia-dev"}),
    ("noct-theming-app.mdx", "noctalia-app-theming", "Noctalia · App theming (GTK, Qt, terminales…)", "https://github.com/noctalia-dev/noctalia/blob/main/docs/user/theming/app-theming.mdx", "doc", {"author": "noctalia-dev"}),
    ("noct-theming-templates.mdx", "noctalia-templates", "Noctalia · Templates", "https://github.com/noctalia-dev/noctalia/blob/main/docs/user/theming/templates.mdx", "doc", {"author": "noctalia-dev"}),
    ("noct-wallpaper.mdx", "noctalia-wallpaper", "Noctalia · Wallpaper", "https://github.com/noctalia-dev/noctalia/blob/main/docs/user/desktop/wallpaper.mdx", "doc", {"author": "noctalia-dev"}),
    ("noct-hyprland.mdx", "noctalia-hyprland-integration", "Noctalia · Hyprland integration", "https://github.com/noctalia-dev/noctalia/blob/main/docs/user/compositor-settings/hyprland.mdx", "doc", {"author": "noctalia-dev"}),
    ("noct-builtin.toml", "noctalia-builtin-templates", "Noctalia · Plantillas integradas (builtin.toml)", "https://github.com/noctalia-dev/noctalia/blob/main/assets/templates/builtin.toml", "doc", {"author": "noctalia-dev"}),
    ("noct-hyprland-template.lua", "noctalia-hyprland-template", "Noctalia · Plantilla Lua para Hyprland", "https://github.com/noctalia-dev/noctalia/blob/main/assets/templates/hyprland/hyprland.lua", "doc", {"author": "noctalia-dev"}),
    ("noct-bar-index.mdx", "noctalia-bar", "Noctalia · Bar", "https://github.com/noctalia-dev/noctalia/blob/main/docs/user/bar/index.mdx", "doc", {"author": "noctalia-dev"}),
    ("arch-hyprland.html", "archwiki-hyprland", "ArchWiki · Hyprland", "https://wiki.archlinux.org/title/Hyprland", "webpage", {"author": "Arch Linux Wiki"}),
    ("nerd-fonts.html", "nerd-fonts-website", "Nerd Fonts · Sitio oficial", "https://www.nerdfonts.com/", "webpage", {}),
    ("nerd-fonts-readme.md", "nerd-fonts-readme", "Nerd Fonts · README", "https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md", "doc", {"author": "Ryan L. McMahon / Nerd Fonts contributors"}),
    ("material-color-utilities.md", "material-you-color-system", "Material Color Utilities · README (base del color dinámico de Material 3)", "https://github.com/material-foundation/material-color-utilities/blob/main/README.md", "doc", {"author": "Google / Material Foundation"}),
    ("pywal-readme.md", "pywal-readme", "pywal · README", "https://github.com/dylanaraps/pywal/blob/master/README.md", "doc", {"author": "dylanaraps"}),
    ("wallust-readme.md", "wallust-readme", "wallust · README", "https://github.com/explosion-mental/wallust/blob/master/README.md", "doc", {"author": "explosion-mental"}),
    ("matugen-readme.md", "matugen-readme", "matugen · README", "https://github.com/InioX/matugen/blob/main/README.md", "doc", {"author": "InioX"}),
    ("catppuccin-readme.md", "catppuccin-readme", "Catppuccin · README", "https://github.com/catppuccin/catppuccin/blob/main/README.md", "doc", {"author": "Catppuccin"}),
    ("waybar-readme.md", "waybar-readme", "Waybar · README", "https://github.com/Alexays/Waybar/blob/master/README.md", "doc", {"author": "Alexays"}),
    ("bibata-readme.md", "bibata-readme", "Bibata Cursor · README", "https://github.com/ful1e5/Bibata_Cursor/blob/main/README.md", "doc", {"author": "ful1e5"}),
    ("adwgtk3-readme.md", "adw-gtk3-readme", "adw-gtk3 · README", "https://github.com/lassekongo83/adw-gtk3/blob/main/README.md", "doc", {"author": "lassekongo83"}),
    ("jakoolit-readme.md", "jakoolit-hyprland-dots", "JaKooLit · Hyprland-Dots README", "https://github.com/JaKooLit/Hyprland-Dots/blob/main/README.md", "doc", {"author": "JaKooLit"}),
    ("gui-tools-metadata.json", "gui-tools-metadata", "Herramientas GUI de ricing · metadatos de GitHub", "https://api.github.com/search/repositories", "report", {"fetcher": "curl + jq"}),
    ("gui-wpgtk.md", "gui-wpgtk", "wpgtk · README (wallpaper + colorscheme + templates con GUI)", "https://github.com/deviantfero/wpgtk/blob/master/README.md", "doc", {"author": "deviantfero"}),
    ("gui-hyprmod.md", "gui-hyprmod", "hyprmod · README (settings GUI nativa para Hyprland)", "https://github.com/BlueManCZ/hyprmod/blob/main/README.md", "doc", {"author": "BlueManCZ"}),
    ("gui-waybar-configurator.md", "gui-waybar-configurator", "Waybar Configurator GUI · README", "https://github.com/veitorman/Waybar-Configurator-GUI/blob/main/README.md", "doc", {"author": "veitorman"}),
    ("gui-themix.md", "gui-themix", "Themix GUI · README (sucesor de oomox)", "https://github.com/themix-project/themix-gui/blob/master/README.md", "doc", {"author": "themix-project"}),
    ("gui-gradience.md", "gui-gradience", "Gradience · README (diseñador de temas GTK)", "https://github.com/GradienceTeam/Gradience/blob/main/README.md", "doc", {"author": "GradienceTeam"}),
    ("gui-kvantum.md", "gui-kvantum", "Kvantum · README (motor de temas Qt + manager GUI)", "https://github.com/tsujan/Kvantum/blob/master/Kvantum/README.md", "doc", {"author": "tsujan"}),
    ("gui-azote.md", "gui-azote", "Azote · README (selector de wallpaper para Wayland)", "https://github.com/nwg-piotr/azote/blob/master/README.md", "doc", {"author": "nwg-piotr"}),
    ("gui-variety.md", "gui-variety", "Variety · README (cambiador de wallpapers con GUI)", "https://github.com/varietywalls/variety/blob/master/README.md", "doc", {"author": "varietywalls"}),
    ("gui-hydrapaper.md", "gui-hydrapaper", "HydraPaper · README (wallpapers multi-monitor con GUI)", "https://github.com/GabMus/HydraPaper/blob/master/README.md", "doc", {"author": "GabMus"}),
    ("gui-hyprland-guiutils.md", "gui-hyprland-guiutils", "hyprland-guiutils · README (utilidades GUI oficiales)", "https://github.com/hyprwm/hyprland-guiutils/blob/main/README.md", "doc", {"author": "hyprwm"}),
]


MARKITDOWN = ROOT / ".tools/venv/bin/markitdown"


def body_for(name: str, source_type: str) -> str:
    src = STAGING / name
    if not src.exists():
        raise FileNotFoundError(src)
    if name.endswith(".json"):
        data = json.loads(src.read_text(encoding="utf-8"))
        if isinstance(data, list):  # releases
            lines = ["# Hyprland releases (datos crudos de la API de GitHub)\n"]
            for r in data[:12]:
                lines.append(f"## {r.get('tag_name')} · {r.get('published_at')}\n")
                lines.append(f"URL: {r.get('html_url')}\n")
                lines.append((r.get("body") or "").strip()[:4000] + "\n")
            return "\n".join(lines)
        if "tools" in data:
            lines = [f"# {data.get('source', 'GitHub API')}\n",
                     f"Consultado: {data.get('queried_at', '')}\n",
                     "| Repositorio | Estrellas | Branch | Último push | Descripción |",
                     "|---|---:|---|---|---|"]
            for t in data["tools"]:
                lines.append(f"| [{t['full_name']}]({t['url']}) | {t['stars']} | {t['default_branch']} | {t['pushed_at']} | {t['description']} |")
            return "\n".join(lines) + "\n"
        lines = [f"# {data.get('full_name', '')}\n"]
        for k in ("description", "html_url", "default_branch", "stargazers_count",
                  "forks_count", "created_at", "updated_at", "pushed_at", "language", "license"):
            lines.append(f"- **{k}**: {data.get(k)}")
        return "\n".join(lines) + "\n"
    if MARKITDOWN.exists() and not name.endswith((".md", ".mdx", ".txt")):
        proc = subprocess.run([str(MARKITDOWN), str(src)], capture_output=True,
                              text=True, timeout=180)
        if proc.returncode == 0 and len(proc.stdout.strip()) > 400:
            return proc.stdout
        print(f"AVISO markitdown fallo en {name}: {proc.stderr[:120]}")
    return html2md(str(src))


def frontmatter(title: str, url: str, source_type: str, fetcher: str, extras: dict) -> str:
    fm = ["---", "type: source", f"source_type: {source_type}", f'url: "{url}"',
          f'title: "{title}"', f"fetched_at: {NOW}", f"fetcher: {fetcher}"]
    for k in ("author", "published_date", "lang"):
        if k in extras:
            fm.append(f"{k}: \"{extras[k]}\"")
    fm.append("---")
    return "\n".join(fm) + "\n\n"


def main() -> None:
    SOURCES.mkdir(exist_ok=True)
    ok = 0
    for name, slug, title, url, stype, extras in MANIFEST:
        default_fetcher = "curl + markitdown" if MARKITDOWN.exists() else "curl + html2md.py"
        fetcher = extras.get("fetcher", default_fetcher)
        try:
            body = body_for(name, stype)
        except Exception as e:  # noqa: BLE001
            print(f"ERROR {name}: {e}")
            continue
        if len(body.strip()) < 400:
            print(f"AVISO {name}: cuerpo corto ({len(body)} chars)")
        out = SOURCES / f"{dt.date.today().isoformat()}-{slug}.md"
        out.write_text(frontmatter(title, url, stype, fetcher, extras) + body, encoding="utf-8")
        ok += 1
        print(f"OK {out.name} ({out.stat().st_size} bytes)")
    print(f"\n{ok}/{len(MANIFEST)} fuentes generadas")


if __name__ == "__main__":
    main()
