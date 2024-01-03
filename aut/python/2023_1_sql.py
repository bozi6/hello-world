#!/usr/bin/env python3
"""
Az autentikus Excel tábla átalakítása mySQL fájllá, ami nekem jó.
Készült 2023.12.04.
"""
import logging
import os.path
import shutil
import time

import openpyxl
from cprint import *

import aut.python.funct.aut_configfile as conf
import aut.python.funct.process as proc

__author__ = "Konta Boáz"
__author_email__ = "kontab6@gmail.com"
__copyright__ = "Konta Boáz 2023"
BemenetiFile = "z:/NYILVÁNOS/Szereplési terv/2023/2023_Autentikus és  munkarend/_______2023_Autentikus_.xlsx"
MasoltFile = "2023_Autentikus.xlsx"
KimenetFile = "../sql/2023_aut.sql"
tancnevezes = conf.TANCNEV
ferfikarnevek = conf.FERFIKARNEVEK

KezdesiIdo = time.time()
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s  - %(message)s")
# logging.disable(logging.DEBUG)  # Akkor kell ha már nem akarunk Debuggolni. :-)
# logging.disable(logging.INFO)
# logging.info(f"Program elkezdődött. {KezdesiIdo}")


def tesztinputfile(filename):
    """
    Bemeneti fájl tesztelése

    :param filename: A bejövő csatolt mappa ellenőrzése
    :return: A készülő fájl neve

    """
    xlsdir = "../xlsxs/"
    masolando_file = xlsdir + "2023_Autentikus.xlsx"
    if os.path.exists(filename):
        shutil.copyfile(filename, masolando_file)
        cprint.info("File másolva a legújabbra.")
        return masolando_file
    else:
        cprint.warn(
            filename,
            " nevű fájl nem található.\n"
            "Lehet nincs csatlakoztatva a távoli hely?\n"
            "mindegy... használom a régit.",
        )
        return masolando_file


if __name__ == "__main__":
    """

    Főprogram a bemeneti fájlból létrehozza az SQL filet.

    """
    BemenetFile = tesztinputfile(BemenetiFile)
    SqlSor = "\nINSERT INTO aut (sorsz,datum,ceg,kezd,hely,musor,kontakt,megjegyzes,helykod,szallitas,tev) VALUES \n"

    kiiroFajl = open(KimenetFile, "w", encoding="utf8")
    sqlalap = conf.SQLDEFAULT
    kiiroFajl.write(sqlalap)
    kiiroFajl.write(SqlSor)
    cprint.info("Bemeneti fájl: ", BemenetFile)
    cprint.info("Kimenetei fájl: ", KimenetFile)
    sqlValues = []
    WorkBook = openpyxl.load_workbook(filename=BemenetFile, read_only=True)
    # read_only elvileg gyorsabb és amúgy sem akarunk írni bele.
    for sh in WorkBook.worksheets:  # Végigmegyünk a munkafüzet lapjain
        cells = sh["A2":"J210"]  # J210 a vége
        i = 0
        cprint.info("Munkalap neve: ", sh.title)
        for c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 in cells:
            SqlSor = "( NULL,"
            if (c1.value and c3.value) and (
                c3.value not in tancnevezes
            ):  # dátum tánckar kitöltve.
                procad = proc.Egysor(
                    c1.value,
                    c2.value,
                    c3.value,
                    c4.value,
                    c5.value,
                    c6.value,
                    c7.value,
                    c8.value,
                    c9.value,
                    c10.value,
                )
                datum = procad.datum
                sqlValues.append(proc.sqlrak(procad))
                i = i + 1  # feldolgozott sorok száma.
            elif (c1.value and c5.value) and (
                c5.value not in ferfikarnevek
            ):  # dátum férfikar kitöltve.
                print(
                    f"Férfikar:{i};1- {c1.value}, 2- {c2.value}, 3- {c3.value}, 4- {c4.value}, 5- {c5.value}, 6- {c6.value} 7- {c7.value}, 8- {c8.value}, 9- {c9.value}, 10- {c10.value}\n"
                )
                procadf = proc.Egysor(
                    c1.value,
                    c2.value,
                    c3.value,
                    c4.value,
                    c5.value,
                    c6.value,
                    c7.value,
                    c8.value,
                    c9.value,
                    c10.value,
                )
                datum = procadf.datum
                logging.debug("Kezdési időpont kialakult: " + str(procadf.kezdes))
                sqlValues.append(proc.sqlrak(procadf))
                i = i + 1  # feldolgozott sorok száma.
                logging.debug(proc.sqlrak(procadf))

        cprint.info(i, "sor feldolgozva.")
    utolsoElem = sqlValues[-1]
    sqlValues.pop()
    utolsoElem = utolsoElem[:-2]
    utolsoElem += ";"
    sqlValues.append(utolsoElem)
    kiiroFajl.writelines([str(i) for i in sqlValues])
    kiiroFajl.close()
    cprint.ok("Fájl kiírása befejezve.")
    VegeIdo = time.time() - KezdesiIdo
    cprint.info(VegeIdo, ". sec alatt lefutott.")
