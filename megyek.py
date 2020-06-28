megyek = ['Bács-Kiskun', 'Baranya', 'Békés', 'Borsod-Abaúj-Zemplén', 'Csongrád-Csanád',
          'Fejér', 'Győr-Moson-Sopron', 'Hajdú-Bihar', 'Heves', 'Jász-Nagykun-Szolnok',
          'Komérom-Esztergom', 'Nógrád', 'Pest', 'Somogy', 'Szabolcs-Szatmár-Bereg',
          'Tolna', 'Vas', 'Veszprém', 'Zala', 'Budapest']
szekhelyek = ['Kecskemét', 'Pécs', 'Békéscsaba', 'Miskolc', 'Szeged', 'Székesfehérvár',
              'Győr', 'Debrecen', 'Eger', 'Szolnok', 'Tatabánya', 'Salgótarján',
              'Budapest', 'Kaposvár', 'Nyíregyháza', 'Szekszárd', 'Szombathely',
              'Veszprém', 'Zalaegerszeg', 'Budapest']

# print(states)  # prints all elements in a list
# print(states[0])  # print first element from a list


lista = [1, 3, 4, 6, 4, 7, 8, 2, 3]
# zip going through multiple lists and extract them
for megye,szeh in zip(megyek, szekhelyek):
    print('Megye: {} - Székhely: {}'.format(megye,szeh))

print(sum(lista))
print(min(lista))
print(max(lista))
print(lista[0])
print(lista[-1])
