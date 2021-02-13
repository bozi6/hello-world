from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


p = Person('John Doe', 34)
print(p)
