# VS Code AlterNative Keybindings

Make VS Code feel faster and more keyboard-first. AlterNative Keybindings provides
directional navigation with `alt` + `arrow` keys or `alt` + `hjkl`, letting you move
between editor groups, the primary/secondary side bars, the panel, and terminal panes
with predictable, ergonomic behavior.

Why use it
- Keeps hands on the keyboard — fast spatial navigation between visible workbench elements.
- Respects in-element movement (lists, trees, and editor splits) when available.
- Configurable handedness and optional wrap behavior for custom layouts.

Highlights
- alt + arrow and alt + hjkl navigation across editors, side bars, panel, and terminals.
- Right- and left-handed navigation modes and optional screen wrapping.
- Lightweight status bar indicator and optional edge notifications.

Install
- From the VS Code Marketplace (recommended) or build/install from source in `extension/`.

Basic usage
- Press `alt+left/alt+right/alt+up/alt+down` (or `alt+h/j/k/l`) to move focus between
	the nearest visible workbench surface. Movement prefers in-element navigation when applicable.

Configuration (selected)
- `altKey.enabled` (boolean): enable/disable the extension (default: `true`).
- `altKey.logLevel` (string): `off|error|info|debug` (default: `off`).
- `altKey.logChannel` (string): name of the output channel (default: `AlterNative Keybindings`).
- `altKey.logFile` (string): optional file path for log output (default: empty).
- `altKey.wrap` (boolean): allow wrap-around navigation based on handedness (default: `true`).

Support & development
- Report issues, feature requests, or contribute on the GitHub repository root.
- Developers: see [DEVELOPMENT.md](DEVELOPMENT.md) for build and
	packaging instructions.

License
- Distributed under the terms in the [LICENSE](LICENSE) file.
