---
description: 'Keybinding directional conventions for the codebase: mapping up/right/k/l to "next" and down/left/j/h to "previous".'
applyTo: "**"
---
# Keybindings Labeling and Documentation Instructions

When writing comments, documentation, or labels related to keybindings in this project, please follow these conventions to ensure clarity and consistency:
- Use clear and concise language that accurately describes the keybinding's function.
- Keep comments short, imperative, and human-readable. Use this structure where practical:
  - `(hint)` — short key or mnemonic in parentheses, e.g. `(l)` or `(right)`.
  - verb phrase describing the action using semantic directions `left`/`down`/`up`/`right`, e.g. `left to ...` or `up to ...`.
  - optional context in parentheses (element/location), e.g. `(sidebar on left)`
  - Example: `// (l) left to editor (sidebar on left)`
- Use `left`/`down`/`up`/`right` in prose and comments instead of literal arrow or `hjkl` names. When necessary include concrete keys in examples or mirrored-note tags.
- Avoid long sentences; keep each comment to one concise idea so scripts and humans can parse intent quickly.
- If labeling or referencing the secondary sidebar, always use "secondary sidebar" instead of "auxiliary sidebar" or other variants.

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
- If adding new keybindings, prefer describing their effect as `left`, `down`, `up`, or `right` in comments and docs, then list the concrete keys in examples or code.

# Keybinding 'when' Clause Conventions

When writing or reviewing keybinding `when` clauses, follow these conventions and guidelines to ensure consistency and clarity:
- Use the correct context keys as specified in the keybindings-expert agent prompt.md.
- Validate that all keybinding commands exist and are appropriate for the described contexts.
- Provide explanations for any changes made, referencing the relevant sections of the keybindings-expert agent prompt.md when necessary.
- Maintain proper sorting of `when` clauses according to the keybinding 'when' clause sorting conventions defined below.
- if "when" clauses are updated then the corresponding comment MUST be updated to reflect the new order
- for consistent terminology, always refer to the official VS Code docs for keybinding and context key names.

# Keybinding 'when' Clause Sorting Conventions

When sorting `when` clauses in keybinding files, adhere to the following conventions:
- "when" clauses MUST be sorted as follows:
    1) unless specified otherwise, all when clauses should be sorted alphabetically with special characters sorting before letters, i.e. !editorFocus && !terminalFocus && panelFocus
    2) user preferences for UI view placements should appear before other clauses, if they exist.  such as `config.workbench.sideBar.location` and/or `panelPosition`.
    3) by focus context, with focused contexts (e.g., `editorFocus`, `terminalFocus`) appearing before visible contexts (e.g., `editorVisible`, `terminalVisible`).
    4) by specific context keys before more general context keys.  for example, `editorTextFocus` should appear before `editorFocus`.
    5) by negative context keys before positive context keys.  for example, `!editorFocus` should appear before `editorFocus`.