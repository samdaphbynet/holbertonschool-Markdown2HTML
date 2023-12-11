#!/usr/bin/python3

"""Convert Markdown file to Html"""

import os
import sys
import markdown


# Convert a Markdown file to HTML and save the result in an output file.
def convertMarkdownToHtml(markdown_file, output_file):
    """
    Convert a Markdown file to HTML and save the result in an output file.

    Args:
        markdown_file (str): The path to the Markdown input file.
        output_file (str): The path to the HTML output file.

    Raises:
        FileNotFoundError: If the specified Markdown file does not exist.

    Returns:
        None
    """
    try:
        # Open the Markdown file and read its content
        with open(markdown_file, 'r') as md_file:
            markdown_content = md_file.read()

            # Convert Markdown to HTML
            html_content = markdown.markdown(markdown_content)

            # Open the output file and write the HTML content
            with open(output_file, 'w') as html_file:
                html_file.write(html_content)

    except FileNotFoundError:
        # Handle the case where the specified Markdown file is not found
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py <markdown_file> <output_file>",
              file=sys.stderr)
        sys.exit(1)

    # Check if the specified Markdown file exists
    if not os.path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    # Convert the Markdown file to HTML
    convertMarkdownToHtml(sys.argv[1], sys.argv[2])

    # Exit with success status
    sys.exit(0)
