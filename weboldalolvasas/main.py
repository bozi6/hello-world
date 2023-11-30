#!/usr/bin/python3
import requests
import os
import sys
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

url = "https://www.malighting.com/downloads/products/grandma3/"


def oldallekeres(oldalcim):
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.content
    except HTTPError as http_err:
        print(f"HTTP hiba történt: {http_err}")
    except Exception as err:
        print(f"Más hiba történt {err}")


def getverzion() -> object:
    if sys.platform == "darwin":
        stream = os.popen('mdls -raw -name kMDItemVersion /Applications/grandMA3.app')
        verzio: str = stream.read()
    return verzio


if __name__ == "__main__":
    html_page = oldallekeres(url)
    soup = BeautifulSoup(html_page, 'html5lib')
    text = soup.find_all("tr", class_="downloads-table__sub-header js-download-search-sub-header")

    output = ''

    verzio = getverzion()

    for t in text:
        output += t.text

    print("Meglévő verzió az applikációból: {}\n".format(verzio), "-" * 80)
    if output.find(verzio) != -1:
        print("Már megvan.")
        print("-" * 80)
        print("Azért itt van amit találtam: \n{}".format(output))
    else:
        print("Újabb verzió elérhető\nEz van most: ")
        print(output)
