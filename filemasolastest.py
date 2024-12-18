"""Fájl másolgatása."""
import shutil
import sys
import time


def main():
    """
    Átmásol egy iso fájlt.

    :return: a másolt file
    :rtype: object

    """
    source = r"z:\boz\progz\Adobe.Photoshop.CC.2018.v19.1.6.HUN.x86-x64-D.G\d.g-ad.ps.2018.v19.1.6.iso"
    target = r"c:\temp\fotoshopp.iso"

    # assert not os.path.isabs(source)
    # target = os.path.join(target, os.path.dirname(source))
    print(target)
    # create the folders if not already exists
    # os.makedirs(target)

    # hibakezelés
    try:
        k = time.time()
        shutil.copy(source, target)
    except IOError as e:
        print("Nem lehet másolni a fájlt. %s" % e)
    except EOFError:
        print("Nem várt hiba történt:", sys.exc_info())

    print("Időben: ", time.time() - k)


if __name__ == "__main__":
    main()
