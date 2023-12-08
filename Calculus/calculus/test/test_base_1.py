from Calculus.base_1 import Calculation
from twisted.trial import unittest

"""
Tesztesetek
"""


class TestBase_1(unittest.TestCase):
    """
    Tesztelési osztály
    """

    def test_add(self):
        """
        Összeadás tesztelése
        """
        calc = Calculation()
        result = calc.add(3, 8)
        self.assertEqual(result, 11)

    def test_subtract(self):
        """ "
        Kivonás tesztelése
        """
        calc = Calculation()
        result = calc.subtract(7, 3)
        self.assertEqual(result, 4)

    def test_multiply(self):
        """
        Szorzás tesztelése
        """
        calc = Calculation()
        result = calc.multiply(12, 5)
        self.assertEqual(result, 60)

    def test_divide(self):
        """
        Osztás tesztelése
        """
        calc = Calculation()
        result = calc.divide(12, 4)
        self.assertEqual(result, 3)
