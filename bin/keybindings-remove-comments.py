#!/usr/bin/env python3

import re
import sys

def strip_comments(jsonc_string):
    # Remove single-line comments
    no_single_line_comments = re.sub(r'//.*', '', jsonc_string)
    # Remove multi-line comments
    no_multi_line_comments = re.sub(r'/\*.*?\*/', '', no_single_line_comments, flags=re.DOTALL)
    return no_multi_line_comments.strip()

if __name__ == "__main__":
    # Read from stdin
    jsonc_string = sys.stdin.read()
    json_string = strip_comments(jsonc_string)
    # Print the resulting JSON
    print(json_string)
