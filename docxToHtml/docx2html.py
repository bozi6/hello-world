#!/usr/bin/python3
import mammoth

# Constants for better readability and reuse
INPUT_FILE = "21.09.27.-10.03.docx"
OUTPUT_FILE = INPUT_FILE[:-4] + "html"

CUSTOM_STYLES = """
table => table.table.table-bordered.table-striped.shadow.bg-light
#r => p.text-light.bg-dark
p => p.my-1.px-1.mx-5
"""

HTML_START_TEMPLATE = """<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>{title}</title>
"""

BOOTSTRAP_CSS = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">\n'
BOOTSTRAP_JS = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous"></script>\n'
HTML_BODY_START = '</head><body><div class="container-fluid px-3 pb-5"><br><br>'
HTML_BODY_END = "</div></body></html>"


def replace_html(content, to_replace, replace_with):
    """Replace a substring in HTML content."""
    return content.replace(to_replace, replace_with)


def process_html(html_content):
    """Process and format HTML content."""
    # Adjust table cells and add new lines for readability
    html_content = html_content.replace("<td>\n<p>", "<td>").replace("</p>\n</td>", "</td>")

    # Replace <strong> with <b>
    html_content = html_content.replace("strong", "b")

    # Add a new line after bold text inside table cells
    html_content = html_content.replace("</b>", "<br></b>")

    # Insert new line for other tags for better structure
    html_content = replace_html(html_content, "><", ">\n<")
    return html_content


def main():
    """
    Converts a .docx file to HTML using Mammoth.
    """
    # Generate HTML from the input file
    with open(INPUT_FILE, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file, style_map=CUSTOM_STYLES)
        html_content = result.value
        print("Conversion messages: ", result.messages)

    # Process the generated HTML
    formatted_html = process_html(html_content)

    # Combine all parts to form final HTML
    final_html = HTML_START_TEMPLATE.format(
        title=INPUT_FILE) + BOOTSTRAP_CSS + HTML_BODY_START + formatted_html + BOOTSTRAP_JS + HTML_BODY_END

    # Write the final HTML to the output file
    with open(OUTPUT_FILE, "w", encoding="utf8") as html_file:
        html_file.write(final_html)


if __name__ == "__main__":
    main()
