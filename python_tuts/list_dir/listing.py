from pathlib import Path

if __name__ == "__main__":
    path = "."

    for path in Path(path).iterdir():
        print(path)
