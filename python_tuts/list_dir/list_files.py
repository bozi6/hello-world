#!/usr/bin/python3

from pathlib import Path


if __name__ == "__main__":
    path = Path("../")

    files = [e for e in path.iterdir() if e.is_file()]

    for file in files:
        print(file)
