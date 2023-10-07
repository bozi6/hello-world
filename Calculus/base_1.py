

class Calculation(object):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


if __name__ == '__main__':
    sz = Calculation()
    print(sz.add(3, 2))
    print(sz.subtract(10, 3))
    print(sz.multiply(5, 3))
    print(sz.divide(30, 3))