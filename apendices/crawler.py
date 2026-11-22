#!/usr/bin/env python3
"""Crawler controlado de sitios oficiales: extrae URLs internas hasta un límite.

Uso: python3 crawler.py <semilla> <salida.txt> [max_paginas] [max_profundidad]
Sólo sigue enlaces del mismo host. No sigue archivos binarios ni anclas.
"""
from __future__ import annotations

import re
import subprocess
import sys
from collections import deque
from urllib.parse import urljoin, urlparse

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125 Safari/537.36"
SKIP_EXT = re.compile(r"\.(png|jpe?g|gif|svg|ico|webp|mp4|pdf|zip|tar|gz|woff2?|ttf|css|js|json|xml)(\?|$)", re.I)


TIMEOUT = 10


def fetch(url: str) -> str:
    try:
        p = subprocess.run(["curl", "-sS", "-L", "--compressed", "--max-time", str(TIMEOUT), "-A", UA, url],
                           capture_output=True, text=True, timeout=TIMEOUT + 5)
        return p.stdout if p.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def links(html: str, base: str) -> list[str]:
    out = []
    for m in re.finditer(r'<a\s[^>]*href=["\']([^"\']+)["\']', html, re.I):
        href = m.group(1).split("#")[0].split("?")[0]
        if not href or href.startswith(("mailto:", "javascript:", "tel:", "data:")):
            continue
        if SKIP_EXT.search(href):
            continue
        out.append(urljoin(base, href))
    return out


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    seed = sys.argv[1]
    outfile = sys.argv[2]
    max_pages = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    max_depth = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    host = urlparse(seed).netloc
    seen: set[str] = set()
    q = deque([(seed, 0)])
    found: list[str] = []
    while q and len(found) < max_pages:
        url, depth = q.popleft()
        url = url.rstrip("/") or url
        if url in seen or depth > max_depth:
            continue
        seen.add(url)
        html = fetch(url)
        if not html:
            continue
        found.append(url)
        if depth < max_depth:
            for link in links(html, url):
                p = urlparse(link)
                if p.netloc == host and link not in seen and link not in [x[0] for x in q]:
                    q.append((link, depth + 1))
    with open(outfile, "w", encoding="utf-8") as f:
        f.write("\n".join(found) + "\n")
    print(f"{host}: {len(found)} URLs -> {outfile}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
