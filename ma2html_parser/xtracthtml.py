
from bs4 import BeautifulSoup


file = open('C:\\ProgramData\\MA Lighting Technologies\\grandma\\gma2_V_3.9.51\\lang\\hu\\help\\structure.html', 'r')
html_doc = file
soup = BeautifulSoup(html_doc, 'html.parser')

for x in soup.ul.li:
    try:
        print(x.attrs)
    except AttributeError:
        x.next_sibling()

