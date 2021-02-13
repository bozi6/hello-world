#!/usr/bin/python

from pathlib import Path

path = Path('../')

files = [e for e in path.iterdir() if e.is_file()]

for file in files:
    print(file)
