#!/usr/bin/env python3
"""Archiva las wikis oficiales de GitHub clonadas en .wikis/.

Cada página .md se copia tal cual (es contenido oficial) y se le añade
frontmatter con la URL raw original de la wiki de GitHub.
"""
from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKIS = ROOT / ".wikis"
OUT = ROOT / "archivo-web"
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

REPOS = {
    "Alexays-Waybar": "Alexays/Waybar",
    "davatorium-rofi": "davatorium/rofi",
    "dunst-project-dunst": "dunst-project/dunst",
    "dylanaraps-pywal": "dylanaraps/pywal",
    "deviantfero-wpgtk": "deviantfero/wpgtk",
    "fastfetch-cli-fastfetch": "fastfetch-cli/fastfetch",
    "ryanoasis-nerd-fonts": "ryanoasis/nerd-fonts",
    "hyprwm-Hyprland": "hyprwm/Hyprland",
    "nwg-piotr-nwg-shell": "nwg-piotr/nwg-shell",
    "InioX-matugen": "InioX/matugen",
    "themix-project-themix-gui": "themix-project/themix-gui",
}


def slugify(s: str, i: int) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).lower().strip("-")[:70]
    return f"{i:04d}-{s or 'index'}"


def main() -> None:
    total = 0
    for dirname, repo in REPOS.items():
        src = WIKIS / dirname
        if not src.exists():
            continue
        site = f"wiki-{dirname}"
        md_dir = OUT / site / "md"
        raw_dir = OUT / site / "raw"
        md_dir.mkdir(parents=True, exist_ok=True)
        raw_dir.mkdir(parents=True, exist_ok=True)
        pages = sorted(p for p in src.rglob("*.md") if ".git" not in p.parts)
        rows = []
        for i, p in enumerate(pages, 1):
            rel = p.relative_to(src).as_posix()
            url = f"https://raw.githubusercontent.com/wiki/{repo}/{rel}"
            body = p.read_text(encoding="utf-8", errors="replace")
            if not body.strip():
                continue
            first = re.search(r"^#\s+(.+)$", body, re.M)
            title = first.group(1).strip() if first else p.stem.replace("-", " ")
            fm = [
                "---", "type: source", "source_type: doc",
                f'url: "{url}"', f'title: "{title[:140].replace(chr(34), chr(39))}"',
                f"fetched_at: {NOW}", 'fetcher: "git clone (wiki oficial)"',
                f'site: "github.com/{repo}/wiki"', "---", "",
            ]
            name = slugify(p.stem, i) + ".md"
            (md_dir / name).write_text("\n".join(fm) + body, encoding="utf-8")
            (raw_dir / name).write_text(body, encoding="utf-8")
            rows.append((url, name))
            total += 1
        lines = [f"# Wiki oficial · {repo}", "", f"- Páginas: **{len(rows)}**",
                 f"- Fecha: {NOW}", "", "| # | Página | Archivo |", "|---:|---|---|"]
        for i, (url, name) in enumerate(rows, 1):
            lines.append(f"| {i} | <{url}> | [md](md/{name}) |")
        (OUT / site / "indice.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{repo}: {len(rows)} páginas -> {site}")
    print(f"TOTAL: {total} páginas de wiki archivadas")


if __name__ == "__main__":
    main()
