# Development Install and Use

This folder contains a VS Code extension that registers configuration under the `altKey.*` namespace. Those settings are exposed to the Settings UI and as `config.altKey.*` context keys that can be used in keybinding `when` clauses.

Quick steps to package, install, and upgrade the extension VSIX:

1. From the repo root, install `vsce`:

```bash
# install globally (optional)
npm install -g @vscode/vsce
```

2. Package the extension and place the artifact in `extension/dist` (run from the repository root):

```bash
cd extension
mkdir -p dist
# package to extension/dist; replace the filename as desired
vsce package --allow-missing-repository --out dist/
```

3. Install the produced VSIX with VS Code (from `extension/`):

```bash
# install the package from the dist folder
code --install-extension dist/vscode-alternative-keybindings-0.0.1.vsix
```

4. Restart VS Code.

Upgrading an existing/previously installed VSIX

- If the new package has a higher `version` in `package.json`, `code --install-extension` will normally upgrade the extension when installing the new VSIX.
- To force reinstall / upgrade (overwrite an existing install), use `--force`:

```bash
code --install-extension --force dist/vscode-alternative-keybindings-0.0.1.vsix
```

- Make sure you bump the `version` field in `extension/package.json` before packaging so Marketplace or VS Code recognizes the update.

Notes

- `--out` (or `-o`) tells `vsce` where to write the artifact; using `dist/` keeps built artifacts separate from source files.
- Add any files you don't want vsce packaged to `extension/.vscodeignore`