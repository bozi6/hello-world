import csv  # árfolyamok csv file kezeléséhez
import logging  # Loggoláshoz modul
import os  # dátum kinyerése
import os.path  # fájlétezés vizsgálatra
import re  # Reguláris kifejezésekhez modul
import shutil  # Fájl másoláshoz
from datetime import datetime, timedelta  # timestampból emberi dátum
from xml.dom import minidom  # xml fájl olvasásához modul

# from forex_python.converter import CurrencyRates  # valutaárfolyam lekérdezőke modul


def file_checker(filename):
    if os.path.exists(filename):
        fileido = datetime.fromtimestamp(
            os.path.getmtime(filename)
        )  # a meglévő file idejének lekérdezése
        now = datetime.now()
        max_delay = timedelta(hours=2)
        if now - fileido > max_delay:
            shutil.copyfile(filename, "{}_{}.csv".format(filename, fileido))
            return False
        else:
            return True
    else:
        return False


class CurrencyRates:
    pass


def arfolyam_feltoltes():
    if file_checker("arfolyamok.csv"):
        with open("arfolyamok.csv", mode="r") as infile:
            reader = csv.reader(infile)
            arfolyam_dict_file = {str(rows[0]): float(rows[1]) for rows in reader}
    else:
        c = CurrencyRates()
        arfolyam_dict_file = c.get_rates("HUF")
        w = csv.writer((open("arfolyamok.csv", "w")))
        for key, value in arfolyam_dict_file.items():
            w.writerow([key, value])
    return arfolyam_dict_file


def penz_valto(mit):
    """Árfolyam váltó függvény
    a bejövő mit hez 123,45 GBP
    kiszámolja, hogy az mennyi forintban"""
    valuta = mit[-3:]  # A bejövő valuta megnevezésének eltávolítása
    if valuta in arfolyam:
        valtoertek = arfolyam[valuta]
        mit = mit[:-4]
        mit = mit.replace(",", ".")
        return float(mit) / valtoertek
    else:
        print("Nem találtam ilyen valutát a fileban! ", mit)
        return False


def egyenleg_kerdez(melyik):
    egyenleg_pattern = r"(Egyenleg:\s)(\+?[0-9]+.[0-9]+\.?[0-9]+)"
    try:
        vissza = re.search(egyenleg_pattern, melyik).group(2)
        return vissza
    except AttributeError:
        return False


def convert_to_mysql_format(string):
    """Az sms-ben lévő dátum pl.: '2022. febr. 4. 9:29:36'
    átalakítása a mysql datetime formátumának megfelelően.
    """
    explode = string.split()
    day_of_the_month = explode[2][:-1]
    if int(explode[2][:-1]) < 10:
        day_of_the_month = "%02d" % (int(explode[2][:-1]),)

    if ev_honapjai.index(explode[1]) < 12:
        explode[1] = "%02d" % (ev_honapjai.index(explode[1]) + 1)
    explode[0] = "%02d" % (int(explode[0][:-1]),)
    return explode[0] + "-" + explode[1] + "-" + day_of_the_month + " " + explode[3]


