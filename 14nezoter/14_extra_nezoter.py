#!/usr/bin/env python3
"""
14_extra_nezoter.py,
Érettségi feladat: 2014. október, Nézőtér
Feladatkiírások: http://www.oktatas.hu/kozneveles/erettsegi/feladatsorok
Program: Koós Antal, 2016
"""


def main():
    nezoter = []
    """
     -- 1. feladat ---
    print("\n1. feladat")
    Így tároljuk az adatokat:
    nézőtér=[ sor1,sor2,... ]; sor=[ szék1,szék2,...]; szék=[foglaltsag,kategoria]
    Megjegyzés: Nem kell, hogy minden sor ugyanolyan hosszú legyen. Tesztelésként rövidítsük le vagy bővítsük
    valamelyik sort a két adatfájlban.
    nézőtér = []
    """

    with open("foglaltsag.txt") as ffog, open("kategoria.txt") as fkat:
        for fog_sor in ffog:
            fog_sor = fog_sor.strip().lower()
            try:
                kat_sor = next(fkat).strip()
            except StopIteration:
                print("Az adatfájlok sorai nem állíthatók párba!")
                exit(1)

            if len(fog_sor) != len(kat_sor):
                print("A foglaltsag és a kategoria nem állíthatók párba!")
                exit(1)

            nezoter.append([[fog_sor[i], kat_sor[i]] for i in range(len(fog_sor))])

    # for sor in nézőtér:
    # 	print(sor)

    # --- 2. feladat ---
    print("\n2. feladat")
    sorok = len(nezoter)
    try:
        megadott_sor = int(input("Adja meg egy sor számát! (1-{}) ".format(sorok)))
        if megadott_sor < 1 or megadott_sor > sorok:
            print("Hibás sorszám!")
            exit(1)

        székek = len(nezoter[megadott_sor - 1])
        megadott_szék = int(input("Adja meg egy szék számát! (1-{}) ".format(székek)))
        if megadott_szék < 1 or megadott_szék > székek:
            print("Hibás székszám!")
            exit(1)

    except ValueError:
        print("Hibás számmegadás!")
        exit(1)

    foglaltsag, kategoria = nezoter[megadott_sor - 1][megadott_szék - 1]
    print(
        "{}. sor {}. szék: {}".format(
            megadott_sor, megadott_szék, "foglalt" if foglaltsag == "x" else "szabad"
        )
    )

    # --- 3. feladat ---
    print("\n3. feladat")
    szekek_szama = 0
    foglaltak = 0
    for sor in nezoter:
        szekek_szama += len(sor)
        for foglaltsag, kategoria in sor:
            if foglaltsag == "x":
                foglaltak += 1

    print(
        "Az előadásra eddig {} jegyet adtak el, ez a nézőtér {}%-a.".format(
            foglaltak, round(foglaltak / szekek_szama * 100)
        )
    )

    # --- 4. feladat ---
    print("\n4. feladat")
    katstat = dict()  # {kategoria:darab} statisztika az eladott jegyek kategóriáira
    for sor in nezoter:
        for foglaltsag, kategoria in sor:
            if foglaltsag == "x":
                katstat[kategoria] = katstat.get(kategoria, 0) + 1

    legtobb = max(katstat.values())
    for (
        kategoria,
        darab,
    ) in katstat.items():  # több kategóriában is eladhattak ugyanolyan sok jegyet
        if darab == legtobb:
            print(
                "A legtobb jegyet a(z) {}. árkategóriában értékesítették.".format(
                    kategoria
                )
            )

    # --- 5. feladat ---
    print("\n5. feladat")
    arak = (5000, 4000, 3000, 2000, 1500)
    # arak=(5000,4000,3000,2000)	#teszthez
    bevetel = 0
    for kategoria, darab in katstat.items():
        try:
            bevetel += arak[int(kategoria) - 1] * darab
        except ValueError:
            print("Hibás kategoria az adatfájlban!")
            exit(1)
        except IndexError:
            print("Az arak és a kategóriák nem párosíthatók!")
            exit(1)

    print("A színház bevétele:", bevetel, "Ft")

    # --- 6. feladat ---
    print("\n6. feladat")
    egyeduliek = 0
    for sor in nezoter:
        ures_szakasz = 0
        for foglaltsag, kategoria in sor:
            if foglaltsag == "o":
                ures_szakasz += 1
            else:  # "x": lezárja az üresek sorozatát
                if ures_szakasz == 1:
                    egyeduliek += 1
                ures_szakasz = 0
        if ures_szakasz == 1:  # a sor végén is vizsgálni kell
            egyeduliek += 1

    print("Az egyedülálló helyek száma:", egyeduliek)

    # --- 7. feladat ---
    # print("\n7. feladat")
    with open("szabad.txt", "w") as ff:
        for sor in nezoter:
            for foglaltsag, kategoria in sor:
                ff.write(kategoria if foglaltsag == "o" else "x")
            ff.write("\n")

    # ---------------------------------------------------------------------------
    # További feladatok: http://sites.google.com/site/eutlantis/erettsegi
    # Ajánlott olvasmány: www.interkonyv.hu/konyvek/koos_antal_python_a_gepben


if __name__ == "__main__":
    main()
