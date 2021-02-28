import sys
import teszteles


class Test(teszteles.TestCase):
    def abstest(self):
        self.assertEqual(abszolut_ertek(17), 17)
        self.assertEqual(abszolut_ertek(-17), 17)
        self.assertEqual(abszolut_ertek(0), 0)
        self.assertEqual(abszolut_ertek(3.14), 3.14)
        self.assertEqual(abszolut_ertek(-3.14), 3.14)


def teszt(sikeres_teszt):
    """ Egy teszt eredményének megjelenítése."""
    sorszam = sys._getframe(1).f_lineno  # a hívó sorának száma.
    if sikeres_teszt:
        msg = "A(z) {}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = "A(z) {}. sorban álló teszt SIKERTELEN.".format(sorszam)
    print(msg)


def abszolut_ertek(x):
    if x < 0:
        return -x
    return x


def tesztkeszlet():
    teszt(abszolut_ertek(17) == 17)
    teszt(abszolut_ertek(-17) == 17)
    teszt(abszolut_ertek(0) == 0)
    teszt(abszolut_ertek(3.14) == 3.14)
    teszt(abszolut_ertek(-3.14) == 3.14)


if __name__ == '__main__':
    teszteles.main()
