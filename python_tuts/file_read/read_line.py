#!/usr/bin/python

with open('works.txt', 'r') as f:

    line = f.readline()
    print(line.rstrip())

    line2 = f.readline()
    print(line2.rstrip())

    line3 = f.readline()
    print(line3.rstrip())