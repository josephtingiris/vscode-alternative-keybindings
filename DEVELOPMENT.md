**Development**

This document captures developer-focused notes for debugging and testing.

**DEBUGGING**

Keyboard shortcuts can be hard to debug because resolution is internal to VS Code.
Below are concise steps to enable the built-in troubleshooting logger and how to find
the output when the Output panel only shows the `Window` channel.

**Keyboard Shortcuts Troubleshooting (live resolver)**

1. Open the Command Palette (Ctrl+Shift+P) and run: "Developer: Toggle Keyboard Shortcuts Troubleshooting".
   - Running this command toggles logging of keyboard events and their resolution.

2. Open the Output panel: View → Output (or `Ctrl+Shift+U`).

3. Select the correct output channel from the dropdown in the Output panel.
   - Preferred channel: `Log (Keybindings)` or `Log (Keybindings) - Extension` (names may vary by VS Code build).
   - If you only see `Window` in the channel dropdown, select `Window` and then press the keystroke you want to inspect — the troubleshooting log often appears there in some builds and distributions.
   - If the `Log (Keybindings)` channel is present but not visible in the dropdown, run the toggle command again to ensure logging started; the channel is created when logging begins.

4. Press the keystroke(s) you want to inspect. The Output channel will show lines similar to:

   - Keyboard event: `<key sequence>`
   - Resolved -> `<command id>`  (source: `user` | `default` | `extension`)
   - When: `<when expression>` = true|false
   - Handled: yes|no

5. To stop logging, run "Developer: Toggle Keyboard Shortcuts Troubleshooting" again.

Autoscroll
- In the Output panel, enable the dropdown menu (three-dot) and turn on **Auto Scroll** so new log lines stay visible while you press keys.

Window-channel log format
- When the Output channel is `Window` the keybinding service logs slightly differently; example lines below show the typical format found in recent VS Code builds:

```
2026-01-29 17:06:46.684 [info] [Window] [KeybindingService]: / Soft dispatching keyboard event
2026-01-29 17:06:46.684 [info] [Window] [KeybindingService]: | Resolving alt+UpArrow
2026-01-29 17:06:46.684 [info] [Window] [KeybindingService]: \ From 13 keybinding entries, matched workbench.action.focusPreviousPart, when: config.workbench.sideBar.location == 'left', source: user.
2026-01-29 17:06:46.684 [info] [Window] [KeybindingService]: / Received  keydown event - modifiers: [alt], code: ArrowUp, keyCode: 38, key: ArrowUp
2026-01-29 17:06:46.684 [info] [Window] [KeybindingService]: | Converted keydown event - modifiers: [alt], code: ArrowUp, keyCode: 16 ('UpArrow')
2026-01-29 17:06:46.684 [info] [Window] [KeybindingService]: | Resolving alt+UpArrow
2026-01-29 17:06:46.684 [info] [Window] [KeybindingService]: \ From 13 keybinding entries, matched workbench.action.focusPreviousPart, when: config.workbench.sideBar.location == 'left', source: user.
2026-01-29 17:06:46.684 [info] [Window] [KeybindingService]: + Invoking command workbench.action.focusPreviousPart.
```

Notes on the `Window` format
- Timestamps and a logger name (`[Window] [KeybindingService]`) prefix each line.
- The lines beginning with `/`, `|`, `\`, `+` are the service's visual markers for stages of resolution: dispatch, conversion, match results, and invocation.
- Look for `matched <command>` and `source: user|default|extension` to identify which keybinding fired and where it came from.

Tips and alternatives
- If you prefer a persistent copy of the log, open the Output panel, select the channel, press `Ctrl+A` then `Ctrl+C` and paste into a file.
- If the Output channel remains empty, try restarting VS Code and re-running the toggle command.
- As a last resort, open the Developer Tools console (Help → Toggle Developer Tools) and check the Console for related messages; however, the recommended place for keybinding resolution is the Output panel's logging channel.

How to interpret the log
- "Source: user" indicates the binding comes from the user's `keybindings.json`.
- When expressions evaluate to `true` means the binding was eligible when the keystroke occurred.
- "Handled: yes" means the event was consumed and the command executed.

If you'd like, I can add a short script to parse the copied output and summarize matches by command or source.
