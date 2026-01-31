---
description: 'VS Code keybindings labeling and documentation conventions for comments, documentation, and "when" clause sorting. Follow these guidelines to ensure clarity and consistency in keybinding-related texts across the project.'
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

This section defines a precise, deterministic algorithm to normalize and sort VS Code `when` expressions so contributors and tools always produce the same canonical form.

Summary (one-line):
- Parse the `when` expression into a boolean AST; normalize tokens; sort operands inside every `AND` node using the precedence rules below; rebuild the expression with canonical spacing and preserved parentheses.

Algorithm (implementable):
1. Parse: build an AST with nodes: AND, OR, NOT, and leaf tokens (atomic operands). Follow VS Code precedence: `&&` binds tighter than `||`.
2. Normalize tokens:
  - Trim whitespace and collapse internal multiple spaces.
  - Normalize `!` to be a prefix with no space (`!editorFocus`).
  - Compare keys case-insensitively for sorting decisions; preserve original casing in output.
  - Treat each leaf operand as an atomic token (e.g., `config.x == 'y'` is one token).
3. Sort rule application:
  - Apply sorting only to operands of AND nodes (including ANDs inside parentheses). Do NOT reorder operands across OR (`||`) at the same level.
  - For each AND node, sort its N operands deterministically using the precedence categories below. Within the same category, use case-insensitive alphabetical order. If equal, preserve original token order as a stable tie-breaker.
4. Reconstruct:
  - Rebuild expressions using ` && ` and ` || ` with single spaces and keep parentheses that were present so semantic grouping is unchanged.
  - Do not remove parentheses even if they become redundant.
5. Idempotence: running the algorithm twice must produce the same output as running it once.

Precedence categories for sorting inside an AND (higher → lower):
1) Positional / UI placement keys: tokens that begin with any of these prefixes (sorted alphabetically using ASCII ordering, so punctuation/special characters sort before letters). These keys indicate placement or container locations in the UI and should sort before focus/visibility keys:
  - `config.workbench.sideBar.location`
  - `panel.location`
  - `panelPosition`
  - `view.`
  - `view.<viewId>.visible`
  - `view.container.`
  - `viewContainer.`
  - `workbench.panel.`
  - `workbench.view.`
2) Focus-related keys: list focus-related context keys alphabetically by base key. The sorter does not special-case negation — `!` is treated as a regular character during sorting. Within each focus-key category, order tokens using ASCII ordering so punctuation (including `!`) sorts before letters; for letter-only comparisons, sort case-insensitively.
  This list includes common editor, input, panel, sidebar, and list focus keys:
  - `activeEditor`
  - `auxiliaryBarFocus`
  - `editorFocus`
  - `editorTextFocus`
  - `focusedView`
  - `inputFocus`
  - `listFocus`
  - `notificationFocus`
  - `panelFocus`
  - `sideBarFocus`
  - `terminalFocus`
  - `textInputFocus`
  - `webviewFindWidgetVisible`
4) Visibility-related keys (negatives first):
  - `auxiliaryBarVisible`
  - `editorVisible`
  - `notificationCenterVisible`
  - `notificationToastsVisible`
  - `outline.visible`
  - `panelVisible`
  - `searchViewletVisible`
  - `sideBarVisible`
  - `terminalVisible`
  - `timeline.visible`
  - `view.<viewId>.visible`
4) Other well-known or project-specific context keys: sort case-insensitively alphabetically unless punctuation is present; punctuation and special characters (including `!`) are ordered by ASCII so they sort before letters. Do not force negated forms before non-negated forms — sorting follows ASCII/alpha rules described here.
5) Final tie-breaker: when two tokens are equivalent under the above rules, preserve the original token order as a stable tie-breaker.

Operator and grouping rules (unambiguous):
- Only reorder operands inside AND nodes. Example: in `A || B && C` (interpreted as `A || (B && C)`), reorder only inside `(B && C)`.
- Do not change OR-level grouping or merge/split OR groups.
- For explicit parentheses, apply sorting inside them but always preserve the parentheses tokens in the output.

