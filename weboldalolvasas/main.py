#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = 'https://www.malighting.com/downloads/products/grandma3/'
res = requests.get(url)
html_page = res.content

soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
output = []
blacklist = [
    '[document]',
    'header',
    'html',
    'meta',
    'head',
    'input'
    'script'

]

for t in text:
    if t.parent.name not in blacklist:
        output.append(t)
if output[112][-10:] == "2022-05-16":
    print("faszom régi\n Azért itt van amit találtam: ")
    print(output[112], output[106])
else:
    print("Valami újabb dolog történt\nEz van most: ")
    print(output[112], output[106])
