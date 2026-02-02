# Development Install and Use

This folder contains a VS Code extension that registers configuration under the `altKey.*` namespace. Those settings are exposed to the Settings UI and as `config.altKey.*` context keys that can be used in keybinding `when` clauses.

Quick steps to package and install the extension as a VSIX:

1. From the repo root, install `vsce` (or use `npx`):

```bash
# install globally (optional)
npm install -g @vscode/vsce

# or use npx to avoid global install
npx @vscode/vsce package
```

2. Package the extension (run in the `extension/` directory):

```bash
cd extension
# using global vsce
vsce package
# or using npx from project root
npx @vscode/vsce package
```

3. Install the produced VSIX with VS Code:

```bash
# from the extension/ directory: the file will be like vscode-alternative-altkey-settings-0.0.1.vsix
code --install-extension vscode-alternative-altkey-settings-0.0.1.vsix
```

4. Restart VS Code.