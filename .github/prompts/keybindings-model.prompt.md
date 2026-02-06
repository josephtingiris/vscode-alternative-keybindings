Create a file named ./references/keybindings-model.json that follows the keybindings.json format.  Overwrite it if it already exists.
The file should contain an array of objects, each representing a keybinding.
Each object should have the following properties: "key", "command", and "when".
Include modifiers: alt+ ctrl+ alt+meta ctrl+alt+ shift+alt+ ctrl+alt+meta+ ctrl+shift+alt+ shift+alt+meta+ ctrl+shift+alt+meta+
Include keys: - = [ ] ; ' , . a d h j k l end home pagedown left down up right
For each of the included keys, create keybindings for each of the modifiers listed above. For example, for the key "a", you would create keybindings for "alt+a", "ctrl+a", "alt+meta+a", "ctrl+alt+a", "shift+alt+a", "ctrl+alt+meta+a", "ctrl+shift+alt+a", "shift+alt+meta+a", and "ctrl+shift+alt+meta+a".
For the "command:" use the form "command": "<exact value of "key:"> <4 random hexidecimal digits>"
For the "when:" use "when": "altKey.enabled"
Output pure JSON content only, without any additional text, comments, or explanation.
Ensure output is pretty-printed with an indentation of 2 spaces.
