#!/usr/bin/env python3
import datetime
import logging
import re
import time

import openpyxl
import sqlescapy

"""
Autentika converter 2021

"""


def main():
    """
    Főprogram xlsből sql 2021-re

    :return: SQL fileok
    :rtype: str

    """
    kezd = time.time()

    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s  - %(message)s")
    logging.disable(logging.DEBUG)  # Akkor kell ha már nem akarunk Debuggolni. :-)
    logging.disable(logging.INFO)
    logging.info("Program elkezdődött.")

    bem = "../xlsxs/2021. AUTENTIKUS.xlsx"
    kim = "../sql/2021_Autentikus.sql"
    sql = ""
    honapok = [
        "JANUÁR",
        "FEBRUÁR",
        "MÁRCIUS",
        "ÁPRILIS",
        "MÁJUS",
        "JÚNIUS",
        "JÚLIUS",
        "AUGUSZTUS",
        "SZEPTEMBER",
        "OKTÓBER",
        "NOVEMBER",
        "DECEMBER",
    ]
    f = open(kim, "w", encoding="utf8")
    f.write("# Honvédelmi adatok 2021-re az autentikusból\n")
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
        Ezek a 2021_AUTENTIKUS.xlsx táblázat fejlécsorának összetevői.
        Továbbá! Közhírré tétetik!
        Az excel fileban a dátum mezőt tessék rendesen beállítani.
        """
        print("Munkalap neve: ", sh.title)
        for c1, c2, c3, c4, c5, c6, c7, c8, c9 in cells:
            if c1.value and c2.value:  # dátum tánckar kitöltve
                if isinstance(c1.value, datetime.date):
                    print("Ejsze, egyszer aztán igen léfutottam he.")
                    d = c1.value.strftime("%Y-%m-%d")  # d = datum
                elif c1.value not in honapok:
                    d = c1.value[0:6].replace(" ", "")
                    d = d[0:5].replace(".", "-")
                    logging.info("Ezek az érdekes dátumok: {}".format(d))
                    # d = c1.value[0:6].replace('.', '-')
                    d = "2021-" + d.strip()
                    # ha string => .->- és marad az első 10 karakter
                    logging.debug("Datum mező:{} , típusa:{} ".format(d, type(d)))
                    logging.debug(
                        """Változók értéke:
                                            Dátum: {}
                                            Tánc: {}
                                            Zkr: {}
                                            FFikar: {}
                                            Egyeztet: {}
                                            Kontakt: {}
                                            Státusz: {}
                                            Külszáll: {}
                                            Megjegy: {}""".format(
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
                        c2db[1] = c2db[1].strip()
                        musor = sqlescapy.sqlescape(c2db[1])
                        # musor = re.escape(c2db[1])
                    except IndexError:
                        musor = "Nincs megadva műsor."
                        logging.debug("IndexError - Nincs megadva műsor.")
                    if idopont:
                        logging.debug("Van időpont!")
                        # kezdes = c1.value.replace(hour=int(idopont.group()[:2]), minute=00)
                        kezdes = idopont.group()
                        hely = c2db[0].replace(kezdes, "", 1)
                        hely = hely.strip()
                        # ely elejéről levesszük a spacet
                        logging.debug("Helyszín eredménye: " + hely)
                    else:
                        kezdes = "Nincs megadva kezdés."
                        hely = c2db[0]
                        logging.debug("Kezdés eredménye: " + hely)
                        # kezdes = c1.value.replace(hour=00, minute=00)
                    if c8.value:
                        kontakt = c8.value
                    else:
                        kontakt = ""
                    if c9.value:
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
                    sql += musor.strip()  # Musor
                    sql += '","'
                    sql += kontakt.strip()  # Kontakt
                    sql += '","'
                    sql += megjegyzes.strip()  # Megjegyzés
                    sql += '","'
                    sql += str(0)  # helykod
                    sql += '");\n'
                    logging.debug(sql)
                    f.write(sql)
                    i = i + 1  # feldolgozott sorok száma.
        print("{} sor feldolgozva.".format(i))
    f.close()
    print("Fájl kiírása befejezve.")
    veg = time.time() - kezd
    print("{:.5f}. sec alatt lefutott".format(veg))


if __name__ == "__main__":
    main()
