# Style

Use the same style as other python scripts in `./bin/`

# Always Clean Up And Start Over

Always start cleanly from the specifications provided in this prompt.
Do not include any content from previous versions of the file, if it exists.
If a `./bin/keybindings-model.py` file already exists, overwrite it or remove it.

# Specifications

Write a new script named `./bin/keybindings-model.py` that generates a JSONC output containing keybindings based on the following specifications:
The ouput should contain an array of JSONC objects, each representing a keybinding.
Each object should have the following properties: "key", "command", and "when".
Include modifiers: `alt+ ctrl+ meta+ alt+meta ctrl+alt+ shift+alt+ ctrl+alt+meta+ ctrl+shift+alt+ shift+alt+meta+ ctrl+shift+alt+meta+`
Include keys: `- = [ ] ; ' , . a d h j k l end home pagedown left down up right`
For each of the include keys, create keybindings for each of the minclude odifiers listed above. For example, for the key "a", you would create keybindings for "alt+a", "ctrl+a", "alt+meta+a", "ctrl+alt+a", "shift+alt+a", "ctrl+alt+meta+a", "ctrl+shift+alt+a", "shift+alt+meta+a", and "ctrl+shift+alt+meta+a".
For the "command:" use the form `"command": "(model) <exact value of "key:"> <4 random hexidecimal digits>"`
Unless otherwise specified, for the "when:" use `"when": "altKey.enabled"`
For the vi keys: `h j k l` use `"when": "altKey.enabled && altKey.vi"`
For the arrow keys: `end home pagedown left down up right` use `"when": "altKey.enabled && altKey.arrows"`

# Additional Specifications for Comments

Comments must appear for single and multi-modifier keys
All `vi` and `arrow` keybindings must have a comment above the "key" property that identifies the type of keybinding it is, as specified below:
- The comment above "key": must be _within_ the JSONC object curly braces, for example `{ // comment }`.
- For the vi keys keys, add or append to a comment above "key": that identifies it as an arrow keybinding, i.e. `// (vi)`
- For the arrow keys keys, add or append to a comment above "key": that identifies it as an arrow keybinding, i.e. `// (arrow)`
- For the left keys: `h [ ; , left]` add or append to a comment above "key": that identifies it as a left keybinding, i.e. `// (left)`
- For the down keys: `j down pagedown` add or append to a comment above "key": that identifies it as a down keybinding, i.e. `// (down)`
- For the up keys: `k up pageup` add or append to a comment above "key": that identifies it as an up keybinding, i.e. `// (up)`
- For the right keys: `l ] ' . right` add or append to a comment above "key": that identifies it as a right keybinding, i.e. `// (right)`


# Output

Output JSONC content only, without any additional text or explanation.
Output no blank or empty lines.
The opening and closing square brackets of the JSON array must be on their own lines.
Ensure output is pretty-printed with an indentation of 2 spaces.
Ensure commas following the objects are on the same line as the closing brace of the object, not on a new line.

# Validation

From the repository root: - Run the script to generate the output and inspect it for correctness. Make any necessary adjustments to the script and re-run until the output meets the specifications. - Run `./bin/keybindings-model.py | ./bin/keybindings-remove-comments.py | jq` . to validate that the output is valid JSON and meets the specifications. jq must produce rc 0 and pretty-print the JSON without errors. If jq produces an error, adjust the script and re-run until jq validates the output successfully with the command above. - Run `./bin/keybindings-model.py | ./bin/keybindings-sort.py -p key -s when | ./bin/keybindings-remove-comments.py | jq` . to validate that the output is valid JSON and meets the specifications. jq must produce rc 0 and pretty-print the JSON without errors. If jq produces an error, adjust the script and re-run until jq validates the output successfully with the command above.
