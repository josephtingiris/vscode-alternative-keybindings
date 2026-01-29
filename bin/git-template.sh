#!/usr/bin/env bash

# Script for managing a git repository template.

# Joseph Tingiris (joseph.tingiris@gmail.com), created 20260119

########################################
# global variables
########################################

GIT_TEMPLATE_NAME="${GIT_TEMPLATE_NAME:-development-template}"
GIT_TEMPLATE_URL="${GIT_TEMPLATE_URL:-git@github.com:josephtingiris/development.git}"

########################################
# functions
########################################

# Function to handle errors and abort execution
aborting() {
    printf '\n%s\n\n' "aborting ... ${*}" >&2
    exit 1
}

# Get git config value
git_config_get() {
    local key="${1}"
    git config "${key}" 2> /dev/null || echo ""
}

# Set git local config value
git_config_set_local() {
    local key="${1}"
    local value="${2}"
    git config --local "${key}" "${value}"
}

# Find the git repository root directory
git_root() {
    local dir="${PWD}"
    while [ "${dir}" != "/" ]; do
        if [ -d "${dir}/.git" ] || [ -f "${dir}/.git" ]; then
            echo "${dir}"
            return 0
        fi
        dir="$(dirname "${dir}")"
    done
    return 1
}

# Add template URL to repository
template_add() {
    if [ -n "${TEMPLATE_URL}" ]; then
        aborting "${REPO_ROOT} already has a template URL: ${TEMPLATE_URL} (try deleting it first)"
    fi
    echo
    echo "Adding template url: ${GIT_TEMPLATE_URL}"
    echo
    git_config_set_local "template.${GIT_TEMPLATE_NAME}.url" "${GIT_TEMPLATE_URL}"
    exit $?
}

# Check if repository has template URL
template_check() {
    echo
    if [ -n "${TEMPLATE_URL}" ]; then
        echo "${REPO_ROOT} has a template URL: ${TEMPLATE_URL}"
        echo
    else
        echo "${REPO_ROOT} does not have a template URL."
        echo
        exit 1
    fi
    exit 0
}

# Delete template URL from repository
template_delete() {
    if [ -z "${TEMPLATE_URL}" ]; then
        aborting "${REPO_ROOT} does not have a template URL to delete."
    fi
    echo
    echo "Deleting template url: ${TEMPLATE_URL}"
    echo
    git config --unset "template.${GIT_TEMPLATE_NAME}.url" 2> /dev/null || true
    exit $?
}

