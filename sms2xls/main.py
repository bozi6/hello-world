import logging  # Loggoláshoz modul
import re  # Reguláris kifejezésekhez modul
from xml.dom import minidom  # xml fájl olvasásához modul

from forex_python.converter import CurrencyRates  # valutaárfolyam lekérdezőke modul
from openpyxl import Workbook  # Excel táblázat kezeléshez modul
from openpyxl.styles import NamedStyle, Font, PatternFill  # Stílus importálása modul
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule

FORMAT = '%(asctime)-2s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)  # loggolás beálltása INFO-ra(csak a lényeg)

# xml fájl betöltése
mydoc = minidom.parse('sms_full.xml')

c = CurrencyRates()  # Aktuális árfolyam lekérdezése
arfolyamok = c.get_rates('HUF')  # átszámítás forint vs. valutákra

# Munkalap stílusának beálítása forintra
still = NamedStyle(name="Pénzecske")
still.number_format = '#,##0 "HUF";-#,##0 "HUF"'
diff_style = DifferentialStyle(fill=PatternFill(bgColor='C6EFCE', fgColor='006100'))
rule = Rule(type="expression", dxf=diff_style)
rule.formula = ["$B2>0"]


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


def ujlap_letrehozasa(lap_elnevezese):
    """ Új munkalap létrehozása a munkafüzetben. """
    logging.debug('ujlap funkció meghívva')
    ws['A1'] = 'Dátum:'  # A cellákba írandó alapszövegek
    ws['A2'] = 'Nyitó:'
    ws['B1'] = 'Pénzmozgás:'
    ws['C1'] = 'Valuta:'
    ws['D1'] = 'Egyenleg:'
    ws['E1'] = 'Kitől:'
    ws['F1'] = 'Mit:'
    ws.title = lap_elnevezese
    ws['A1'].font = Font(bold=True)
    ws['A2'].font = Font(bold=True)
    ws['B1'].font = Font(bold=True)
    ws['C1'].font = Font(bold=True)
    ws['D1'].font = Font(bold=True)
    ws['E1'].font = Font(bold=True)
    ws['F1'].font = Font(bold=True)
    ws['B2'].font = Font(italic=True, bold=True)
    ws.column_dimensions['A'].width = 25  # Az oszlopok alapvető szélességének megadása
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 57
    ws.column_dimensions['F'].width = 61
    ws.cell(row=2, column=2, value='=D3-B3').style = still


# Munkalap létrehozása a memóriában
wb = Workbook()
wb.add_named_style(still)
ws = wb.active

items = mydoc.getElementsByTagName('sms')  # smsek beolvasása az items-be
lapnev = items[0].attributes['readable_date'].value
lapnev = lapnev[:4]
ujlap_letrehozasa(lapnev)
sor = 3  # a táblázat írni kívánt első sora
i = 1  # belső változó

