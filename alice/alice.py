import unittest


class TestFuggveny(unittest.TestCase):
    def test_teljes_kereses(self):
        self.assertEqual(teljes_kereses(baratok, "Zoltán"), 1)
        self.assertEqual(teljes_kereses(baratok, "Péter"), 0)
        self.assertEqual(teljes_kereses(baratok, "Panni"), 6)
        self.assertEqual(teljes_kereses(baratok, "Béla"), -1)

    def test_ismeretlen_szavak_keresese(self):
        self.assertNotEqual(ismeretlen_szavak_keresese(szokincs, konyv_szavai), ["alice", "s", "adventures"])


def teljes_kereses(xs, ertek):
    """ Keresse meg és térjen vissza az érték indexével az xs sorozatban. """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1


szokincs = ["apple", "fell", "considering", "trees", "down", "the", "up"]
konyv_szavai = "az alma a fáról le esett a fűre".split()


def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden szót kisbetűssé alakít. """

    helyettesites = szoveg.maketrans(
        # Ha bármelyikükkel találkozol
        "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Cseréld őket ezekre
        "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz                                          ")

    # Most alakítsd át a szöveget
    tisztitott_szoveg = szoveg.translate(helyettesites)
    szavak = tisztitott_szoveg.split()
    return szavak


def szavak_a_konyvbol(fajlnev):
    """ Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját."""
    f = open(fajlnev, "r")
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak


konyv_szavai = szavak_a_konyvbol("alice_in_wonderland.txt")
print("A könyvben {0} szó található, az első 10 a következő:\n{1}".format(len(konyv_szavai), konyv_szavai[:10]))


def linearis_kereses(kincs, szok):
    check = all(item in kincs for item in szok)
    if check is True:
        return 1
    else:
        return -1


def ismeretlen_szavak_keresese(szokincs, szavak):
    """ Visszatérünk a könyv azon szavainak listájával, amelyek nincsenek benne a szókincsben. """
    eredmeny = []
    for w in szavak:
        if linearis_kereses(szokincs, w) < 0:
            eredmeny.append(w)
    return eredmeny


baratok = ["Péter", "Zoltán", "János", "Kata", "Zita", "Sándor", "Panni"]

szavak_a_konyvbol("alice_in_wonderland.txt")