Canonical formatting rules:
- Use single spaces around `&&` and `||`: `a && b`, `a || b`.
- Use `!` immediately adjacent to the key: `!editorFocus`.
- No extra spaces inside parentheses: `(a && b)`.
- Preserve original key casing in output, but sort case-insensitively.
- Preserve comparison operators and right-hand operands as part of the leaf token (they are not split for sorting).

Examples (input → expected canonical output):

Example 1 — simple conjunction + negation
```text
Input:  editorFocus && !terminalFocus && !editorFocus && terminalFocus
Output: !editorFocus && editorFocus && !terminalFocus && terminalFocus
```

Example 2 — positional key precedence
```text
Input:  panelFocus && config.workbench.sideBar.location == 'right' && editorFocus
Output: config.workbench.sideBar.location == 'right' && panelFocus && editorFocus
```

Example 3 — AND inside OR (only inner sorting)
```text
Input:  A || terminalFocus && !editorFocus && B
Output: A || !editorFocus && terminalFocus && B
```

Example 4 — nested parentheses
```text
Input:  (terminalFocus && editorFocus) && (!panelVisible || editorVisible)
Output: (editorFocus && terminalFocus) && (!panelVisible || editorVisible)
```

Example 5 — same key negative before positive
```text
Input:  editorFocus && !editorFocus
Output: !editorFocus && editorFocus
```

Example 6 — idempotence (already canonical)
```text
Input:  !editorFocus && editorFocus && config.workbench.sideBar.location == 'left'
Output: !editorFocus && editorFocus && config.workbench.sideBar.location == 'left'
```

Machine-checkable unit-test mapping (JSON array):
```json
[
  {"input":"editorFocus && !terminalFocus && !editorFocus && terminalFocus","expected":"!editorFocus && editorFocus && !terminalFocus && terminalFocus"},
  {"input":"panelFocus && config.workbench.sideBar.location == 'right' && editorFocus","expected":"config.workbench.sideBar.location == 'right' && panelFocus && editorFocus"},
  {"input":"A || terminalFocus && !editorFocus && B","expected":"A || !editorFocus && terminalFocus && B"},
  {"input":"(terminalFocus && editorFocus) && (!panelVisible || editorVisible)","expected":"(editorFocus && terminalFocus) && (!panelVisible || editorVisible)"},
  {"input":"editorFocus && !editorFocus","expected":"!editorFocus && editorFocus"},
  {"input":"!editorFocus && editorFocus && config.workbench.sideBar.location == 'left'","expected":"!editorFocus && editorFocus && config.workbench.sideBar.location == 'left'"}
]
```

Comment update requirement:
- When any `when` clause is changed, add or update an inline comment using this template directly above the clause or on the same line after it:
  - `// when-sorted: [YYYY-MM-DD] — reason: [brief reason or PR#]`
- Update this comment every time the clause is edited.

Implementation notes and clarifying behaviors:
- Treat a leaf token like `config.x == 'y'` as a single atomic token; sorting uses the left-most identifier when deciding category membership (e.g., `config.` prefix).
- Do not remove redundant parentheses; preserving them avoids accidental semantic shifts.
- The sorter must preserve semantic equivalence: only reorder commutative AND operands.

Questions (if your repo needs different preferences):
1. Are there extra project-specific keys that must be elevated above the precedence categories? If yes, list them and their desired rank.
2. Are any context keys case-sensitive in comparisons? If yes, list them.
3. Do you prefer removing redundant parentheses when provably unnecessary, or always preserving them? (Default: preserve.)
4. Should expressions with different comparison operators be split for sorting, or treated as a single atomic operand? (Default: single atomic operand.)

This specification is intentionally deterministic and implementable by a formatter or lint rule. If you want, I can implement a small Node/Python script that applies these rules and a test harness using the JSON test vectors above.