for elem in items:  # SMS-ek beolvasása
    if 'SIKERTELEN' in elem.attributes['body'].value:  # Ha a SIKERTELEN üzenetet kaptuk, akkor nem kell törődni vele
        continue  # Itt ugrunk a következő üzenetre
    tel = elem.attributes['address'].value  # telefonszám kinyerése az üzenetből, később lehet szűrni.
    rd = elem.attributes['readable_date'].value  # Dátum hozzáadása az rd változóhoz
    bd = elem.attributes['body'].value  # Az üzenet szövege
    cn = elem.attributes['contact_name'].value  # Az üzenetküldő neve
    penz_pattern = r'(-|\+)[0-9]+(,?|\.?)[0-9]+\s?,?-?[A-Z][A-Z][A-Z]'
    egyenleg_pattern = r'(Egyenleg:\s)(\+?[0-9]+.[0-9]+\.?[0-9]+)'
    # előjel - vagy +, utána 0 vagy több szám, aztán 0 vagy egy karakter,
    # 0 vagy több szám, 0 vagy 1 szóköz 0 vagy 1 , 0 vagy 1 - és három karakter a pénznem azonosításhoz.
    # x = re.findall(pattern, bd)
    aktev = rd[:4]  # Az aktális évszám kinyerése a dátumból.
    if aktev != ws.title:  # Ha ez nem egyezik a lap nevével akkor új lapot nyitunk
        ws.conditional_formatting.add("B2:B{}".format(ws.max_row), rule)
        ws = wb.create_sheet(aktev)
        wb.active
        ujlap_letrehozasa(aktev)
        sor = 3
    try:
        x = re.search(penz_pattern, bd).group()  # megkeressük a pénzeket az üzenetből
        egybd = bd.replace("Egy:", "Egyenleg: ")
        ketbd = egybd.replace(",-HUF;", " HUF;")
        egyenleg = re.search(egyenleg_pattern, ketbd).group(2)
        logging.debug('Egyenleg értéke: {} - Üzi: {}'.format(egyenleg, bd))
        x = x.replace(".", "")  # kivesszük a pontot (ezres elválasztó) az összegek közül
        x = x.replace(",-HUF", " HUF")  # Ha az üzenetben ,-HUF van azt átalakítjuk HUf-ra
        if x.find("HUF") > -1:  # Ha benne van az összegben a HUF => forint alapú a dolog
            x = x.replace(" HUF", "")  # Kivesszük a HUF szöveget az excel pénznem felismerése miatt.
            ws.cell(row=sor, column=2, value=float(x)).style = still  # beírjuk az aktuális sorba a második oszlopba
        else:  # ha nem HUF-ban van megadva a pénz
            ws.cell(row=sor, column=3, value=x)  # Beírjuk a harmadik oszlopba az összeget
            forintban = penzvalto(x)  # Átváltjuk az összeget forintra
            ws.cell(row=sor, column=2, value=forintban).style = still  # Ezt beírjuk  a második oszlopba
            logging.debug('Valuta értéke:', ws.cell(row=sor, column=2).value)
        egyenleg = egyenleg.replace(".", "")
        ws.cell(row=sor, column=1, value=rd)  # A dátumot beírjuk az első oszlopba
        bd = bd.replace("...", "")  # Az üzenet elejéről a pontokat kivesszük még.
        bd = bd.split(';')  # Üzenet feldarabolása a ; alapján
        logging.debug(bd)
        # ws.cell(row=sor, column=5, value=bd)  # Az üzenetet beírjuk az ötödik oszlopba, ellenőrzés czéljából
        ws.cell(row=sor, column=4, value=float(egyenleg)).style = still  # Az egyenleget beírjuk a negyedik oszlopba
        ws.cell(row=sor, column=5, value=bd[1])  # Az üzenetet beírjuk az ötödik oszlopba, ellenőrzés czéljából
        ws.cell(row=sor, column=6, value=bd[0])  # Az üzenetet beírjuk az ötödik oszlopba, ellenőrzés czéljából
        logging.debug("{}; Dátum: {} - Érték: {} - Üzi: {}".format(i, rd, x, bd))  # ha DEBUG-ra van állítva a loggolás
        i += 1  # sorszám növelése
    except AttributeError:
        logging.debug("{}; - Nem átutalásos sms - {}".format(i, bd))
        continue
    sor += 1
    # Az összegeket az oszlop végén öszeadjuk és beírjuk az eredményt. és hozzáadjuk a stílust
    ws.cell(row=ws.max_row + 1, column=2, value="=SUM(B2:B{})".format(ws.max_row)).style = still
    ws.cell(row=ws.max_row, column=2).font = Font(bold=True, italic=True)  # A betűtípust vastaggá tesszük az eredményen
    logging.debug('Munkalap max sorszáma: {}'.format(ws.max_row))
# wb.save('../../../../OneDrive/Dokumentumok/balance.xlsx')  # táblázat kírása.
print('Elkészült munkalapok:')
for sheet in wb:
    print('{}'.format(sheet.title), end='-')
