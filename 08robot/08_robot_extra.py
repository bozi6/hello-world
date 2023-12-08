#!/usr/bin/env python3
import math  # sqrt

"""
 08_robot_extra.py
 Érettségi feladat: 2008. október, Robot
 Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
 Program: Koós Antal, 2018
"""


def beolvas():
    """
    Fájl beolvasása és a sorok visszaadása

    :return: programok listája
    :rtype: list

    """
    programok = []
    with open("program.txt") as ff:
        ff.readline()  # A fájl első sorát beolvassuk, de nincs rá szükségünk.
        programok = [
            sor.strip() for sor in ff
        ]  # A második sortól folytatódik a beolvasás.
    return programok


if __name__ == "__main__":
    """
    Főprogram

    :return: Kiirogatja az eredményeket
    :rtype: str

    """
    # --- 1. feladat ---
    print("\n1. feladat: Az adatok beolvasása.")
    programok = beolvas()

    # --- 2. feladat ---
    print("\n2. feladat")
    # --- 2a. ---
    sorszam = int(input("Kérem az utasítás sorszámát (1-{}):".format(len(programok))))
    sor = programok[sorszam - 1]
    print(sor)
    for minta in ("ED", "DE", "KN", "NK"):
        if minta in sor:
            print("egyszerűsíthető")
            break
    else:  # A 'for'-hoz tartozik; akkor hajtódik végre, ha nem volt a ciklusban 'break'.
        print("nem egyszerűsíthető")

    # --- 2b.,2c. ---
    x, y, maxtav2, lepesszam = 0, 0, 0, 0
    mozgas = {
        "E": (1, 0),
        "D": (-1, 0),
        "K": (0, 1),
        "N": (0, -1),
    }  # Kiegészíthetnénk pl. az ÉNy-i iránnyal: "Q":(1,-1)

    for index, irany in enumerate(sor):
        dy, dx = mozgas[irany]
        y += dy
        x += dx

        tav2 = x * x + y * y
        if tav2 > maxtav2:
            lepesszam = index + 1
            maxtav2 = tav2

    print(
        "{} lépést kell tenni az ED, {} lépést a KN tengely mentén.".format(
            abs(y), abs(x)
        )
    )
    print(lepesszam, round(math.sqrt(maxtav2), 3))

    # --- 3. feladat ---
    print("\n3. feladat")

    for progindex, sor in enumerate(programok):
        fogyasztás = 2 + len(sor)
        for index in range(1, len(sor)):
            if sor[index] != sor[index - 1]:
                fogyasztás += 2

        if fogyasztás <= 100:
            print(progindex + 1, fogyasztás)

    # --- 4. feladat ---
    print("\n4. feladat: az új programok kiírása")

    with open("ujprog.txt", "w") as ff:
        for prog in programok:
            db = [1]
            irany = [prog[0]]
            for index in range(1, len(prog)):
                if prog[index] == irany[-1]:
                    db[-1] += 1
                else:
                    irany.append(prog[index])
                    db.append(1)

            for index in range(len(irany)):
                if db[index] > 1:
                    ff.write(str(db[index]))
                ff.write(irany[index])

            ff.write("\n")

    # --- 5. feladat ---
    ujformatum = input("\n5. feladat: Adjon meg egy új formátumú programot: ")
    szam = 0
    for karakter in ujformatum:
        if karakter.isdigit():
            szam = 10 * szam + int(karakter)
        else:
            print(karakter if szam == 0 else szam * karakter, end="")
            szam = 0

    print()

    # ---------------------------------------------------------------------------
    # További feladatok: http://sites.google.com/site/eutlantis/erettsegi
    # Ajánlott olvasmány: www.interkonyv.hu/konyvek/koos_antal_python_a_gepben
