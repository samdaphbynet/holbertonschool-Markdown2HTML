#!/usr/bin/python3
""" Markdown to HTML Converter """

from os.path import isfile
import sys
import markdown


def markdown_to_html(markdown_file, output_file):
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not isfile(sys.argv[1]):
        print("Missing " + sys.argv[1], file=sys.stderr)
        sys.exit(1)
    try:
        # Read the file and convert it to HTML
        with open(markdown_file, 'r') as md_file:
            markdown_content = md_file.read()
            html_content = markdown.markdown(markdown_content,
                extensions=['markdown.extensions.extra'])
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)

    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    markdown_to_html(sys.argv[1], sys.argv[2])
