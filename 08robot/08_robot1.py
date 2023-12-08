import logging
import math

"""
2008-as informatika robot programozó feladat

"""


def beolvas(prog="program.txt"):
    """
    Sorok beolvasása a program.txt fileból

    :param prog: A beolvasandó program fájl
    :type prog: str
    :return: a beolvasott sorok tömbje
    :rtype: list

    """
    sorok = []
    with open(prog, "rt") as myfile:
        for myline in myfile:
            sorok.append(myline.strip())
    myfile.close()
    return sorok


def main():
    """
    Főprogram
    """
    logging.basicConfig(
        level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s"
    )
    sorok = beolvas()
    maxsor = sorok[0].strip()
    logging.debug(f"maxsor értéke: {maxsor}")
    # utasítássor bekérése
    sorszam = int(input("2. feladat. Kérem a kezdősor számát:"))
    logging.debug(f"sorszam értéke: {sorszam}")
    if int(maxsor) < sorszam:
        print("Kisebb számot adjon meg:")
    else:
        egysor = sorok[sorszam]
    # egyszerűsíthető ha ED KN DE NK van benne
    logging.debug(f"Egysor : {egysor}")
    print("2.a feladat")
    print(egysor)
    if "ED" in egysor or "DE" in egysor or "KN" in egysor or "NK" in egysor:
        print("Egyszerűsíthető.")
    else:
        print("Nem egyszerűsíthető.")
    # kiírni hány utasítással lehet visszajutni az origoba
    ed = 0
    kn = 0
    for tengelyek in egysor:
        if tengelyek == "E" or tengelyek == "D":
            ed += 1
        if tengelyek == "K" or tengelyek == "N":
            kn += 1
    print("2b feladat")
    print(
        "{} lépést kell megtenni az ED, {} lépést az KN tengely mentén".format(ed, kn)
    )

    # A végén milyen messze van a kiindulási ponttól.
    xkord, ycord = (0, 0)
    maxtav = 0
    tav = 0
    lepesszam = 0
    for index, kords in enumerate(egysor):
        if kords == "E":
            ycord += 1
        if kords == "D":
            ycord -= 1
        if kords == "K":
            xkord += 1
        if kords == "N":
            xkord -= 1

        tav = xkord * xkord + ycord * ycord
        if tav > maxtav:
            lepesszam = index + 1
            maxtav = tav

    logging.debug(f"Vége koordináták: {xkord}, {ycord}")
    tavolsag = math.hypot(xkord - 0, ycord - 0)
    print("3. feladat")
    print("A robotka távolsága jelenleg légvonalban: {:.3f} cm".format(tavolsag))
    print(
        "A robotka legmesszebb a {} lépésben, {:.3f} távolságra volt".format(
            lepesszam, math.sqrt(maxtav)
        )
    )
    # todo aksitöltés 1cm hez 1 egység irányváltás és indulás 2 egység

    # todo van 100 és 1000 egységes megadni azt a sort amelyikhez elég a kicsi is. újsorban a sorszámot & az energiát
    # todo az ujprogba átírni az ismétlődéseket pl 2dK3N ezt az ujprogba kiirni
    # todo újból vissza régibe is legyen progi ami az újat visszaírja régire.
