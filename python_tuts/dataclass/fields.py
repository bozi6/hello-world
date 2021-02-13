from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int
    occupation: str = field(init=False, repr=False)


p = Person('John Doe', 34)
print(p)

p.occupation = "Gardener"
print(f'{p.name} is a {p.occupation}')
