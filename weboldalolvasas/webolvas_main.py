#!/usr/bin/python3
import requests
import os
import sys
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

# Constant
GRANDMA3_DOWNLOAD_URL = "https://www.malighting.com/downloads/products/grandma3/"


def fetch_webpage_content(url: str) -> str:
    """
    Fetch the content of the website.
    :param url: URL of the requested site
    :return: Content of the site as a string
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return ""


def get_installed_version() -> str:
    """
    Get the current installed version of the application.
    :return: Application version string
    """
    if sys.platform == "darwin":
        return os.popen("mdls -raw -name kMDItemVersion /Applications/grandMA3.app").read().strip()
    if sys.platform == "nt":
        return os.popen(
            'wmic datafile where name="C:/Program Files/MALightingTechnology/ma3/gma3.exe" get Version /value'
        ).read().strip()
    return ""


def print_separator():
    """Print a separator line for better readability in output."""
    print("-" * 80)


if __name__ == "__main__":
    """
    Main program: gets the website, fetches the current version,
    compares it with the installed version, and prints the result.
    """
    html_page = fetch_webpage_content(GRANDMA3_DOWNLOAD_URL)
    soup = BeautifulSoup(html_page, "html5lib")

    download_rows = soup.find_all(
        "tr", class_="downloads-table__sub-header js-download-search-sub-header"
    )
    available_versions_text = "\n".join(row.text for row in download_rows)
    installed_version = get_installed_version()

    print(f"Installed version from the application: {installed_version}\n")
    print_separator()
    if installed_version in available_versions_text:
        print("The latest version is already installed.")
    else:
        print("A newer version is available!")
        print(f"Currently available versions: \n{available_versions_text}")
    print_separator()
