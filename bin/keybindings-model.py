#!/usr/bin/env python3
"""
(C) 2026 Joseph Tingiris (joseph.tingiris@gmail.com)

Generate a JSON array of keybinding objects.

Usage:
  ./bin/keybindings-model.py [--out PATH]

Examples:
  ./bin/keybindings-model.py
  ./bin/keybindings-model.py --out references/keybindings-model.json

Description:
  Emit a pretty-printed JSON array of keybinding objects to stdout or write
  to `--out` when specified. Each item contains `key`, `command`, and
  `when` properties. `command` is the exact `key` string followed by 4
  random hexadecimal characters.
"""
from __future__ import annotations

import argparse
import json
import secrets
import sys
from pathlib import Path
from typing import List, Set


# ---- Python version check ----
if sys.version_info < (3, 7):
    sys.stderr.write("Error: this script requires Python 3.7 or newer.\n")
    sys.exit(2)


MODIFIERS: List[str] = [
    "alt+",
    "ctrl+",
    "alt+meta+",
    "ctrl+alt+",
    "shift+alt+",
    "ctrl+alt+meta+",
    "ctrl+shift+alt+",
    "shift+alt+meta+",
    "ctrl+shift+alt+meta+",
]

KEYS: List[str] = [
    "-",
    "=",
    "[",
    "]",
    ";",
    "'",
    ",",
    ".",
    "a",
    "d",
    "h",
    "j",
    "k",
    "l",
    "end",
    "home",
    "pagedown",
    "left",
    "down",
    "up",
    "right",
]

VI_KEYS: Set[str] = {"h", "j", "k", "l"}
ARROW_KEYS: Set[str] = {"end", "home", "pagedown", "left", "down", "up", "right"}


def make_command(key_str: str) -> str:
    """Return a command string "<key> <4hex>"."""
    return f"{key_str} {secrets.token_hex(2)}"


def when_for(key: str) -> str:
    """Return the appropriate `when` clause for the base key."""
    if key in VI_KEYS:
        return "altKey.enabled && altKey.vi"
    if key in ARROW_KEYS:
        return "altKey.enabled && altKey.arrows"
    return "altKey.enabled"


def build_bindings() -> List[dict]:
    """Construct the array of keybinding objects."""
    out: List[dict] = []
    for k in KEYS:
        for mod in MODIFIERS:
            key_str = f"{mod}{k}"
            out.append({
                "key": key_str,
                "command": make_command(key_str),
                "when": when_for(k),
            })
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate keybindings JSON")
    parser.add_argument("--out", type=Path, help="Write output to path instead of stdout")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bindings = build_bindings()
    text = json.dumps(bindings, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f'Wrote {args.out}')
    else:
        print(text)


if __name__ == "__main__":
    main()
