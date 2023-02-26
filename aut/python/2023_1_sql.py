import numpy as np
import pandas as pd

bem = "../xlsxs/2023_Autentikus.xlsx"
kim = "../sql/2023_aut.sql"
sql = ''
honapok = ['JANUÁR', 'FEBRUÁR', 'MÁRCIUS', 'ÁPRILIS', 'MÁJUS',
           'JÚNIUS', 'JÚLIUS', 'AUGUSZTUS', 'SZEPTEMBER', 'OKTÓBER',
           'NOVEMBER', 'DECEMBER']


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

Autentikus = pd.read_excel(bem, usecols="A,C:J")
sor("head rész")
# print(Autentikus.to_string())
sor("Előtte")
print(Autentikus.info())
Tanckar = Autentikus.dropna(subset=['Tánckar', 'Unnamed: 0']) # eldobtuk azokat a sorokat ahol nincs a tánckar kitöltve.
sor("Első dobás")
print(Tanckar.info())
print(Tanckar.to_string())
print(Tanckar.shape)
print(Tanckar.columns)

''' Linkek:
https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_data.asp
https://pythonguides.com/pandas-drop/
https://pandas.pydata.org/docs/user_guide/10min.html
https://www.w3schools.com/python/python_tuples.asp
'''