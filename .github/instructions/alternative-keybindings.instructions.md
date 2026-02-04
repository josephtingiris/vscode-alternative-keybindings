---
description: 'VS Code keybindings labeling and documentation conventions for comments, documentation, and "when" clause sorting. Follow these guidelines to ensure clarity and consistency in keybinding-related texts across the project.'
applyTo: "**"
---
# VS Code Official Terminology Guidelines

Please constructively correct me if I use the wrong or incorrect terminology, or you suspect a contextual misunderstanding.

"Workbench" refers to the overall Visual Studio Code UI that encompasses the following UI 'components':

- Title Bar (only on Windows/Linux)
- Activity Bar
- (Primary) Side Bar
- (Secondary) Side Bar (aka Auxiliary Bar)
- Panel
- Editor Group
- Status Bar

The "UI components" are the individual sections of the Workbench that can be focused, shown/hidden, or rearranged.  The are sometimes referred to as "surfaces" in the VS Code documentation.  Each UI component, or surface, has its own set of context keys and commands for focusing, showing/hiding, and moving focus between them.

'Views' are another concept in VS Code that refer to specific panels or sections within the UI components.  Examples of views include the Explorer view, Search view, Source Control view, and Extensions view.  Views are contained within UI components like the a Side Bar or Panel.

