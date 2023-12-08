import requests
from bs4 import BeautifulSoup

"""
Weboldal részleteinek kiiratása

"""


def main():
    """
    Főprogram

    :return: weboldal csak szöveges részének kiíratása
    :rtype: str

    """
    # Making a GET request
    r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

    # check status code for response received
    # success code - 200
    print(r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, "html.parser")
    """
    # Getting the title tag
    print(soup.title)
    
    # Getting the name of the tag
    print(soup.title.name)
    
    # Getting the name of parent tag
    print(soup.title.parent.name)
    
    # minden kiiratása
    print(soup.prettify())
    
    # Making GET request
    r = requests.get(url, headers)
    
    # show connection info
    print(r)
    
    # parsing HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # print everything
    print(soup.prettify())
    
    
    s = soup.find('ul', class_='list-group')
    linkek = s.find_all('a')
    linkek_lista = []
    for line in linkek:
        print(line)
        linkek_lista.append(line)
    #print(linkek_lista)
    """

    s = soup.find("div", class_="entry-content")

    lines = s.find_all("p")

    for line in lines:
        print(line.text.strip())


if __name__ == "__main__":
    main()
