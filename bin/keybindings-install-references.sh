#!/usr/bin/env bash

# Script for installing references/keybindings.json in my VS Code setup.

# Joseph Tingiris (joseph.tingiris@gmail.com), created 20260120

########################################
# global variables
########################################

KEYBINDINGS_JSON=""

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
    echo "usage: ${0##*/} [keybindings.json]"
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

# find vscode user home directory
vscode_user_home() {
    local vscode_home=""
    if [ -n "${WSL_DISTRO_NAME}" ]; then
        vscode_home=$(which wslconfig.exe 2> /dev/null | grep AppData | awk -F\/AppData '{print $1}')
    else
        vscode_home="${HOME}"
    fi
    echo "${vscode_home}"
}

main() {
    [ -z "${1}" ] && usage

    KEYBINDINGS_JSON="${1}"

    if [ ! -f "${KEYBINDINGS_JSON}" ]; then
        aborting "file '${KEYBINDINGS_JSON}' does not exist"
    fi

    validate_json "${KEYBINDINGS_JSON}"

    local user_keybindings_json
    user_keybindings_json="$(vscode_user_home)/AppData/Roaming/Code/User/keybindings.json"
    if [ ! -r "${user_keybindings_json}" ]; then
        aborting "'${user_keybindings_json}' file not found readable"
    fi

	KEYBINDINGS_SORT_ARGUMENTS="${KEYBINDINGS_SORT_ARGUMENTS:--p key -s when}"
    if type -p keybindings-sort.py > /dev/null 2>&1; then
        keybindings-sort.py ${KEYBINDINGS_SORT_ARGUMENTS} < "${KEYBINDINGS_JSON}" > /tmp/keybindings-sorted.json
        mv /tmp/keybindings-sorted.json "${KEYBINDINGS_JSON}"
    fi

    echo -n "Installing 'references/$(basename "${KEYBINDINGS_JSON}")' to '$(vscode_user_home)' ... "
    cp "${KEYBINDINGS_JSON}" "${user_keybindings_json}"
    echo "Done."

    #cat "${KEYBINDINGS_JSON}"
}

########################################
# main
########################################

DIRNAME="$(dirname "$0")"

[ "$#" -lt 1 ] && KEYBINDINGS_JSON="${DIRNAME}/../references/keybindings.json" || KEYBINDINGS_JSON="$1"
[ ! -r "${KEYBINDINGS_JSON}" ] && aborting "'${KEYBINDINGS_JSON}' file not readable"
KEYBINDINGS_JSON="$(realpath "${KEYBINDINGS_JSON}")"

main "${KEYBINDINGS_JSON}"
