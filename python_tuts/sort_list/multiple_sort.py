#!/usr/bin/env python3

from operator import attrgetter
from typing import NamedTuple


def multi_sort(data, specs):
    for key, reverse in reversed(specs):
        data.sort(key=attrgetter(key), reverse=reverse)
    return data


class Student(NamedTuple):
    id: int
    name: str
    grade: str
    age: int


s1 = Student(1, 'Patrick', 'A', 21)
s2 = Student(2, 'Lucia', 'B', 19)
s3 = Student(3, 'Robert', 'C', 19)
s4 = Student(4, 'Monika', 'A', 22)
s5 = Student(5, 'Thomas', 'D', 20)
s6 = Student(6, 'Petra', 'B', 18)
s6 = Student(7, 'Sofia', 'A', 18)
s7 = Student(8, 'Harold', 'E', 22)
s8 = Student(9, 'Arnold', 'B', 23)

students = [s1, s2, s3, s4, s5, s6, s7, s8]

multi_sort(students, (('grade', False), ('age', True)))

for student in students:
    print(student)
