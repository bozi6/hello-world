import sys
import time

baratok = ["Péter", "Zoltán", "János", "Kata", "Zita", "Sándor", "Panni"]
szokincs = ["alma", "esett", "fűre", "fáról", "alá", "a", "fel"]
konyv_szavai = "az alma a fáról le esett a fűre".split()
xs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
ys = [4, 8, 12, 16, 20, 24]
zs = xs + ys
zs.sort()


def teszt(sikeres_teszt):
    """
    :param sikeres_teszt:
    :return: kiirja az eredményt
    Egy teszt eredményének megjelenítése.
    """
    sorszam = sys._getframe(1).f_lineno  # A hívó sorénak széma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = "A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam)
    print(msg)


def tesztkeszlet():
    """Az ehhez a modulhoz tartozó tesztkészlet futtatása."""
    teszt(abszolut_ertek(17) == 17)
    teszt(abszolut_ertek(-17) == 17)
    teszt(abszolut_ertek(0) == 0)
    teszt(abszolut_ertek(3.14) == 3.14)
    teszt(abszolut_ertek(-3.14) == 3.14)
    teszt(teljes_kereses(baratok, "Zoltán") == 1)
    teszt(teljes_kereses(baratok, "Péter") == 0)
    teszt(teljes_kereses(baratok, "Panni") == 6)
    teszt(teljes_kereses(baratok, "Béla") == -1)
    teszt(ismeretlen_szavak_keresese(szokincs, konyv_szavai) == ["az", "le"])
    teszt(ismeretlen_szavak_keresese([], konyv_szavai) == konyv_szavai)
    teszt(ismeretlen_szavak_keresese(szokincs, ["alma", "alá", "esett"]) == [])
    teszt(szovegbol_szavak("Az én nevem Alice!") == ["az", "én", "nevem", "alice"])
    teszt(szovegbol_szavak('"Nem, én soha!", mondta Alice.') == ["nem", "én", "soha", "mondta", "alice"])
    teszt(szomszedos_dupl_eltavolit([1, 2, 3, 3, 3, 3, 5, 6, 6, 9, 9, 7]) == [1, 2, 3, 5, 6, 9, 7])
    teszt(szomszedos_dupl_eltavolit([]) == [])
    teszt(szomszedos_dupl_eltavolit(["egy", "kis", "kis", "kölyök", "kutya"]) == ["egy", "kis", "kölyök", "kutya"])
    teszt(osszefesul(xs, []) == xs)
    teszt(osszefesul([], ys) == ys)
    teszt(osszefesul([], []) == [])
    teszt(osszefesul(xs, ys) == zs)
    teszt(osszefesul([1, 2, 3], [3, 4, 5]) == [1, 2, 3, 3, 4, 5])
    teszt(osszefesul(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) ==
          ["cica", "cica", "egér", "kakas", "kutya", "medve"])


def abszolut_ertek(n):
    """
    Egy szám abszolút értékét adja meg.
    :param n: a vizsgálandó szám
    :return: a szám abszolútértéke
    """
    if n < 0:
        return -n
    return n


def teljes_kereses(xs, ertek):
    """Keresse meg és térjen visza az érték indexével az xs sorozatban. """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1


def ismeretlen_szavak_keresese(szokincs, szavak):
    """ Visszatérünk a könyv azon szavainak listájával, amelyek ninccsenek benne a szókincsben"""
    eredmeny = []
    for w in szavak:
        if teljes_kereses(szokincs, w) < 0:
            eredmeny.append(w)
    return eredmeny


def ismeretlen_szavak_keresese_bin(szokincs, szavak):
    """ Visszatérünk a könyv azon szavainak listájával, amelyek ninccsenek benne a szókincsben"""
    eredmeny = []
    for w in szavak:
        if binaris_kereses(szokincs, w) < 0:
            eredmeny.append(w)
    return eredmeny


def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev, "r")
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak


