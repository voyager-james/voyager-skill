#!/usr/bin/env python3
"""Scan customer-facing copy for dash and AI-tell signals.

Exit codes: 0 = clean, 1 = violations found, 2 = usage error.
"""

import argparse
import json
import re
import sys
from pathlib import Path

EM_DASH = "—"
EN_DASH = "–"
DEFAULT_TELLS_FILE = Path(__file__).parent.parent / "references" / "ai_tells.txt"


def load_phrases(tells_file: Path) -> list[str]:
    if not tells_file.exists():
        return []
    phrases = []
    for raw in tells_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            phrases.append(line)
    return phrases


def build_phrase_regex(phrases: list[str]):
    if not phrases:
        return None
    parts = []
    for phrase in phrases:
        pattern = re.escape(phrase)
        if phrase[:1].isalnum():
            pattern = r"\b" + pattern
        if phrase[-1:].isalnum():
            pattern += r"\b"
        parts.append(pattern)
    return re.compile("(?:" + "|".join(parts) + ")", re.IGNORECASE)


def scan_file(path: Path, phrase_regex):
    violations = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as err:
        return [{"file": str(path), "line": 0, "column": 0, "type": "error",
                 "match": f"(could not read: {err})", "context": ""}]

    for line_num, line in enumerate(text.splitlines(), start=1):
        for col, char in enumerate(line, start=1):
            if char == EM_DASH:
                violations.append({"file": str(path), "line": line_num, "column": col,
                                   "type": "em-dash", "match": char, "context": line.strip()[:160]})
            elif char == EN_DASH:
                violations.append({"file": str(path), "line": line_num, "column": col,
                                   "type": "en-dash", "match": char, "context": line.strip()[:160]})
        if phrase_regex is not None:
            for match in phrase_regex.finditer(line):
                violations.append({"file": str(path), "line": line_num,
                                   "column": match.start() + 1, "type": "ai-tell",
                                   "match": match.group(0), "context": line.strip()[:160]})
    return violations


def collect_files(paths: list[str], extensions: set[str]) -> list[Path]:
    files = []
    for raw in paths:
        path = Path(raw)
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            for ext in extensions:
                files.extend(path.rglob(f"*{ext}"))
        else:
            print(f"warning: {raw} not found, skipping.", file=sys.stderr)
    return sorted({path.resolve() for path in files}, key=str)


def format_text_report(violations, files_scanned: int) -> str:
    if not violations:
        return f"OK clean. Scanned {files_scanned} file(s). No dash or AI-tell violations found."
    by_file = {}
    for violation in violations:
        by_file.setdefault(violation["file"], []).append(violation)
    lines = []
    for filename, items in by_file.items():
        lines.extend(["", filename, "=" * min(len(filename), 80)])
        for item in items:
            shown = repr(item["match"]) if item["type"] in ("em-dash", "en-dash") else item["match"]
            lines.append(f"  [{item['type'].upper()}] line {item['line']}, col {item['column']}: {shown}")
            if item["context"]:
                lines.append(f"      -> {item['context']}")
    lines.extend(["", f"{len(violations)} violation(s) across {len(by_file)} file(s). "
                       f"Scanned {files_scanned} file(s)."])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan copy for em dashes, en dashes, and AI-tell phrases."
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to scan.")
    parser.add_argument("--json", action="store_true", help="Output JSON.")
    parser.add_argument("--tells-file", type=Path, default=DEFAULT_TELLS_FILE,
                        help="Custom AI-tell phrase file.")
    parser.add_argument("--ext", default=".md,.txt,.html",
                        help="Comma-separated directory scan extensions.")
    parser.add_argument("--no-tells", action="store_true", help="Skip phrase matching.")
    args = parser.parse_args()

    phrases = [] if args.no_tells else load_phrases(args.tells_file)
    extensions = {item.strip() if item.strip().startswith(".") else "." + item.strip()
                  for item in args.ext.split(",") if item.strip()}
    files = collect_files(args.paths, extensions)
    if not files:
        print("error: no files to scan.", file=sys.stderr)
        return 2

    violations = []
    phrase_regex = build_phrase_regex(phrases)
    for path in files:
        violations.extend(scan_file(path, phrase_regex))

    if args.json:
        print(json.dumps({"files_scanned": len(files),
                          "violation_count": len(violations),
                          "clean": not violations,
                          "tells_file": None if args.no_tells else str(args.tells_file),
                          "phrases_loaded": len(phrases),
                          "violations": violations}, indent=2, ensure_ascii=False))
    else:
        print(format_text_report(violations, len(files)))
    return 0 if not violations else 1


if __name__ == "__main__":
    raise SystemExit(main())
