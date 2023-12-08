if __name__ == "__main__":

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"Person{{name: {self.name}, age: {self.age}}}"

    p = Person("John Doe", 34)
    print(p)
