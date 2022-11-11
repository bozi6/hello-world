import requests
from bs4 import BeautifulSoup

# Making get request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# show connection info
print(r)

# parsing HTML
soup = BeautifulSoup(r.content, 'html.parser')

# find all the anchor tags with "href"
# for link in soup.find_all('a'):
#    print(link.get('href'))

# extract images
images_list = []

images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})

for image in images_list:
    print(image)
