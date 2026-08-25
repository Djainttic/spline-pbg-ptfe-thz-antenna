#!/usr/bin/env python3
"""Audit manuscript sources for missing assets, bibliography files, and placeholders."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX_FILES = sorted((ROOT / "manuscripts").rglob("*.tex"))
PLACEHOLDERS = re.compile(
    r"\b(?:INSERT|PLACEHOLDER|TODO|TBD|00\s*/\s*00|DOI\s*to\s*be\s*added|VERSION\s*-\s*INSERT)\b",
    re.IGNORECASE,
)
GRAPHICS = re.compile(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}")
BIBLIOGRAPHY = re.compile(r"\\bibliography\{([^}]+)\}")
CITATION = re.compile(r"\\cite[a-zA-Z*]*\{([^}]+)\}")
BIB_KEY = re.compile(r"^\s*@\w+\s*\{\s*([^,]+),", re.MULTILINE)


def audit(tex: Path) -> list[str]:
    errors: list[str] = []
    text = tex.read_text(encoding="utf-8", errors="replace")

    for asset in GRAPHICS.findall(text):
        path = tex.parent / asset
        if not path.exists():
            errors.append(f"missing figure: {asset}")

    for bib in BIBLIOGRAPHY.findall(text):
        bib_path = tex.parent / f"{bib}.bib"
        if not bib_path.exists():
            errors.append(f"missing bibliography: {bib_path.relative_to(ROOT)}")
        else:
            keys = set(BIB_KEY.findall(bib_path.read_text(encoding="utf-8", errors="replace")))
            cited = {key.strip() for group in CITATION.findall(text) for key in group.split(",")}
            missing_keys = sorted(cited - keys)
            if missing_keys:
                errors.append(f"missing BibTeX keys: {', '.join(missing_keys)}")

    placeholders = sorted(set(PLACEHOLDERS.findall(text)))
    if placeholders:
        errors.append("production placeholders found: " + ", ".join(placeholders))
    return errors


def main() -> int:
    if not TEX_FILES:
        print("No TeX files found.", file=sys.stderr)
        return 1
    failed = False
    for tex in TEX_FILES:
        errors = audit(tex)
        if errors:
            failed = True
            print(f"FAIL {tex.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {tex.relative_to(ROOT)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
