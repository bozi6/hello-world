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

import funct.process as proc

__author__ = "Konta Boáz"
__author_email__ = "kontab6@gmail.com"
__copyright__ = "Konta Boáz 2023"
BemenetiFile = "z:/NYILVÁNOS/Szereplési terv/2023/2023_Autentikus és  munkarend/_______2023_Autentikus_.xlsx"
MasoltFile = "2023_Autentikus.xlsx"
KimenetFile = "../sql/2023_aut.sql"
tancnevezes = ["Tánckar", "tánckar", "TÁNCKAR (és Zenekar)"]
ferfikarnevek = ["FÉRFIKAR"]

KezdesiIdo = time.time()
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s  - %(message)s")
logging.disable(logging.DEBUG)  # Akkor kell ha már nem akarunk Debuggolni. :-)
# logging.disable(logging.INFO)
logging.info(f"Program elkezdődött. {KezdesiIdo}")


def testinpufile(filename):
    """
    Bemeneti fájl tesztelése
    :param filename: A bejövő csatolt mappa ellenőrzése
    :return: A készülő fájl neve

    """
    xlsdir = "../xlsxs/"
    MasolandoFile = xlsdir + "2023_Autentikus.xlsx"
    if os.path.exists(filename):
        shutil.copyfile(filename, MasolandoFile)
        cprint.info("File másolva a legújabbra.")
        return MasolandoFile
    else:
        cprint.warn(
            filename,
            " nevű fájl nem található.\n"
            "Lehet nincs csatlakoztatva a távoli hely?\n"
            "mindegy... használom a régit.",
        )
        return MasolandoFile


def main():
    """
    Főprogram a bemeneti fájlból létrehozza az SQL filet.
    """
    BemenetFile = testinpufile(BemenetiFile)
    SqlSor = "\nINSERT INTO aut (sorsz,datum,ceg,kezd,hely,musor,kontakt,megjegyzes,helykod,szallitas,tev) VALUES \n"

    kiiroFajl = open(KimenetFile, "w", encoding="utf8")
    sqlalap = """-- Honvédelmi adatok 2023-ra az autentikusból.
    -- Készítette: Konta Boáz (kontab6@gmail.com)
    -- Select current database
    USE honved2;
    -- Increase max allowed packets to 500MB from 1MB
    SET GLOBAL max_allowed_packet=524288000;
    DELETE FROM aut WHERE datum >= '2023-01-01';
    """
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
            # egyadat = funkciok.Bemeno(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, '')
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
                logging.debug("Kezdési időpont kialakult: " + str(procad.kezdes))
                sqlValues.append(proc.sqlrak(procad))
                logging.debug(SqlSor)
                i = i + 1  # feldolgozott sorok száma.
            elif (c1.value and c5.value) and (
                c5.value not in ferfikarnevek
            ):  # dátum férfikar kitöltve.
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
                logging.debug(SqlSor)
                i = i + 1  # feldolgozott sorok száma.

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


if __name__ == "__main__":
    main()
