""""
A hőmérsékleti modul: Az éves hőméréskletet könyedén manipulálja


Könnyedén kiszámolja a napi átlagos hőnérsékletet
"""

from typing import List


class Probaoszt:
    """
    Osztály ami semmit nem csinál csak létezik...
    """

    def __init__(self):
        self.valami = 5


class HighTemperature:
    """Osztály ami mutatja a nagyon magas hőméréskletet"""

    def __init__(self, value: float):
        """
        :param value: hőméréskleti érték
        """

        self.value = value


def daily_average(temperatures: List[float]) -> float:
    """
    Napi átlaghőmérésklet megszerzése

    :param temperatures: hőmérsékletek listája
    :return: átlaghőnérséklet
    """

    return sum(temperatures) / len(temperatures)
