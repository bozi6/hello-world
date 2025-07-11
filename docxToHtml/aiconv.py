#!/usr/bin/python3
import mammoth

# Constants for file paths and styles
INPUT_FILE = "21.09.27.-10.03.docx"
OUTPUT_FILE = INPUT_FILE[:-5] + ".html"

CUSTOM_STYLES = """
table => table.table.table-bordered.table-striped.shadow.bg-light
p => p.my-1.px-1.mx-5
"""

HTML_START_TEMPLATE = """<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=0.8, shrink-to-fit=no">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl"
          crossorigin="anonymous">
</head>
<body>
<div class="container-fluid px-3 pb-5"><br><br>
"""

HTML_END_TEMPLATE = """
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0"
        crossorigin="anonymous"></script>
</body>
</html>
"""


def process_html(html_content):
    """
    Processes the raw HTML content to match the required format.
    """
    html_content = html_content.replace("<td>\n<p>", "<td>").replace("</p>\n</td>", "</td>")
    html_content = html_content.replace("<strong>", "<b>").replace("</strong>", "</b>")
    return html_content.replace("><", ">\n<")  # Insert new lines for better formatting


def convert_docx_to_html(input_file, output_file):
    """
    Converts a .docx file to HTML format.
    """
    # Parse the .docx file
    with open(input_file, "rb") as docx_file:
        result = mammoth.convert_to_html(docx_file, style_map=CUSTOM_STYLES)

    # Process the raw HTML
    rendered_html = process_html(result.value)
    full_html = HTML_START_TEMPLATE.format(title=input_file) + rendered_html + HTML_END_TEMPLATE

    # Save the generated HTML to the output file
    with open(output_file, "w", encoding="utf8") as html_file:
        html_file.write(full_html)

    # Log conversion messages (if any)
    print("Conversion messages:", result.messages)


if __name__ == "__main__":
    convert_docx_to_html(INPUT_FILE, OUTPUT_FILE)
