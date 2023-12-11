#!/usr/bin/python3
"""
Markdown to HTML Converter
Task 1: convert heading
"""

import sys
import os
import markdown

def convert_markdown_to_html(markdown_file, output_file):
    """Check if the Markdown file exists"""
    if not os.path.exists(markdown_file):
        sys.stderr.write("Missing " + markdown_file + "\n")
        exit(1)

    with open(markdown_file, 'r') as md_file:
        """read Markdown file"""
        markdown_content = md_file.read()
        html_content = markdown.markdown(
            markdown_content,
            extensions=['markdown.extensions.nl2br'])

        with open(output_file, 'w') as html_file:
            """write Markdown"""
            html_file.write(html_content)


if __name__ == "__main__":
    """Check if the correct number of arguments is provided"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html")
        exit(1)

    convert_markdown_to_html(sys.argv[1], sys.argv[2])
    sys.exit(0)
