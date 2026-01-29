#!/usr/bin/env bash

# Script for evolving VS Code keybindings.json files.

# Joseph Tingiris (joseph.tingiris@gmail.com), created 20260120

########################################
# global variables
########################################

KEYBINDINGS_JSON=""
TMPFILE="/tmp/keybindings-evolve.json"

########################################
# functions
########################################

# Function to handle errors and abort execution
aborting() {
    printf '\n%s\n\n' "aborting ... ${*}" >&2
    exit 1
}

# Function to display usage information
usage() {
    echo
    echo "usage: ${0##*/} <keybindings.json>"
    echo
    echo "Process a VS Code keybindings.json file to remove defunct commands and sort the remaining keybindings."
    echo
    exit 99
}

# Validate the keybindings JSON file
validate_json() {
    local file="${1}"
    if ! cat "${file}" | keybindings-remove-comments.py | jq . > /dev/null 2>&1; then
        aborting "'${file}' is not valid JSON"
    fi
}

# Remove defunct commands and sort keybindings
process_keybindings() {
    local file="${1}"
    local dirname
    dirname="$(dirname "${0}")"

    "${dirname}/keybindings-remove.py" command gigachad < "${file}"
}

# Main function
main() {
    # Ensure at least one argument is provided
    [ -z "${1}" ] && usage

    KEYBINDINGS_JSON="${1}"

    if [ ! -f "${KEYBINDINGS_JSON}" ]; then
        aborting "file '${KEYBINDINGS_JSON}' does not exist"
    fi

    # Remove existing tmpfile if present
    [ -f "${TMPFILE}" ] && rm -f "${TMPFILE}"

    # Validate JSON
    validate_json "${KEYBINDINGS_JSON}"

    # Process the keybindings
    process_keybindings "${KEYBINDINGS_JSON}"
}

########################################
# main
########################################

main "$@"
