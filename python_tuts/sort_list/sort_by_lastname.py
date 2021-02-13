#!/usr/bin/env python3


names = ['John Doe', 'Jane Doe', 'Robert Brown', 'Robert Novak',
         'Lucia Smith', 'Patrick Dempsey', 'George Marshall', 'Alan Brooke',
         'Harold Andras', 'Albert Doe']

names.sort()
names.sort(key=lambda e: e.split()[-1])

for name in names:
    print(name)
