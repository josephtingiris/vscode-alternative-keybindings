# Build AlterNative Keybindings (alt-key)

You are building a VS Code extension named AlterNative Keybindings that follows the existing naming convention (brand: AlterNative, repo: vscode-alternative-keybindings, config prefix: altKey). The goal is a first-class keyboard navigation experience that enables alt+arrow and alt+h/j/k/l (VIM-style) navigation across VS Code workbench elements under varying focus conditions.

## Objectives
- Prefetch and summarize all References before designing keybindings or commands.
- Provide fast, context-aware navigation between workbench elements (Title Bar, Activity Bar, Side Bar, Panel, Editor Groups).
- Provide fast, context-aware navigation within workbench elements that support directional movement (left/right/up/down), including editor groups, side bar views, panel views (Problems/Output/Debug Console/Terminal), and other focusable views.
- Explicitly exclude elements that do not benefit from directional navigation (for example, Status Bar).

## Output locations
- Files required for the extension to function must live under extension/.
- Repo-level docs and non-extension assets go in the repository root (./).

## Core Strategy
- Prefer a comprehensive keybindings matrix (many when-clauses) over runtime logic.
- Use functions only when a single behavior can replace dozens of keybindings for a specific component.
- Avoid caching; always respond to current visibility/focus state.

## Navigation Policy
- Directional keybindings should map to:
	1) in-element navigation when supported,
	2) otherwise focus movement between visible elements.
- Prefer built-in VS Code commands for focus shifts; use more specific commands when they feel correct (for example, group focus commands when multiple editor groups are open).
- Use *Focus and *Visible contexts heavily; do not assume spatial adjacency unless VS Code exposes reliable context keys.

## Commands & Keybindings
- Require altKey.* only for core directional commands (for example, altKey.left/right/up/down).
- Other keybindings may map directly to VS Code commands where feasible.
- Command titles must be “AlterNative Keybindings: …”.
- Bind both arrow keys and H/J/K/L variants (Alt-based), with explicit when clauses.

## Logging & Diagnostics
- Log to a dedicated OutputChannel (not Debug Console).
- Configuration options:
	- altKey.logLevel: off|error|info|debug (default off)
	- altKey.logChannel: string (default AlterNative Keybindings)
	- altKey.logFile: optional path (default unset; if unset, no file logging)
- Errors should be concise and consistent. Avoid noisy UI.

## Status Bar
- Minimal, unobtrusive status bar item indicating the extension is loaded (icon + “AlterNative Keybindings”).
- Optional extras (guarded by config): last direction indicator or edge/wrap hint count.
- Keep updates throttled.

## Configuration Schema (use altKey.* prefix)
- altKey.edgeBehavior: enum bounded|wrap, default bounded.
- altKey.showStatusBar: boolean, default true.
- altKey.showEdgeNotifications: boolean, default true.
- Logging options as above.

## Package & Metadata
- name: vscode-alternative-keybindings
- displayName: AlterNative Keybindings
- description: mention alt+arrow and alt+hjkl (VIM) navigation across editors, sidebars, panels, and terminal.
- keywords: include alt, alternative, keybindings, navigation, keyboard, hjkl, alt-key.
- Icon: reference an img/icon.png placeholder (you may stub this path).
- Engines: target a recent VS Code version (1.90+ is acceptable); add dev deps for TypeScript, @types/vscode, eslint as needed.
- Keep ASCII-only and add only essential comments where logic is non-obvious.

## Deliverables
- A ready-to-build extension folder under extension/ with package.json and all other files required for implementing the features above.
- Include default keybindings and configuration schema in package.json contributes block using the altKey prefix.
- Provide a succinct README.md describing goals, default shortcuts, configuration options, etc. Mention compatibility with keyboard-only workflows and vim-style navigation.
- Provide a succinct HOWTO.md describing how to quickly install the extension in VS Code for testing and daily use.
- Provide a detailed INSTALL.md with step-by-step build and install instructions, including any prerequisites (e.g. Node.js, VS Code), build commands, and installation via VSIX or code --install-extension.
- Provide F5 debugging support in VS Code (include launch.json and any tasks needed).
- Build test framework structure for future tests (no GitHub Actions required yet).
- Keep code ASCII-only and add only essential comments where logic is non-obvious.

## Style & QA
- Follow the repo’s naming convention (AlterNative Keybindings, altKey) and avoid unrelated prefixes.
- Prefer async/await with minimal sleeps for probing; guard command executions with try/catch but keep logs informative, concise, and consistently formatted.
- Keep the status bar indicator lightweight and avoid noisy popups and unnecessary distractions. Use brief messages for edges/wraps only when enabled.

## Output
- Generate and/or modify all necessary files and content per the Output locations rules. Do not change anything in tmp/. Do not run installers. Do not commit changes. The output should be written to the workspace, not returned inline.

## References

- ./create/vscode-commands.txt (all available VS Code workbench actions; review before design)
- https://code.visualstudio.com/api/extension-capabilities/extending-workbench
- https://code.visualstudio.com/api/references/vscode-api
- https://code.visualstudio.com/api/references/commands
- https://code.visualstudio.com/api/references/when-clause-contexts
