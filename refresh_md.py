"""Refresh the readme.md file."""

import os
from datetime import datetime
from pathlib import Path

intro = """
# Python Home Projects
## Projects list:
| File Name | Creation Date | Last Modificated Date | Description |
| --------- | ------------- | --------------------- | ----------- |
"""

footer = """
---
## License  
MIT  
---  
Created by kontab@gmail.com  
Latest version generated:
"""
footer += str(datetime.today().strftime('%Y-%m-%d %H:%m:%S'))


def dispcrmod(mappa):
    """
    Create a dictionary from directories with some date info.

    :param mappa: current working directory
    :return:dictionary: contains number, filename, creation date, modified date
    """
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
        szoveg[i]['createdate'] = creadate.strftime('%Y-%m-%d %H:%m:%S')
        szoveg[i]['moddate'] = moddate.strftime('%Y-%m-%d %H:%m:%S')
        i += 1
    return szoveg


def mappalista(mappa):
    """
    Return list of directories not included hidden one.

    :param mappa: current working directory
    :return: array of directories
    """
    dirs = []
    for f in sorted(mappa.iterdir()):
        if f.is_dir():
            if f.name[0] != '.':
                dirs.append(f.name)
    return dirs


def leirasszedo(mappa):
    """Description.txt file reader."""
    filepath = Path.cwd() / mappa / "description.txt"
    try:
        with filepath.open("r", encoding="utf-8") as f:
            leir = f.read()
    except:
        leir = '-'
    return leir


def main():
    """
    Refresh the README.md file in current working directory.

    :return: nothing
    """
    link = "https://github.com/bozi6/hello-world/tree/master/"
    path = Path.cwd()
    szovegek = dispcrmod(path)
    filepath = path / "README.md"
    with filepath.open("w", encoding="utf-8") as f:
        f.write(intro)
        for k, v in szovegek.items():
            if v['filename'][0] != '.':
                desc = leirasszedo(path / v['filename'])
                irando = f"| [{v['filename']}]({link + v['filename']}) | {v["createdate"]} | {v["moddate"]} | {desc}\n"
                f.write(irando)
        f.write(footer)


if __name__ == '__main__':
    main()
