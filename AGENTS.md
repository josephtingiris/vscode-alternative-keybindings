# Agent Instructions

## Project overview
- Workspace is a VS Code Extension to facilitate easier navigation of VS Code windows and tabs using keyboard shortcuts.
- The extension enhances productivity by allowing users to quickly navigate or switch between open files and tabs without relying on the mouse.
- Built using TypeScript and leverages the VS Code API and keybindings.json when context clauses for seamless integration with the editor.
- Prefers Podman for containerized development environments to ensure consistency across different setups.
- Layout mirrors the Filesystem Hierarchy Standard (FHS): `bin/` for installable CLIs, `scripts/` for repo-scoped helpers, `etc/bash.d/` for sourced shell snippets, and `examples/` for template projects.

## Conventions to follow
- Keep paths relative to the repository root; avoid hard-coded absolute paths.

## Key workflows

## Documentation & references
- Keep README.md lightweight; expand detailed contributor docs in CONTRIBUTING.md and reference them from new examples.
- When touching bd integration, cite https://github.com/bash-d/bd and mirror the instructions already captured in etc/bash.d/README.md.
