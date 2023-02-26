import pandas as pd


def sor(uzi):
    char = 80
    print("-" * char)
    print(uzi.center(char))
    print("-" * char)


mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
sor("mydataset kiratása:")
print(myvar)
sor("Pandas verzió:")
print("Pandas verzió: ", pd.__version__)
sor("Pandas sorozatok")
#  Pandas series
a = [1, 7, 2]
myvar = pd.Series(a)  # Sorozat megadása
sor("Sorozat kiiratása")
print(myvar)  # sorozat kiirása
sor("Első elem")
print(myvar[0])  # első elem indexelt kiiratása
myvar = pd.Series(a, index=["x", "y", "z"])  # Label megadása
sor("Saját indexelés megadása")
print(myvar)
print(myvar["y"])  # kiirás label szerint
sor("megadható kulcs érték pár szerint is")
calories = {"day1": 420, "day2": 300, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
sor("Sorozat készítése csak két adat alapján")
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
sor("DataFramek több dimenziós tömbök")
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# myvar = pd.DataFrame(data, index=["hétfő", "kedd", "szerda"])
# itt is megadhatunk saját indexet
myvar = pd.DataFrame(data)

print(myvar)
sor("Sorok kinyerése")
print(myvar.loc[0])  # Az első sor visszaadása.
sor("Első két sor")
print(myvar.loc[[0, 1]])  # Az első két sor visszaadása.
# index helyett elnevezve is vissza lehet keresni.
''' 
    Külső fájlból lehet kinyerni
    
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string()) # Az egész DataFrame-t kirja
 
'''
sor("Kiiratott sorok max száma")
print(pd.options.display.max_rows)
''' Alapból 60 ami azt jelenti hogyha több mint
60 sor van a DataFrameban akkor csak a fejléc
és az első öt sor tér vissza.

Ezt lehet növelni a 
pd.options.display.max_rows = 9999 -el.
ilyenkor a print(df) visszaadja az egészet
'''
sor("csv fájl gyors átnézése")
df = pd.read_csv('data.csv')
print(df.head(10))
sor("információk az adatokról")
print(df.info())
print("Ebből látszik, hogy 169 sor és négy oszlop van\n "
      "Range index és Data Columns szöveg\n"
      "És minden oszlop az adattípusokkal.")
sor("Adattisztítás.")
print("Eredeti")
print(df.info())
new_df = df.dropna()  # ha az eredetit is megváltoztatnád akkor az inplace=True-t kell még beleírni.
print("Pucolt")
print(new_df.info())
''' Másik megoldás ha feltöltjük a nulla értékeket.
Ezt a fillna() metódussal lehet megtenni.
'''
new_df = df.fillna(130)  # Ez mindenhol cseréli
# lehet csak az adott oszlopra a
# df["Calories"].fillna(130, inplace = True) -val
print(new_df.info())
