import datetime
from datetime import date

from mysqlcrud import helykerd

"""
Régebbi (szar) funkciók az autentikhoz

"""


class Bemeno:
    """
    Bemenő adatok szortírozása, vagy mi a lófa.

    """

    def __init__(
        self,
        datum: date,
        napok,
        tkzkr,
        zkr="-",
        ffk="-",
        kuls="-",
        kont="-",
        stat="-",
        kulsz="-",
        megjegy="-",
        tev="-",
    ):
        """
        :type datum: date
        :type napok: str
        :type tkzkr: str
        :type zkr: str
        :type ffk: str
        :type kuls: str
        :type kont: str
        :type stat: str
        :type kulsz: str
        :type megjegy: str
        :type tev: str
        """
        helykod = 0
        self.honapok = [
            "JANUÁR",
            "FEBRUÁR",
            "MÁRCIUS",
            "ÁPRILIS",
            "MÁJUS",
            "JÚNIUS",
            "JÚLIUS",
            "AUGUSZTUS",
            "SZEPTEMBER",
            "OKTÓBER",
            "NOVEMBER",
            "DECEMBER",
        ]

        self._erdekes = {
            "datum": datum,
            "napok": napok,
            "tkzkr": tkzkr,
            "zkr": zkr,
            "ffk": ffk,
            "kuls": kuls,
            "kont": kont,
            "stat": stat,
            "kulsz": kulsz,
            "megjegy": megjegy,
            "tev": tev,
            "helykod": helykod,
        }

    @property
    def datum(self):
        """dátum bevitele"""
        return self._erdekes["datum"]

    @property
    def napok(self):
        """napok bevitele / nincs használva semmire"""
        return self._erdekes["napok"]

    @property
    def tkzkr(self):
        """tánckar zenekar mező"""
        return self._erdekes["tkzkr"]

    @property
    def zkr(self):
        """zenekar önálló mező"""
        return self._erdekes["zkr"]

    @property
    def ffk(self):
        """Férfikari mező"""
        return self._erdekes["ffk"]

    @property
    def kuls(self):
        """külsős mező"""
        return self._erdekes["kuls"]

    @property
    def kont(self):
        """kontakt mező"""
        return self._erdekes["kont"]

    @property
    def stat(self):
        """státusz mező"""
        return self._erdekes["stat"]

    @property
    def kulsz(self):
        """külső szállítás mező"""
        return self._erdekes["kulsz"]

    @property
    def megjegy(self):
        """megjegyzés mező"""
        return self._erdekes["megjegy"]

    @property
    def tev(self):
        """tevékenység mező /kitalált"""
        return self._erdekes["tev"]

    @property
    def helykod(self):
        """helykód visszaadása"""
        return self._erdekes["helykod"]

    @datum.setter
    def datum(self, value):
        """dátum beállítása"""
        if type(value) is not datetime.datetime:
            self._erdekes["datum"] = date.fromisoformat(value)
        else:
            datumszo = value.strftime("%Y-%m-%d")
            self._erdekes["datum"] = datumszo

    @napok.setter
    def napok(self, _value):
        self._erdekes["napok"] = _value

    @tkzkr.setter
    def tkzkr(self, tkzkr):
        """tánckar beállítása"""
        self._erdekes["tkzkr"] = tkzkr

    @zkr.setter
    def zkr(self, zkr):
        """ "zenekar beállítása"""
        self._erdekes["zkr"] = zkr

    @ffk.setter
    def ffk(self, ffk):
        self._erdekes["ffk"] = ffk

    @kuls.setter
    def kuls(self, kuls):
        self._erdekes["kuls"] = kuls

    @kont.setter
    def kont(self, kont):
        """kontakt mező beállítása"""
        if kont is not None:
            szkont = " ".join(kont.split())
            self._erdekes["kont"] = szkont
        else:
            self._erdekes["kont"] = "-"

    @stat.setter
    def stat(self, stat):
        self._erdekes["stat"] = stat

    @kulsz.setter
    def kulsz(self, kulsz):
        if kulsz is not None:
            self._erdekes["kulsz"] = kulsz
        else:
            self._erdekes["kulsz"] = "-"

    @megjegy.setter
    def megjegy(self, megjegy):
        if megjegy is not None:
            szmeg = " ".join(megjegy.split())
            self._erdekes["megjegy"] = szmeg
        else:
            self._erdekes["megjegy"] = "-"

    @tev.setter
    def tev(self, tev):
        engtev = (
            "beépítés",
            "bejárás",
            "egyeztetés",
            "elmarad",
            "előadás",
            "építés",
            "esküvő",
            "esőnap",
            "felvétel",
            "forgatás",
            "fotózás",
            "főpróba",
            "gumicsere",
            "hakken",
            "karácsony",
            "lemondva",
            "molyirtás",
            "munka",
            "pihenő",
            "prezentáció",
            "próba",
            "sajtótájékoztató",
            "stream",
            "szabadság",
            "tanítás",
            "társulati",
            "temetés",
            "turné",
            "TV felvétel",
            "utazás",
            "utazónap",
            "világítás",
        )
        if tev.lower() in engtev:
            self._erdekes["tev"] = tev
        else:
            self._erdekes["tev"] = "-"
            print("Nem ismert tevékenység:", tev)

    @helykod.setter
    def helykod(self, value):
        return helykerd(value)


if __name__ == "__main__":
    bem = Bemeno(
        "2022-09-01",
        "hétfő",
        "Mindenki",
        "Hegedős",
        "férfikar",
        "Rudi Pietsch",
        "joskapista@nagyonfontos.tr",
        "Valamilyen állapot",
        "Egér haknizik, a többiek dolgoznak",
        "Ide írok\n sok \t\t\n szép      megjegyzést",
        "előadás",
    )
    result = helykerd("Bp., Müpa Fesztivál Színház")
    print("Keresés eredménye: ", result)
    print("találat(ok):")
    i = 1
    if result:
        for x in result:
            print("{}; - {}".format(i, x))
            i += 1
        i = 1
    else:
        print("Nincs találat.")