if __name__ == "__main__":
    # Loggolás alapbeállításai
    FORMAT = "%(levelname)s: %(asctime)-2s prgsor: %(lineno)d %(message)s"  # Loggolás formátumának beállításra
    logging.basicConfig(
        format=FORMAT, level=logging.INFO
    )  # loggolás beálltása INFO-ra(csak a lényeg)

    # Alapértelmezett változók
    olvasando_fajl = "sms_full.xml"
    logging.info("A beolvasandó file: " + olvasando_fajl)
    kiirando_fajl = "balance.sql"
    logging.info("A kiírandó file: " + kiirando_fajl)
    arfolyam_file = "arfolyamok.csv"
    logging.info("A használt árfolyamok file: " + arfolyam_file)
    arfolyam = {}
    egyenleg2 = ""
    ev_honapjai = [
        "jan.",
        "febr.",
        "márc.",
        "ápr.",
        "máj.",
        "jún.",
        "júl.",
        "aug.",
        "szept.",
        "okt.",
        "nov.",
        "dec.",
    ]
    sql = "INSERT INTO beki (sorsz, datum, bekiv, valuta, egyenleg, sms, hely) VALUES "
    sql_sorok_szama = 1
    # xml fájl betöltése
    mydoc = minidom.parse(olvasando_fajl)

    # Árfolyam file meglétének ellenőrzése és frissítése ha két óránál régebbi
    try:
        arfolyam = arfolyam_feltoltes()
    except IOError:
        print("nincseh meg a file")
        logging.debug("Nem található a file.")

    items = mydoc.getElementsByTagName("sms")  # smsek beolvasása az items-be

    lapnev = (
        items[0].attributes["readable_date"].value
    )  # Az első sms dátumának kinyerése
    lapnev = lapnev[:4]  # Csak az évszám kivágása

    i = 1  # belső változó
    f = open("bevetel.sql", "w")
    f.writelines("/*\n")
    f.write("\tMySQL exportálva a \n\tkövetkező időpontban:\n\t")
    f.writelines(str(datetime.now()))
    f.writelines("\n*/\n\n")
    for elem in items:  # SMS-ek beolvasása
        if (
            "SIKERTELEN" in elem.attributes["body"].value
        ):  # Ha a SIKERTELEN üzenetet kaptuk, akkor nem törődünk vele
            continue
        tel = elem.attributes[
            "address"
        ].value  # telefonszám kinyerése az üzenetből, később lehet szűrni.
        rd = elem.attributes["readable_date"].value  # Dátum hozzáadása az rd változóhoz
        bd = elem.attributes["body"].value  # Az üzenet szövege
        cn = elem.attributes["contact_name"].value  # Az üzenetküldő neve
        # penz_pattern = r'(-|\+)[0-9]+(,?|\.?)[0-9]+\s?,?-?[A-Z][A-Z][A-Z]'
        penz_pattern = r"(-|\+|\ )\d{1,}(\.|,|\s)(\d{1,3}|,)*.(\d{1,3}|\w{1,3});"
        # előjel - vagy +, utána 0 vagy több szám, aztán 0 vagy egy karakter,
        # 0 vagy több szám, 0 vagy 1 szóköz 0 vagy 1 , 0 vagy 1 - és három karakter a pénznem azonosításhoz.
        # x = re.findall(pattern, bd)
        aktev = rd[:4]  # Az aktulis évszám kinyerése a dátumból.
        try:
            osszeg = re.search(
                penz_pattern, bd
            ).group()  # megkeressük a pénzeket az üzenetből
            egybd = re.sub(
                r"(;\sEgy:)|(;\sEgy\.:)", "; Egyenleg: ", bd
            )  # csak az sms végi egyenleg keresése
            egybd = " ".join(egybd.split())  # A két szóköz eltávolítása
            ketbd = egybd.replace(",-HUF;", " HUF;")  # A ",-HUF" átíráasa "HUF"-ra
            if not egyenleg_kerdez(
                ketbd
            ):  # Hs nincs egyenleg az SMS végén akkor az előzőt használjuk
                egyenleg = egyenleg2
            else:
                egyenleg = egyenleg_kerdez(ketbd)
                egyenleg2 = egyenleg_kerdez(ketbd)
            osszeg = osszeg.replace(
                ".", ""
            )  # kivesszük a pontot (ezres elválasztó) az összegek közül
            osszeg = osszeg.replace(
                ";", ""
            )  # kivesszük a végén a ;-t (kellet az smsek miatt a regexphez)
            osszeg = osszeg.replace(
                ",-HUF", " HUF"
            )  # Ha az üzenetben ,-HUF van azt átalakítjuk HUF-ra
            valuta = "0"
            if (
                osszeg.find("HUF") > -1
            ):  # Ha benne van az összegben a HUF => forint alapú a dolog
                osszeg = osszeg.replace(
                    " HUF", ""
                )  # Kivesszük a HUF szöveget az excel pénznem felismerése miatt.
            else:  # ha nem HUF-ban van megadva a pénz
                valuta = osszeg
                osszeg = penz_valto(osszeg)  # Átváltjuk az összeget forintra
                #  logging.debug('Valuta értéke: {} külföldi, {} HUF'.format(osszeg, forintban))
            egyenleg = egyenleg.replace(".", "")
            bd = bd.replace("...", "")  # Az üzenet elejéről a pontokat kivesszük még.
            i += 1  # sorszám növelése
            jodate = convert_to_mysql_format(rd)
            bd = bd.replace("'", "'")
            bd = " ".join(bd.split())
            """
            Így kell kinéznie:
            INSERT INTO `beki` (`sorsz`, `datum`, `bekiv`, `valuta`, `egyenleg`, `sms`) VALUES 
            (NULL, '2022-02-14 18:36:08.000000', '-456', '0', '+948647', '7878 Szàmla (120904) MUNKABÉR 
            àTUTALàS:+142.934,-HUF; Közl:165; Partner:Honvéd Együttes Müvészeti; Egy:+763.192,-HUF; OTPdirekt'); 
            """
            explode = bd.split(";")
            sql += '\n(NULL, "{}", "{}", "{}", "{}", "{}", "{}"),'.format(
                jodate, osszeg, valuta, egyenleg, bd, explode[1]
            )
            print(explode[1])

        except AttributeError:
            logging.debug("Sorszám:{}; - Nem átutalásos sms - {}".format(i, bd))
            continue
        if sql_sorok_szama % 25 == 0:
            sql = sql[:-1] + ";"
            sql += "\nINSERT INTO beki (sorsz, datum, bekiv, valuta, egyenleg, sms, hely) VALUES  "
        sql_sorok_szama += 1
    f.write(sql[:-1] + ";")
    f.close()
