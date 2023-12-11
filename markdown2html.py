#!/usr/bin/env python3

"""
    script markdown2html.py that takes an argument 2 strings:

            First argument is the name of the Markdown file
            Second argument is the output file name
"""

import os
import sys
import markdown

def convertMarkdownToHtml(markdown_file, output_file):
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_content = md_file.read()
            html_content = markdown.markdown(markdown_content)

            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
                print(f"Missing {markdown_file}", file=sys.stderr)
    except FileNotFoundError:
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)


    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
    
    convertMarkdownToHtml(sys.argv[1], sys.argv[2])
    sys.exit(0)