---
description: 'Shell scripting additional practices and conventions for bash, sh, zsh, and other shells'
applyTo: "**/*.sh,**/*.bash"
---
# Shell Scripting Guidelines

These mirror the Google Shell Style Guide with project-local tweaks: two-space
indentation (spaces only), GNU-style short/long flags, and POSIX-friendly Bash.

## 1. Shebang

Always start shell scripts with the appropriate shebang line:

```bash
#!/bin/bash
```

or, for better portability:

````bash
#!/usr/bin/env bash
```

## 2. Comments and Documentation

- Use comments to explain the purpose of the script and any complex logic.
- Include a usage function to display help when the script is run with `-h` or `--help`.

## 3. Variable Naming

- Use uppercase letters with underscores for environment variables (e.g., `MY_VAR`).
- Use lowercase letters with underscores for local variables (e.g., `my_var`).

## 4. Quoting

Always quote variables and use curly brackets {} to prevent word splitting and globbing issues, for example:

```bash
echo "${my_var}"
```

## 5. Functions

- Use functions to encapsulate logic and improve readability.
- Functions in all scripts should be sorted alphabetically for easier navigation.
- Declare functions using the following syntax (2-space indent, spaces only):

```bash
my_function() {
  # function body
}
```

- Prefer `${var}` over legacy ``var`` expansions and `$(...)` over backticks.
- All scripts should contain an aborting() function that outputs to stderr to handle errors, for example:

```bash
aborting() {
  printf '\n%s\n\n' "aborting ... ${*}" >&2
  exit 1
}
```

- All scripts should contain a usage() function that outputs to stdout to display help, for example:

```bash
usage() {
  echo
  echo "usage: ${0##*/} [options]"
  echo
  echo "options:"
  echo "  -h, --help        Show this help message and exit"
  echo
  exit 99
}
```

## 6. Error Handling

- Check the exit status of commands and handle errors gracefully.
- Use `trap` to clean up resources on exit or error.

## 7. Logging

- Use `echo` or `printf` for logging messages.
- Consider using different log levels (INFO, WARN, ERROR) for better clarity.

## 8. Testing

- Test scripts in a safe environment before deploying them to production.
- Use shfmt to lint and format your shell scripts consistently.

## 9. Arguments (GNU-style)

- Support paired short/long flags (for example `-h`/`--help`).
- Prefer `getopts` for short flags; for long flags, parse in a `case` loop to stay
  POSIX-friendly and avoid Bash-only `getopts` extensions.
- Show both forms in `usage()` output so users know they are equivalent.
- Reject unknown flags explicitly to prevent silent misconfiguration.

## 10. Indentation and formatting

- Keep scripts POSIX-friendly unless a Bash feature is required; when using Bash,
- Use 4-space indentation; NEVER use tabs. Configure editors accordingly.
  state it with `#!/usr/bin/env bash`.
- Use `shfmt --indent 4 --space-redirects --case-indent --simplify` for consistent formatting.
