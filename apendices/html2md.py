#!/usr/bin/env python3
"""Convertidor HTML -> Markdown basado solo en la stdlib de Python.

Uso: python3 html2md.py archivo.html [archivo2.md ...]
Para .md/.mdx devuelve el contenido tal cual. Para HTML extrae <article>/<main>
(si existen) y convierte etiquetas basicas a Markdown. Es la herramienta de
conversion usada por build-sources.sh cuando markitdown no esta disponible.
"""
from __future__ import annotations

import html
import re
import sys
from html.parser import HTMLParser

SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "header", "form", "button"}
BLOCK = {"p", "div", "section", "article", "main", "br", "hr", "ul", "ol", "li",
         "table", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "blockquote"}


class MD(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.skip = 0
        self.in_pre = 0
        self.href: str | None = None
        self.link_buf: list[str] = []
        self.capture = 0          # 0 = indiferente, 1 = dentro de article/main
        self.preferred_seen = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag in SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in {"article", "main"}:
            if not self.preferred_seen:
                self.out.clear()
                self.preferred_seen = True
            self.capture += 1
        if tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
            self.out.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "br":
            self.out.append("\n")
        elif tag == "pre":
            self.in_pre += 1
            self.out.append("\n\n```\n")
        elif tag == "code" and not self.in_pre:
            self.out.append("`")
        elif tag == "a" and a.get("href"):
            self.href = a["href"]
            self.link_buf = []
        elif tag in BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag in {"article", "main"}:
            self.capture = max(0, self.capture - 1)
        if tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
            self.out.append("\n")
        elif tag == "pre":
            self.in_pre = max(0, self.in_pre - 1)
            self.out.append("\n```\n")
        elif tag == "code" and not self.in_pre:
            self.out.append("`")
        elif tag == "a" and self.href:
            txt = "".join(self.link_buf).strip() or self.href
            self.out.append(f"[{txt}]({self.href})")
            self.href = None
            self.link_buf = []
        elif tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        if self.href is not None:
            self.link_buf.append(data)
        txt = data if self.in_pre else re.sub(r"\s+", " ", data)
        if txt:
            self.out.append(txt)

    def result(self) -> str:
        s = "".join(self.out)
        s = re.sub(r"[ \t]+\n", "\n", s)
        s = re.sub(r"\n{3,}", "\n\n", s)
        return html.unescape(s).strip() + "\n"


def convert(path: str) -> str:
    raw = open(path, encoding="utf-8", errors="replace").read()
    if path.endswith((".md", ".mdx", ".txt")):
        return raw
    p = MD()
    p.feed(raw)
    return p.result()


if __name__ == "__main__":
    for path in sys.argv[1:]:
        sys.stdout.write(convert(path))
