#  main.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 05. 19. 11:55

import requests
from bs4 import BeautifulSoup


def get_page(url):
    try:
        page = requests.get(url)
        page.raise_for_status()
        return page.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None


def get_links(page):
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.find_all('a')
    return links


def get_class(page, cssclass):
    soup = BeautifulSoup(page, 'html.parser')
    class_ = soup.find_all(class_=cssclass)
    #print(class_)
    return class_


def get_bold(page):
    soup = BeautifulSoup(page, 'html.parser')
    bold = soup.find_all('b')
    return bold


oldal_url = "https://ageofempires.fandom.com/wiki/Cheat_code_(Age_of_Empires)"
soup = get_page(oldal_url)
css_class = get_class(soup, "mw-content-ltr mw-parser-output")


print(css_class)
