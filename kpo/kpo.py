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
        self.pont = 0

    def addpont(self):
        self.pont += 1

    def reset(self):
        self.pont = 0


class Papir:
    def __init__(self):
        self.num = 2
        self.uti = 1
        self.kb = 3
        self.nev = "Papír"
        self.pont = 0

    def addpont(self):
        self.pont += 1

    def reset(self):
        self.pont = 0


class Ollo:
    def __init__(self):
        self.num = 3
        self.uti = 2
        self.kb = 1
        self.nev = "Olló"
        self.pont = 0

    def addpont(self):
        self.pont += 1

    def reset(self):
        self.pont = 0


def main():
    ko = Ko()
    papir = Papir()
    ollo = Ollo()
    targyak = [ko, papir, ollo]
    iteraciok = 1000000
    for i in range(iteraciok):
        egy = random.choice(targyak)
        ketto = random.choice(targyak)
        if egy.num == ketto.num:
            ketto = random.choice(targyak)
        # print(f"{egy.nev} VS {ketto.nev}")
        if egy.num == ketto.uti:
            # print(f"A(z) {ketto.nev} kiütötte a(z) {egy.nev}-t")
            ketto.addpont()
        if ketto.num == egy.uti:
            # print(f"A(z) {egy.nev} kiütötte a(z) {ketto.nev}-t")
            egy.addpont()
    print(iteraciok, " iterációból.")
    for i in targyak:
        print(f"{i.nev} - {i.pont:,.0f} db.")


if __name__ == "__main__":
    main()
