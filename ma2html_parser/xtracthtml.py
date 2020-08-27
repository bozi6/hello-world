
from bs4 import BeautifulSoup


file = open('C:\\ProgramData\\MA Lighting Technologies\\grandma\\gma2_V_3.9.51\\lang\\hu\\help\\structure.html', 'r')
soup = BeautifulSoup(file, 'html.parser')
for x in soup.find_all('li'):
    print(x.attrs['id'])
    print(x.attrs['rel'])
    print(x.attrs['data-id'])
    print(x.attrs['title'])
    print(x.contents[0])
    print(x.attrs['data-keyword'])



