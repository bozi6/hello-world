import logging  # Loggoláshoz modul
import re  # Reguláris kifejezésekhez modul
import sys  # Rendszerdolgokhoz modul
from xml.dom import minidom  # xml fájl olvasásához modul

from forex_python.converter import CurrencyRates  # valutaárfolyam lekérdezőke modul
from openpyxl import Workbook  # Excel táblázat kezeléshez modul
from openpyxl.styles import NamedStyle, Font  # Stílus importálása modul

logging.basicConfig(stream=sys.stderr, level=logging.INFO)  # loggolás beálltása INFO-ra(minimál)

# xml fájl betöltése
mydoc = minidom.parse('sms_full.xml')

c = CurrencyRates()  # Aktuális árfolyam lekérdezése
arfolyamok = c.get_rates('HUF')  # átszámítás forint vs. valutákra

# Munkalap stílusának beálítása forintra
still = NamedStyle(name="Pénzecske")
still.number_format = '#,##0 "HUF";-#,##0 "HUF"'


def penzvalto(mit, arfolyam=arfolyamok):
    """ Árfolyam váltó függvény
    a bejövő mit hez 123,45 GBP
    kiszámolja, hogy az mennyi forintban """
    valuta = mit[-3:]
    if valuta in arfolyam:
        logging.debug('Váltás 1 HUF = {} - {}-ben/ban'.format(arfolyam[valuta], valuta))
        valtoertek = arfolyam[valuta]
        mit = mit[:-4]
        mit = mit.replace(",", ".")
        return float(mit) / valtoertek
    else:
        return False


# új lapok alapbeállítása
def ujlap():
    ws['A1'] = 'Dátum:'  # A cellákba írandó alapszövegek
    ws['A2'] = 'Nyitó:'
    ws['B1'] = 'Pénzmozgás:'
    ws['C1'] = 'Valuta:'
    ws['D1'] = 'Üzenet:'
    ws['A1'].font = Font(bold=True)
    ws['A2'].font = Font(bold=True)
    ws['B1'].font = Font(bold=True)
    ws['C1'].font = Font(bold=True)
    ws['D1'].font = Font(bold=True)
    ws['B2'].font = Font(italic=True, bold=True)
    ws.column_dimensions['A'].width = 25  # Az oszlopok alapvető szélességének megadása
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 160


# Munkalap létrehozása a memóriában
wb = Workbook()
wb.add_named_style(still)
ws = wb.active
ws.title = '2012'  # A kezdő dátuma az ami a legrégebbi sms elvileg
ujlap()

items = mydoc.getElementsByTagName('sms')  # smsek beolvasása az items-be

sor = 3  # a táblázat írni kívánt első sora

i = 1  # belső változó
for elem in items:  # SMS-ek beolvasása
    if 'SIKERTELEN' in elem.attributes['body'].value:  # Ha a SIKERTELEN üzenetet kaptuk, akkor nem kell törődni vele
        continue  # Itt folytatjuk a ciklust
    tel = elem.attributes['address'].value  # telefonszám kinyerése az üzenetből, később lehet szűrni.
    rd = elem.attributes['readable_date'].value  # Dátum hozzáadása az rd változóhoz
    bd = elem.attributes['body'].value  # Az üzenet szövege
    # pattern = r'(-|\+)\d*.?\d*\s?,?-?...'
    pattern = r'(-|\+)[0-9]+(,?|\.?)[0-9]+\s?,?-?[A-Z][A-Z][A-Z]'
    # előjel - vagy +, utána 0 vagy több szám, aztán 0 vagy egy karakter,
    # 0 vagy több szám, 0 vagy 1 szóköz 0 vagy 1 , 0 vagy 1 - és három karakter.
    # x = re.findall(pattern, bd)
    aktev = rd[:4]  # Az aktális évszám kinyerése a dátumból.
    if aktev != ws.title:  # Ha ez nem egyezik a lap nevével akkor új lapot nyitunk
        ws = wb.create_sheet(aktev)
        wb.active
        ujlap()
        sor = 3
    try:
        x = re.search(pattern, bd).group()  # megkereessük a pénzeket az üzenetből
        x = x.replace(".", "")  # kvesszük a pontot az összegek közül
        x = x.replace(",-HUF", " HUF")  # Ha az üzenetben ,-HUF van azt átalakítjuk
        if x.find("HUF") > -1:  # Ha benne van az összegben a HUF => forint alapú a dolog
            x = x.replace(" HUF", "")  # Kivesszük a HUF szöveget
            ws.cell(row=sor, column=2, value=float(x)).style = still  # beírjuk az aktuális sorba a második oszlopba
        else:  # ha nem HUF-ban van megadva a pénz
            ws.cell(row=sor, column=3, value=x)  # Beírjuk a harmadik oszlopba az összeget
            forintban = penzvalto(x)  # Átváltjuk az összeget forintra
            ws.cell(row=sor, column=2, value=forintban).style = still  # Ezt beírjuk  a második oszlopba
            logging.debug(ws.cell(row=sor, column=2).value)
        ws.cell(row=sor, column=1, value=rd)  # A dátumot beírjuk az első oszlopba
        bd = bd.replace("...", "")  # Az üzenet elejéről a pontokat kivesszük még.
        ws.cell(row=sor, column=4, value=bd)  # Az üzenetet beírjuk a negyedik oszlopba, ellenőrzés czéljából
        logging.debug("{}; Dátum: {} - Érték: {} - Üzi: {}".format(i, rd, x, bd))  # ha DEBUG-ra van állítva a loggolás
        i += 1  # sorszám növelése
    except AttributeError:
        logging.debug("{}; Nem átutalásos sms: \t{}".format(i, bd))
        continue
    sor += 1
    ws.cell(row=ws.max_row + 1, column=2, value="=SUM(B2:B{})".format(ws.max_row)).style = still
    ws.cell(row=ws.max_row, column=2).font = Font(bold=True, italic=True)


    logging.debug(ws.max_row)

wb.save('balance.xlsx')  # táblázat kírása.
print('Elkészült munkalapok:')
for sheet in wb:
    print('{}'.format(sheet.title), end='-')
