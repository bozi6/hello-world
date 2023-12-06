#!/usr/bin/env python3
import datetime
import logging
import re

import openpyxl

"""
Autentik converter 2020

"""


def main():
    """
    Főprogram
    :return: None

    """
    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s  - %(message)s")
    logging.disable(logging.DEBUG)  # Akkor kell ha már nem akarunk Debuggolni. :-)
    logging.disable(logging.INFO)
    logging.info("Program elkezdődött.")

    bem = "../xlsxs/2020. AUTENTIKUS.xlsx"
    kim = "2020_Autentikus.sql"

    f = open(kim, "w")
    f.write("# Honvédelmi adatok 2020-ra az autentikusból\n")
    f.write("# Készítette: Konta Boáz (kontab6@gmail.com).\n")
    f.write("USE honved2;\n")
    print("Bemeneti fájl: " + bem)
    print("Kimenetei fájl: " + kim)
    wb = openpyxl.load_workbook(filename=bem, read_only=True)
    # read_only elvileg gyorsabb és amúgy sem akarunk írni bele.
    for sh in wb.worksheets:  # Végigmegyünk a munkafüzet lapjain
        cells = sh["A2":"I210"]  # I210 a vége
        i = 0
        """ Az értékek a következők:
        c1  - Dátum ( óraperc nélkül )
        c2  - Tánckar és Zenekar
        c3  - Zenekar önálló
        c4  - Férfikar
        c5  - Közreműködők egyeztetés alatt
        c6  - Kontakt
        c7  - Státusz
        c8  - Külsős szállítás
        c9  - megjegyzés
        c10 -  megjegyzés volt de már elmúlt
        Ezek a 2018_AUTENTIKUS.xlsx táblázat fejlécsorának összetevői.
        Továbbá! Közhírré tétetik!
        Az excel fileban a dátum mezőt tessék rendesen beállítani.
        """
        print(sh.title)
        for c1, c2, c3, c4, c5, c6, c7, c8, c9 in cells:
            if c1.value is not None and c2.value is not None:  # dátum tánckar kitöltve
                if isinstance(c1.value, datetime.date):
                    d = c1.value.strftime("%Y-%m-%d")  # d = datum
                else:
                    d = c1.value[0:6].replace(" ", "")
                    d = d[0:5].replace(".", "-")
                    logging.info("datum valtozo értéke most: ".format(d))
                    # d = c1.value[0:6].replace('.', '-')
                    d = "2020-" + d.strip()
                    # ha string => .->- és marad az első 10 karakter
                logging.debug("Datum mező:{} , típusa:{} ".format(d, type(d)))
                logging.debug(
                    "Változók értéke:\n\t Dátum: {}\n\t Tánc: {}\n\t Zkr: {}\n\t FFikar: {}\n\t \
                        Egyeztet: {}\n\t Kontakt: {}\n\t Státusz: {}\n\t Külszáll: {}\n\t Megjegy: {}\n\t".format(
                        c1.value,
                        c2.value,
                        c3.value,
                        c4.value,
                        c5.value,
                        c6.value,
                        c7.value,
                        c8.value,
                        c9.value,
                    )
                )
                sql = "INSERT INTO aut (sorsz,datum,ceg,kezd,hely,musor,kontakt,megjegyzes,helykod) VALUES ( NULL,"
                c2db = c2.value.split(
                    "/"
                )  # A 0 az időpont/helyszín, az 1 pedig a műsor.
                idopont = re.match("[0-9][0-9].?[0-9][0-9]", c2db[0])
                try:
                    musor = re.escape(c2db[1])
                except IndexError:
                    musor = "Nincs megadva műsor."
                    logging.debug("IndexError - Nincs megadva műsor.")
                if idopont:
                    logging.debug("Van időpont!")
                    # kezdes = c1.value.replace(hour=int(idopont.group()[:2]), minute=00)
                    kezdes = idopont.group()
                    hely = c2db[0].replace(kezdes, "", 1)
                    logging.debug("Helyszín eredménye: " + hely)
                else:
                    kezdes = "Nincs megadva kezdés."
                    hely = c2db[0]
                    logging.debug("Kezdés eredménye: " + hely)
                    # kezdes = c1.value.replace(hour=00, minute=00)
                if c8.value is not None:
                    kontakt = c8.value
                else:
                    kontakt = ""
                if c9.value is not None:
                    megjegyzes = c9.value
                else:
                    megjegyzes = ""
                datum = d
                logging.debug("Kezdési időpont kialakult: " + str(kezdes))
                sql += '"'
                sql += str(datum)  # Dátum
                sql += '",'
                sql += '"24","'  # Cég
                sql += kezdes  # Kezdes
                sql += '","'
                sql += hely.strip()  # Hely
                sql += '","'
                sql += musor  # Musor
                sql += '","'
                sql += kontakt  # Kontakt
                sql += '","'
                sql += megjegyzes  # Megjegyzés
                sql += '","'
                sql += str(0)  # helykod
                sql += '");\n'
                logging.debug(sql)
                f.write(sql)
                # print(c1.value,c2.value,c3.value,c4.value,c5.value,c6.value,c7.value,c8.value,c9.value)
                i = i + 1  # feldolgozott sorok száma.
        print("{}. sor feldolgozva.".format(i))
    f.close()
    print("Fájl kiírása befejezve.")


if __name__ == "__main__":
    main()
