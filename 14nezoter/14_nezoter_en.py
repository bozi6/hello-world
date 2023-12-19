#!/bin/env python3
"""
Nézőtéri feladatok, saját mgeoldással

"""


class NezoTer:
    """
    Nézőtéri osztály, székekkel, meg széksorokkal, meg foglaltsággal, meg árakkal.
    """

    file2: str = None
    file1: str = None
    szekszam: int = 0
    sorokszama: int = 0
    fogkat: list = []
    katstat = dict()
    foglalt: int = 0
    jegyarak: dict = (5000, 4000, 3000, 2000, 1500)
    # (Sor,szék,foglalt,kategória)

    def __init__(self, foglfile, katfile, arak=jegyarak):
        self.file1 = foglfile
        self.file2 = katfile
        self.setSor()
        self.setFogkat()
        self.getbev()
        self.arak = arak

    def setFogkat(self):
        """
        Foglaltság és kategória fájlok beolvasása, és áthelyzése a fogkat listába

        :file1: a foglaltsági fájl
        :file2: a kategoriak fájl
        :return: fogkat
        :rtype: object

        """
        with open(self.file1, "r") as foglaltsag, open(self.file2, "r") as kateg:
            for sor, egysor in enumerate(foglaltsag):
                egysor = egysor.strip()
                katsor = next(kateg).strip()
                for i in range(len(egysor)):  # fogkat = [sor,szék,foglalt,árkategória]
                    NezoTer.fogkat.append([sor + 1, i + 1, egysor[i], int(katsor[i])])

    @staticmethod
    def getFogkat():
        """Foglalt kategória lekérése"""
        cols = tuple(NezoTer.fogkat)
        return cols
        # print(cols)

    def getFoglalt(self, sorszam, szekszam):
        """
        Adott sor / szék foglalt-e

        :param sorszam:  a keresett sor száma
        :type sorszam: int
        :param szekszam: a keresett szék száma az adott sorban
        :type szekszam: int
        :return: Szöveg, a szék foglalt = x, még szabad = o
        :rtype: str

        """
        for sor, szek in enumerate(self.fogkat):
            if szek[0] == sorszam:
                if szek[1] == szekszam:
                    if szek[2] == "x":
                        return f"A(z) {sorszam}.sor - {szekszam}.széke már foglalt."
                    elif szek[2] == "o":
                        return f"A {sorszam}.sor - {szekszam}.széke még szabad."
                    else:
                        return f"Hibás bejövő érték van a széksorok között."
                # return 'Foglalt helyek összesen: {} db'.format(NezoTer.foglalt)

    def setSor(self):
        """Nézőtéri székszám és sorokszáma feltöltése, meg a foglaltság feltöltése is"""
        with open(self.file1, "r") as sor:
            for egysor in sor:
                NezoTer.szekszam += len(egysor)
                NezoTer.sorokszama += 1
                for szek in egysor:
                    if szek == "x":
                        self.foglalt += 1

    @classmethod
    def getSor(self):
        """Nézőtéri sorok számának visszaadása"""
        return "Sorok száma a nézőtéren: {} db".format(NezoTer.sorokszama)

    @classmethod
    def getSzek(self):
        """Nézőtéri székek visszadaása"""
        return "Összes szék száma: {} db".format(NezoTer.szekszam)

    def hanyjegyet(self):
        """
        A foglaltság alapján összesíti a foglalt helyeket (x)

        :return: Az eladott jegyek db.
        :rtype: int

        """
        # fogkat = [sor,szék,foglalt,árkategória]
        eladott = 0
        for fogl in self.fogkat:
            if fogl[2] == "x":
                eladott += 1
        return eladott

    def eladottszazalek(self):
        """
        Eladott jegyek százalékban

        :return: százalék az eladott jegyek alapján
        :rtype: int

        """
        return round((100 / self.szekszam) * self.foglalt)

    def getKatRog(self):
        """
        Melyik kategóriából adták el a legtöbbet.

        :return: az adott kategoria
        :rtype: int

        """
        # fogkat = [sor,szék,foglalt,árkategória]
        for kateglist in self.fogkat:
            if kateglist[2] == "x":
                kateg = kateglist[3]
                self.katstat[kateg] = self.katstat.get(kateg, 0) + 1
        legtobb = max(self.katstat.values())
        for kategoria, db in self.katstat.items():
            if db == legtobb:
                return kategoria

    def getbev(self):
        """
        Bevétel kiszámolása

        :return: A foglaltság alapján a bevétel.
        :rtype:  int

        """

        bevetel: int = 0
        for kat, db in self.katstat.items():
            bevetel += self.arak[kat - 1] * db
        return bevetel

    def egyeduliek(self):
        """
        Egyedüli székek

        :return: egyedül álló székek
        :rtype: int

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

    def szabad(self):
        """
        A szabad helyek kiirása a *szabadhelyek.txt* be

        :return: *szabadhelyek.txt* file kiirva az aktuális mappába.
        :rtype: textIOWrapper.

        """
        with open("szabadhelyek.txt", "w") as f:
            for i, szek in enumerate(self.fogkat):
                if self.fogkat[i][2] == "x":
                    egyszek = "x"
                elif self.fogkat[i][2] == "o":
                    egyszek = self.fogkat[i][3]
                if self.fogkat[i][1] == 20:
                    egyszek = "\n"
                f.write(str(egyszek))
        f.close()


def main():
    """
    Főporgram

    :return: Null

    """
    nezoter = NezoTer("foglaltsag.txt", "kategoria.txt")
    print("1. feladat...")
    # print(nezoter.getFogkat())  # Az egész tömb kiíratása.
    print("\tBeolvasva eltárolva.")
    try:
        # ssz = int(input("\tAdja meg a sor számát:"))
        ssz = 7
        # szksz = int(input("\tAdja meg a szék számát:"))
        szksz = 14
        print("2.feladat...")
        print("\t", nezoter.getFoglalt(ssz, szksz))
    except ValueError:
        print("Egész számot tessék megadni.")
    # print(nezoter.getSor())
    # print(nezoter.getSzek())
    print("3. feladat...")
    print(
        f"\tAz előadásra eddig {nezoter.hanyjegyet()} jegyet adtak el, ez a nézőtér {nezoter.eladottszazalek()}%-a."
    )
    print("4.feladat...")
    print(f"\tA legtöbb jegyet a {nezoter.getKatRog()}. árkategóriában rögzítették.")
    print("5. feladat...")
    print("\tA színház bevétele: {:,.1f} Ft.".format(nezoter.getbev()))
    print("6. feladat...")
    print("\tAz egyedülálló helyek száma: {}".format(nezoter.egyeduliek()))
    print("7. feladat.")
    nezoter.szabad()
    print("\tA szabad.txt kiírása...")


if __name__ == "__main__":
    main()
