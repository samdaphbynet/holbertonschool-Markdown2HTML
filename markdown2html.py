#!/usr/bin/python3
"""
Markdown to HTML Converter
convert heading
"""

from os.path import isfile
import sys
import markdown


def file_exist(argv):
    """Verify if the necessary files exist and if the correct number of arguments are provided."""
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not isfile(argv[1]):
        print("Missing " + argv[1], file=sys.stderr)
        sys.exit(1)


def markdown_to_html(markdown_file, output_file):
    """Converts a Markdown file to HTML."""
    try:
        # Open the Markdown file and read its content
        with open(markdown_file, 'r') as md_file:
            markdown_content = md_file.read()

            # Convert Markdown to HTML with extra extensions
            html_content = markdown.markdown(
                markdown_content,
                extensions=['markdown.extensions.extra']
            )

            # Open the output file and write the HTML content
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)

    except FileNotFoundError:
        # Handle the case where the specified Markdown file is not found
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    file_exist(sys.argv)
    markdown_to_html(sys.argv[1], sys.argv[2])
