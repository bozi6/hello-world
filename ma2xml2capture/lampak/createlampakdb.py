"""
A lampakdb.lol fájl megnyitása és beállítása a későbbi
ellenőrzések céljából, ha van benne ilyen bejegyzés akkor
a lámpa optikája, teljesítménye, tömege, egységneve kinyerésre kerül.
A # kezdődő sorokkal lehet újabb lámpát hozzáadni, de lehet, hogy a
./lampak/lampakdb-t át kell írni arra ahonna meghívódik, mert ide teszi alapból
és ha meghívjuk akkor meg máshol keresi.
"""
from lol.database import database, serializer

data = database.Database("./lampak/lampakdb", ["fixture", "optics", "wattage", "unit", 'weight'])
# Adatbázisfájl betöltése és a mezők megadása
data.set_track_modification(False)
# valami logoolás kikapcsolása

"""
Ezekkel a sorokkal adtam hozzá az újabb lámpákat, itt kell megadni a mezőket hozzá.
"""
# data.add(["4 Source Four LED Lustr + Quick Setup - High Impact", "750/230V", "750W", "S4LL QHI", "8,5kg"])
# data.add(["5 Alpha Beam 1500 Standard - lamp off", "1500/230V", "1500W", "ABe15St", "25,0kg"])
# data.add(["Generic Par 64", "CP60", "1000W", "2 Dimmer", "1.8kg"])
# data.add(["3 Scroller Dimmer 00", "50°", "12.5W", "Scroller Dimmer 00", "2.5kg"])
keys = data.ids()
