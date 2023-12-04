import re
import datetime
import sys
from cprint import *


def cleaner(mit):
    """
    Cseréli az újsor és a dupla szóközt
    :rtype: basestring
    :type mit: string
    :param mit: bejövő szöveg
    :return: a kicserélt szöveg
    """
    if mit:
        mit = mit.replace('\n', ' ')
        mit = mit.replace('  ', ' ')
        mit = mit.strip()
        return mit


def sqlrak(beobj):
    """
    Összeállítja az sqlsort ami kell az autentikusba.
    :param beobj: A kész osztály paraméterei
    :return: A kész stringet adja vissza.
    :rtype: str
    """
    SqlSor = '( NUll, '
    SqlSor += '"'
    SqlSor += beobj.datum  # Dátum
    SqlSor += '",'
    SqlSor += '"24","'  # Cég
    SqlSor += beobj.kezdes  # Kezdes
    SqlSor += '","'
    SqlSor += beobj.hely.strip()  # Hely
    SqlSor += '","'
    SqlSor += beobj.musor.strip()  # Musor
    SqlSor += '","'
    SqlSor += beobj.kontakt.strip()  # Kontakt
    SqlSor += '","'
    SqlSor += beobj.megjegy  # Megjegyzés
    SqlSor += '","'
    SqlSor += str(0)  # helykod
    SqlSor += '","'
    SqlSor += beobj.kulszal  # Külső szállítás
    SqlSor += '","'
    SqlSor += beobj.tevekenyseg
    SqlSor += '"),\n'
    return SqlSor


class Egysor:
    """
    Egy sor feldolgozásáért felelős osztály
    """

    def __init__(self, c1: object, c2: object, c3: object = None, c4: object = False, c5: object = False,
                 c6: object = False, c7: object = False, c8: object = False, c9: object = False,
                 c10: object = False) -> object:
        """
        :param c1: Dátum: date
        :param c2: Napok: str
        :param c3: Tánckar
        :param c4: Zenekar önálló
        :param c5: Férfikar
        :param c6: Közreműködők
        :param c7: Kontakt
        :param c8: Státusz
        :param c9: Külső szállítás
        :param c10: Megjegyzés
        :return:
        """
        self.datum = c1
        self.napok = c2
        self.tanckar = c3
        self.zkr = c4
        self.ffkar = c5
        self.egyez = c6
        self.kontakt = c7
        self.stat = c8
        self.kulszal = c9
        self.megjegy = c10
        self.tevekenyseg = ""

    @property
    def datum(self):
        return self._datum

    @datum.setter
    def datum(self, d):
        result = re.match(r'^\d+.\d+.\d+', str(d))
        if result:
            if isinstance(d, datetime.date):
                self._datum = d.strftime('%Y-%m-%d')
                # d = c1.value.strftime('%Y-%m-%d')  # d = datum ez mire jó?
        else:
            self._datum = "1978-02-26"

    @property
    def tanckar(self):
        return self._tanckar

    @tanckar.setter
    def tanckar(self, v):
        if v:
            # self._tanckar = v
            c2db = v.split('/')  # A 0 az időpont/helyszín, az 1 pedig a műsor.
            idopont = re.match("[0-9][0-9].?[0-9][0-9]", c2db[0])
            try:
                c2db[1] = c2db[1].strip()
                self.musor = c2db[1]
                self.musor = " ".join(self.musor.split())
                # musor = re.escape(c2db[1])
            except IndexError:
                self.musor = 'Nincs megadva műsor.'
            if idopont:
                # kezdes = c1.value.replace(hour=int(idopont.group()[:2]), minute=00)
                self.kezdes = idopont.group()
                self.hely = c2db[0].replace(self.kezdes, '', 1)
                self.hely = " ".join(self.hely.split())
                # egyadat.helykod = hely
                # print(hely)
            else:
                self.kezdes = 'Nincs megadva kezdés.'
                self.hely = c2db[0]
                # kezdes = c1.value.replace(hour=00, minute=00)

    @property
    def ffkar(self):
        return self._ffkar

    @ffkar.setter
    def ffkar(self, v):
        # outfile = open("ferfikarkimenet.txt", "a")
        if v:
            c2db = v.split('/')
        #    outfile.write('\t|'.join(c2db))
        #    outfile.write('\n')
            idopont = re.match("[0-9][0-9].?[0-9][0-9]", c2db[0])
            try:
                c2db[1] = c2db[1].strip()
                self.musor = c2db[1]
                self.musor = " ".join(self.musor.split())
            except IndexError:
                self.musor = 'Nincs megadva műsor'
            if idopont:
                self.kezdes = idopont.group()
                self.hely = c2db[0].replace(self.kezdes, '', 1)
                self.hely = " ".join(self.hely.split())
            else:
                self.kezdes = 'Nincs megadva kezdés.'
                self.hely = c2db[0]
        #    outfile.close()

    @property
    def megjegy(self):
        return self._megjegy

    @megjegy.setter
    def megjegy(self, v):
        if v:
            v = cleaner(v)
            self._megjegy = v
        else:
            self._megjegy = ""

    @property
    def kulszal(self):
        return self._kulszal

    @kulszal.setter
    def kulszal(self, v):
        if v:
            self._kulszal = v
        else:
            self._kulszal = ""

    @property
    def kontakt(self):
        return self._kontakt

    @kontakt.setter
    def kontakt(self, v):
        if v:
            self._kontakt = cleaner(v)
        else:
            self._kontakt = ""


