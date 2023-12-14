#!/usr/bin/python3
"""
This is a module that converts a Markdown file to HTML.
"""

import sys
import os
import re
import markdown

def markdown2html():
    """
    This function checks if the number of arguments is less than 2 and if the Markdown file exists.
    If either of these conditions is not met, it prints an error message to STDERR and exits with status code 1.
    Otherwise, it reads the Markdown file, converts the headings to HTML, writes the result to the HTML file, and exits with status code 0.
    """
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(markdown_file):
        print("Missing " + markdown_file, file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as f:
        lines = f.read()
        html = markdown.markdown(lines)

        with open(html_file, 'w') as f:
            f.write(html)

    # If the Markdown file exists and is successfully converted to HTML, do nothing and exit with status code 0
    sys.exit(0)

if __name__ == "__main__":
    markdown2html()