# Update repository contents from template
template_update() {
    if [ -z "${TEMPLATE_URL}" ]; then
        aborting "${REPO_ROOT} does not have a template URL. Use --add first."
    fi

    if ! command -v rsync > /dev/null 2>&1; then
        aborting "rsync command not found (install it)"
    fi

    if git remote -v | grep "[[:space:]]${TEMPLATE_URL}[[:space:]](" > /dev/null 2>&1; then
        aborting "refusing to update from template URL (${TEMPLATE_URL}) because it matches a remote URL (check git remote -v')!"
    else
        if git remote -v | grep "[[:space:]]${TEMPLATE_URL//.git/}[[:space:]](" > /dev/null 2>&1; then
            aborting "refusing to update from template URL (${TEMPLATE_URL//.git/}) because it matches a remote URL (check git remote -v')!"
        fi
    fi

    TEMP_DIR="$(mktemp -d -t git-template-XXXXXX)"
    trap 'rm -rf "${TEMP_DIR}"' EXIT

    echo
    echo "Updating '${REPO_ROOT}' from template: ${TEMPLATE_URL}"
    echo

    REMOVE_PATHS=()

    HAS_PATHS=()
    HAS_PATHS+=(CHANGELOG.md)
    HAS_PATHS+=(CLONING.md)
    HAS_PATHS+=(CONTRIBUTING.md)
    HAS_PATHS+=(DEVELOPMENT.md)
    HAS_PATHS+=(LICENSE)
    HAS_PATHS+=(Makefile)
    HAS_PATHS+=(README.md)
    HAS_PATHS+=(bin/develop)
    HAS_PATHS+=(examples)
    HAS_PATHS+=(scripts)

    for HAS_PATH in "${HAS_PATHS[@]}"; do
        if [ ! -e "${REPO_ROOT}/${HAS_PATH}" ]; then
            REMOVE_PATHS+=("${HAS_PATH}")
        fi
    done
    unset HAS_PATH

    git clone --depth 1 "${TEMPLATE_URL}" "${TEMP_DIR}"
    echo

    RSYNC_ARGS=(
        -av
        --exclude .git
    )

    echo rsync "${RSYNC_ARGS[@]}" "${TEMP_DIR}/" "${REPO_ROOT}/"
    echo
    rsync "${RSYNC_ARGS[@]}" "${TEMP_DIR}/" "${REPO_ROOT}/"
    echo

    REVERT_PATHS=()
    REVERT_PATHS+=(.gitignore)
    REVERT_PATHS+=(.github/copilot-instructions.md)
    REVERT_PATHS+=(etc/bash.d/README.md)
    REVERT_PATHS+=(CHANGELOG.md)
    REVERT_PATHS+=(CONTRIBUTING.md)
    REVERT_PATHS+=(LICENSE)
    REVERT_PATHS+=(Makefile)
    REVERT_PATHS+=(README.md)

    for REVERT_PATH in "${REVERT_PATHS[@]}"; do
        if [ -f "${REPO_ROOT}/${REVERT_PATH}" ]; then
            echo "Reverting ${REVERT_PATH} ..."
            git checkout -- "${REVERT_PATH}" &> /dev/null || true
        fi
    done
    unset REVERT_PATH

    for REMOVE_PATH in "${REMOVE_PATHS[@]}"; do
        if [ -d "${REPO_ROOT}/${REMOVE_PATH}" ]; then
            echo "Removing directory ${REMOVE_PATH} ..."
            rm -rf "${REPO_ROOT}/${REMOVE_PATH}"
        else
            if [ -f "${REPO_ROOT}/${REMOVE_PATH}" ]; then
                echo "Removing file ${REMOVE_PATH} ..."
                rm -f "${REPO_ROOT}/${REMOVE_PATH}"
            fi
        fi
    done
    unset REMOVE_PATH

    echo
    echo git status
    echo

    git status
    echo

    exit $?
}

# Function to display usage information
usage() {
    echo
    echo "usage: ${0##*/} <options>"
    echo
    echo "options:"
    echo "  -a, --add [url]          Add a git template URL to the repository [default=${GIT_TEMPLATE_URL}]"
    echo "  -u, --update             Update repository contents from the template URL"
    echo "  -c, --check              Check if the repository has a template URL"
    echo "  -d, --delete             Delete the template URL from the repository"
    echo "  -h, --help               Show this help message and exit"
    echo
    exit 99
}

# Main function
main() {
    # Ensure at least one argument is provided
    [ -z "${1}" ] && usage

    # Parse command-line arguments
    ADD_URL=false
    UPDATE=false
    CHECK=false
    DELETE=false

    while [ $# -gt 0 ]; do
        case "${1}" in
            -a | --add)
                ADD_URL=true
                if [ "${2}" != "" ]; then
                    GIT_TEMPLATE_URL="${2}"
                    shift 2
                else
                    shift
                fi
                ;;
            -u | --update)
                UPDATE=true
                shift
                ;;
            -c | --check)
                CHECK=true
                shift
                ;;
            -d | --delete)
                DELETE=true
                shift
                ;;
            -h | --help)
                usage
                ;;
            *)
                aborting "unknown option: ${1}"
                ;;
        esac
    done

    # Check if in a git repository
    if ! git_root > /dev/null; then
        aborting "${PWD} is not in a git repository"
    fi

    REPO_ROOT="$(git_root)"

    echo "Repository root       : ${REPO_ROOT}"
    echo "Using template name   : ${GIT_TEMPLATE_NAME}"
    echo "Using template url    : ${GIT_TEMPLATE_URL}"

    cd "${REPO_ROOT}"

    # Check for existing 'template' remote and warn
    if git remote | grep -q '^template$'; then
        echo && echo "Warning: A remote named 'template' exists. Consider renaming or removing it." >&2
    fi

    # Get current template URL
    TEMPLATE_URL="$(git_config_get "template.${GIT_TEMPLATE_NAME}.url")"

    # The following is order specific
    if [ "${DELETE}" = true ]; then
        template_delete
    fi

    if [ "${ADD_URL}" = true ]; then
        template_add
    fi

    if [ "${CHECK}" = true ]; then
        template_check
    fi

    if [ "${UPDATE}" = true ]; then
        template_update
    fi

    # If no options specified, show usage
    usage
}

########################################
# main
########################################

main "$@"
