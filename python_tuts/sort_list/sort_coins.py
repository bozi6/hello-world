#!/usr/bin/env python3

from functools import total_ordering
from typing import NamedTuple


# a gold coin equals to two silver and six bronze coins


class Coin(NamedTuple):
    rank: str


@total_ordering
class Pouch:

    def __init__(self):
        self.bag = []

    def add(self, coin):

        self.bag.append(coin)

    def __eq__(self, other):

        val1, val2 = self.__evaluate(other)

        if val1 == val2:
            return True
        else:
            return False

    def __lt__(self, other):

        val1, val2 = self.__evaluate(other)

        if val1 < val2:
            return True
        else:
            return False

    def __str__(self):

        return f'Pouch with: {self.bag}'

    def __evaluate(self, other):

        val1 = 0
        val2 = 0

        for coin in self.bag:

            if coin.rank == 'g':
                val1 += 6

            if coin.rank == 's':
                val1 += 3

            if coin.rank == 'b':
                val1 += 1

        for coin in other.bag:

            if coin.rank == 'g':
                val2 += 6

            if coin.rank == 's':
                val2 += 3

            if coin.rank == 'b':
                val2 += 1

        return val1, val2


def create_pouches():
    p1 = Pouch()

    p1.add(Coin('g'))
    p1.add(Coin('b'))
    p1.add(Coin('s'))

    p2 = Pouch()

    p2.add(Coin('g'))
    p2.add(Coin('s'))

    p3 = Pouch()

    p3.add(Coin('b'))
    p3.add(Coin('s'))
    p3.add(Coin('s'))

    p4 = Pouch()

    p4.add(Coin('b'))
    p4.add(Coin('s'))

    p5 = Pouch()

    p5.add(Coin('g'))
    p5.add(Coin('s'))
    p5.add(Coin('s'))
    p5.add(Coin('b'))
    p5.add(Coin('b'))
    p5.add(Coin('b'))

    p6 = Pouch()

    p6.add(Coin('b'))
    p6.add(Coin('b'))
    p6.add(Coin('b'))
    p6.add(Coin('b'))
    p6.add(Coin('b'))

    p7 = Pouch()
    p7.add(Coin('g'))

    p8 = Pouch()
    p8.add(Coin('g'))
    p8.add(Coin('g'))
    p8.add(Coin('s'))

    bag = [p1, p2, p3, p4, p5, p6, p7, p8]

    return bag


bag = create_pouches()
bag.sort()

for e in bag:
    print(e)
