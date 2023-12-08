NAME = "hemath"
YOB = 1999
ID_NUM = 17783


# access class constants from superclass to subclass
class C1:
    a_constant = 0.167355


class C2(C1):
    def this_constant(self):
        print(self.a_constant)


def main():
    print(NAME)
    an_object = C2()
    an_object.this_constant()


if __name__ == "__main__":
    main()
