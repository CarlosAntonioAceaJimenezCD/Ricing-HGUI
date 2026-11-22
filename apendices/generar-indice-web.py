#!/usr/bin/env python3
"""Genera archivo-web/INDICE.md a partir de los índices de cada sitio archivado."""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "archivo-web"
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

CRITERIOS = [
    "Documentación **oficial** del compositor Hyprland y su ecosistema (wiki.hypr.land).",
    "Wikis oficiales de GitHub y documentación `docs/` de los repositorios de las herramientas.",
    "Sitios web oficiales de herramientas que se integran con Hyprland para ricing.",
    "Se excluyen tutoriales de terceros, foros y contenido no oficial.",
]


def main() -> None:
    sites = sorted(p for p in OUT.iterdir() if p.is_dir() and (p / "indice.md").exists())
    total = 0
    rows = []
    for s in sites:
        txt = (s / "indice.md").read_text(encoding="utf-8")
        m = re.search(r"\*\*(\d+)\*\*", txt)
        n = int(m.group(1)) if m else len(list((s / "md").glob("*.md")))
        total += n
        rows.append((s.name, n, (s / "md").is_dir()))
    lines = [
        "# Archivo web · Índice maestro", "",
        f"- Sitios archivados: **{len(sites)}**",
        f"- Páginas totales: **{total}**",
        f"- Generado: {NOW}", "",
        "## Criterios de inclusión", "",
    ]
    lines += [f"{i}. {c}" for i, c in enumerate(CRITERIOS, 1)]
    lines += ["", "## Sitios", "", "| Sitio | Páginas | Enlace |", "|---|---:|---|"]
    for name, n, has_md in rows:
        lines.append(f"| `{name}` | {n} | [índice]({name}/indice.md) |")
    lines += ["", "## Notas", "",
              "- Cada `md/*.md` lleva frontmatter con la URL original, título, fecha y conversor.",
              "- Los HTML crudos están en `raw/` dentro de cada sitio.",
              "- Los fallos de descarga se registran en `fallos.json` cuando aplica.",
              "- El cuerpo de las fuentes nunca se editó a mano: sale de `curl` + `markitdown`.",
              ""]
    (OUT / "INDICE.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Índice maestro: {len(sites)} sitios, {total} páginas")


if __name__ == "__main__":
    main()
