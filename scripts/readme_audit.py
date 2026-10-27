#!/usr/bin/env python3
"""Read-only, deterministic README hygiene check (Python stdlib only)."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HTML_IMAGE = re.compile(r"<img\b[^>]*\bsrc\s*=\s*['\"]([^'\"]+)['\"]", re.I)
HEADINGS = re.compile(r"^#{1,6}\s+(.+)$", re.M)
BADGES = re.compile(r"shields\.io|badgen\.net", re.I)


def analyze(readme: Path) -> dict:
    if not readme.is_file():
        raise FileNotFoundError(f"README not found: {readme}")
    markdown = readme.read_text(encoding="utf-8")
    root = readme.parent.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    images = IMAGE.findall(markdown)
    links = LINK.findall(markdown)

    if not re.search(r"^#\s+\S", markdown, re.M):
        warnings.append("Missing a clear H1 project title.")
    if len(HEADINGS.findall(markdown)) > 1 and not re.search(
        r"^#{1,2}\s+(?:installation|quick\s*start|getting\s*started|usage|instalaci[oó]n|uso)\b",
        markdown, re.M | re.I,
    ):
        warnings.append("Check whether an installation/usage/quickstart section is needed.")
    if len(BADGES.findall(markdown)) > 6:
        warnings.append("Badge-heavy README: review whether each badge helps users.")
    if re.search(r"\b(?:TODO|TBD|lorem ipsum|your[- ]project[- ]name|enter[- ]project)\b", markdown, re.I):
        warnings.append("Potential placeholder content found; verify before publication.")
    if len(re.findall(r"^\s*`{3,}", markdown, re.M)) % 2:
        errors.append("Uneven number of fenced Markdown code blocks.")
    if not images and not HTML_IMAGE.search(markdown):
        warnings.append("No inline images; authentic screenshots or diagrams may help if appropriate.")

    for alt, _ in images:
        if not alt.strip():
            warnings.append("Markdown image with empty alt text.")

    targets = [url for _, url in images + links]
    targets += HTML_IMAGE.findall(markdown)
    for target in targets:
        target = target.strip().split(" ", 1)[0].strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith(("#", "//", "mailto:", "data:")):
            continue
        candidate_raw = unquote(parsed.path)
        if not candidate_raw:
            continue
        candidate = Path(candidate_raw)
        if candidate.is_absolute():
            warnings.append(f"Absolute local path in README: {target}")
            continue
        resolved = (root / candidate).resolve()
        if not resolved.is_relative_to(root):
            warnings.append(f"Relative link escapes README directory: {target}")
            continue
        if not resolved.exists():
            errors.append(f"Missing relative target: {target}")

    return {
        "file": str(readme),
        "image_count": len(images) + len(HTML_IMAGE.findall(markdown)),
        "heading_count": len(HEADINGS.findall(markdown)),
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "limitations": "Does not check external URLs, code correctness, visual rendering, dynamic GitHub links or factual claims.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", nargs="?", default="README.md", type=Path)
    parser.add_argument("--json", action="store_true", help="Machine-readable output")
    args = parser.parse_args()
    try:
        result = analyze(args.readme)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"readme_audit: {exc}\n")
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Audited: {result['file']}")
        for level in ("errors", "warnings"):
            for item in result[level]:
                print(f"{level[:-1].upper()}: {item}")
        print(result["limitations"])
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
