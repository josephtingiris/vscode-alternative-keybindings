Write a script named `./bin/keybindings-model.py` that generates a JSON standard output containing keybindings based on the following specifications:
The ouput should contain an array of JSON objects, each representing a keybinding.
Each object should have the following properties: "key", "command", and "when".
Include modifiers: `alt+ ctrl+ alt+meta ctrl+alt+ shift+alt+ ctrl+alt+meta+ ctrl+shift+alt+ shift+alt+meta+ ctrl+shift+alt+meta+`
Include keys: `- = [ ] ; ' , . a d h j k l end home pagedown left down up right`
For each of the included keys, create keybindings for each of the include modifiers listed above. For example, for the key "a", you would create keybindings for "alt+a", "ctrl+a", "alt+meta+a", "ctrl+alt+a", "shift+alt+a", "ctrl+alt+meta+a", "ctrl+shift+alt+a", "shift+alt+meta+a", and "ctrl+shift+alt+meta+a".
For the "command:" use the form `"command": "<exact value of "key:"> <4 random hexidecimal digits>"`
Unless otherwise specified, for the "when:" use `"when": "altKey.enabled"`
For the vi keys: `h j k l` use `"when": "altKey.enabled && altKey.vi"`
For the vi keys keys, add or append to a comment above "key": that identifies it as an arrow keybinding, i.e. `// (vi)`
For the arrow keys: `end home pagedown left down up right` use `"when": "altKey.enabled && altKey.arrows"`
For the arrow keys keys, add or append to a comment above "key": that identifies it as an arrow keybinding, i.e. `// (arrow)`
For the left keys: `h [ ; , left]` add or append to a comment above "key": that identifies it as a left keybinding, i.e. `// (left)`
For the down keys: `j down pagedown` add or append to a comment above "key": that identifies it as a down keybinding, i.e. `// (down)`
For the up keys: `k up pageup` add or append to a comment above "key": that identifies it as an up keybinding, i.e. `// (up)`
For the right keys: `l ] ' . right` add or append to a comment above "key": that identifies it as a right keybinding, i.e. `// (right)`
Output pure JSON content only, without any additional text, comments, or explanation.
Ensure output is pretty-printed with an indentation of 2 spaces.
