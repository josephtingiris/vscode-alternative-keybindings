## Development Guide

This document contains developer-focused notes for debugging, testing, packaging,
and working with the VS Code AlterNative Keybindings extension and repository tools.

### Quick index

- Debugging keybindings
- Interpreting logs
- Active development (watcher for `references/keybindings.json`)
- Packaging & installing the extension (VSIX)
- Contributing

---

## Debugging keybindings (live resolver)

Keyboard shortcut resolution is internal to VS Code. Use the live resolver to
capture how VS Code resolves key events and which `when` clauses evaluated true.

Steps:

1. Open the Command Palette (Ctrl+Shift+P) and run **Developer: Toggle Keyboard Shortcuts Troubleshooting**.
   - This toggles logging of keyboard events and their resolution.
2. Open the Output panel: View → Output (Ctrl+Shift+U) and choose the appropriate channel.
   - Preferred channels: `Log (Keybindings)` or `Log (Keybindings) - Extension` (names vary by build).
   - If only `Window` appears, select `Window` and press the keys you want to inspect; some builds route the log there.
3. Press the keystroke(s) to inspect and watch output lines like: `Resolved -> <command id>` and `When: <when expression> = true|false`.
4. Run the toggle command again to stop logging.

### Autoscroll

Enable **Auto Scroll** in the Output panel (three-dot menu) to keep new lines visible while testing.

### Window-channel format notes

Some builds print keybinding logs to the `Window` channel with lines prefixed by `/`, `|`, `\`, `+` that indicate dispatch, conversion, match results, and invocation. Look for `matched <command>` and `source: user|default|extension`.

---

## Active development: auto-install references

To test changes to `references/keybindings.json` automatically (copies into a Windows user profile when applicable), use the watcher:

```bash
chmod +x bin/watch-runner.sh bin/keybindings-install-references.sh
./bin/watch-runner.sh references/keybindings.json bin/keybindings-install-references.sh
```

The watcher runs quietly and executes the installer script on file changes. Stop it with Ctrl+C or `pkill -f watch-runner.sh`.

Notes on the installer: the script attempts to detect WSL vs native Windows and copy the file into the proper user keybindings location.

---

## Packaging & local install (VSIX)

Package and install a local VSIX for testing:

1. Install `vsce` (if required):

```bash
npm install -g @vscode/vsce
```

2. From the repo root, package the extension into `extension/dist`:

```bash
cd extension
mkdir -p dist
vsce package --allow-missing-repository --out dist/
```

3. Install the produced VSIX:

```bash
code --install-extension dist/vscode-alternative-keybindings-<version>.vsix
```

To force an overwrite during testing:

```bash
code --install-extension --force dist/vscode-alternative-keybindings-<version>.vsix
```

Make sure to bump `extension/package.json` `version` before packaging when creating upgrades.

Exclude development docs and other files from the packaged VSIX using `extension/.vscodeignore`.

---

## Contributing

- Open issues and pull requests on the repository.
- Follow any contribution guidelines in `CONTRIBUTING.md` if present.
- Use the `bin/` helper scripts for packaging, testing, and repetitive tasks.

---
