#!/usr/bin/env python3


vals = [(4, 0), (0, -2), (3, 5), (1, 1), (-1, 3)]

vals.sort()
print(vals)

vals.sort(key=lambda e: e[1])
print(vals)
