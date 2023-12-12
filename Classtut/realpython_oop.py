import math


class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value


class Circle:
    radius = PositiveNumber()

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius**2, 2)


class Square:
    side = PositiveNumber()

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return round(self.side**2, 2)


circle_1 = Circle(42)
circle_2 = Circle(7)
print(circle_2.radius)
print(circle_2.calculate_area())
print(circle_1.radius)
print(circle_1.calculate_area())
circle_1.radius = 100
print(circle_1.radius)
print(circle_1.calculate_area())
circle_1.radius = 0
circle_1.radius = -100
circle_1.radius = "20"
