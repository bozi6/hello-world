#  kpo.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 03. 24. 9:49

import random


class Ko:
    def __init__(self):
        self.num = 1
        self.uti = 3
        self.kb = 2
        self.nev = "Kaics"


class Papir:
    def __init__(self):
        self.num = 2
        self.uti = 1
        self.kb = 3
        self.nev = "Papír"


class Ollo:
    def __init__(self):
        self.num = 3
        self.uti = 2
        self.kb = 1
        self.nev = "Olló"


def prog():
    ko = Ko()
    papir = Papir()
    ollo = Ollo()
    targyak = [ko, papir, ollo]
    for i in range(3):
        egy = random.choice(targyak)
        ketto = random.choice(targyak)
        if egy.num == ketto.num:
            ketto = random.choice(targyak)
        print(f"{egy.nev} VS {ketto.nev}")
        if egy.num == ketto.uti:
            print(f"A(z) {ketto.nev} kiütötte a(z) {egy.nev}-t")
        if ketto.num == egy.uti:
            print(f"A(z) {egy.nev} kiütötte a(z) {ketto.nev}-t")


if __name__ == "__main__":
    prog()
