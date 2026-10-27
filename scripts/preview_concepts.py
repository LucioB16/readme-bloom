#!/usr/bin/env python3
"""Render three clearly conceptual, deterministic SVG README compositions."""
from __future__ import annotations

import argparse
from html import escape
from pathlib import Path

STYLES = {
    "editorial": ("#f4f1e8", "#203d33", "#b76547"),
    "product": ("#f5f8f7", "#1a302c", "#328c75"),
    "expressive": ("#f0eef8", "#343167", "#cc7747"),
}


def render(style: str, name: str, tagline: str) -> str:
    bg, ink, accent = STYLES[style]
    if style == "product":
        art = f"""
  <rect x="740" y="140" width="390" height="230" rx="18" fill="#fff" stroke="{ink}" stroke-opacity=".2"/>
  <rect x="763" y="163" width="344" height="24" rx="6" fill="{ink}" fill-opacity=".12"/>
  <rect x="763" y="211" width="150" height="137" rx="8" fill="{accent}" fill-opacity=".22"/>
  <rect x="935" y="211" width="172" height="63" rx="8" fill="{ink}" fill-opacity=".08"/>
  <rect x="935" y="288" width="172" height="60" rx="8" fill="{ink}" fill-opacity=".06"/>
  <text x="742" y="410" font-size="13" fill="{ink}" font-family="Arial">Place an actual screenshot here</text>"""
    elif style == "expressive":
        art = f"""
  <circle cx="978" cy="245" r="140" fill="{accent}" fill-opacity=".19"/>
  <path d="M843 332 Q996 64 1141 303" stroke="{accent}" stroke-width="26" stroke-linecap="round" fill="none"/>
  <path d="M853 314 Q1012 189 1124 344" stroke="{ink}" stroke-width="5" fill="none"/>"""
    else:
        art = f"""
  <path d="M968 367 C851 304 850 190 937 151 C986 203 1005 295 968 367Z" fill="{accent}"/>
  <path d="M968 367 C1033 251 1105 205 1171 247 C1155 334 1059 368 968 367Z" fill="{ink}" fill-opacity=".25"/>"""
    family = "Georgia,serif" if style == "editorial" else "Arial,sans-serif"
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" role="img" aria-label="{escape(style)} README visual concept">
  <rect width="1200" height="520" fill="{bg}"/>
  <rect x="45" y="45" width="1110" height="430" rx="18" fill="none" stroke="{ink}" stroke-opacity=".16"/>
  <text x="90" y="110" font-family="Arial" font-size="19" letter-spacing="4" fill="{ink}">{style.upper()} / README</text>
  <text x="90" y="237" font-family="{family}" font-size="70" fill="{ink}">{escape(name[:28])}</text>
  <text x="93" y="291" font-family="Arial" font-size="23" fill="{ink}" opacity=".78">{escape(tagline[:54])}</text>
  <rect x="93" y="341" width="145" height="44" rx="22" fill="{accent}"/>
  <text x="119" y="369" font-family="Arial" font-size="18" fill="{bg}">Get started</text>
  {art}
  <text x="90" y="448" font-family="Arial" font-size="13" fill="{ink}" opacity=".60">Discussion concept only. Not a real screenshot or a finished README.</text>
</svg>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--tagline", required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true", help="Allow replacement of existing preview SVGs")
    args = parser.parse_args()
    targets = [args.out_dir / f"readme-bloom-{name}.svg" for name in STYLES]
    existing = [str(path) for path in targets if path.exists()]
    if existing and not args.overwrite:
        parser.exit(2, "Refusing to overwrite existing preview files: " + ", ".join(existing) + "\n")
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for name, target in zip(STYLES, targets):
        target.write_text(render(name, args.name, args.tagline), encoding="utf-8")
        print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
