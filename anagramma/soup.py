import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
# print(soup.title)

# Getting the name of the tag
# print(soup.title.name)

# Getting the name of parent tag
# print(soup.title.parent.name)

# minden kiiratása
# print(soup.prettify())

s = soup.find('div', class_='entry-content')

lines = s.find_all('p')

for line in lines:
    print(line.text)