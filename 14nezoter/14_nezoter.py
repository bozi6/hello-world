#!/usr/bin/env python3
"""14_nezoter.py.

Érettségi feladat: 2014. október, Nézőtér
Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
Program: Koós Antal, 2016"""

from typing import List, Dict, Tuple

# Konstansok
ARKATEGORIAK = (5000, 4000, 3000, 2000, 1500)
FOGLALT_JEL = 'x'
SZABAD_JEL = 'o'


def beolvas_nezoter() -> List[List[List[str]]]:
    """Nézőtéri adatok beolvasása fájlokból."""
    nezoter = []
    with open("foglaltsag.txt") as ffog, open("kategoria.txt") as fkat:
        for fog_sor in ffog:
            fog_sor = fog_sor.strip()
            kat_sor = next(fkat).strip()
            nezoter.append([[fog_sor[i], kat_sor[i]] for i in range(len(fog_sor))])
    return nezoter


def szek_allapot_lekerdezese(nezoter: List[List[List[str]]], sor: int, szek: int) -> str:
    """A megadott szék foglaltságának lekérdezése."""
    szek_adat = nezoter[sor - 1][szek - 1]
    return "foglalt" if szek_adat[0] == FOGLALT_JEL else "szabad"


def foglaltsag_statisztika(nezoter: List[List[List[str]]]) -> Tuple[int, int]:
    """Foglaltsági statisztika számítása"""
    szekek_szama = sum(len(sor) for sor in nezoter)
    foglaltak = sum(1 for sor in nezoter for szek in sor if szek[0] == FOGLALT_JEL)
    return foglaltak, szekek_szama


def kategoria_statisztika(nezoter: List[List[List[str]]]) -> Dict[str, int]:
    """Árkategória statisztika számítása."""
    katstat = dict()
    for sor in nezoter:
        for szek in sor:
            if szek[0] == FOGLALT_JEL:
                kategoria = szek[1]
                katstat[kategoria] = katstat.get(kategoria, 0) + 1
    return katstat


def szamol_bevetel(katstat: Dict[str, int]) -> int:
    """Bevétel számítása."""
    return sum(ARKATEGORIAK[int(kategoria) - 1] * darab for kategoria, darab in katstat.items())


def szamol_egyedulallo_helyek(nezoter: List[List[List[str]]]) -> int:
    """Egyedülálló üres helyek számolása."""
    egyeduliek = 0
    for sor in nezoter:
        ures_szakasz = 0
        for szek in sor:
            if szek[0] == SZABAD_JEL:
                ures_szakasz += 1
            else:
                if ures_szakasz == 1:
                    egyeduliek += 1
                ures_szakasz = 0
        if ures_szakasz == 1:
            egyeduliek += 1
    return egyeduliek


def ment_szabad_helyek(nezoter: List[List[List[str]]]) -> None:
    """Szabad helyek mentése fájlba."""
    with open("szabad.txt", "w") as ff:
        for sor in nezoter:
            for szek in sor:
                ff.write(szek[1] if szek[0] == SZABAD_JEL else FOGLALT_JEL)
            ff.write("\n")


def main() -> None:
    nezoter = beolvas_nezoter()

    print("\n2. feladat")
    megadott_sor = int(input("Adja meg egy sor számát! "))
    megadott_szek = int(input("Adja meg egy szék számát! "))
    print(f"{megadott_sor}. sor {megadott_szek}. szék: "
          f"{szek_allapot_lekerdezese(nezoter, megadott_sor, megadott_szek)}")

    print("\n3. feladat")
    foglaltak, szekek_szama = foglaltsag_statisztika(nezoter)
    print(f"Az előadásra eddig {foglaltak} jegyet adtak el,"
          f" ez a nezoter {round(foglaltak / szekek_szama * 100)}%-a.")

    print("\n4. feladat")
    katstat = kategoria_statisztika(nezoter)
    legtobb = max(katstat.values())
    for kategoria, darab in katstat.items():
        if darab == legtobb:
            print(f"A legtöbb jegyet a(z) {kategoria}. árkategóriában értékesítették.")

    print("\n5. feladat")
    bevetel = szamol_bevetel(katstat)
    print(f"A színház bevétele: {bevetel} Ft.")

    print("\n6. feladat")
    egyeduliek = szamol_egyedulallo_helyek(nezoter)
    print(f"Az egyedülálló üres helyek száma: {egyeduliek}")

    print("\n7. feladat")
    ment_szabad_helyek(nezoter)
    print("A szabad helyek felöltve a szabad.txt fájlba.")


if __name__ == "__main__":
    main()
