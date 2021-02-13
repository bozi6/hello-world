#!/usr/bin/env python3


data = 'A+ A A- B+ B B- C+ C C- D+ D'
grades = {grade: idx for idx, grade in enumerate(data.split())}


def mc(e):
    return grades.get(e[1])


students = [('Anna', 'A+'), ('Jozef', 'B'), ('Rebecca', 'B-'), ('Michael', 'D+'),
            ('Zoltan', 'A-'), ('Jan', 'A'), ('Michelle', 'C-'), ('Sofia', 'C+')]

print(grades)

students.sort(key=mc)
print(students)

# from operator import itemgetter
# students.sort(key=lambda e: itemgetter(e[1])(grades))
