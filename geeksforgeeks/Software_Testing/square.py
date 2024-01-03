#  square.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 19. 21:41
class Square:
    def __init__(self, side):
        """
        Create a square having the given side

        :param side: The square side
        :type side: int

        """
        self.side = side

    def area(self):
        """
        Returns Area of the square

        :return: Area
        :rtype: int

        """
        try:
            if self.side >= 0:
                return self.side**2
            else:
                return -1
        except TypeError:
            return -1

    def perimeter(self):
        """
        Returns the perimeter of the square

        :return: Perimeter
        :rtype: int

        """
        try:
            if self.side >= 0:
                return 4 * self.side
            else:
                return -1
        except TypeError:
            return -1
        except ValueError:
            return -1

    def __repr__(self):
        """
        Declare how a Square object should be printed

        :return: printed object
        :rtype: str

        """
        s = (
            "Négyzet, oldala = "
            + str(self.side)
            + "\n"
            + "Terület = "
            + str(self.area())
            + "\n"
            + "Kerület = "
            + str(self.perimeter())
        )
        return s


if __name__ == "__main__":
    # Read input from user
    side = int(input("add meg a négyzet oldalát: "))

    # Create a square with the provided side
    square = Square(side)

    # Print the created square
    print(square)
