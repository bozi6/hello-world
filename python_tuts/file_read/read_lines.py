#!/usr/bin/python

with open('works.txt', 'r') as f:
    lines = f.readlines()

    print(lines)

    for line in lines:
        print(line.strip())
