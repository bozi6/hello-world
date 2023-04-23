import datetime
import pprint
from datetime import date

class Bemeno:
    def __init__(self, datum, napok: None, tkzkr: None, zkr: None, ffk: None,
                 kuls: None, kont: None, stat: None, kulsz: None, megjegy: None, tev: None):
        self.honapok = ['JANUÁR', 'FEBRUÁR', 'MÁRCIUS',
                        'ÁPRILIS', 'MÁJUS', 'JÚNIUS',
                        'JÚLIUS', 'AUGUSZTUS', 'SZEPTEMBER',
                        'OKTÓBER', 'NOVEMBER', 'DECEMBER']

        self._erdekes = {'datum': datum,
                         'napok': napok,
                         'tkzkr': tkzkr,
                         'zkr': zkr,
                         'ffk': ffk,
                         'kuls': kuls,
                         'kont': kont,
                         'stat': stat,
                         'kulsz': kulsz,
                         'megjegy': megjegy,
                         'tev': tev,
                         }

    @property
    def datum(self):
        return self._erdekes['datum']

    @property
    def napok(self):
        return self._erdekes['napok']

    @property
    def tkzkr(self):
        return self._erdekes['tkzkr']

    @property
    def zkr(self):
        return self._erdekes['zkr']

    @property
    def ffk(self):
        return self._erdekes['ffk']

    @property
    def kuls(self):
        return self._erdekes['kuls']

    @property
    def kont(self):
        return self._erdekes['kont']

    @property
    def stat(self):
        return self._erdekes['stat']

    @property
    def kulsz(self):
        return self._erdekes['kulsz']

    @property
    def megjegy(self):
        return self._erdekes['megjegy']

    @property
    def tev(self):
        return self._erdekes['tev']

    @datum.setter
    def datum(self, value):
        if type(value) is not datetime.datetime:
            self._erdekes['datum'] = date.fromisoformat(value)
        else:
            datumszo = value.strftime("%Y-%m-%d")
            self._erdekes['datum'] = datumszo

    @napok.setter
    def napok(self, napok):
        self._erdekes['napok'] = napok

    @tkzkr.setter
    def tkzkr(self, tkzkr):
        self._erdekes['tkzkr'] = tkzkr

    @zkr.setter
    def zkr(self, zkr):
        self._erdekes['zkr'] = zkr

    @ffk.setter
    def ffk(self, ffk):
        self._erdekes['ffk'] = ffk

    @kuls.setter
    def kuls(self, kuls):
        self._erdekes['kuls'] = kuls

    @kont.setter
    def kont(self, kont):
        if kont is not None:
            szkont = " ".join(kont.split())
            self._erdekes['kont'] = szkont
        else:
            self._erdekes['kont'] = '-'

    @stat.setter
    def stat(self, stat):
        self._erdekes['stat'] = stat

    @kulsz.setter
    def kulsz(self, kulsz):
        self._erdekes['kulsz'] = kulsz

    @megjegy.setter
    def megjegy(self, megjegy):
        if megjegy is not None:
            szmeg = " ".join(megjegy.split())
            self._erdekes['megjegy'] = szmeg
        else:
            self._erdekes['megjegy'] = '-'

    @tev.setter
    def tev(self, tev):
        engtev = ('beépítés', 'bejárás', 'egyeztetés', 'elmarad', 'előadás', 'építés',
                  'esküvő', 'esőnap', 'felvétel', 'forgatás', 'fotózás', 'főpróba',
                  'gumicsere', 'hakken', 'karácsony', 'lemondva', 'molyirtás', 'munka',
                  'pihenő', 'prezentáció', 'próba', 'sajtótájékoztató', 'stream',
                  'szabadság', 'tanítás', 'társulati', 'temetés', 'turné', 'TV felvétel',
                  'utazás', 'utazónap', 'világítás')
        if tev.lower() in engtev:
            self._erdekes['tev'] = tev
        else:
            self._erdekes['tev'] = '-'
            raise ValueError('Nem ismert tevékenység:', tev)


if __name__ == "__main__":
    bem = Bemeno("2022.09.01", 'hétfő', 'Mindenki', 'Hegedős', 'férfikar',
                 'Rudi Pötsch', 'joskapista@nagyonfontos.tr', 'Valamilyen állapot',
                 'Egér haknizik, a többiek dolgoznak', 'Ide írok\n sok \t\t\n szép      megjegyzést', 'előadás')
    pprint.pprint(bem.__dict__)
    bem.tev = 'próba'
    print(bem.tev)
