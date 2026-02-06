# Changelog

All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog" and uses `YYYY-mm-dd` dated headings.

## 2026-01-29

### Added
- Initial release: VS Code extension providing alt+arrow and alt+hjkl navigation across editor groups, side bars, panels, and terminals (extension/README.md, extension/).
- Command-line tooling for keybinding maintenance and transformations (bin/keybindings-evolve, bin/keybindings-merge.py, bin/keybindings-remove.py, bin/keybindings-remove-comments.py, bin/keybindings-sort.py).
- Repository-level agent and contributor guidance, project overview, and conventions (AGENTS.md, README.md).

### Documentation
- Add lightweight top-level README describing goals and license (README.md).
- Add extension-specific README with configuration options and highlights (extension/README.md).

## 2026-02-05

### Fixed
- Packaging: `vsce package` failed to detect the repository and produced a broken-link warning; added `repository` metadata to `extension/package.json` so packaging succeeds.

### Added
- Command: `altKey.resetLayout` — resets the workbench layout using `altKey.orientation` (supports `default`, `left`, `right`) and forces the panel to the bottom. Bound to the keybinding `Alt+A Escape` by default.

### Packaging
- Produced updated VSIX: `extension/alt-key-0.0.5.vsix`.

<!--
Notes:
- This is an initial/summary entry created because no CHANGELOG.md existed in the repository root. Bullets reference file paths for traceability.
-->
