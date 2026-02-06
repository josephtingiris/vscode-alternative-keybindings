# Style

Follow the coding and output style of existing Python scripts in `./bin/`.

# Intent

Produce a deterministic, well-formatted JSONC keybindings model generator script at `./bin/keybindings-model.py`.
The script should output a single JSONC array (pretty-printed) containing objects that describe candidate keybindings used by the project tooling.

# Core requirements

- Script path: `./bin/keybindings-model.py` (overwrite or replace an existing file if present).
- Output: a JSONC array of objects. Each object must include the properties: `key`, `command`, and `when`.
- Output must be JSONC only — no surrounding prose, no blank lines. The opening `[` and closing `]` must each be on their own line.
- Pretty-print with 2-space indentation. Put commas on the same line as the closing brace of each object.

# Keys and modifiers

Base modifiers to include (generate keybinding entries for these combinations):

- single modifiers: `alt`, `ctrl`, `meta`, `shift`
- common multi-modifier combinations: `ctrl+alt`, `alt+meta`, `ctrl+alt+meta`, `ctrl+shift+alt`, `shift+alt+meta`, `ctrl+shift+alt+meta`

Keys to generate bindings for (literal key names used in the `key` field):

`-`, `=`, `[`, `]`, `;`, `'`, `,`, `.`, `a`, `d`, `h`, `j`, `k`, `l`, `end`, `home`, `pageup`, `pagedown`, `left`, `down`, `up`, `right`

For each base key, generate bindings for the single modifiers and for the listed multi-modifier combinations above. Example: for `a` emit entries for `alt+a`, `ctrl+a`, `alt+meta+a`, `ctrl+alt+a`, `shift+alt+a`, ... `ctrl+shift+alt+meta+a`.

# `command` and `when` formats

- `command`: use exactly the format: `(model) <key-string> <4-hex-digits>`
	- Example: for `alt+a` the command should be `(model) alt+a 3f9a` (where `3f9a` is randomly generated hexadecimal digits)
- Default `when` clause: `altKey.enabled`
- vi keys (`h`, `j`, `k`, `l`): use `when`: `altKey.enabled && altKey.vi`
- arrow / navigation keys (`end`, `home`, `pageup`, `pagedown`, `left`, `down`, `up`, `right`): use `when`: `altKey.enabled && altKey.arrows`

# Commenting rules (JSONC)

- Keybindings that do not match any of the mapping categories below must not have comments.
- Each object representing a matching keybinding must include a single-line comment immediately above the `"key"` property inside the same object. The comment must be a JSONC `//` comment.
- Comment content must identify the logical category of the keybinding using an alphabetically sorted list of one or more of these tags: `(vi)`, `(arrow)`, `(left)`, `(down)`, `(up)`, `(right)`.
- Mapping (examples):
	- vi keys: `h`, `j`, `k`, `l` → `// (vi)`
	- arrow/navigation keys: `end`, `home`, `pageup`, `pagedown`, `left`, `down`, `up`, `right` → `// (arrow)`
	- left group: `h`, `[`, `;`, `,`, `left` → `// (left)`
	- down group: `j`, `down`, `pagedown` → `// (down)`
	- up group: `k`, `up`, `pageup` → `// (up)`
	- right group: `l`, `]`, `'`, `.`, `right` → `// (right)`

Examples (in JSONC object form):

{
	"key": "alt+a",
	"command": "(model) alt+a f3da",
	"when": "altKey.enabled"
},

{
	// (left)
	"key": "alt+[",
	"command": "(model) alt+[ 55b3",
	"when": "altKey.enabled"
},

{
	// (left) (vi)
	"key": "alt+h",
	"command": "(model) alt+h 1a2b",
	"when": "altKey.enabled && altKey.vi"
},

{
	// (down)
	"key": "alt+pagedown",
	"command": "(model) alt+pagedown dd1e",
	"when": "altKey.enabled"
}

{
	// (down) (arrow)
	"key": "ctrl+down",
	"command": "(model) ctrl+down abcd",
	"when": "altKey.enabled && altKey.arrows"
}

# Output constraints and validation

- Emit JSONC only. Do not print any logging, progress, or extra text to stdout when the script is used as a generator for downstream tooling.
- No blank lines in the output.
- The generated JSONC must be valid JSON after comments are removed. Validate with the repository tooling:

```
./bin/keybindings-model.py | ./bin/keybindings-remove-comments.py | jq
./bin/keybindings-model.py | ./bin/keybindings-sort.py -p key -s when | ./bin/keybindings-remove-comments.py | jq
```

Both commands must exit with rc 0 and `jq` must pretty-print the resulting JSON without errors.