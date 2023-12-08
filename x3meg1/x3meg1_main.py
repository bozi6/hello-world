import random

import matplotlib.pyplot as plt


def main():
    """
    MAthplotlib-el rajzolunk

    :return: Rajzocska
    :rtype: object

    """
    vonalszin = [
        "blue",
        "red",
        "yellow",
        "green",
        "black",
        "gray",
        "autumn",
        "bone",
        "cool",
        "copper",
        "flag",
        "hot",
        "hsv",
        "jet",
        "pink",
        "prism",
        "spring",
        "summer",
        "winter",
    ]
    plt.title("Ha az x páratlan akkor (x * 3 + 1), ha páros akkor (x / 2)")
    rajz = []
    for i in range(1000):  # Minták száma
        szam = random.randint(1, 10)
        rajz.append(szam)
        #  print(i, szam)
        while szam > 1:
            if (szam % 2) == 1:
                szam = szam * 3 + 1
            else:
                szam = szam // 2
            rajz.append(szam)
        plt.plot(rajz, label="számok", color=random.shuffle(vonalszin))
        rajz.clear()
    plt.xlabel("Lépések")
    plt.ylabel("Számok")
    plt.show()
