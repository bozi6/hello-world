# Refresh README.md file
import os
from datetime import datetime

from pathlib import Path

intro = """
# Python Home Projects
## Projects list:
| File Name | Creation Date | Last Modificated Date |
| --------- | ------------- | ------------------ |
"""

footer = """
---
## License

MIT

---
Created by kontab@gmail.com
\nLatest version generated:
"""
footer += str(datetime.now())

def dispcrmod(mappa):
    fdpaths = [fd for fd in os.listdir(mappa)]
    szoveg = {}
    i = 0
    for fdpath in fdpaths:
        statinfo = os.stat(str(mappa) + "/" + fdpath)
        creadate = datetime.fromtimestamp(statinfo.st_ctime)
        moddate = datetime.fromtimestamp(statinfo.st_mtime)
        szoveg[i] = {}
        szoveg[i]['sorsz'] = i
        szoveg[i]['filename'] = fdpath
        szoveg[i]['createdate'] = creadate
        szoveg[i]['moddate'] = moddate
        i += 1
    return szoveg


def mappalista(mappa):
    dirs = []
    for f in sorted(mappa.iterdir()):
        if f.is_dir():
            if f.name[0] != '.':
                dirs.append(f.name)
    return dirs


def main():
    link = "https://github.com/bozi6/hello-world/tree/master/"
    path = Path.cwd()
    szovegek = dispcrmod(path)
    filepath = Path.cwd() / "README.md"
    with filepath.open("w", encoding="utf-8") as f:
        f.write(intro)
        for k, v in szovegek.items():
            if v['filename'][0] != '.':
                irando = f"| [{v['filename']}]({link+v['filename']}) | {v["createdate"]} | {v["moddate"]} |\n"
                f.write(irando)
        f.write(footer)

if __name__ == '__main__':
    main()
