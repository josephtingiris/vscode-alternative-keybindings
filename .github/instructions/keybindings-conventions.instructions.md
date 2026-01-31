---
description: 'Keybinding directional conventions for the codebase: mapping up/right/k/l to "next" and down/left/j/h to "previous".'
applyTo: "**"
---
# Keybindings Directional Conventions

This instruction file documents the project's directional keybinding convention so it can be referenced across the codebase and contributor docs.

Rules
- Treat `up`, `k`, `right`, or `l` as the semantic direction `next`.
- Treat `down`, `j`, `left`, or `h` as the semantic direction `previous`.

Usage
- Apply these semantics when writing documentation, comments, or keybinding conditionals so readers and contributors think in terms of `next`/`previous` rather than physical arrow keys or modality-specific keys.
- Examples:
  - "Alt+Right (or `l`) — next" — use `next` in prose and comments.
  - "Alt+Down (or `j`) — previous" — use `previous` in prose and comments.

Notes
- The convention intentionally maps both arrow keys and vim-style `hjkl` to the same abstract verbs to keep docs, tests, and code consistent.
- If adding new keybindings, prefer describing their effect as `next` or `previous` in comments and docs, then list the concrete keys in examples or code.

Comment convention
- Keep comments short, imperative, and human-readable. Use this structure where practical:
  - `(hint)` — short key or mnemonic in parentheses, e.g. `(l)` or `(right)`.
  - verb phrase describing the action using semantic directions `next`/`previous`, e.g. `focus next part` or `focus previous part`.
  - optional context in parentheses (element/location), e.g. `(sidebar on left)`, or a short `when` summary in square brackets.
  - Example: `// (l) focus next part (sidebar on left) [mirrors alt+right]`

- Use `next`/`previous` in prose and comments instead of literal arrow or `hjkl` names. When necessary include concrete keys in examples or mirrored-note tags.
- Avoid long sentences; keep each comment to one concise idea so scripts and humans can parse intent quickly.
