#!/usr/bin/python3
"""
Markdown to HTML Converter
convert heading
"""

from os.path import isfile
import sys

def file_exist(argv):
    """Verify if the necessary files exist and if the correct number of arguments are provided."""
    if len(argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not isfile(argv[1]):
        print("Missing " + argv[1], file=sys.stderr)
        sys.exit(1)

def markdown_to_html(md_file, html_file):
    """Converts a Markdown file to HTML."""
    try:
        with open(md_file, 'r') as f:
            lines = f.readlines()

        with open(html_file, 'w') as f:
            in_ul = False
            in_ol = False
            in_para = False
            
            for index in range(len(lines)):
                line = lines[index].rstrip("\n")
                next_line = lines[index + 1].rstrip("\n") if index + 1 < len(lines) else ''
                
                # Closing tags if needed before starting new ones
                if line.startswith(('#', '-', '*')) and in_para:
                    f.write('</p>\n')
                    in_para = False
                if line.startswith(('#', '')) and in_ul:
                    f.write('</ul>\n')
                    in_ul = False
                if line.startswith(('#', '')) and in_ol:
                    f.write('</ol>\n')
                    in_ol = False
                
                # Processing lines
                if line.startswith('#'):
                    level = line.count('#')
                    heading = line.strip('#').strip()
                    html_heading = f'<h{level}>{heading}</h{level}>'
                    f.write(html_heading + '\n')
                elif line.startswith('-'):
                    if not in_ul:
                        f.write('<ul>\n')
                        in_ul = True
                    list_item = line.strip('-').strip()
                    f.write(f'<li>{list_item}</li>\n')
                elif line.startswith('*'):
                    if not in_ol:
                        f.write('<ol>\n')
                        in_ol = True
                    list_item = line.strip('*').strip()
                    f.write(f'<li>{list_item}</li>\n')
                elif line:
                    if not in_para:
                        f.write('<p>\n')
                        in_para = True
                    if next_line == '' or next_line.startswith(('#', '-', '*')):
                        f.write(f'{line}\n')
                        f.write('</p>\n')
                        in_para = False
                    else:
                        f.write(f'{line}<br/>\n')
                else:
                    if in_para:
                        f.write('</p>\n')
                        in_para = False

            # Close any open tags at the end of file
            if in_ul:
                f.write('</ul>\n')
            if in_ol:
                f.write('</ol>\n')
            if in_para:
                f.write('</p>\n')

    except IOError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    file_exist(sys.argv)
    markdown_to_html(sys.argv[1], sys.argv[2])