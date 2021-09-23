#!/usr/bin/python3
import mammoth

befile = "21.09.27.-10.03.docx"
outfile = "output.html"


def htmlcser(bej, mit, mire):
    return bej.replace(mit, mire)


custom_styles = """
                table => table.table.table-bordered.table-striped.shadow
                #r => p.text-light.bg-dark
                #a pt lecseréli td class p re majd beszúr egy mt-0 class text-centert
                p => p.py-1
                #p => td.p > mt-0.text-center
                #r => tr.w-25.p-3
                """
htmlkezd = '''<!DOCTYPE html>
    <html lang="hu">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Próbatábla</title>\n
    '''
bootstrap_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">\n'
bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>\n'
headerend = '</head><body><div class="container"><br><br>'
htmlveg = "</div></body></html>"

with open(befile, 'rb') as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map=custom_styles)
    html = result.value
    messages = result.messages

# html új sorok beszúrása
ker = "><"
cser = ">\n<"
"".join(html.split())
html = html.replace(ker, cser)
html = html.replace('</strong>', '</strong>\n<br />\n')

edited_html = htmlkezd + bootstrap_css + headerend + html + bootstrap_js + htmlveg
print("Hibaüzik: ", result.messages)
with open(outfile, 'w') as html_file:
    html_file.write(edited_html)
