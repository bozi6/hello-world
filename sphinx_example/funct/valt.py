"""
Váltó modul ami segíti az átváltásokat.
"""


class Valto:
    """Váltó ősosztály, a váltások alapjai :-)"""

    def __init__(self):
        """
        Kezdeti érték megadása
        """
        self.mit = "celsius"

    @property
    def adod(self, a, b):
        """
        Két érték összeadása
        :param a:
        :param b:
        :return:
        """
        return a + b
