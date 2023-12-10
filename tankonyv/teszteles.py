import unittest


class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        """
        Int to float conversion tester

        :return: Float presentation of number
        :rtype: float

        """
        self.assertEqual(1, 1.0)
