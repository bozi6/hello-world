#!/usr/bin/python3

from pathlib import Path

if __name__ == "__main__":
    path = Path(".")

    dirs = [e for e in path.iterdir() if e.is_dir()]

    for dir in dirs:
        print(dir)
        # print(dir.parts[-1])
