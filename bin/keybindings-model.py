#!/usr/bin/env python3
import json
import sys
from random import Random

# Deterministic RNG for reproducible outputs
rng = Random(0)

MODIFIERS_SINGLE = ["alt", "ctrl", "meta", "shift"]
MODIFIERS_MULTI = [
    "ctrl+alt",
    "alt+meta",
    "ctrl+alt+meta",
    "ctrl+shift+alt",
    "shift+alt+meta",
    "ctrl+shift+alt+meta",
]

KEYS = [
    "-", "=", "[", "]", ";", "'", ",", ".",
    "a", "d", "h", "j", "k", "l",
    "end", "home", "pageup", "pagedown", "left", "down", "up", "right",
]

VI_KEYS = {"h", "j", "k", "l"}
ARROW_KEYS = {"end", "home", "pageup", "pagedown", "left", "down", "up", "right"}

# Mapping groups for comments
LEFT_GROUP = {"h", "[", ";", ",", "left"}
DOWN_GROUP = {"j", "down", "pagedown"}
UP_GROUP = {"k", "up", "pageup"}
RIGHT_GROUP = {"l", "]", "'", ".", "right"}

TAG_ORDER = ["(arrow)", "(down)", "(left)", "(right)", "(up)", "(vi)"]


def hex4():
    return f"{rng.randint(0, 0xFFFF):04x}"


def tags_for(key):
    tags = []
    if key in VI_KEYS:
        tags.append("(vi)")
    if key in ARROW_KEYS:
        tags.append("(arrow)")
    if key in LEFT_GROUP:
        tags.append("(left)")
    if key in DOWN_GROUP:
        tags.append("(down)")
    if key in UP_GROUP:
        tags.append("(up)")
    if key in RIGHT_GROUP:
        tags.append("(right)")
    # Sort tags according to TAG_ORDER
    tags_sorted = [t for t in TAG_ORDER if t in tags]
    return tags_sorted


def when_for(key):
    if key in VI_KEYS:
        return "altKey.enabled && altKey.vi"
    if key in ARROW_KEYS:
        return "altKey.enabled && altKey.arrows"
    return "altKey.enabled"


def emit_record(key_str, command_str, when_str, comment_tags):
    parts = []
    parts.append("  {")
    if comment_tags:
        parts.append("    // " + " ".join(comment_tags))
    parts.append(f'    "key": "{key_str}",')
    parts.append(f'    "command": "{command_str}",')
    parts.append(f'    "when": "{when_str}"')
    parts.append("  }")
    return "\n".join(parts)


records = []

all_mods = MODIFIERS_SINGLE + MODIFIERS_MULTI

for key in KEYS:
    for mod in all_mods:
        key_str = f"{mod}+{key}"
        cmd = f"(model) {key_str} {hex4()}"
        when = when_for(key)
        tags = tags_for(key)
        # Only include comment if key belongs to at least one mapping group
        comment_tags = tags if tags else []
        records.append((key_str, cmd, when, comment_tags))

# Emit JSONC array
out_lines = []
out_lines.append("[")
for i, (k, c, w, tags) in enumerate(records):
    obj = emit_record(k, c, w, tags)
    comma = "," if i < len(records) - 1 else ""
    # Ensure comma is on same line as closing brace
    if comma:
        # append comma to last line of obj
        obj = obj + comma
    out_lines.append(obj)
out_lines.append("]")

sys.stdout.write("\n".join(out_lines) + "\n")
try:
    sys.stdout.flush()
except Exception:
    pass
