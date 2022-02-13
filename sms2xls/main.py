import csv  # árfolyamok csv file kezeléséhez
import logging  # Loggoláshoz modul
import os  # dátum kinyerése
import re  # Reguláris kifejezésekhez modul
import shutil  # Fájl másoláshoz
from datetime import datetime, timedelta  # timestampból emberi dátum
from xml.dom import minidom  # xml fájl olvasásához modul
from colorama import Fore
from forex_python.converter import CurrencyRates  # valutaárfolyam lekérdezőke modul
from openpyxl import Workbook  # Excel táblázat kezeléshez modul
from openpyxl.formatting.rule import Rule
from openpyxl.styles import NamedStyle, Font, PatternFill  # Stílus importálása modul
from openpyxl.styles.differential import DifferentialStyle

# Loggolás alapbeállításai
FORMAT = '%(levelname)s: %(asctime)-2s prgsor: %(lineno)d %(message)s'  # Loggolás formátumának beállításra
logging.basicConfig(format=FORMAT, level=logging.INFO)  # loggolás beálltása INFO-ra(csak a lényeg)

# Alapértelmezett változók
olvasando_fajl = "sms_full.xml"
logging.info('A beolvasando file: ' + olvasando_fajl)
kiirando_fajl = "balance.xlsx"
logging.info('A kiírandó file: ' + kiirando_fajl)
arfolyam_file = "arfolyamok.csv"
logging.info('A használt árfolyamok file: ' + arfolyam_file)
arfolyam = {}
egyenleg2 = ""

# xml fájl betöltése
mydoc = minidom.parse(olvasando_fajl)

# Munkalap stílusának beálítása forintra
still = NamedStyle(name="Pénzecske")  # Ilyen nevű stílus hozzáadása
still.number_format = '#,##0 "HUF";-#,##0 "HUF"'  # A számformátum beállítása forintra
diff_style = DifferentialStyle(fill=PatternFill(bgColor='C6EFCE', fgColor='006100'))  # A feltételes formázás beállítása
rule = Rule(type="expression", dxf=diff_style)  # Feltételes kifejezés megadása
rule.formula = ["$B2>0"]  # Formula a feltételes formázáshoz

# Árfolyam file meglétének ellenőrzése és frissítése ha két óránál régebbi
fileido = datetime.fromtimestamp(os.stat('./arfolyamok.csv').st_ctime)  # a meglévő file idejének lekérdezése
now = datetime.now()
max_delay = timedelta(hours=2)
try:
    if now - fileido > max_delay:
        shutil.copyfile('arfolyamok.csv', 'arfolyamok.old')
        logging.debug("Régi a fájl ezért lekérdezem az árfolyamokat: {} ".format(fileido))
        c = CurrencyRates()  # Aktuális árfolyam lekérdezése
        arfolyam = c.get_rates('HUF')  # átszámítás forint vs. valutákra
        w = csv.writer(open("arfolyamok.csv", "w"))
        for key, value in arfolyam.items():
            w.writerow([key, value])
    else:
        logging.debug('Jó a file ideje, ezért a meglévőt használom.')
        with open('arfolyamok.csv', mode='r') as infile:
            reader = csv.reader(infile)
            arfolyam = {str(rows[0]): float(rows[1]) for rows in reader}
except IOError:
    print("nincseh meg a file")
    logging.debug('Nem található a file.')


def penz_valto(mit):
    """ Árfolyam váltó függvény
    a bejövő mit hez 123,45 GBP
    kiszámolja, hogy az mennyi forintban """
    valuta = mit[-3:]  # A bejövő valuta megnevezésének eltávolítása
    if valuta in arfolyam:
        logging.debug('Váltás 1 HUF = {} - {}-ben/ban'.format(arfolyam[valuta], valuta))
        valtoertek = arfolyam[valuta]
        mit = mit[:-4]
        mit = mit.replace(",", ".")
        return float(mit) / valtoertek
    else:
        logging.info('Nem találtam ilyen valutát a fileban!', mit)
        return False


