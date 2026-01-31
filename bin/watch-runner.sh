#!/usr/bin/env bash

# Execute a binary or script when a file changes.
#
# Usage: watch-runner.sh <file-to-watch> <runner-executable>
# The script is quiet while watching; before each run it prints a
# delimiter line with an ISO UTC datestamp. The runner's stdout/stderr
# are passed straight through to the script's stdout/stderr.
#
# Joseph Tingiris
# created: 20260130

set -euo pipefail

WATCH=""
RUNNER=""

aborting() {
    printf '%s\n' "aborting ... ${*}" >&2
    exit 1
}

usage() {
    echo
    echo "usage: ${0##*/} <file-to-watch> <runner-executable>"
    echo
    exit 2
}

validate_requirements() {
    if ! command -v realpath > /dev/null 2>&1; then
        aborting "realpath is required but not found"
    fi
    if ! command -v inotifywait > /dev/null 2>&1; then
        aborting "inotifywait is required; install with: sudo apt install inotify-tools"
    fi
}

main() {
    [ "$#" -ne 2 ] && usage

    WATCH="$1"
    RUNNER="$2"

    validate_requirements

    WATCH_REAL=$(realpath "${WATCH}" 2> /dev/null) || aborting "file not found: ${WATCH}"
    [ ! -f "${WATCH_REAL}" ] && aborting "not a regular file: ${WATCH_REAL}"

    if [[ ${RUNNER} == */* ]]; then
        [ ! -x "${RUNNER}" ] && aborting "runner not executable: ${RUNNER}"
    else
        ! command -v "${RUNNER}" > /dev/null 2>&1 && aborting "runner not found in PATH: ${RUNNER}"
    fi

    # Watch loop: quiet while waiting, print a delimiter then execute runner
    while inotifywait -q -e close_write,modify,move,create "${WATCH_REAL}" > /dev/null 2>&1; do
        echo "---- RUN: $(date -u '+%Y-%m-%dT%H:%M:%SZ') ----"
        "${RUNNER}" "${WATCH_REAL}"
    done
}

DIRNAME="$(dirname "$0")"

main "$@"
