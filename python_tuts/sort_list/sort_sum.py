#!/usr/bin/env python3


data = [[10, 11, 12, 13], [9, 10, 11, 12], [8, 9, 10, 11], [10, 9, 8, 7],
        [6, 7, 8, 9], [5, 5, 5, 1], [5, 5, 5, 5], [3, 4, 5, 6], [10, 1, 1, 2]]

data.sort()
print(data)

data.sort(key=sum)
print(data)
