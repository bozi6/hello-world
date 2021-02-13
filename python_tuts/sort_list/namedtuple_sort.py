#!/usr/bin/env python3

from typing import NamedTuple


class City(NamedTuple):
    id: int
    name: str
    population: int


c1 = City(1, 'Bratislava', 432000)
c2 = City(2, 'Budapest', 1759000)
c3 = City(3, 'Prague', 1280000)
c4 = City(4, 'Warsaw', 1748000)
c5 = City(5, 'Los Angeles', 3971000)
c6 = City(6, 'Edinburgh', 464000)
c7 = City(7, 'Berlin', 3671000)

cities = [c1, c2, c3, c4, c5, c6, c7]

cities.sort(key=lambda e: e.name)

for city in cities:
    print(city)