def ujlap_letrehozasa(lap_elnevezese):
    """ Új munkalap létrehozása a munkafüzetben. """
    logging.debug('új lap funkció meghívva')
    """Alapértékek megadása"""
    szotar = {'A1': 'Dátum', 'A2': 'Nyitó összeg', 'B1': 'Pénzmozgás',
              'C1': 'Valuta', 'D1': 'LU egyenleg', 'E1': 'Üzenet',
              'F1': 'Egyenleg', 'G1': 'Ez hibádzik'}
    for kulcs, ertek in szotar.items():
        ws[kulcs] = ertek
        ws[kulcs].font = Font(bold=True)
    ws.title = lap_elnevezese  # Az új lap elnevezése
    ws['B2'].font = Font(italic=True, bold=True)
    # Az egyes oszlopok szélessége
    szelessegek = {'A': 20, 'B': 15, 'C': 15, 'D': 15, 'E': 160, 'F': 13, 'G': 13}
    for kulcs, ertek in szelessegek.items():
        ws.column_dimensions[kulcs].width = ertek
    ws.cell(row=2, column=2, value='=D3-B3').style = still
    # A B2 cellába beírjuk a kezdőértéket első sms egyenlegéből kivonva az első levonást = nyitó egyenleg
    ws.sheet_view.zoomScale = 125  # A nézet kinagyítása az aktuális oldalon


def egyenleg_kerdez(melyik):
    egyenleg_pattern = r'(Egyenleg:\s)(\+?[0-9]+.[0-9]+\.?[0-9]+)'
    try:
        vissza = re.search(egyenleg_pattern, melyik).group(2)
        return vissza
    except AttributeError:
        return False


# Munkalap létrehozása a memóriában
wb = Workbook()
wb.add_named_style(still)
ws = wb.active

items = mydoc.getElementsByTagName('sms')  # smsek beolvasása az items-be

lapnev = items[0].attributes['readable_date'].value  # Az első sms dátumának kinyerése
lapnev = lapnev[:4]  # Csak az évszám kivágása

ujlap_letrehozasa(lapnev)  # beküldjük az új laphoz
sor = 3  # a táblázat írni kívánt első sora
i = 1  # belső változó

