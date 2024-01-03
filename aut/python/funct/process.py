"""
Az adatok feldolgozásáért végző
funkciók osztályok meg miegyebek.
"""

import datetime
import re

from cprint import *


def cleaner(mit):
    """
    Cseréli az újsor és a dupla szóközt

    :rtype: base string
    :type: mit: string
    :param: mit: bejövő szöveg
    :return: a kicserélt szöveg

    """

    if mit:
        mit = mit.replace("\n", " ")
        mit = mit.replace("  ", " ")
        mit = mit.strip()
        return mit


def sqlrak(beobj):
    """
    Összeállítja az sqlsort ami kell az autentikusba.

    :param: beobj: A kész osztály paraméterei
    :return: A kész stringet adja vissza.
    :rtype: str

    """
    SqlSor = "( NUll, "
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
    SqlSor += str(995)  # helykod
    SqlSor += '","'
    SqlSor += beobj.tevekenyseg
    SqlSor += '"),\n'
    return SqlSor


class Egysor:
    """
    Egy sor feldolgozásáért felelős osztály

    """

    def __init__(
        self,
        datum: object,
        napok: str,
        tanckar: str = None,
        zkr: str = False,
        ffikar: str = False,
        kozrem: str = False,
        kontakt: str = False,
        status: str = False,
        megjegy: str = False,
    ):
        """

        :param datum: Dátum: date
        :param napok: Napok: str
        :param tanckar: Tánckar
        :param zkr: Zenekar önálló
        :param ffikar: Férfikar
        :param kozrem: Közreműködők
        :param kontakt: Kontakt
        :param status: Státusz
        :param megjegy: Megjegyzés
        :return:

        """
        self.datum = datum
        self.napok = napok
        self.tanckar = tanckar
        self.zkr = zkr
        self.ffkar = ffikar
        self.egyez = kozrem
        self.kontakt = kontakt
        self.stat = status
        self.megjegy = megjegy
        self.tevekenyseg = None

    @property
    def tevekenyseg(self):
        """
        Ha a tevékenység nem megadott akkor
        automatikusan Előadás állítódik be.

        :return: A megadott vagy "Előadás"

        """
        return self._tevekenyseg

    @tevekenyseg.setter
    def tevekenyseg(self, t):
        if t:
            self._tevekenyseg = t
        else:
            self._tevekenyseg = "Előadás"

    @property
    def datum(self):
        """
        Dátum visszaadása

        :return: Dátum

        """
        return self._datum

    @datum.setter
    def datum(self, d):
        result = re.match(r"^\d+.\d+.\d+", str(d))
        if result:
            if isinstance(d, datetime.date):
                self._datum = d.strftime("%Y-%m-%d")
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
            c2db = v.split("/")  # A 0 az időpont/helyszín, az 1 pedig a műsor.
            idopont = re.match("[0-9][0-9].?[0-9][0-9]", c2db[0])
            try:
                c2db[1] = c2db[1].strip()
                self.musor = c2db[1]
                self.musor = " ".join(self.musor.split())
                # musor = re.escape(c2db[1])
            except IndexError:
                self.musor = "Nincs megadva műsor."
            if idopont:
                # kezdes = c1.value.replace(hour=int(idopont.group()[:2]), minute=00)
                self.kezdes = idopont.group()
                self.hely = c2db[0].replace(self.kezdes, "", 1)
                self.hely = " ".join(self.hely.split())
                # egyadat.helykod = hely
                # print(hely)
            else:
                self.kezdes = "Nincs megadva kezdés."
                self.hely = c2db[0]
                # kezdes = c1.value.replace(hour=00, minute=00)

    @property
    def ffkar(self):
        """
        műsor,hely,kezdés kiválogatása a bejövő adatokból

        :return: musor,hely,kezdes
        :rtype: str

        """
        return self._ffkar

    @ffkar.setter
    def ffkar(self, v):
        # outfile = open("ferfikarkimenet.txt", "a")
        if v:
            c2db = v.split("/")
            #    outfile.write('\t|'.join(c2db))
            #    outfile.write('\n')
            idopont = re.match("[0-9][0-9].?[0-9][0-9]", c2db[0])
            try:
                c2db[1] = c2db[1].strip()
                self.musor = c2db[1]
                self.musor = " ".join(self.musor.split())
            except IndexError:
                self.musor = "Nincs megadva műsor"
            if idopont:
                self.kezdes = idopont.group()
                self.hely = c2db[0].replace(self.kezdes, "", 1)
                self.hely = " ".join(self.hely.split())
                self.hely = cleaner(self.hely)
            else:
                self.kezdes = "Nincs megadva kezdés."
                self.hely = c2db[0]
        #    outfile.close()

    @property
    def megjegy(self):
        """
        Megjegyzés

        :return: a megjegyzés átírása

        """
        return self._megjegy

    @megjegy.setter
    def megjegy(self, v):
        if v:
            v = cleaner(v)
            self._megjegy = v
        else:
            self._megjegy = ""

    @property
    def kontakt(self):
        """
        Kapcsolattartó visszaadása

        :return: kontakt személy
        """
        return self._kontakt

    @kontakt.setter
    def kontakt(self, v):
        """
        Kapcslattartó beállítása

        :param: v: kontakt változó
        :type: v: str
        :return: kontakt vagy '' beállítása
        :rtype: str

        """
        if v:
            self._kontakt = cleaner(v)
        else:
            self._kontakt = ""