def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az
    összes írásjelet és minden szót kisbetüssé alakít"""
    helyettesites = szoveg.maketrans("AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
                                     "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz                                          ")
    tisztitott_szoveg = szoveg.translate(helyettesites)
    szavak = tisztitott_szoveg.split()
    return szavak


def szavak_a_konyvbol(fajlnev):
    """ Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját. """
    f = open(fajlnev, "r")
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak


def binaris_kereses(xs, ertek):
    """ Keressük meg és térjünk vissza az érték
    indexével az xs sorozatban. """
    ah = 0
    fh = len(xs)
    while True:
        if ah == fh:  # Ha a vizsgált terület üres
            return -1

        # A következő összehasonlítás a ROI közepén kell legyen
        kozep_index = (ah + fh) // 2
        # Fogjuk a középső indexen lévő elemet
        kozep_elem = xs[kozep_index]
        # print("ROI[{0}:{1}](méret={2}), próba='{3}', érték='{4}'"
        #      .format(ah, fh, fh-ah, kozep_elem, ertek))

        # Hasonlítsuk össze az elemet az adott pozícióban lévővel
        if kozep_elem == ertek:
            return kozep_index  # Megtaláltuk !
        if kozep_elem < ertek:
            ah = kozep_index + 1  # Használjuk a felső ROI-t
        else:
            fh = kozep_index  # Használjuk az also ROI-t


def szomszedos_dupl_eltavolit(xs):
    """
    Visszatér egy új listával, amelyben a szomszédos
    duplikátumok el vannak távolítva az xs listából.
    """
    eredmeny = []
    aktualis_elem = None
    for e in xs:
        if e != aktualis_elem:
            eredmeny.append(e)
            aktualis_elem = e
    return eredmeny


def osszefesul(xs, ys):
    """
    Összefésüli a rendezett xs és ys listákat.
    Visszatér a rendezett eredménnyel.
    :type ys: list
    :type xs: list
    :param xs: Az első rendezett lista
    :param ys: A második rendezett lista
    :return: az eredmény lista
    """
    eredmeny = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(xs):               # Ha az xs lista végére értünk
            eredmeny.extend(ys[yi:])    # Még vannak elemek az ys listában
            return eredmeny             # Készen vagyunk
        if yi >= len(ys):               # Ugyanaz csak fordítva
            eredmeny.extend(xs[xi:])
            return eredmeny
        # Ha mindkét listában vannak még elemek, akkor a kisebbik elemet másoljuk
        # az eredmény listába
        if xs[xi] <= ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
        else:
            eredmeny.append(ys[yi])
            yi += 1


def ismeretlen_szavak_osszefesulessel(szokincs, szavak):
    """ Mind a szókincs és könyv szavai rendezettek kell, legyenek.
        Visszatérünk egy új szólistával, mely szavak benne vannak a könyvben,
        de nincsenek a szókincsben.
    """
    eredmeny = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(szokincs):
            eredmeny.extend(szavak[yi:])
            return eredmeny
        if yi >= len(szavak):
            return eredmeny
        if szokincs[xi] == szavak[yi]:  # A szó benne van a szókincsben
            yi += 1
        elif szokincs[xi] < szavak[yi]:  # Haladjon tovább
            xi += 1
        else:  # Találtunk olyan szót, mely nincs a szókincsben
            eredmeny.append(szavak[yi])
            yi += 1


def main():
    t0 = time.time()
    nagyobb_szokincs = szavak_betoltese_fajlbol("szotar_sorted.txt")
    konyv_szavai = szavak_a_konyvbol("alice_csodaorszagban.txt")
    print("A könyvben {} szó található, az első 10 a következő:\n{}".format(len(konyv_szavai), konyv_szavai[:10]))
    print(f"A szókincsben {len(nagyobb_szokincs)} szó található, kezdve: \n{nagyobb_szokincs[:6]}")
    hianyzo_szavak = ismeretlen_szavak_keresese_bin(nagyobb_szokincs, konyv_szavai)
    t1 = time.time()
    print("{} ismeretlen szó van.".format(len(hianyzo_szavak)))
    print("Ez {0:.4f} másodpercet vett igénybe".format(t1 - t0))
    osszes_szo = szavak_a_konyvbol("alice_csodaorszagban.txt")
    osszes_szo.sort()
    konyv_szavai = szomszedos_dupl_eltavolit(osszes_szo)
    print("A könyvben {} szó van. Csak {} egyedi.".format(len(osszes_szo), len(konyv_szavai)))
    print("Az elso 10 szó\n{}".format(konyv_szavai[:10]))
    hianyzo_szavak = ismeretlen_szavak_osszefesulessel(nagyobb_szokincs, konyv_szavai)
    t1 = time.time()
    print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
    print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))
    tesztkeszlet()


if __name__ == "__main__":
    main()