for elem in items:  # SMS-ek beolvasása
    # if 'SIKERTELEN' in elem.attributes['body'].value:  # Ha a SIKERTELEN üzenetet kaptuk, akkor nem törődünk vele
    #     continue
    tel = elem.attributes['address'].value  # telefonszám kinyerése az üzenetből, később lehet szűrni.
    rd = elem.attributes['readable_date'].value  # Dátum hozzáadása az rd változóhoz
    bd = elem.attributes['body'].value  # Az üzenet szövege
    cn = elem.attributes['contact_name'].value  # Az üzenetküldő neve
    # penz_pattern = r'(-|\+)[0-9]+(,?|\.?)[0-9]+\s?,?-?[A-Z][A-Z][A-Z]'
    penz_pattern = r'(-|\+|\ )\d{1,}(\.|,|\s)(\d{1,3}|,)*.(\d{1,3}|\w{1,3});'
    # előjel - vagy +, utána 0 vagy több szám, aztán 0 vagy egy karakter,
    # 0 vagy több szám, 0 vagy 1 szóköz 0 vagy 1 , 0 vagy 1 - és három karakter a pénznem azonosításhoz.
    # x = re.findall(pattern, bd)
    aktev = rd[:4]  # Az aktulis évszám kinyerése a dátumból.
    if aktev not in wb.sheetnames:  # Ha ez nem egyezik a lap nevével akkor új lapot nyitunk
        logging.debug('Új lapot kellett nyitnom.')
        ws.conditional_formatting.add("B2:B{}".format(ws.max_row), rule)
        # összeadjuk a bevételeket. Ezt még az aktuális és nem új lapon tesszük.
        ws.cell(row=ws.max_row + 1, column=1, value='Bevétel:')
        ws.cell(row=ws.max_row + 1, column=1, value='=SUMIF(B2:B{},">0")'.format(ws.max_row - 2)).style = still
        ws.cell(row=ws.max_row + 1, column=1, value='Kiadás:')
        ws.cell(row=ws.max_row + 1, column=1, value='=SUMIF(B2:B{},"<0")'.format(ws.max_row - 4)).style = still
        ws = wb.create_sheet()  # itt csinálunk új lapot
        wb.active  # itt pedig aktívvá tesszük.
        ujlap_letrehozasa(aktev)  # meghívjuk rá az alapbeállításokat.
        sor = 3
    try:
        osszeg = re.search(penz_pattern, bd).group()  # megkeressük a pénzeket az üzenetből
        egybd = re.sub(r"(;\sEgy:)|(;\sEgy\.:)", "; Egyenleg: ", bd)  # csak az sms végi egyenleg keresése
        egybd = " ".join(egybd.split())  # A két szóköz eltávolítása
        ketbd = egybd.replace(",-HUF;", " HUF;")  # A ",-HUF" átíráasa "HUF"-ra
        if not egyenleg_kerdez(ketbd):  # Hs nincs egyenleg az SMS végén akkor az előzőt használjuk
            egyenleg = egyenleg2
        else:
            egyenleg = egyenleg_kerdez(ketbd)
            egyenleg2 = egyenleg_kerdez(ketbd)
        osszeg = osszeg.replace(".", "")  # kivesszük a pontot (ezres elválasztó) az összegek közül
        osszeg = osszeg.replace(";", "")  # kivesszük a végén a ;-t (kellet az smsek miatt a regexphez)
        osszeg = osszeg.replace(",-HUF", " HUF")  # Ha az üzenetben ,-HUF van azt átalakítjuk HUf-ra
        if osszeg.find("HUF") > -1:  # Ha benne van az összegben a HUF => forint alapú a dolog
            osszeg = osszeg.replace(" HUF", "")  # Kivesszük a HUF szöveget az excel pénznem felismerése miatt.
            ws.cell(row=sor, column=2, value=float(osszeg)).style = still  # beírjuk az aktuális sorba a második
            # oszlopba
        else:  # ha nem HUF-ban van megadva a pénz
            ws.cell(row=sor, column=3, value=osszeg)  # Beírjuk a harmadik oszlopba az összeget
            forintban = penz_valto(osszeg)  # Átváltjuk az összeget forintra
            ws.cell(row=sor, column=2, value=forintban).style = still  # Ezt beírjuk a második oszlopba
            logging.debug('Valuta értéke: {} külföldi, {} HUF'.format(osszeg, forintban))
        egyenleg = egyenleg.replace(".", "")
        ws.cell(row=sor, column=1, value=rd)  # A dátumot beírjuk az első oszlopba
        bd = bd.replace("...", "")  # Az üzenet elejéről a pontokat kivesszük még.
        ws.cell(row=sor, column=4, value=float(egyenleg)).style = still  # Az egyenleget beírjuk a negyedik oszlopba
        ws.cell(row=sor, column=5, value=bd)  # Az üzenetet beírjuk az ötödik oszlopba, ellenőrzés czéljából
        ws.cell(row=sor, column=6, value="=SUM(D{},B{})".format(sor, sor + 1)).style = still
        # Nem mindegy, hogy a képletbe elválsztónak , vagy ; van itt a ; hibát dob az excelben.
        ws.cell(row=sor, column=7, value="=D{}-F{}".format(sor + 1, sor)).style = still
        # logging.debug("Sorszám:{}; Dátum: {} - Érték: {} - Üzi: {}".format(i, rd, x, bd))
        i += 1  # sorszám növelése
    except AttributeError:
        logging.debug("Sorszám:{}; - Nem átutalásos sms - {}".format(i, bd))
        continue
    sor += 1
    # Az összegeket az oszlop végén öszeadjuk és beírjuk az eredményt. és hozzáadjuk a stílust
    ws.cell(row=ws.max_row + 1, column=2, value="=SUM(B2:B{})".format(ws.max_row)).style = still  # stílus megadása
    ws.cell(row=ws.max_row, column=2).font = Font(bold=True, italic=True)  # A betűtípust vastaggá tesszük az eredményen
ws.conditional_formatting.add("B2:B{}".format(ws.max_row), rule)
# összeadjuk a bevételeket.
ws.cell(row=ws.max_row + 1, column=1, value='Bevétel:')
ws.cell(row=ws.max_row + 1, column=1, value='=SUMIF(B2:B{},">0")'.format(ws.max_row - 2)).style = still
ws.cell(row=ws.max_row + 1, column=1, value='Kiadás:')
ws.cell(row=ws.max_row + 1, column=1, value='=SUMIF(B2:B{},"<0")'.format(ws.max_row - 4)).style = still
wb.save(kiirando_fajl)  # táblázat elmentése
print('Elkészült munkalapok:')
for sheet in wb:
    print(Fore.GREEN + sheet.title + Fore.WHITE + ' kész!')
