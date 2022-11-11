import requests
from bs4 import BeautifulSoup as bs
import csv

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

URL = 'https://www.geeksforgeeks.org/page/1'

req = requests.get(URL, headers)
print(req)
soup = bs(req.text, 'html.parser')

titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []

# fill titles list
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text.strip()
    count += 1
    titles_list.append(d)

# write csv file
filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['Title Number', 'Title Name'])
    w.writeheader()

    w.writerows(titles_list)
