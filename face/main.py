from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

GROUP_URL = "https://www.facebook.com/groups/396809868538303"
SCROLL_COUNT = 10
WAIT_BETWEEN_SCROLLS = 3

# Brave-specifikus beállítás
BRAVE_PATH = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

options = Options()
options.binary_location = BRAVE_PATH
options.add_argument("--start-maximized")

# Indítás Brave-vel
driver = webdriver.Chrome(options=options)

driver.get(GROUP_URL)
input("Lépj be kézzel, majd nyomj Entert...")

# Görgetés és bejegyzés mentés
for i in range(SCROLL_COUNT):
    print(f"Görgetés {i+1}/{SCROLL_COUNT}")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(WAIT_BETWEEN_SCROLLS)

posts = driver.find_elements(By.XPATH, "//div[@role='article']")
print(f"{len(posts)} bejegyzés találva.")

with open("fb_posts.txt", "w", encoding="utf-8") as f:
    for idx, post in enumerate(posts):
        try:
            content = post.text
            if content.strip():
                f.write(f"--- BEJEGYZÉS {idx+1} ---\n")
                f.write(content + "\n\n")
        except Exception as e:
            print(f"Hiba a {idx+1}. bejegyzésnél: {e}")

driver.quit()
print("Kész! Mentve: fb_posts.txt")
