#  tests.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 19. 21:55
import unittest

from .. import square


class TestClass(unittest.TestCase):
    def test_area(self):
        sq = square.Square(2)

        self.assertEqual(
            sq.area(), 4, f"Area is shown {sq.area()} for side = {sq.side} units"
        )

    def test_area_negative(self):
        sq = square.Square(-3)
        self.assertEqual(sq.area(), -1, f"Area is shown {sq.area()} rather than -1")

    def test_perimeter(self):
        sq = square.Square(5)
        self.assertEqual(
            sq.perimeter(), 20, f"Perimeter is {sq.perimeter()} rather than 20"
        )

    def test_perimeter_negative(self):
        sq = square.Square(-6)
        self.assertEqual(
            sq.perimeter(), -1, f"Perimeter is {sq.perimeter()} rather than -1"
        )

    def test_area_isint(self):
        sq = square.Square("lófasz")
        self.assertEqual(sq.area(), -1, f"Area is {sq.area()} rather than -1")

    def test_perimeter_isint(self):
        sq = square.Square("lófasz")
        self.assertEqual(
            sq.perimeter(), -1, f"Perimeter is {sq.perimeter()} rather than -1"
        )


if __name__ == "__main__":
    unittest.main()
