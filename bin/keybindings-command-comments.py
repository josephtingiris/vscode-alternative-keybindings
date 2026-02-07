#!/usr/bin/env python3
"""
(C) 2026 Joseph Tingiris (joseph.tingiris@gmail.com)

Add placeholder command comments above each "command" in a keybindings.json.

Usage:
    python3 bin/keybindings-command-comments.py <path/to/keybindings.json>

Examples:
    python3 bin/keybindings-command-comments.py references/keybindings.json
    python3 bin/keybindings-command-comments.py --no-inplace references/keybindings.json

This script preserves surrounding comments and formatting, writes a backup
at `<path>.bak` when modifying in-place, and inserts lines like:

    // "command": "ctrl+k 1a2b"

immediately above existing `"command":` properties when a matching
placeholder is not already present.
"""
from __future__ import annotations

import argparse
import re
import uuid
from pathlib import Path
from typing import Tuple
import sys
import os

def usage(prog: str | None = None) -> None:
    if prog is None:
        prog = os.path.basename(sys.argv[0])
    msg = (
        f"Usage: {prog} <path/to/keybindings.json> [--no-inplace]\n\n"
        "Options:\n  --no-inplace    Don't write files; print to stdout\n"
        "  -h, --help      Show this usage message and exit\n"
    )
    print(msg, file=sys.stderr)
    sys.exit(1)


KEY_RE = re.compile(r'"key"\s*:\s*"([^\"]+)"')
COMMAND_RE = re.compile(r'"command"\s*:\s*"([^\"]*)"')


def make_id() -> str:
    """Return a short 4-character id suitable for placeholder comments."""
    return uuid.uuid4().hex[:4]


def add_placeholders(path: Path, inplace: bool = True) -> None:
    """Read `path`, insert missing placeholder comments, and write output.

    When `inplace` is False the resulting content is printed to stdout.
    """
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines(keepends=True)

    out: list[str] = []
    current_key: str | None = None
    in_object = False

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('{'):
            in_object = True
            current_key = None
            out.append(line)
            continue
        if in_object and stripped.startswith('}'):  # end of object
            in_object = False
            current_key = None
            out.append(line)
            continue

        if in_object:
            mkey = KEY_RE.search(line)
            if mkey:
                current_key = mkey.group(1)
                out.append(line)
                continue

            mcmd = COMMAND_RE.search(line)
            if mcmd:
                # look for the last non-blank output line to detect existing placeholder
                prev_idx = len(out) - 1
                while prev_idx >= 0 and out[prev_idx].strip() == '':
                    prev_idx -= 1

                has_placeholder = False
                if prev_idx >= 0:
                    prev_line = out[prev_idx].lstrip()
                    if prev_line.startswith('//') and '"command":' in prev_line:
                        if current_key and current_key in prev_line:
                            has_placeholder = True

                if not has_placeholder and current_key:
                    indent = line[: len(line) - len(line.lstrip())]
                    placeholder = f'{indent}// "command": "{current_key} {make_id()}"\n'
                    out.append(placeholder)

                out.append(line)
                continue

        out.append(line)

    new_content = ''.join(out)
    if inplace:
        backup = path.with_suffix(path.suffix + '.bak')
        backup.write_text(text, encoding='utf-8')
        path.write_text(new_content, encoding='utf-8')
        print(f'Wrote {path} (backup at {backup})')
    else:
        print(new_content)


def parse_args() -> Tuple[Path, bool]:
    raw_argv = sys.argv[1:]
    if any(a in ('-h', '--help') for a in raw_argv):
        usage()
    parser = argparse.ArgumentParser(
        description='Add placeholder command comments.')
    parser.add_argument('path', type=Path, help='Path to keybindings.json')
    parser.add_argument('--no-inplace', action='store_true',
                        help="Don't write files; print to stdout")
    args = parser.parse_args()
    return args.path, not args.no_inplace


def main() -> None:
    path, inplace = parse_args()
    add_placeholders(path, inplace=inplace)


if __name__ == '__main__':
    main()
