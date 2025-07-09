#  pizza.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 11. 21:55
import math


class Pizza:
    def __init__(self, radius, ingredients=None):
        if ingredients is None:
            ingredients = []
        self.radius = radius
        self.ingredients = ingredients


    def __repr__(self):
        return f"Pizza({self.radius!r}, {self.ingredients!r})"

    @classmethod
    def margherita(cls):
        return cls(4, ["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(4, ["mozarella", "tomatoes", "ham"])

    def area(self):
        """Calculate and return the area of the pizza."""
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r**2 * math.pi

  
if __name__ == "__main__":
    p = Pizza(4, ["sajt", "paradicsom"])
    d = Pizza.margherita()
    print(p)
    print(p.area())
    print(p.circle_area(4))
