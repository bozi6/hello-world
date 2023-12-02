#!/usr/bin/python3
import requests
import os
import sys
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

"""
Get current grandMA3 application version
from malihting.com websites, and compare
with installed version.
"""

url = "https://www.malighting.com/downloads/products/grandma3/"


def oldallekeres(oldalcim):
    """
    Try to get the website
    :param oldalcim: url of the requested site
    :return: content of the site
    """
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.content
    except HTTPError as http_err:
        print(f"HTTP hiba történt: {http_err}")
    except Exception as err:
        print(f"Más hiba történt: {err}")


def getverzion() -> object:
    """
    Get current version of installed application
    :return: Application version string
    """
    if sys.platform == "darwin":
        stream = os.popen('mdls -raw -name kMDItemVersion /Applications/grandMA3.app')
        AppVersion: str = stream.read()
    elif sys.platform == "nt":
        stream = os.popen('wmic datafile where name="C:/Program Files/MALightingTechnology/ma3/gma3.exe"'
                          ' get Version /value')
        AppVersion: str = stream.read()
    else:
        AppVersion = ''
    return AppVersion


def main():
    """
        Main program, gets the website and
        find the current version of it then
        compare with installed version, and
        print if it is the same, or the different version
        """
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


if __name__ == "__main__":
    main()
