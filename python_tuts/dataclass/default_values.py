if __name__ == "__main__":
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str = "ismeretlen"
        age: int = 0

    p = Person("John Doe", 34)
    print(p)

    p2 = Person()
    print(p2)
