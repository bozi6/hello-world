#!/usr/bin/env python3
import os.path
import re
import datetime
import shutil

import openpyxl
import sqlescapy
import logging
import time
import aut.python.funct.funkciok as funkciok

KezdesiIdo = time.time()

logging.basicConfig(level=logging.INFO, format=' %(asctime)s  - %(message)s')
# logging.disable(logging.DEBUG)  # Akkor kell ha már nem akarunk Debuggolni. :-)
# logging.disable(logging.INFO)
# logging.info('Program elkezdődött.')

# BemenetFile = "../xlsxs/2023_Autentikus.xlsx"
MasoltFile = "../xlsxs/2023_Autentikus.xlsx"
TestBemenetiFile = "z:/NYILVÁNOS/Szereplési terv/2023/2023_Autentikus és  munkarend/_______2023_Autentikus_.xlsx"
if os.path.exists(TestBemenetiFile):
    shutil.copyfile(TestBemenetiFile, MasoltFile)
    print("File másolva")
    BemenetFile = MasoltFile
else:
    print(TestBemenetiFile, " nem található.")

KimenetFile = "../sql/2023_aut.sql"
SqlSor = '\nINSERT INTO aut (sorsz,datum,ceg,kezd,hely,musor,kontakt,megjegyzes,helykod,szallitas,tev) VALUES \n'
ujSqlSor = SqlSor

kiiroFajl = open(KimenetFile, 'w', encoding='utf8')
kiiroFajl.write('# Honvédelmi adatok 2023-ra az autentikusból\n')
kiiroFajl.write('# Készítette: Konta Boáz (kontab6@gmail.com).\n')
kiiroFajl.write('USE honved2;\n')  # select current database
kiiroFajl.write("SET GLOBAL max_allowed_packet=524288000;\n")  # increase max allowed packets to 500MB from 1MB
kiiroFajl.write("DELETE FROM aut WHERE datum >= '2023-01-01';")  # delete previos records from actual date.
kiiroFajl.write(SqlSor)
print('Bemeneti fájl: ' + BemenetFile)
print('Kimenetei fájl: ' + KimenetFile)
sqlValues = []
WorkBook = openpyxl.load_workbook(filename=BemenetFile, read_only=True)
# read_only elvileg gyorsabb és amúgy sem akarunk írni bele.
for sh in WorkBook.worksheets:  # Végigmegyünk a munkafüzet lapjain
    cells = sh['A2':'J210']  # I210 a vége
    i = 0
    ''' Az értékek a következők:
    c1  - Dátum ( óraperc nélkül )
    c2  - Napok???
    c3  - Tánckar
    c4  - Zenekar önálló
    c5  - Férfikar
    c6  - Közreműködők egyeztetés alatt
    c7  - Kontakt
    c8  - Státusz
    c9  - Külsős szállítás
    c10  - megjegyzés
    Ezek a 2022_AUTENTIKUS.xlsx táblázat fejlécsorának összetevői.
    Továbbá! Közhírré tétetik!
    Az excel fileban a dátum mezőt tessék rendesen beállítani.
    '''
    print("Munkalap neve: ", sh.title)
    for c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 in cells:
        egyadat = funkciok.Bemeno(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, '')
        if (c1.value and c3.value) and (c3.value != 'Tánckar'):  # dátum tánckar kitöltve
            result = re.match(r'^\d+.\d+.\d+', str(c1.value))
            if result:
                if isinstance(c1.value, datetime.date):
                    egyadat.datum = c1.value
                    d = c1.value.strftime('%Y-%m-%d')  # d = datum
                elif c1.value not in egyadat.honapok:
                    d = c1.value[0:6].replace(' ', '')
                    d = d[0:5].replace('.', '-')
                    logging.info('Ezek az érdekes dátumok: {}'.format(d))
                    # d = c1.value[0:6].replace('.', '-')
                    d = '2023-' + d.strip()
                    # ha string => .->- és marad az első 10 karakter
                    logging.debug('Datum mező:{} , típusa:{} '.format(d, type(d)))
                    logging.info('''Változók értéke:
                                            Dátum: {}
                                            Napok: {}
                                            Tánc: {}
                                            Zkr: {}
                                            FFikar: {}
                                            Egyeztet: {}
                                            Kontakt: {}
                                            Státusz: {}
                                            Külszáll: {}
                                            Megjegy: {}'''
                                 .format(c1.value, c2.value, c3.value, c4.value, c5.value,
                                         c6.value, c7.value, c8.value, c9.value, c10.value))
                SqlSor = "( NULL,"
                c2db = c3.value.split('/')  # A 0 az időpont/helyszín, az 1 pedig a műsor.
                idopont = re.match("[0-9][0-9].?[0-9][0-9]", c2db[0])
                try:
                    c2db[1] = c2db[1].strip()
                    musor = sqlescapy.sqlescape(c2db[1])
                    musor = " ".join(musor.split())
                    # musor = re.escape(c2db[1])
                except IndexError:
                    musor = 'Nincs megadva műsor.'
                    logging.debug('IndexError - Nincs megadva műsor.')
                if idopont:
                    logging.debug('Van időpont!')
                    # kezdes = c1.value.replace(hour=int(idopont.group()[:2]), minute=00)
                    kezdes = idopont.group()
                    hely = c2db[0].replace(kezdes, '', 1)
                    hely = " ".join(hely.split())
                    egyadat.helykod = hely

                    # hely elejéről levesszük a spacet
                    # print(hely)
                    logging.debug('Helyszín eredménye: ' + hely)
                else:
                    kezdes = 'Nincs megadva kezdés.'
                    hely = c2db[0]
                    logging.debug('Kezdés eredménye: ' + hely)
                    # kezdes = c1.value.replace(hour=00, minute=00)
                egyadat.kont = c7.value
                kontakt = egyadat.kont
                egyadat.megjegy = c10.value
                megjegyzes = egyadat.megjegy
                egyadat.kulsz = c9.value
                kulsoszallitas = egyadat.kulsz
                egyadat.tev = 'előadás'
                tevekenyseg = egyadat.tev

                datum = d
                logging.debug('Kezdési időpont kialakult: ' + str(kezdes))
                SqlSor += '"'
                SqlSor += str(datum)  # Dátum
                SqlSor += '",'
                SqlSor += '"24","'  # Cég
                SqlSor += kezdes  # Kezdes
                SqlSor += '","'
                SqlSor += hely.strip()  # Hely
                SqlSor += '","'
                SqlSor += musor.strip()  # Musor
                SqlSor += '","'
                SqlSor += kontakt.strip()  # Kontakt
                SqlSor += '","'
                SqlSor += megjegyzes  # Megjegyzés
                SqlSor += '","'
                SqlSor += str(0)  # helykod
                SqlSor += '","'
                SqlSor += kulsoszallitas  # Külső szállítás
                SqlSor += '","'
                SqlSor += tevekenyseg
                SqlSor += '"),\n'
                sqlValues.append(SqlSor)
                logging.debug(SqlSor)
                i = i + 1  # feldolgozott sorok száma.

    print('{} sor feldolgozva.'.format(i))
utolsoElem = sqlValues[-1]
sqlValues.pop()
utolsoElem = utolsoElem[:-2]
utolsoElem += ";"
sqlValues.append(utolsoElem)
kiiroFajl.writelines([str(i) for i in sqlValues])
kiiroFajl.close()
print('Fájl kiírása befejezve.')
VegeIdo = time.time() - KezdesiIdo
print('{:.5f}. sec alatt lefutott'.format(VegeIdo))