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
    if sys.platform == "darwin":  # macOS
        return os.popen("mdls -raw -name kMDItemVersion /Applications/grandMA3.app").read().strip()
    if sys.platform == "win32":  # Windows
        return os.popen(
            'wmic datafile where name="C:\\\\Program Files\\\\MALightingTechnology\\\\ma3\\\\gma3.exe" get Version /value'
        ).read().strip().split('=')[-1].strip()
    else:
        print("Unsupported platform.")
    return ""


def extract_latest_version(html_content: str) -> str:
    """
    Extract the latest version of grandMA3 software from the webpage content.
    :param html_content: HTML content of the webpage
    :return: Latest version string
    """
    soup = BeautifulSoup(html_content, "html.parser")
    version_elements = soup.find_all("tr", class_="downloads-table__sub-header js-download-search-sub-header")

    if version_elements:
        # Extract the version from the first (latest) entry
        latest_version = version_elements[0].text.strip()
        return latest_version
    return "Unknown"


if __name__ == "__main__":
    """
    Main program to fetch and compare installed and latest version.
    """
    print("Checking for grandMA3 software updates...\n")
    # Fetch latest version from website
    html_page = fetch_webpage_content(GRANDMA3_DOWNLOAD_URL)

    if html_page:
        latest_version = extract_latest_version(html_page)
        print(f"Latest available version on the website: {latest_version}")

        # Get the currently installed version
        installed_version = get_installed_version()
        print(f"Installed version: {installed_version}")

        # Compare versions and notify user
        if latest_version and installed_version:
            if installed_version == latest_version:
                print("\nYou already have the latest version installed!")
            else:
                print("\nA newer version is available! Please update your software.")
        else:
            print(
                "\nCould not compare versions. Please ensure the application is installed correctly, or check the "
                "website manually.")
    else:
        print("\nFailed to fetch the latest version. Please check your internet connection or the MA Lighting website.")
