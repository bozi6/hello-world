#!/bin/env python3
"""
Nézőtéri feladatok, saját mgeoldással

"""
from typing import List, Dict, Tuple, Optional

#Konstansok
FOGLALT = "x"
SZABAD = "o"
ALAPARAK = (5000, 4000, 3000, 2000, 1500)


class NezoTer:
    def __init__(self, foglaltsag_file: str, kategoria_file: str, arak: Tuple[int, ...] = ALAPARAK):
        self.foglaltsag_file = foglaltsag_file
        self.kategoria_file = kategoria_file
        self.arak = arak
        self.fogkat: List[List[int]] = []
        self.katstat: Dict[int, int] = {}
        self.sorok_szama = 0
        self.szekek_szama = 0
        self.foglalt_helyek = 0

        self._beolvas_adatok()

    def _beolvas_adatok(self):
        """
        Adatok beolvasása
        """
        with open(self.foglaltsag_file, "r") as foglaltsag, open(self.kategoria_file, "r") as kateg:
            for sor_index, (foglaltsag_sor, kateg_sor) in enumerate(zip(foglaltsag, kateg)):
                foglaltsag_sor = foglaltsag_sor.strip()
                kateg_sor = kateg_sor.strip()
                self.szekek_szama += len(foglaltsag_sor)
                self.sorok_szama += 1

                for szek_index, (fogl, kat) in enumerate(zip(foglaltsag_sor, kateg_sor)):
                    self.fogkat.append([sor_index + 1, szek_index + 1, fogl, int(kat)])
                    if fogl == FOGLALT:
                        self.foglalt_helyek += 1
                        kat_szam = int(kat)
                        self.katstat[kat_szam] = self.katstat.get(kat_szam, 0) + 1

    def get_hely_statusz(self, sorszam: int, szekszam: int) -> Optional[str]:
        """A megadott sor / szék foglalt-e"""
        for hely in self.fogkat:
            if hely[0] == sorszam and hely[1] == szekszam:
                if hely[2] == FOGLALT:
                    return f"A(z) {sorszam}.sor - {szekszam}.széke már foglalt."
                elif hely[2] == SZABAD:
                    return f"A {sorszam}.sor - {szekszam}.széke még szabad."
                else:
                    return f"Hibás bejövő érték van a széksorok között."
        return None

    def get_foglaltsag_szazalek(self) -> int:
        """A foglaltság alapján összesíti a foglalt egyedüláló helyeket (x)"""
        return round((100 / self.szekek_szama) * self.foglalt_helyek)

    def get_legnepszerubb_kategoria(self) -> Optional[int]:
        """Legtöbb foglalással rendelkező kategória meghatározása."""
        if not self.katstat:
            return None
        max_foglalt = max(self.katstat.values())
        return next(kateg for kateg, db in self.katstat.items() if db == max_foglalt)

    def get_bevetel(self) -> int:
        """ Bevétel kiszámolása"""
        return sum(self.arak[kateg - 1] * db for kateg, db in self.katstat.items())

    def get_egyeduliek(self) -> int:
        """Egyedüli székek"""
        egyeduli = 0
        sor_szekek: List[str] = []
        aktualis_sor = 1

        for hely in self.fogkat:
            if hely[0] != aktualis_sor:
                egyeduli += self._szamol_egyeduliek(sor_szekek)
                sor_szekek = []
                aktualis_sor = hely[0]
            sor_szekek.append(hely[2])

        egyeduli += self._szamol_egyeduliek(sor_szekek)
        return egyeduli

    @staticmethod
    def _szamol_egyeduliek(szekek: List[str]) -> int:
        """
        Egyedüláló székek számának számolása
        """
        egyeduliek = 0
        ures_szakasz = 0

        for szek in szekek:
            if szek == SZABAD:
                ures_szakasz += 1
            else:
                if ures_szakasz == 1:
                    egyeduliek += 1
                ures_szakasz = 0
        if ures_szakasz == 1:
            egyeduliek += 1

        return egyeduliek

    def ment_szabad_helyek(self) -> None:
        """
        Szabad helyek mentése fájlba szabad.txt néven.
        A fájlban a szabad helyeknél a kategória számot írjuk ki,
        foglalt helyeknél x karaktert használunk.
        """
        with open("szabad.txt", "w") as ff:
            aktualis_sor = 1
            sor_helyek = []

            for hely in self.fogkat:
                if hely[0] != aktualis_sor:
                    # Új sor kezdődik, írjuk ki az előzőt
                    ff.write("".join(sor_helyek) + "\n")
                    sor_helyek = []
                    aktualis_sor = hely[0]

                # Ha szabad a hely, akkor a kategória számát írjuk ki, egyébként x-et
                sor_helyek.append(str(hely[3]) if hely[2] == SZABAD else FOGLALT)

            # Az utolsó sort is kiírjuk
            if sor_helyek:
                ff.write("".join(sor_helyek) + "\n")


def main():
    """
    Főporgram
    :return: None
    """
    nezoter = NezoTer("foglaltsag.txt", "kategoria.txt")
    print("1. feladat...")
    # print(nezoter.getFogkat())  # Az egész tömb kiíratása.
    print("\tBeolvasva eltárolva.")
    try:
        ssz = int(input("\tAdja meg a sor számát:"))
        szksz = int(input("\tAdja meg a szék számát:"))
        print("2.feladat...")
        print("\t", nezoter.get_hely_statusz(ssz, szksz))
    except ValueError:
        print("Egész számot tessék megadni.")
    # print(nezoter.getSor())
    # print(nezoter.getSzek())
    print("3. feladat...")
    print(
        f"\tAz előadásra eddig {nezoter.foglalt_helyek} jegyet adtak el,"
        f" ez a nézőtér {nezoter.get_foglaltsag_szazalek()}%-a."
    )
    print("4.feladat...")
    print(f"\tA legtöbb jegyet a {nezoter.get_legnepszerubb_kategoria()}. árkategóriában rögzítették.")
    print("5. feladat...")
    print(f"\tA színház bevétele: {nezoter.get_bevetel():,.1f} Ft.")
    print("6. feladat...")
    print(f"\tAz egyedülálló helyek száma: {nezoter.get_egyeduliek()}")
    print("7. feladat.")
    print("\tA szabad.txt kiírása...")
    nezoter.ment_szabad_helyek()


if __name__ == "__main__":
    main()