When referencing VS Code features, commands, or context keys, always use the official names as defined in the [VS Code documentation](https://code.visualstudio.com/api/extension-capabilities/extending-workbench)

Always use the exact official names as defined in the VS Code documentation to avoid ambiguity.

# Directional and Navigational Conventions

This instruction file documents the project's conceptual directional and navigational convention so it can be referenced across the codebase and contributor docs.  The purpose of the following rules is to establish a consistent, deterministic mental model for people reasoning about simple directional navigation among the VS Code Workbench UI components.  It should serve as a decision tree for deciding where to navigate when a directional keybinding is applied to a layout of the Workbench.

Rules
- Forward navigation is always left-to-right, top-to-bottom.
- Backward navigation is always right-to-left, bottom-to-top.
- Treat `up`, `k`, `right`, or `l` as the semantic direction `next`.
- Treat `down`, `j`, `left`, or `h` as the semantic direction `previous`.
- When faced with a navigation decision, if going right or up then navigate to the "next" ui component that is to the right or 'on top'.  when going left or down then navigate to the "previous" ui component that is to the left or 'on bottom'.  Conceptually this is like navigating 'around' a grid 'forward' from left-to-right, top-to-bottom and 'backward' from right-to-left, bottom-to-top.  It ultimately allows for focusing into every component in a predictable order by going either 'forward' or 'backward'.
- Workbench UI navigation centers around the Editor Group as the primary focus area.
- The Editor Group is always considered the "center" of navigation.  The other UI Components are positioned relative to the Editor Group.
- The Primary Side Bar MUST be on the Left or Right of the Editor Group.
- The Activity Bar is always WITHIN the Primary Side Bar and MAY be oriented on the Top, Bottom, Left, or Right of the Primary Side Bar.
- The Panel MAY be positioned on the Top, Bottom, Left, or Right of the Editor Group and always appears ADJACENT to the Editor Group.
- The Panel is the ONLY workbench UI component that MAY be positioned on the Top or Bottom of the Editor Group.
- The Secondary Side Bar (Auxiliary Bar) MAY be on the Left or Right of the Editor Group and always appears OPPOSITE the Primary Side Bar.

Notes
- The convention intentionally maps both arrow keys and vim-style `hjkl` to the same abstract verbs to keep docs, tests, and code consistent.
- For the purposes of intuitive, useful, or ifluid keyboard navigation, it seems unlikely there would be a fluent use case for navigating diagonally across the Workbench (e.g., from Primary Side Bar directly to Panel) or 'over' certain UI components such as the Activity Bar or Status Bar.  Therefore, in the interest of fluency and continuity, angle vectors and/or certain UI components MAY and probably SHOULD be avoided, skipped, or noop'ed when navigating. Is it better to stop navigation at the edge of the Workbench or to skip over certain UI components to maintain fluidity?  This is a design decision that should be made on a case-by-case basis considering usability and user experience.
- The concept and actions for 'wrap' navigation should be included in the design considerations for and implementation of keyboard navigation.  For example, when navigating right from the Panel on the Right side of the Editor Group, should the navigation wrap around to the Primary Side Bar on the Left side of the Editor Group?  This is a user preference that should be considered on a case-by-case 'edge' keybinding basis.  The overall goal is to be able to support a configuration simply enabling or disabling wrap navigation.
- The resuling keybindings should be able to be 'mirrored' for left/right and/or top/bottom configurations.  For example, if the Primary Side Bar is on the Right side of the Editor Group, then the 'next' and 'previous' keybindings should be reversed accordingly to maintain consistent directional navigation.
- Handedness is a visual/layout preference that specifically references the position of the Primary Side Bar.  By default, the Primary Side Bar is on the left hand side of the Editor Group and is considered 'left-handed' layout.  If the Primary Side Bar is moved to the right hand side of the Editor Group, then it is considered 'right-handed' layout.  This preference should be considered when designing and implementing directional navigation keybindings to ensure they feel natural and intuitive for both left-handed and right-handed layouts.  Essentially, the 'next' and 'previous' navigation keybindings should adapt based on the handedness of the layout to maintain a consistent user experience.
- The Side Bars (Primary and Secondary) are conceptually grouped together as 'side' components of the Workbench. VS Code does not offer a method to place them on on the Top or Borrom of the Editor Group.  They are always oriented vertically on either side of the Editor Group.  Therefore, when navigating 'up' or 'down', it may make sense to only focus on navigating Up and Down between the Editor Group and the Panel (if the Panel is Positioned on the Top or Bottom of the Editor Group). And, within the Editor Group itself when there are splits or multiple editor views and/or groups.  Navigating 'up' or 'down' into the Side Bars may be unintuitive since they are not vertically aligned with the Editor Group.  As well, some Side Bar views (such as the Explorer) have their own, native Up/Down navigation bindings that should be preserved. This is a design consideration that should be evaluated based on usability and user experience.

# Keybindings Labeling, Commenting, and Documentation Instructions

When writing comments, documentation, or labels related to keybindings in this project, please follow these conventions to ensure clarity and consistency:
- Avoid long sentences; keep each comment to one concise idea so scripts and humans can parse intent quickly.
- Use clear and concise language that accurately describes the keybinding's function.
- Use `left`/`down`/`up`/`right` in prose and comments instead of literal arrow or `hjkl` names. When necessary include concrete keys in examples or mirrored-note tags.
- If adding new keybindings, prefer describing their effect as `left`, `down`, `up`, or `right` in comments and docs, then list the concrete keys in examples or code.
- Keep comments short, in English, and easily human-readable. Use this structure where practical:
  1) `(direction)` - if appropriate include the relative direction, e.g. `(left)`, `(down)`, `(up)`, `(right)`
  2) `(optional context or nodes)` -  in brackets, e.g. `[default]` or `[corner case]`
  3) `(english grammar phrase)` - in English, in a single sentence or pseudo-sentence, describe:
    a) the 'when' condition in a single sentence that starts with 'when', e.g. `when the primary sidebar is on left ...`
    b) the action performed, e.g. `... then focus on the editor.`
  - Example:
```
  {
    // (left) [corner case] when the primary sidebar is on the left, the focus is on the primary sidebar, and the secondary sidebar is visible then go to the secondary sidebar
    "key": "alt+h",
    "command": "workbench.action.focusAuxiliaryBar",
    "when": "config.workbench.sideBar.location == 'left' && sideBarFocus && auxiliaryBarVisible"
  },
```
- If labeling or referencing the primary sidebar, always use "primary sidebar" instead of simply "sidebar" or other variants.
- If labeling or referencing the secondary sidebar, always use "secondary sidebar" instead of "auxiliary sidebar" or other variants.

# Keybinding 'when' Clause Conventions