def teszt(sikeres_teszt):
    """
    :param sikeres_teszt:
    :return: kiirja az eredményt
    Egy teszt eredményének megjelenítése.
    """
    sorszam = sys._getframe(1).f_lineno  # A hívó sorénak széma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
        cprint.info(msg)
    else:
        msg = "A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam)
        cprint.err(msg)


def tesztkeszlet():
    """Az ehhez a modulhoz tartozó tesztkészlet futtatása."""
    egy = Egysor(datetime.date(2023, 1, 1), "hétfő")
    egy.datum = datetime.date(2023, 1, 1)
    teszt(egy.datum == "2023-01-01")
    egy.datum = ""
    teszt(egy.datum == datetime.date(1978, 2, 26))
    ketto = Egysor(datetime.date(2023, 1, 1), "hétfő", "17:30 HM Eger, Egri Vár/ Táncra magyar! (KÜLÖN KERET 3.)",
                   "14:00 Évadnyitó társulati ülés", "11:00 HM Budapest, Bálna, központi ünnepség (20 perc)",
                   "10:00 Rendezvény kezdete, 11:30 HM Szabadszállás József Attila Művelődési Ház (Szabadszállás, "
                   "Kossuth Lajos u. 4.) 40 perc",
                   "Farkas Zoltán ny. alezredes 06302082062", "Zsurával egyeztetve 23.02.20.",
                   "Táncművészeti Egyetem/ Bécs NWK 348",
                   "A lejáró próbát Kernács Péter jelezte, mind Vicuska mind a kis Gergő kettős szereposztása miatt,"
                   " minden a négyen új beállók, nem szükséges a teljes tánckar")
    teszt(ketto.datum == "2023-01-01")
    teszt(ketto.napok == "hétfő")
    teszt(ketto.kezdes == "17:30")
    teszt(ketto.hely == "HM Eger, Egri Vár")
    teszt(ketto.musor == "Táncra magyar! (KÜLÖN KERET 3.)")
    teszt(ketto.zkr == "14:00 Évadnyitó társulati ülés")
    teszt(ketto.ffkar == "11:00 HM Budapest, /Bálna, /központi ünnepség (20 perc)")
    teszt(ketto.egyez == "10:00 Rendezvény kezdete, 11:30 HM Szabadszállás József Attila Művelődési Ház ("
                         "Szabadszállás, Kossuth Lajos u. 4.) 40 perc")
    teszt(ketto.kontakt == "Farkas Zoltán ny. alezredes 06302082062")
    teszt(ketto.stat == "Zsurával egyeztetve 23.02.20.")
    teszt(ketto.kulszal == "Táncművészeti Egyetem/ Bécs NWK 348")
    teszt(ketto.megjegy == "A lejáró próbát Kernács Péter jelezte, mind Vicuska mind a kis Gergő kettős szereposztása "
                           "miatt,"
                           " minden a négyen új beállók, nem szükséges a teljes tánckar")
    """
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
    """


if __name__ == "__main__":
    tesztkeszlet()
