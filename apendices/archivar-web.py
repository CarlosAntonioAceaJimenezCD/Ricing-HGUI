#!/usr/bin/env python3
"""Archiva páginas web oficiales: descarga el HTML crudo y lo convierte a Markdown.

Uso:
  python3 archivar-web.py <slug-del-sitio> <archivo-de-urls.txt> [workers]

El archivo de URLs lleva una URL por línea (se ignoran líneas vacías y #).
Salida en archivo-web/<slug>/:
  raw/NNNN.ext    artefacto original descargado con curl
  md/NNNN-slug.md Markdown con frontmatter de proveniencia
  indice.md       índice del sitio
  fallos.json     URLs que fallaron y motivo
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "archivo-web"
MARKITDOWN = ROOT / ".tools/venv/bin/markitdown"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125 Safari/537.36"
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def slugify(url: str, i: int) -> str:
    p = urlparse(url)
    path = unquote(p.path).strip("/")
    parts = [x for x in re.split(r"[^a-zA-Z0-9]+", path) if x]
    s = "-".join(parts[-6:]).lower()[:70].strip("-")
    return f"{i:04d}-{s or p.netloc.replace('.', '-')}"


def fetch(url: str, dest: Path) -> tuple[bool, str]:
    proc = subprocess.run(
        ["curl", "-sS", "-L", "--compressed", "--max-time", "50", "-A", UA,
         url, "-o", str(dest), "-w", "%{http_code}"],
        capture_output=True, text=True,
    )
    code = proc.stdout.strip()
    size = dest.stat().st_size if dest.exists() else 0
    if proc.returncode != 0 or code != "200" or size < 200:
        return False, f"HTTP {code}, {size} bytes, curl={proc.returncode} {proc.stderr[:100]}"
    return True, ""


def title_from(raw: Path, url: str) -> str:
    txt = raw.read_text(encoding="utf-8", errors="replace")[:20000]
    m = re.search(r"<title[^>]*>(.*?)</title>", txt, re.I | re.S)
    if m:
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip()[:140]
    m = re.search(r"^#\s+(.+)$", txt, re.M)
    if m:
        return m.group(1).strip()[:140]
    return urlparse(url).path.strip("/") or urlparse(url).netloc


def convert(raw: Path, url: str) -> str:
    if raw.suffix.lower() in {".md", ".mdx", ".txt"}:
        body = raw.read_text(encoding="utf-8", errors="replace")
    else:
        proc = subprocess.run([str(MARKITDOWN), str(raw)], capture_output=True,
                              text=True, timeout=180)
        if proc.returncode != 0 or len(proc.stdout.strip()) < 100:
            return ""  # se marca como fallo de conversión
        body = proc.stdout
    title = title_from(raw, url).replace('"', "'")
    fm = [
        "---", "type: source", "source_type: webpage",
        f'url: "{url}"', f'title: "{title}"', f"fetched_at: {NOW}",
        'fetcher: "curl + markitdown"',
        f'site: "{urlparse(url).netloc}"', "---", "",
    ]
    return "\n".join(fm) + body


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    site = sys.argv[1]
    urls_file = Path(sys.argv[2])
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    urls = [u.strip() for u in urls_file.read_text(encoding="utf-8").splitlines()
            if u.strip() and not u.startswith("#")]
    site_dir = OUT / site
    raw_dir = site_dir / "raw"
    md_dir = site_dir / "md"
    raw_dir.mkdir(parents=True, exist_ok=True)
    md_dir.mkdir(parents=True, exist_ok=True)

    ok: list[tuple[str, str]] = []
    fail: list[dict[str, str]] = []

    def work(item: tuple[int, str]) -> None:
        i, url = item
        slug = slugify(url, i)
        ext = ".md" if urlparse(url).path.endswith((".md", ".mdx")) else ".html"
        raw = raw_dir / f"{slug}{ext}"
        good, err = fetch(url, raw)
        if not good:
            fail.append({"url": url, "error": err})
            return
        body = convert(raw, url)
        if not body:
            fail.append({"url": url, "error": "conversion vacia"})
            return
        out = md_dir / f"{slug}.md"
        out.write_text(body, encoding="utf-8")
        ok.append((url, out.name))

    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(work, x) for x in enumerate(urls, 1)]
        for n, f in enumerate(as_completed(futs), 1):
            f.result()
            if n % 25 == 0:
                print(f"  {site}: {n}/{len(urls)}", flush=True)

    ok.sort()
    lines = [f"# Archivo web · {site}", "",
             f"- Descargadas: **{len(ok)}**", f"- Fallidas: **{len(fail)}**",
             f"- Fecha: {NOW}", "", "| # | Página | Archivo |", "|---:|---|---|"]
    for i, (url, name) in enumerate(ok, 1):
        lines.append(f"| {i} | <{url}> | [md](md/{name}) |")
    (site_dir / "indice.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (site_dir / "fallos.json").write_text(json.dumps(fail, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{site}: OK {len(ok)} / fallos {len(fail)} -> {site_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
