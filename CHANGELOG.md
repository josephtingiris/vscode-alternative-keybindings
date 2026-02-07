# Changelog

All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog" and uses `YYYY-mm-dd` dated headings.


## 2026-02-06

- Changed: Update and refine the keybindings model and references (references/keybindings-model.json, commit ea5373d7).
- Changed: Merge and deduplicate references snapshot (references/keybindings.json) (commit a1ed1bc).
- Fixed: Improve "when" context handling in model and scripts (references/keybindings-model.jsonc, bin/keybindings-model.py) (commit 6c5f2c7, commit c0b0820).
- Added: Packaging and extension metadata bump for v0.0.8 release candidate (extension/package.json) (commit 34454a4).
- Changed: Formatting and sorting improvements for keybinding tools (bin/keybindings-sort.py, commit 808999e, f2aca04).

## 2026-02-05

- Changed: Refactor and improve keybinding sorting logic and normalization (bin/keybindings-sort.py) (commit 134cb92).
- Added: `altKey.resetLayout` command and packaging fixes (extension/extension.js, extension/package.json) (commit 4f70eaf).
- Fixed: Multiple references and dedupe fixes for `references/keybindings.json` (commit 2cd91aa, 5a049baa).

## 2026-02-04

- Added: `keybindings-evolve` script and evolution helpers (bin/keybindings-evolve.sh) (commit dd10e9c).
- Added: initial prompts and debug reference snapshots (references/debug/*) (commit 272d550).
- Changed: Various checkpoints for crafting references and scripts (references/keybindings.json, bin/keybindings-sort.py) (commits 1610839, af215bc).

## 2026-02-03

- Added: Technical reference for VS Code keybinding resolution (references/vscode-keybindings-resolution.md) (commit feccb2d).
- Added: tools to manage command comments and continuity (`bin/keybindings-command-comments.py`) (commit ea8a1b9).
- Changed: Numerous documentation and conventions updates for keybinding instructions and prompts (.github/instructions/*, DEVELOPMENT.md, README.md) (commits d179394, 5d099ea, bde7b84).
- Fixed: Various formatting and example fixes across references (references/keybindings.json) (commit 73d6911).

## 2026-02-02

- Added: extension packaging and installation improvements (extension/.vscodeignore, extension/package.json) (commit 1503de5).
- Added: assets and extension development instructions (extension/assets, extension/DEVELOPMENT.md) (commits b2cf296, 747ee3a).
- Added: initial extension release artifacts and license (extension/vscode-alternative-keybindings-0.0.1.vsix, extension/LICENSE) (commit dbbe648).

## 2026-02-01

- Changed: Enhanced directional navigation and terminology guidance in keybinding instructions (.github/instructions/alternative-keybindings.instructions.md) (commit d395c4e).
- Added: new feature keybindings and improved documentation for context keys (references/keybindings.json, commit 1288880).
- Changed: multiple documentation refactors and clarifications across prompts and agents (.github/prompts, .github/agents) (commits 3f6c922, 04d245d).

## 2026-01-31

- Added: new keybindings for sidebar and auxiliary bar visibility and directional conventions (references/keybindings.json) (commit 13512b0).
- Changed: keybinding sorting and comment normalization improvements (bin/keybindings-sort.py, .github/instructions/keybindings-conventions.instructions.md) (commits e147fea, 0020a73).
- Added: development and contributor docs including AGENTS.md and DEVELOPMENT.md (AGENTS.md, DEVELOPMENT.md) (commits b0bee2e, 9b2e04d).

## 2026-01-30

- Added: `bin/watch-runner.sh` and helper scripts for development automation (bin/watch-runner.sh, bin/keybindings-install-references.sh) (commits 80ab0b6, 6ce1cf9).
- Added: initial keybinding continuity guidelines and helper prompts (.github/prompts/keybindings-continuity.prompt.md) (commit 7870be3).

## 2026-01-29

- Added: project scaffolding and core tools (README.md, bin/* keybindings utilities) (commits 908157d, 554c45c).
- Added: initial references and API docs for VS Code commands and when-contexts (references/vscode-api-commands.md, references/vscode-when-contexts.md) (commit eadf11d, 1dde1f57).
- Added: initial CHANGELOG and project metadata (CHANGELOG.md, .gitignore, LICENSE) (commit 659c480, 558ea4d).
