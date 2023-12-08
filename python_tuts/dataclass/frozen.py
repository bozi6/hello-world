if __name__ == "__main__":
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Person:
        name: str
        age: int

    p = Person("John Doe", 34)
    p.occupation = "gardener"

    print(p)
    print(p.occupation)
