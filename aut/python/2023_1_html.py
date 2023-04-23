import numpy as np
import pandas as pd

bem = "../xlsxs/2023_Autentikus.xlsx"
kim = "../sql/2023_aut.html"
sql = ''
honapok = ('JANUÁR', 'FEBRUÁR', 'MÁRCIUS', 'ÁPRILIS', 'MÁJUS',
           'JÚNIUS', 'JÚLIUS', 'AUGUSZTUS', 'SZEPTEMBER', 'OKTÓBER',
           'NOVEMBER', 'DECEMBER')


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
# f.write('# Honvédelmi adatok 2023-ra az autentikusból\n')
# f.write('# Készítette: Konta Boáz (kontab6@gmail.com).\n')
# f.write('USE honved2;\n')
f.write('''<!doctype html>
            <html lang="hu">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
            </head>
            <body class="container text-bg-secondary text-black">
            ''')
'''
    Itt történne az autentikus felodgozása
'''

Autentikus = pd.read_excel(bem, usecols="A,C:J")
Autentikus.rename(columns={'Unnamed: 0': 'datum',
                           'Tánckar': 'tanckar',
                           'Zenekar önálló': 'zkr',
                           'FÉRFIKAR': 'ffkar',
                           'KÖZREMŰK. EGY. ALATT/ KÜLSŐS': 'kozrem',
                           'KONTAKT': 'kontakt',
                           'STÁTUSZ': 'status',
                           'KÜLSŐS SZÁLLÍTÁS': 'kulszall',
                           'MEGJEGYZÉS': 'comment'}, inplace=True)  # Oszlopok átnevezése
Autentikus.dropna(how='all', inplace=True)  # Kidobunk minden töküres sort
print(Autentikus.columns)
Autentikus = Autentikus[Autentikus.tanckar.str.contains('Tánckar') == False]
print(Autentikus.to_string())
# Autentikus.dropna(thresh=2, inplace=True)

Autentikus.replace('\n', '<br>', inplace=True)
AutDropped = Autentikus.to_html(classes="table-sm table-bordered", na_rep='-')
#  htmlkesz = AutDropped.replace('\n', '<br>')
htmlkesz = AutDropped
f.write(htmlkesz)
f.write('</body>\n</html>')

#exit(0)
sor("Alap")
print(Autentikus.info())
print("Shape: ", Autentikus.shape)
sor("Összesítő a hiányzó értékekről")
print(Autentikus.ne(honapok))
Tanckar = Autentikus.dropna(subset=['Unnamed: 0'])  # eldobtuk azokat a sorokat ahol nincs a tánckar.
sor("Első dobás")
print(Tanckar.info())
print(Tanckar.to_string())
print("Shape: ", Tanckar.shape)
print(Tanckar.columns)

''' Linkek:
https://www.w3schools.com/python/pandas/pandas_cleaning_wrong_data.asp
https://pythonguides.com/pandas-drop/
https://pandas.pydata.org/docs/user_guide/10min.html
https://www.w3schools.com/python/python_tuples.asp
'''
