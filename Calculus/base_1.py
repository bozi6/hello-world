"""
Számológép próbálkozás

"""


class Calculation(object):
    """
    Számológép osztály

    """

    def add(self, a, b):
        """
        Összeadó rész
        :return: az összeget adja vissza
        """
        return a + b

    def subtract(self, a, b):
        """
        Kivonás
        :return: az eredményt adja vissza
        """
        return a - b

    def multiply(self, a, b):
        """
        Szorzó rész
        :return: Az eredményt adja vissza
        """
        return a * b

    def divide(self, a, b):
        """
        Osztás fv.
        :return: Az erdményt adja vissza
        """
        return a / b


if __name__ == "__main__":
    sz = Calculation()
    print(sz.add(3, 2))
    print(sz.subtract(10, 3))
    print(sz.multiply(5, 3))
    print(sz.divide(30, 3))