When writing or reviewing keybinding `when` clauses, follow these conventions and guidelines to ensure consistency and clarity:
- Use the correct context keys as specified in the keybindings-expert agent prompt.md.
- Validate that all keybinding commands exist and are appropriate for the described contexts.
- Provide explanations for any changes made, referencing the relevant sections of the keybindings-expert agent prompt.md when necessary.
- Maintain proper sorting of `when` clauses according to the keybinding 'when' clause sorting conventions defined below.
- if "when" clauses are updated then the corresponding comment MUST be updated to reflect the new order
- for consistent terminology, always refer to the official VS Code docs for keybinding and context key names.

# Keybinding 'when' Clause Sorting

This section defines a precise, deterministic algorithm to normalize and sort VS Code `when` expressions so contributors and tools always produce the same canonical form.

Summary (one-line):
- Parse the `when` expression into a boolean AST; normalize tokens; sort operands inside every `AND` node using the precedence rules below; rebuild the expression with canonical spacing and preserved parentheses.

Algorithm (implementable):
1. Parse: build an AST with nodes: AND, OR, NOT, and leaf tokens (atomic operands). Follow VS Code precedence: `&&` binds tighter than `||`.
2. Normalize tokens:
  - Trim whitespace and collapse internal multiple spaces.
  - Normalize `!` to be a prefix with no space (`!editorFocus`).
  - Compare tokens case-insensitively for sorting decisions; preserve original casing in output.
  - Treat each leaf operand as an atomic token (e.g., `config.x == 'y'` is one token).
3. Sort rule application:
  - Apply sorting only to operands of AND nodes (including ANDs inside parentheses). Do NOT reorder operands across OR (`||`) at the same level.
  - For each AND node, sort its N operands deterministically using the precedence categories below. Within the same category, use case-insensitive alphabetical order of the full token. If equal, preserve original token order as a stable tie-breaker.
4. Reconstruct:
  - Rebuild expressions using ` && ` and ` || ` with single spaces and keep parentheses that were present so semantic grouping is unchanged.
  - Do not remove parentheses even if they become redundant.
5. Idempotence: running the algorithm twice must produce the same output as running it once.

Precedence categories for sorting inside an AND (higher → lower):
1) Configuration keys: tokens that begin with `config.` (sorted alphabetically using ASCII ordering, so punctuation/special characters sort before letters). These keys indicate configuration preferences and should sort before focus/visibility keys.
2) Focus-related keys: list focus-related context keys alphabetically by base key. The sorter does not special-case negation — `!` is treated as a regular character during sorting. Within this category, order tokens using case-insensitive alphabetical order of the full token.
  This list includes common editor, input, panel, sidebar, and list focus keys:
  - `activeEditor`
  - `auxiliaryBarFocus`
  - `editorFocus`
  - `editorTextFocus`
  - `focusedView`
  - `inputFocus`
  - `listFocus`
  - `notificationFocus`
  - `panel.location`
  - `panelFocus`
  - `panelPosition`
  - `sideBarFocus`
  - `terminalFocus`
  - `textInputFocus`
  - `view.`
  - `view.<viewId>.visible`
  - `view.container.`
  - `viewContainer.`
  - `webviewFindWidgetVisible`
  - `workbench.panel.`
  - `workbench.view.`
3) Visibility-related keys: list visibility-related context keys alphabetically by base key. The sorter does not special-case negation — `!` is treated as a regular character during sorting. Within this category, order tokens using case-insensitive alphabetical order of the full token.
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
4) Other well-known or project-specific context keys: sort case-insensitively alphabetically by the full token. Do not force negated forms before non-negated forms — sorting follows standard case-insensitive lexical ordering of the full token.
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

# References

- https://code.visualstudio.com/docs
- https://code.visualstudio.com/api/references/commands
- https://code.visualstudio.com/api/extension-capabilities/extending-workbench
- https://code.visualstudio.com/api/references/when-clause-contexts
- https://code.visualstudio.com/api/references/vscode-api
- https://code.visualstudio.com/api/extension-guides/overview