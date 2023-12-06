#!/bin/env python3
"""
Nézőtéri feladatok, saját mgeoldással
"""


class NezoTer:
    """
    Nézőtéri osztály, székekkel, meg széksorokkal, meg foglaltsággal.
    """

    szekszam: int = 0
    sorokszama: int = 0
    fogkat = []
    katstat = dict()
    foglalt: int = 0
    # (Sor,szék,foglalt,kategória)

    def __init__(self, foglfile, katfile):
        self.file1 = foglfile
        self.file2 = katfile
        self.setSor()
        self.setFogkat()
        self.getbev()

    def setFogkat(self):
        """Foglaltság és kategória fájlok beolvasása, és áthelyzése a fogkat listába"""
        with open(self.file1, "r") as foglaltsag, open(
            self.file2, "r"
        ) as kateg:  # foglalt.txt sorokba
            for sor, egysor in enumerate(foglaltsag):
                egysor = egysor.strip()
                katsor = next(kateg).strip()
                for i in range(len(egysor)):  # fogkat = [sor,szék,foglalt,árkategória]
                    NezoTer.fogkat.append([sor + 1, i + 1, egysor[i], int(katsor[i])])

    def getFogkat(self):
        """Foglalt kategória lekérése"""
        cols = tuple(NezoTer.fogkat)
        print(cols)

    def getFoglalt(self, sorszam, szekszam):
        """Összes foglalt hely visszaadása"""
        with open(self.file1, "r") as sor:
            for idx, egysor in enumerate(sor):
                if idx == sorszam:
                    for idsz, szekek in enumerate(egysor):
                        if idsz == szekszam:
                            if szekek == "x":
                                return "\t{}. sor, {}. szék foglalt.".format(
                                    sorszam, szekszam
                                )
                            else:
                                return "\t{}. sor, {}. szék szabad.".format(
                                    sorszam, szekszam
                                )
                # return 'Foglalt helyek összesen: {} db'.format(NezoTer.foglalt)

    def setSor(self):
        """Nézőtéri szekszam és sorokszáma feltöltése, meg a foglaltság feltöltése is"""
        with open(self.file1, "r") as sor:
            for egysor in sor:
                NezoTer.szekszam += len(egysor)
                NezoTer.sorokszama += 1
                for szek in egysor:
                    if szek == "x":
                        self.foglalt += 1

    def getSor(self):
        """Nézőtéri sorok számának visszaadása"""
        return "Sorok száma a nézőtéren: {} db".format(NezoTer.sorokszama)

    def getSzek(self):
        """Nézőtéri székek visszadaása"""
        return "Összes szék száma: {} db".format(NezoTer.szekszam)

    def hanyjegyet(self):
        """
        Eladott jegyeket kiszámolja
        :return: Az eladott jegyek db.
        """
        # fogkat = [sor,szék,foglalt,árkategória]
        eladott = 0
        for fogl in self.fogkat:
            if fogl[2] == "x":
                eladott += 1
        return eladott

    def eladottszazalek(self):
        """Eladott jegyek százalékban"""
        return round((100 / NezoTer.szekszam) * self.foglalt)

    def getKatRog(self):
        """
        Árkategória szerint
        :return: kategoria
        """
        # fogkat = [sor,szék,foglalt,árkategória]
        for kateglist in NezoTer.fogkat:
            if kateglist[2] == "x":
                kateg = kateglist[3]
                NezoTer.katstat[kateg] = NezoTer.katstat.get(kateg, 0) + 1
        legtobb = max(NezoTer.katstat.values())
        for kategoria, db in NezoTer.katstat.items():
            if db == legtobb:
                return kategoria

    def getbev(self):
        """Bevétel kiszámolása"""
        bevetel: int = 0
        arak = (5000, 4000, 3000, 2000, 1500)
        for kat, db in NezoTer.katstat.items():
            bevetel += arak[kat - 1] * db
        return bevetel

    def egyeduliek(self):
        """
        Egyedüli székek
        :return:
        """
        egyeduli: int = 0
        for egysor in self.fogkat:
            ures_szakasz = 0
            # fogkat = [sor,szék,foglalt,árkategória]
            if egysor[2] == "o":
                ures_szakasz += 1
            else:
                if ures_szakasz == 1:
                    egyeduli += 1
                ures_szakasz = 0
            if ures_szakasz == 1:
                egyeduli += 1
        return egyeduli


def main():
    """
    Főporgram
    :return: Null
    """
    nezoter = NezoTer("foglaltsag.txt", "kategoria.txt")
    print("1. feladat...")
    print("\tBeolvasva eltárolva.")
    # print(nezoter.getFogkat())  # Az egész tömb kiíratása.
    try:
        # ssz = int(input("\tAdja meg a sor számát:"))
        ssz = 5
        # szksz = int(input("\tAdja meg a szék számát:"))
        szksz = 5
        print("2.feladat...")
        print(nezoter.getFoglalt(ssz, szksz))
    except ValueError:
        print("Egész számot tessék megadni.")
    # print(nezoter.getSor())
    # print(nezoter.getSzek())
    print("3. feladat...")
    print(
        "\tAz előadásra eddig {} jegyet adtak el, ez a nézőtér {}%-a.".format(
            nezoter.hanyjegyet(), nezoter.eladottszazalek()
        )
    )
    print("4.feladat...")
    print(
        "\tA legtöbb jegyet a {}. árkategóriában rögzítették.".format(
            nezoter.getKatRog()
        )
    )
    print("5. feladat...")
    print("A színház bevétele: {} Ft.".format(nezoter.getbev()))
    print("6. feladat...")
    print("Az egyedülálló helyek száma: {}".format(nezoter.egyeduliek()))


if __name__ == "__main__":
    main()
