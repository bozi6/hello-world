#!/usr/bin/python

f = None

try:

    f = open('works.txt', 'r')

    for line in f:
        print(line.rstrip())

except IOError as e:

    print(e)

finally:

    if f:
        f.close()
