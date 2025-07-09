#  imgdownloader.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 07. 09. 15:31

import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# A cél URL megadása
url = 'https://books.toscrape.com/'

# Mappa létrehozása a képeknek
folder = "downloaded"
os.makedirs(folder, exist_ok=True)

# HTML letöltése
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Képek keresése
img_tags = soup.find_all("img")

print(f"{len(img_tags)} kép találva.")

# Képek letöltése
for img in img_tags:
    img_url = img.get("src")
    if not img_url:
        continue

    # Teljes URL létrehozása, ha relatív
    full_url = urljoin(url, img_url)

    # Fájlnév meghatározása
    filename = os.path.basename(urlparse(full_url).path)
    if not filename:
        filename = "unnamed.jpg"

    filepath = os.path.join(folder, filename)

    try:
        img_data = requests.get(full_url).content
        with open(filepath, "wb") as f:
            f.write(img_data)
        print(f"✔ Letöltve: {filename}")
    except Exception as e:
        print(f"✘ Hiba a(z) {full_url} letöltésekor: {e}")
