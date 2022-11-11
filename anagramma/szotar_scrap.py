import encodings.utf_8

import requests
from bs4 import BeautifulSoup


kimeneti_file = open('szotar.txt', 'a')

"""
abc = ('a', 'aa', 'b', 'c', 'cs', 'd', 'dz', 'e', 'ee', 'f', 'g', 'gy', 'h', 'i',
       'ii', 'j', 'k', 'l', 'ly', 'm', 'n', 'o', 'oo', 'oe', 'ooe', 'p', 'q', 'r',
       's', 'sz', 't', 'ty', 'u', 'uu', 'ue', 'uue', 'v', 'W', 'x', 'y', 'z', 'zs')
"""
abc = ('w', 'x', 'y',)
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

url = 'https://szotar.com/szokereso/kezdobetu/'

i = 1
for page in abc:
    req_betu = requests.get(url + page, headers)
    # print(req)
    # print(req.encoding)
    soup_betu = BeautifulSoup(req_betu.content, 'html5lib')
    # print("Encoding: ", soup.original_encoding)
    oldalszoveg = soup_betu.find_all('span')
    kovlink = oldalszoveg[8].findNext().get('href')
    print(kovlink)
    for szo in soup_betu.find_all('li', attrs={'role': 'presentation'}):
        print("{}; {}".format(i, szo.text))
        irom = szo.text+'\n'
        kimeneti_file.write(irom)
        i += 1
    while kovlink is not None:
        req_szamos = requests.get(kovlink, headers)
        soup2 = BeautifulSoup(req_szamos.content, 'html5lib')
        oldalszoveg = soup2.find_all('span')
        kovlinkkov = oldalszoveg[8].findNext().get('href')
        print(kovlinkkov)
        kovlink = kovlinkkov
        for szo in soup2.find_all('li', attrs={'role': 'presentation'}):
            print("{}; {}".format(i, szo.text))
            irom = szo.text+'\n'
            kimeneti_file.write(irom)
            i += 1

kimeneti_file.close()
# Making GET request
#  r = requests.get(url, headers)

# show connection info
#  print(r)

# parsing HTML
#  soup = BeautifulSoup(r.content, 'html.parser')

# print everything
#  print(soup.prettify())

"""
s = soup.find('ul', class_='list-group')
linkek = s.find_all('a')
linkek_lista = []
for line in linkek:
    print(line)
    linkek_lista.append(line)
#print(linkek_lista)
"""
