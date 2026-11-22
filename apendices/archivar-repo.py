#!/usr/bin/env python3
"""Archiva toda la documentación Markdown de un repositorio oficial clonado.

Uso: python3 archivar-repo.py <dir-local> <owner/repo> <branch> <slug-sitio>
"""
from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "archivo-web"
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def main() -> int:
    if len(sys.argv) < 5:
        print(__doc__)
        return 2
    src = Path(sys.argv[1]).resolve()
    repo = sys.argv[2]
    branch = sys.argv[3]
    site = sys.argv[4]
    md_dir = OUT / site / "md"
    raw_dir = OUT / site / "raw"
    md_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)

    pages = sorted(p for p in src.rglob("*")
                   if p.is_file() and p.suffix.lower() in {".md", ".mdx"}
                   and ".git" not in p.parts and "node_modules" not in p.parts)
    rows = []
    for i, p in enumerate(pages, 1):
        rel = p.relative_to(src).as_posix()
        url = f"https://raw.githubusercontent.com/{repo}/{branch}/{rel}"
        body = p.read_text(encoding="utf-8", errors="replace")
        if not body.strip():
            continue
        first = re.search(r"^#\s+(.+)$", body, re.M)
        title = first.group(1).strip() if first else p.stem.replace("-", " ")
        fm = [
            "---", "type: source", "source_type: doc",
            f'url: "{url}"', f'title: "{title[:140].replace(chr(34), chr(39))}"',
            f"fetched_at: {NOW}", 'fetcher: "git clone (repositorio oficial)"',
            f'site: "github.com/{repo}"', "---", "",
        ]
        name = f"{i:04d}-" + re.sub(r"[^a-zA-Z0-9]+", "-", p.stem).lower().strip("-")[:60] + ".md"
        (md_dir / name).write_text("\n".join(fm) + body, encoding="utf-8")
        (raw_dir / name).write_text(body, encoding="utf-8")
        rows.append((url, name))

    lines = [f"# Documentación oficial · {repo} ({branch})", "",
             f"- Páginas: **{len(rows)}**", f"- Fecha: {NOW}", "",
             "| # | Página | Archivo |", "|---:|---|---|"]
    for i, (url, name) in enumerate(rows, 1):
        lines.append(f"| {i} | <{url}> | [md](md/{name}) |")
    (OUT / site / "indice.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{repo}: {len(rows)} páginas -> {site}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
