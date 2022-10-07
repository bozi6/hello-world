class Bemeno(object):
    def __init__(self):
        self.honapok = ['JANUÁR', 'FEBRUÁR', 'MÁRCIUS',
                        'ÁPRILIS', 'MÁJUS', 'JÚNIUS',
                        'JÚLIUS', 'AUGUSZTUS', 'SZEPTEMBER',
                        'OKTÓBER', 'NOVEMBER', 'DECEMBER']
        self._erdekes = {'datum': '',
                         'napok': '',
                         'tkzkr': '',
                         'zkr': '',
                         'ffk': '',
                         'kuls': '',
                         'kont': '',
                         'stat': '',
                         'kulsz': '',
                         'megjegy': '',
                         }

    @property
    def datum(self):
        return self._erdekes['datum']

    def napok(self):
        return self._erdekes['napok']

    def tkzkr(self):
        return self._erdekes['tkzkr']

    def zkr(self):
        return self._erdekes['zkr']

    def ffk(self):
        return self._erdekes['ffk']

    def kuls(self):
        return self._erdekes['kuls']

    def kont(self):
        return self._erdekes['kont']

    def stat(self):
        return self._erdekes['stat']

    def kulsz(self):
        return self._erdekes['kulsz']

    def megjegy(self):
        return self._erdekes['megjegy']

    @datum.setter
    def datum(self, date):
        if date >= '2022.12.12':
            raise ValueError("Ez már jövendőbeli dátum")
        self._erdekes['datum'] = date


if __name__ == "__main__":
    bem = Bemeno()
    bem.datum = "2022.09.01"
    print(bem.__dict__)
