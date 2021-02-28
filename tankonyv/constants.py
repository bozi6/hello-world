NAME = 'hemath'
YOB = 1999
ID_NUM = 17783
print(NAME)


# access class constants from superclass to subclass
class C1:
    a_constant = 0.167355


class C2(C1):
    def this_constant(self):
        print(self.a_constant)


an_object = C2()
an_object.this_constant()