def teszt(sikeres_teszt):
    """
    Egy teszt eredményének megjelenítése.

    :param sikeres_teszt:
    :return: kiirja a tesztelt sort és az eredményt sikeres/SIKERTELEN

    """
    sorszam = sys._getframe(1).f_lineno  # A hívó sorénak széma
    if sikeres_teszt:
        print("A(z) {0}. sorban álló teszt".format(sorszam), end=" ")
        cprint.info("sikeres.")
    else:
        print("A(z) {0}. sorban álló teszt".format(sorszam), end=" ")
        cprint.info("SIKERTELEN.")


def tesztkeszlet():
    """
    Tesztkészlet a process funkciók miatt

    :return: Igaz vagy hamis lett a teszt
    :rtype: bool

    """
    egy = Egysor(datetime.date(2023, 1, 1), "hétfő")
    egy.datum = datetime.date(2023, 1, 1)
    teszt(egy.datum == "2023-01-01")
    egy.datum = ""
    teszt(egy.datum == "1978-02-26")
    ketto = Egysor(
        datetime.date(2023, 1, 1),
        "hétfő",
        "17:30 HM Eger, Egri Vár/ Táncra magyar! (KÜLÖN KERET 3.)",
        "14:00 Évadnyitó társulati ülés",
        "11:00 HM Budapest, Bálna, központi ünnepség (20 perc)",
        "10:00 Rendezvény kezdete, 11:30 HM Szabadszállás József Attila Művelődési Ház (Szabadszállás, "
        "Kossuth Lajos u. 4.) 40 perc",
        "Farkas Zoltán ny. alezredes 06302082062",
        "Zsurával egyeztetve 23.02.20.",
        "Táncművészeti Egyetem/ Bécs NWK 348",
        "A lejáró próbát Kernács Péter jelezte, mind Vicuska mind a kis Gergő kettős szereposztása miatt,"
        " minden a négyen új beállók, nem szükséges a teljes tánckar",
    )
    teszt(ketto.datum == "2023-01-01")
    teszt(ketto.napok == "hétfő")
    teszt(ketto.kezdes in ["17:30", "11:00"])
    teszt(
        ketto.hely
        in ["HM Eger, Egri Vár", "HM Budapest, Bálna, központi ünnepség (20 perc)"]
    )
    teszt(ketto.musor in ["Táncra magyar! (KÜLÖN KERET 3.)", "Nincs megadva műsor"])
    teszt(ketto.zkr == "14:00 Évadnyitó társulati ülés")
    teszt(
        ketto.egyez
        == "10:00 Rendezvény kezdete, 11:30 HM Szabadszállás József Attila Művelődési Ház ("
        "Szabadszállás, Kossuth Lajos u. 4.) 40 perc"
    )
    teszt(ketto.kontakt == "Farkas Zoltán ny. alezredes 06302082062")
    teszt(ketto.stat == "Zsurával egyeztetve 23.02.20.")
    teszt(ketto.kulszal == "Táncművészeti Egyetem/ Bécs NWK 348")
    teszt(
        ketto.megjegy
        == "A lejáró próbát Kernács Péter jelezte, mind Vicuska mind a kis Gergő kettős szereposztása "
        "miatt,"
        " minden a négyen új beállók, nem szükséges a teljes tánckar"
    )


if __name__ == "__main__":
    tesztkeszlet()
