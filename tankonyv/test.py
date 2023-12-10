import sys
import unittest as teszteles


class Test(teszteles.TestCase):
    def abstest(self):
        self.assertEqual(abszolut_ertek(17), 17)
        self.assertEqual(abszolut_ertek(-17), 17)
        self.assertEqual(abszolut_ertek(0), 0)
        self.assertEqual(abszolut_ertek(3.14), 3.14)
        self.assertEqual(abszolut_ertek(-3.14), 3.14)


def teszt(sikeres_teszt):
    """ """
    sorszam = sys._getframe(1).f_lineno  # a hívó sorának száma.
    if sikeres_teszt:
        msg = "A(z) {}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = "A(z) {}. sorban álló teszt SIKERTELEN.".format(sorszam)
    print(msg)


def abszolut_ertek(x):
    """
    A szám abszolút értékét adja vissza

    :param x: a szám
    :type x: int
    :return: a szám abszolút értéke
    :rtype: int

    """
    if x < 0:
        return -x
    return x


def tesztkeszlet():
    teszt(abszolut_ertek(17) == 17)
    teszt(abszolut_ertek(-17) == 17)
    teszt(abszolut_ertek(0) == 0)
    teszt(abszolut_ertek(3.14) == 3.14)
    teszt(abszolut_ertek(-3.14) == 3.14)


class Foo:
    """Docstring for class Foo."""

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5  #: Doc comment for Foo.flox. One line only.

    baz = 2
    """Docstring for class attribute Foo.baz."""

    def __init__(self):
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""


if __name__ == "__main__":
    teszteles.main()
