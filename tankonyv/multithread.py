import json
import time
from threading import Thread
from urllib.request import urlopen

CITIES = [
    "Budapest",
    "Pecs",
    "Debrecen",
    "Miskolc",
    "Nyiregyhaza",
    "Sopron",
    "Gyor",
    "Szombathely",
]


class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.temperature = None
        self.city = city

    def run(self):
        """
        Hőmérséklet lekérdezése az openweathermapról

        :return: a hőmérésklet eredméye
        :rtype: list

        """
        """API key is: 50780273338917e2854cb8a68ef9fcf1"""
        api_key = "50780273338917e2854cb8a68ef9fcf1"
        url_template = "http://api.openweathermap.org/data/2.5/weather?q={},hu&units=metric&appid={}&lang=hu"
        response = urlopen(url_template.format(self.city, api_key))
        data = json.loads(response.read().decode())
        self.temperature = data["main"]["temp"]


def main():
    threads = [TempGetter(c) for c in CITIES]
    start = time.time()
    for thread in threads:
        print(thread.name, "started")
        thread.start()

    for thread in threads:
        print(thread.name, " joined back")
        thread.join()

    for thread in threads:
        print("{0.temperature:.0f} C° van {0.city}-en".format(thread))
    print(
        "{} hőmérsékleti érték lekérdezve {} másodperc alatt".format(
            len(threads), time.time() - start
        )
    )


if __name__ == "__main__":
    main()
