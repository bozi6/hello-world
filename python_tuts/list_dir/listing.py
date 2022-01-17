

from pathlib import Path

path = '.'

for path in Path(path).iterdir():
    print(path)
