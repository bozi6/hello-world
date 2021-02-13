from dataclasses import dataclass, asdict


@dataclass
class Person:
    name: str
    occupation: str
    age: int


p = Person('John Doe', 'gardener', 34)
print(p)

print(asdict(p))
