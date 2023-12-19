#!/usr/bin/env python3
"""
14_nezoter.py,
Érettségi feladat: 2014. október, Nézőtér
Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
Program: Koós Antal, 2016
"""


def main():
    """
    Főprogram

    :return: Null

    """
    # --- 1. feladat ---
    # print("\n1. feladat")
    # Így tároljuk az adatokat:
    # nezoter=[ sor1,sor2,... ]; sor=[ szék1,szék2,...]; szék=[foglaltság,kategória]
    nezoter = []
    with open("foglaltsag.txt") as ffog, open("kategoria.txt") as fkat:
        for fog_sor in ffog:
            fog_sor = fog_sor.strip()
            kat_sor = next(fkat).strip()
            nezoter.append([[fog_sor[i], kat_sor[i]] for i in range(len(fog_sor))])

    # for sor in nezoter:
    #    print(sor)

    # --- 2. feladat ---
    print("\n2. feladat")
    megadott_sor = int(input("Adja meg egy sor számát! "))
    megadott_szek = int(input("Adja meg egy szék számát! "))

    szek = nezoter[megadott_sor - 1][megadott_szek - 1]
    print(
        "{}. sor {}. szék: {}".format(
            megadott_sor, megadott_szek, "foglalt" if szek[0] == "x" else "szabad"
        )
    )

    # --- 3. feladat ---
    print("\n3. feladat")
    szekek_szama = 0
    foglaltak = 0
    for sor in nezoter:
        szekek_szama += len(sor)
        for szek in sor:
            if szek[0] == "x":
                foglaltak += 1

    print(
        "Az előadásra eddig {} jegyet adtak el, ez a nezoter {}%-a.".format(
            foglaltak, round(foglaltak / szekek_szama * 100)
        )
    )

    # --- 4. feladat ---
    print("\n4. feladat")
    katstat = dict()  # {kategória:darab} statisztika az eladott jegyek kategóriáira
    for sor in nezoter:
        for szek in sor:
            if szek[0] == "x":
                kategoria = szek[1]
                katstat[kategoria] = katstat.get(kategoria, 0) + 1

    legtobb = max(katstat.values())
    for (
        kategoria,
        darab,
    ) in katstat.items():  # több kategóriában is eladhattak ugyanolyan sok jegyet
        if darab == legtobb:
            print(
                "A legtöbb jegyet a(z) {}. árkategóriában értékesítették.".format(
                    kategoria
                )
            )

    # --- 5. feladat ---
    print("\n5. feladat")
    árak = (5000, 4000, 3000, 2000, 1500)
    bevétel = 0
    for kategoria, darab in katstat.items():
        bevétel += árak[int(kategoria) - 1] * darab

    print("A színház bevétele:", bevétel, "Ft")

    # --- 6. feladat ---
    print("\n6. feladat")
    egyedüliek = 0

    for sor in nezoter:
        üres_szakasz = 0
        for szek in sor:
            if szek[0] == "o":
                üres_szakasz += 1
            else:  # "x": lezárja az üresek sorozatát
                if üres_szakasz == 1:
                    egyedüliek += 1
                üres_szakasz = 0
        if üres_szakasz == 1:  # a sor végén is vizsgálni kell
            egyedüliek += 1

    print("Az egyedülálló helyek száma:", egyedüliek)

    # --- 7. feladat ---
    # print("\n7. feladat")
    with open("szabad.txt", "w") as ff:
        for sor in nezoter:
            for szek in sor:
                ff.write(szek[1] if szek[0] == "o" else "x")
            ff.write("\n")

    # ---------------------------------------------------------------------------
    # További feladatok: http://sites.google.com/site/eutlantis/erettsegi
    # Ajánlott olvasmány: www.interkonyv.hu/konyvek/koos_antal_python_a_gepben


if __name__ == "__main__":
    main()
