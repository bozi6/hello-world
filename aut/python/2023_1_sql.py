import pandas as pd

bem = "../xlsxs/2023_Autentikus.xlsx"
kim = "../sql/2023_aut.sql"
sql = ''


def sor(uzi):
    emptyspaces = 80
    print("-" * emptyspaces)
    print(uzi.center(emptyspaces))
    print("-" * emptyspaces)


'''
    Itt megnyitjuk a kimeneti sql fájlt a megfelelő qsl 
    parancs létrehozásához
'''
f = open(kim, "w", encoding='utf8')
f.write('# Honvédelmi adatok 2023-ra az autentikusból\n')
f.write('# Készítette: Konta Boáz (kontab6@gmail.com).\n')
f.write('USE honved2;\n')
'''
    Itt történne az autentikus felodgozása
'''

Autentikus = pd.read_excel(bem)
sor("head rész")
print(Autentikus.head(6))
sor("index")
print(Autentikus.index)
print(Autentikus.columns[Autentikus.isnull().any()])
print(Autentikus["Unnamed: 0"].to_list())
