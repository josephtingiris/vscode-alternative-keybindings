#!/usr/bin/env python3
"""
(C) 2026 Joseph Tingiris (joseph.tingiris@gmail.com)

Lint comments for keybinding `key` attributes in references/keybindings.json.

Checks:
 - comment exists inside object and immediately above the "key" line
 - exactly one comment line directly above the "key" (no stacked header comments)
 - comment loosely matches the project's convention: series of `(token)` groups, then
   ` - ` then action, optional `{meta}`

Usage:
    python3 bin/keybindings-lint-comments.py [path/to/keybindings.json]

Options:
    --details    Print surrounding lines for each issue
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple


CONVENTION_RE = re.compile(r"^\s*//\s*(?:\([^\)]+\)\s*)+(?:-\s*[^\{\n]+)?(?:\s*\{[^\}]+\})?\s*$")


def usage(prog: str | None = None) -> None:
    if prog is None:
        prog = os.path.basename(sys.argv[0])
    msg = (
        f"Usage: {prog} [path/to/keybindings.json] [--details]\n\n"
        "Options:\n  --details    Print surrounding lines for each issue\n"
        "  -h, --help   Show this usage message and exit\n"
    )
    print(msg, file=sys.stderr)
    # Help/usage should exit successfully when requested
    sys.exit(0)


def find_top_level_objects(lines: List[str]) -> List[List[Tuple[int, str]]]:
    objs: List[List[Tuple[int, str]]] = []
    buf: List[Tuple[int, str]] = []
    depth = 0
    in_array = False
    for i, line in enumerate(lines):
        if not in_array and '[' in line:
            in_array = True
        opens = line.count('{')
        closes = line.count('}')
        prev_depth = depth
        depth += opens - closes
        if in_array and prev_depth == 0 and depth > 0:
            buf = [(i + 1, line)]
        elif in_array and depth > 0:
            buf.append((i + 1, line))
        elif in_array and prev_depth > 0 and depth == 0:
            objs.append(buf)
            buf = []
    return objs


def analyze_object(buf: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    issues: List[Tuple[int, str]] = []
    for idx, (ln, line) in enumerate(buf):
        if '"key"' in line:
            key_line_idx = idx
            # previous line must exist and be a single-line comment
            if key_line_idx == 0:
                issues.append((ln, 'key at start of object; no space for comment above'))
                continue
            prev_ln, prev_line = buf[key_line_idx - 1]
            if not prev_line.lstrip().startswith('//'):
                issues.append((ln, 'missing in-object comment directly above "key"'))
            else:
                if key_line_idx - 2 >= 0 and buf[key_line_idx - 2][1].lstrip().startswith('//'):
                    issues.append((prev_ln, 'multiple comment lines found directly above "key" — only one allowed'))
                if not CONVENTION_RE.match(prev_line):
                    issues.append((prev_ln, 'comment does not match convention pattern'))
    return issues


def lint(path: Path) -> List[Tuple[int, str]]:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    objs = find_top_level_objects(lines)
    all_issues: List[Tuple[int, str]] = []
    for buf in objs:
        issues = analyze_object(buf)
        all_issues.extend(issues)
    return all_issues


def parse_args() -> Tuple[Path, bool]:
    raw_argv = sys.argv[1:]
    if any(a in ('-h', '--help') for a in raw_argv):
        usage()
    parser = argparse.ArgumentParser(description='Lint keybinding comments (in-object, above "key")')
    parser.add_argument('path', nargs='?', type=Path, default=Path('references/keybindings.json'), help='Path to JSONC keybindings file')
    parser.add_argument('--details', action='store_true', help='Print surrounding lines for each issue')
    args = parser.parse_args()
    return args.path, args.details


def main() -> None:
    try:
        path, details = parse_args()
    except SystemExit:
        # argparse already printed help/usage; exit cleanly
        return

    if not path.exists():
        print(f'ERROR: file not found: {path}', file=sys.stderr)
        return

    try:
        issues = lint(path)
    except Exception as exc:
        print(f'ERROR: failed to lint {path}: {exc}', file=sys.stderr)
        return
    if not issues:
        print('OK: all checked key entries have an in-object comment directly above and match convention (heuristic)')
        return
    print(f'Found {len(issues)} issue(s):')
    for lineno, msg in issues:
        print(f' - [line {lineno}] {msg}')
        if details:
            # print a small context window
            text = path.read_text(encoding='utf-8')
            lines = text.splitlines()
            start = max(0, lineno - 3)
            end = min(len(lines), lineno + 2)
            for i in range(start, end):
                prefix = '>' if (i + 1) == lineno else ' '
                print(f'{prefix} {i+1:5d}: {lines[i]}')
            print('')
    print('\nNotes:')
    print(' - This linter is conservative and uses heuristics; it expects the JSONC layout similar to repository conventions.')
    print(' - It does not modify files (read-only).')


if __name__ == '__main__':
    main()
