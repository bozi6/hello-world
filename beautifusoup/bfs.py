import requests
from bs4 import BeautifulSoup

result = requests.get('https://www.google.com')
print(result.status_code)
#print(result.headers)
src = result.content
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all("a")
#print(links)
# Perhaps we just want to extract the link that has contains th text
# "About" on the page instead of every link. We can use the built-in
# "text" function to access the text content between the <a> </a>
# tags,
for link in links:
    if "Rólunk" in link.text:
        print(link)
        print(link.attrs['href'])
