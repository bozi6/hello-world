#!/usr/bin/python3

import openpyxl
import logging as log
import re
import datetime

log.basicConfig(level=log.INFO, format=' %(asctime)s  - %(message)s')
log.disable(log.DEBUG) # Akkor kell ha már nem akarunk Debuggolni. :-)
# log.disable(log.INFO)
log.info('Program elkezdődött.')

bem = "../xlsxs/2018. Autentikus.xlsx"
kim = "tanckari_json.txt"

f = open(kim, 'w')
log.info(kim+' megnyitva')
f.write('[\n')
book = openpyxl.load_workbook(bem, read_only=True)
lap = book.active
i = 1
for lap in book.worksheets:  # Végigmegyünk a munkafüzet lapjain
    cells = lap['A3':'I204']  # K210 a vége
    log.info(lap.title)
    """
    c1 -datum
    c2 - tanckar
    c3 - zenekar
    c4 - férfikar
    c5 - egy alatt
    c6 - kontakt
    c7 - status
    c8 - külsős száll
    c9 - megjegyzes
    """
    for c1, c2, c3, c4, c5, c6, c7, c8, c9 in cells:
        try:
            if c1.value is not None and c2.value is not None:
                f.write('\t{ _id:' + str(i))  # Elkezdjük a fileba írást
                if isinstance(c1.value, datetime.date):  # megnézzük hogy datetime-e
                    d = c1.value
                    f.write(', datum: "' + d.strftime("%Y-%m-%d") + '"')  # levágjuk az órapercet beírjuk
                else:
                    f.write(', datum: "' + c1.value[0:10].replace('.', '-') + '"')
                    # ha string => pont->- a pontot és marad az első 10 karaktert
                c2db = c2.value.split('/')
                log.debug(c2db)
                idopont = re.match('[0-9][0-9].?[0-9][0-9]', c2db[0])
                if idopont:
                    kezdes = idopont.group()
                    f.write(', kezd: "'+kezdes+'"')
                else:
                    hely = c2db[0].replace(kezdes, '', 1)
                    f.write(', hely: "'+hely.strip()+'"')
                f.write(', tanckari: "'+c2.value+'"')
                try:
                    f.write(', musor: "'+c2db[1].strip()+'"')
                except IndexError:
                    log.debug('IndexError - Nincs megadva műsor.')
                if c6.value:
                    f.write(', kontakt: "' + c6.value + '"')
                if c7.value:
                    f.write(', status: "' + c7.value + '"')
                if c8.value:
                    f.write(', kulsos: "' + c8.value + '"')
                if c9.value:
                    f.write(', megjegyzes: "' + c9.value + '"')
                f.write(' },\n')
                i = i+1
            else:
                log.debug("{}: - c1: {} typ:{} -c2: {} - typ:{}".format\
                        (c1.row, c1.value, type(c1.value), c2.value, type(c2.value)))
        except TypeError as e:
            log.info('Kezeletlen típushiba: '+str(e))
            log.info(cells)
f.write(']\n')
f.close()
