#!/usr/bin/python3
"""
This is a module that converts a Markdown file to HTML.
"""

import sys
import os

def markdown2html():
    """
    This function checks if the number of arguments is less than 2 and if the Markdown file exists.
    If either of these conditions is not met, it prints an error message to STDERR and exits with status code 1.
    Otherwise, it does nothing and exits with status code 0.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        print("Missing " + markdown_file, file=sys.stderr)
        sys.exit(1)

    # If the Markdown file exists, do nothing and exit with status code 0
    sys.exit(0)

if __name__ == "__main__":
    markdown2html()