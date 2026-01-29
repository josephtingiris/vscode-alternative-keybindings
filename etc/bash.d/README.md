# Project Bash Helpers

This directory stores project-scoped shell helpers that the [bd Bash Directory autoloader](https://github.com/bash-d/bd) can load automatically.

## Install bd

### Automatic install

```bash
cd
curl -Ls https://raw.githubusercontent.com/bash-d/bd/main/bd-install.sh | /usr/bin/env bash -s _ replace
. "$HOME/.bash_profile"
bd env
```

### Manual install

1. Download a release into `~/.bd`.
2. Add the following to your shell profile:
   ```bash
   [ -r "$HOME/.bd/bd.sh" ] && source "$HOME/.bd/bd.sh"
   bd env
   ```

## Using bd with this repo

1. From the repository root, export this directory into the autoloader search path:
   ```bash
   export BD_AUTOLOADER_DIRS="$PWD/etc/bash.d:${BD_AUTOLOADER_DIRS:-}"
   ```
2. Source `bd.sh` (or start a shell where your profile does it) so bd discovers the directory:
   ```bash
   [ -r "$HOME/.bd/bd.sh" ] && source "$HOME/.bd/bd.sh"
   bd env
   ```
3. Drop `*.sh` or `*.bash` helpers in this folder; bd will source them in lexical order, so prefer numbered prefixes (for example `10-path.sh`) for explicit ordering.

## Recommended practices

- Keep functions idempotent and safe when sourced multiple times.
- Group related helpers into separate files to aid discoverability.
- Use comments at the top of each script to explain purpose and any prerequisites.
- Consult the bd documentation for advanced configuration, debugging flags, and namespace features.
