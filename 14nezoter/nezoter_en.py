#!/bin/env python3


class NezoTer:
    """
    Nézőtéri alaposztály, székekkel, meg széksorokkal, meg foglaltsággal.
    """
    szekszam = 0
    sorokszama = 0
    foglalt = 0

    def __init__(self, foglfile, katfile):
        self.foglalt = 0
        self.file1 = foglfile
        self.file2 = katfile
        self.setSor()

    def setFoglalt(self):
        pass

    def getFoglalt(self, sorszam, szekszam):
        with open(self.file1, 'r') as sor:
            for idx, egysor in enumerate(sor):
                if idx == sorszam:
                    for idsz, szekek in enumerate(egysor):
                        if idsz == szekszam:
                            if szekek == 'x':
                                return '{}. sor, {}. szék foglalt.'.format(sorszam,szekszam)
                            else:
                                return '{}. sor, {}. szék szabad.'.format(sorszam,szekszam)
                # return 'Foglalt helyek összesen: {} db'.format(NezoTer.foglalt)

    def setSor(self):
        with open(self.file1, 'r') as sor:
            for egysor in sor:
                NezoTer.szekszam += len(egysor)
                NezoTer.sorokszama += 1
                for szek in egysor:
                    if szek == 'x':
                        NezoTer.foglalt += 1

    def getSor(self):
        return 'Sorok száma a nézőtéren: {} db'.format(NezoTer.sorokszama)

    def getSzek(self):
        return 'Összes szék száma: {} db'.format(NezoTer.szekszam)

    def setSzek(self, szek):
        pass


nezoter = NezoTer('foglaltsag.txt', 'kategoria.txt')
print("Első feladat:")
ssz = int(input("Adja meg a sor számát:"))
szksz = int(input("Adja meg a szék számát:"))
print(nezoter.getSor())
print(nezoter.getSzek())
print(nezoter.getFoglalt(ssz, szksz))


