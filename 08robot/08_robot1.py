import logging
import math
from itertools import groupby

"""
2008-as informatika robot programozó feladat
"""

# Konstansok
IRANYOK = {'E': (0, 1), 'D': (0, -1), 'K': (1, 0), 'N': (-1, 0)}
EGYSZERUSITHETO_PAROK = ['ED', 'DE', 'KN', 'NK']
KIS_AKKU_KAPACITAS = 100
NAGY_AKKU_KAPACITAS = 1000
MOZGAS_ENERGIA = 1
IRANYVALTAS_ENERGIA = 2


def fajl_beolvasasa(fajlnev="program.txt"):
    """Sorok beolvasása fájlból"""
    with open(fajlnev, "rt") as fajl:
        return [sor.strip() for sor in fajl]


def utasitas_sor_bekeres(sorok):
    """Bekéri és ellenőrzi az utasítás sor számát"""
    max_sor_szam = int(sorok[0])
    sor_szam = int(input("2. feladat. Kérem a kezdősor számát:"))

    if max_sor_szam < sor_szam:
        print("Kisebb számot adjon meg:")
        return None
    return sorok[sor_szam]


def egyszerusitheto_e(utasitas_sor):
    """Ellenőrzi, hogy az utasítás sor egyszerűsíthető-e"""
    return any(par in utasitas_sor for par in EGYSZERUSITHETO_PAROK)


def szukseges_lepesek_szamitasa(utasitas_sor):
    """Kiszámítja a szükséges lépések számát az origóba való visszajutáshoz"""
    ed_lepesek = sum(1 for irany in utasitas_sor if irany in 'ED')
    kn_lepesek = sum(1 for irany in utasitas_sor if irany in 'KN')
    return ed_lepesek, kn_lepesek


def robot_mozgasanak_szimulalasa(utasitas_sor):
    """Szimulálja a robot mozgását és visszaadja a végkoordinátákat és a legnagyobb távolságot"""
    x_koordinata, y_koordinata = 0, 0
    max_tavolsag_negyzetben = 0
    max_tavolsag_lepese = 0

    for lepes_index, irany in enumerate(utasitas_sor):
        if irany in IRANYOK:
            dx, dy = IRANYOK[irany]
            x_koordinata += dx
            y_koordinata += dy

            tavolsag_negyzetben = x_koordinata * x_koordinata + y_koordinata * y_koordinata
            if tavolsag_negyzetben > max_tavolsag_negyzetben:
                max_tavolsag_negyzetben = tavolsag_negyzetben
                max_tavolsag_lepese = lepes_index + 1

    return x_koordinata, y_koordinata, max_tavolsag_negyzetben, max_tavolsag_lepese


def energia_szamitas(utasitas_sor):
    """Kiszámítja a szükséges energiát az utasítássor végrehajtásához"""
    if not utasitas_sor:
        return 0

    # Indulási energia
    energia = IRANYVALTAS_ENERGIA

    # Mozgási energia (minden utasítás 1 egység)
    energia += len(utasitas_sor) * MOZGAS_ENERGIA

    # Irányváltási energia számítása
    for i in range(1, len(utasitas_sor)):
        if utasitas_sor[i] != utasitas_sor[i - 1]:
            energia += IRANYVALTAS_ENERGIA

    return energia


def kis_akkuval_vegrehajthatoak(sorok):
    """Megkeresi azokat az utasítássorokat, amelyek kis akkuval végrehajthatók"""
    vegrehajthatoak = []

    for i in range(1, len(sorok)):  # Az első sor a maximális sorszám
        energia = energia_szamitas(sorok[i])
        if energia <= KIS_AKKU_KAPACITAS:
            vegrehajthatoak.append((i, energia))

    return vegrehajthatoak


def utasitassor_tomoritese(utasitas_sor):
    """Tömöríti az utasítássort az új formátum szerint"""
    if not utasitas_sor:
        return ""

    tomoritve = []
    for irany, csoport in groupby(utasitas_sor):
        darab = len(list(csoport))
        if darab == 1:
            tomoritve.append(irany)
        else:
            tomoritve.append(f"{darab}{irany}")

    return ''.join(tomoritve)


def ujprog_letrehozasa(sorok):
    """Létrehozza az ujprog.txt fájlt a tömörített utasítássorokkal"""
    with open("ujprog.txt", "w") as fajl:
        fajl.write(f"{sorok[0]}\n")  # Első sor a maximális sorszám
        for i in range(1, len(sorok)):
            tomoritve = utasitassor_tomoritese(sorok[i])
            fajl.write(f"{tomoritve}\n")


def eredmenyek_kiirasa(utasitas_sor, ed_lepesek, kn_lepesek, veg_x, veg_y, max_tavolsag_negyzetben,
                       max_tavolsag_lepese):
    """Kiírja az összes eredményt"""
    print("2.a feladat")
    print(utasitas_sor)

    if egyszerusitheto_e(utasitas_sor):
        print("Egyszerűsíthető.")
    else:
        print("Nem egyszerűsíthető.")

    print("2b feladat")
    print(f"{ed_lepesek} lépést kell megtenni az ED, {kn_lepesek} lépést az KN tengely mentén")

    vegso_tavolsag = math.hypot(veg_x, veg_y)
    max_tavolsag = math.sqrt(max_tavolsag_negyzetben)

    print("3. feladat")
    print(f"A robotka távolsága jelenleg légvonalban: {vegso_tavolsag:.3f} cm")
    print(f"A robotka legmesszebb a {max_tavolsag_lepese} lépésben, {max_tavolsag:.3f} távolságra volt")


def main():
    """Főprogram"""
    logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")

    sorok = fajl_beolvasasa()
    utasitas_sor = utasitas_sor_bekeres(sorok)

    if utasitas_sor is None:
        return

    logging.debug(f"Utasítás sor: {utasitas_sor}")

    ed_lepesek, kn_lepesek = szukseges_lepesek_szamitasa(utasitas_sor)
    veg_x, veg_y, max_tavolsag_negyzetben, max_tavolsag_lepese = robot_mozgasanak_szimulalasa(utasitas_sor)

    logging.debug(f"Végkoordináták: {veg_x}, {veg_y}")

    eredmenyek_kiirasa(utasitas_sor, ed_lepesek, kn_lepesek, veg_x, veg_y, max_tavolsag_negyzetben, max_tavolsag_lepese)

    # 3. feladat - kis akkuval végrehajtható utasítássorok
    print("\n3. feladat - Kis akkuval végrehajtható utasítássorok:")
    vegrehajthatoak = kis_akkuval_vegrehajthatoak(sorok)
    for sor_szam, energia in vegrehajthatoak:
        print(f"{sor_szam} {energia}")

    # 4. feladat - tömörített utasítássorok létrehozása
    ujprog_letrehozasa(sorok)
    print("\n4. feladat - Az ujprog.txt fájl létrehozva.")


if __name__ == "__main__":
    main()
