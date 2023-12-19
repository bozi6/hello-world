#  person.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 19. 9:24
from datetime import date


# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def from_FathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def from_BirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

    @staticmethod
    def isAdult(age):
        return age > 18


class Man(Person):
    sex = "Female"


man = Man.from_BirthYear("John", 1985)
print(isinstance(man, Man))
man1 = Man.from_FathersAge("John", 1965, 20)
print(isinstance(man1, Man))
person1 = Person("mayank", 21)
person2 = Person.from_BirthYear("mayank", 1996)
print(person1.age)
print(person2.age)
print(Person.isAdult(22))
