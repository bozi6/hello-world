#  kpo.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 03. 24. 9:49
import random
from dataclasses import dataclass

# ... existing code ...

KOROK_SZAMA = 1_000_000


@dataclass
class JatekElem:
    azonosito: int
    utes_ellen: int
    nev: str
    pont: int = 0

    def pontot_ad(self) -> None:
        self.pont += 1

    def reset(self) -> None:
        self.pont = 0


class Ko(JatekElem):
    def __init__(self) -> None:
        super().__init__(azonosito=1, utes_ellen=3, nev="Kaics")


class Papir(JatekElem):
    def __init__(self) -> None:
        super().__init__(azonosito=2, utes_ellen=1, nev="Papír")


class Ollo(JatekElem):
    def __init__(self) -> None:
        super().__init__(azonosito=3, utes_ellen=2, nev="Olló")


def valassz_ketto_kulonbozot(elemmek: list[JatekElem]) -> tuple[JatekElem, JatekElem]:
    """Visszaad két különböző, véletlenszerűen választott elemet."""
    elso = random.choice(elemmek)
    masodik = random.choice(elemmek)
    while masodik.azonosito == elso.azonosito:
        masodik = random.choice(elemmek)
    return elso, masodik


def jatsz_kor(egy: JatekElem, ketto: JatekElem) -> None:
    """Lejátszik egy kört és kiosztja a pontokat."""
    if egy.azonosito == ketto.utes_ellen:
        ketto.pontot_ad()
    elif ketto.azonosito == egy.utes_ellen:
        egy.pontot_ad()


def main() -> None:
    ko = Ko()
    papir = Papir()
    ollo = Ollo()
    targyak: list[JatekElem] = [ko, papir, ollo]

    for _ in range(KOROK_SZAMA):
        egy, ketto = valassz_ketto_kulonbozot(targyak)
        jatsz_kor(egy, ketto)

    print(f"{KOROK_SZAMA} iterációból.")
    for elem in targyak:
        print(f"{elem.nev} - {elem.pont:,.0f} db.")


if __name__ == "__main__":
    main()
