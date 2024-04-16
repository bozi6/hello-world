#  icsprobe.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 01. 27. 9:33
import re

from icalendar import Calendar
from lxml import etree


def strip_tags(html):
    if isinstance(html, str):
        parser = etree.HTMLParser()
        tree = etree.fromstring(html, parser)
        return etree.tostring(tree, encoding="unicode", method="text")
    elif html is None:
        return html


def datum(cucc: object):
    ev = cucc.get("dtstart").dt.year
    ho = cucc.get("dtstart").dt.month
    nap = cucc.get("dtstart").dt.day
    return f"'{ev}-{ho:02d}-{nap:02d}',"


def kezdesido(cucc: object):
    try:
        hh = cucc.get("dtstart").dt.hour
        mm = cucc.get("dtstart").dt.minute
        return f"'{hh:02d}:{mm:02d}',"
    except AttributeError:
        return "'Nincs megadva kezdés',"


def osszegzes(cucc: object):
    if cucc.get("summary") is not None:
        vissz = cucc.get("summary").strip().replace("/", "-")
        spacetelenitett = re.sub(" +", " ", vissz)
        return f"'{spacetelenitett}',"
    else:
        return "'Nincs megadva műsor',"


def musorbolmuszak(cucc: object):
    descript = cucc.get("description")
    if descript is not None:
        # descript = descript.to_ical().decode("utf-8").replace('\r\n', '\n').strip()
        if str(descript) != "":
            descript = descript.to_ical().decode("utf-8").strip()
            descript = strip_tags(descript)
            descript = re.split(r"\\n", descript)
            for text in descript:
                if "Műszak" in text:
                    try:
                        x = re.search(r"^Műszak:", text)
                        return f"'{x.string[8:]}',"
                    except AttributeError:
                        return "NULL,"
                else:
                    continue
        return "NULL,"
    else:
        return "NULL,"


def musbolkontakt(cucc: object):
    descript = cucc.get("description")
    if descript is not None:
        # descript = descript.to_ical().decode("utf-8").replace('\r\n', '\n').strip()
        if str(descript) != "":
            descript = descript.to_ical().decode("utf-8").strip()
            descript = strip_tags(descript)
            descript = re.split(r"\\n", descript)
            for text in descript:
                if "Kontakt" in text:
                    try:
                        x = re.search(r"^Kontakt:", text)
                        return f"'{x.string[9:]}',"
                    except AttributeError:
                        return "'-',"
                else:
                    continue
        return "'-',"
    else:
        return "'-',"


def musorboljelmeztar(cucc: object):
    descript = cucc.get("description")
    if descript is not None:
        # descript = descript.to_ical().decode("utf-8").replace('\r\n', '\n').strip()
        if str(descript) != "":
            descript = descript.to_ical().decode("utf-8").strip()
            descript = strip_tags(descript)
            descript = re.split(r"\\n", descript)
            for text in descript:
                if "Jelmeztár" in text:
                    try:
                        x = re.search(r"^Jelmeztár:", text)
                        return f"'{x.string[11:]}',"
                    except AttributeError:
                        return "NULL,"
                else:
                    continue
        return "NULL,"
    else:
        return "NULL,"


def musorbolfelelos(cucc: object):
    descript = cucc.get("description")
    if descript is not None:
        if str(descript) != "":
            # descript = descript.to_ical().decode("utf-8").replace('\r\n', '\n').strip()
            descript = descript.to_ical().decode("utf-8").strip()
            descript = strip_tags(descript)
            descript = re.split(r"\\n", descript)
            for text in descript:
                if "Felelős" in text:
                    try:
                        x = re.search(r"^Felelős:", text)
                        return f"'{x.string[9:]}',"
                    except AttributeError:
                        return "NULL,"
                else:
                    continue
        return "NULL,"
    else:
        return "NULL,"


def desc_min_mfjk(cucc: object):
    descript = cucc.get("description")
    if descript is not None:
        if str(descript) != "":
            descript = descript.to_ical().decode("utf-8").strip()
            descript = strip_tags(descript)
            descript = re.split(r"\\n", descript)
            for text in descript:
                try:
                    x = re.search(r"^Műszak:", text)
                    if x is not None:
                        descript.pop(descript.index(x.string))
                    x = re.search(r"^Felelős:", text)
                    if x is not None:
                        descript.pop(descript.index(x.string))
                    x = re.search(r"^Jelmeztár:", text)
                    if x is not None:
                        descript.pop(descript.index(x.string))
                except ValueError:
                    continue
                except AttributeError:
                    continue
            return f"'{" ".join(descript).strip()}',"
        else:
            return f"'-',"
    else:
        return f"'-',"


def helyformat(cucc: object):
    helyszin = cucc.get("location")
    if helyszin is not None:
        if str(helyszin) != "None":
            helyszin = helyszin.to_ical().decode("utf-8").strip()
            return f"'{helyszin}',"
        else:
            return f"'Nincs helyszín megadva.',"
    else:
        return f"'Nincs helyszín megadva.',"


g = open("honvedegyuttes@gmail.com.ics", "rb")
sq = open("honvedelmi.sql", "w")
gcal = Calendar.from_ical(g.read())
kezdet = []
megjegyzeshosszok = []
sql = "-- 2007 november 2 óta van gugli naptárban bejegyzés\n"
sql += "-- Tábla törlése!:\n"
sql += "TRUNCATE aut;\n"
sql += (
    "INSERT INTO aut "
    "(sorsz, datum, ceg, kezd, HM, hely, helykod, musor, tev, honv, kulsos, "
    "megjegyzes, kontakt, muszak, jelmezt, szallitas, kiallas, felelos, alkjell, "
    "bevitel_time, slug) \nVALUES"
)
sor = 1
for component in gcal.walk():
    # print(component.name)
    if component.name == "VEVENT":
        sql += "(NULL, "  # sorszám
        sql += datum(component)  # dátum
        ceg = 24
        sql += f"{ceg},"  # ceg
        sql += kezdesido(component)
        sql += f"0,"  # HM
        sql += helyformat(component)  # hely
        sql += "965,"  # helykod
        sql += osszegzes(component)  # musor
        sql += "'előadás',"  # tev
        sql += "'',"  # honv
        sql += "'',"  # kulsos
        sql += desc_min_mfjk(component)  # megjegyzes
        sql += musbolkontakt(component)  # kontakt
        sql += musorbolmuszak(component)  # muszak
        sql += musorboljelmeztar(component)  # jelmezt
        sql += "'-',"  # szallitas
        sql += "'-',"  # kiallas
        sql += musorbolfelelos(component)  # felelos
        sql += "'-',"  # alkjell
        sql += "NOW(),"  # bevitel_time
        sql += "''"  # slug
        sql += "),\n"
        # print("-" * 80)
        # print("Összegzés: ", component.get("summary"))
        tev = "előadás"
        HM = 0
        helykod = 965

        hely = component.get("location")
        # print("Helyszín: ", component.get("location"))
        # try:
        #     leir = component.get("description")
        #     print("Leírás: ", leir.replace("<br>", "\n"))
        # except AttributeError:
        #     pass
        # print("Kezdés: ", component.get("dtstart").dt)
        datumok = (
            component.get("dtstart").dt.year,
            component.get("dtstart").dt.month,
            component.get("dtstart").dt.day,
        )
        kezdet.append(datumok)
        # print("Vége: ", component.get("dtend"))
        # print("Időbélyeg: ", component.get("dtstamp"))
        print(sor)
        sor += 1
        sq.write(sql)
        sql = ""
sql = sql[:-3]
sql += ";"

g.close()
sq.close()
