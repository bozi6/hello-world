megyek = ['Bács-Kiskun', 'Baranya', 'Békés', 'Borsod-Abaúj-Zemplén', 'Csongrád-Csanád',
          'Fejér', 'Győr-Moson-Sopron', 'Hajdú-Bihar', 'Heves', 'Jász-Nagykun-Szolnok',
          'Komérom-Esztergom', 'Nógrád', 'Pest', 'Somogy', 'Szabolcs-Szatmár-Bereg',
          'Tolna', 'Vas', 'Veszprém', 'Zala', 'Budapest']
szekhelyek = ['Kecskemét', 'Pécs', 'Békéscsaba', 'Miskolc', 'Szeged', 'Székesfehérvár',
              'Győr', 'Debrecen', 'Eger', 'Szolnok', 'Tatabánya', 'Salgótarján',
              'Budapest', 'Kaposvár', 'Nyíregyháza', 'Szekszárd', 'Szombathely',
              'Veszprém', 'Zalaegerszeg', 'Budapest']

# print(megyek)  # prints all elements in a list
# print(megyek[0])  # print first element from a list


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# zip going through multiple lists and extract them
for megye, szeh in zip(megyek, szekhelyek):
    print('Megye: {} - Székhely: {}'.format(megye,szeh))

print("Összeg:")
print(sum(lista))
print("Minimum")
print(min(lista))
print("Maximum")
print(max(lista))
print("Lista első eleme:")
print(lista[0])
print("Lista utolsó eleme:")
print(lista[-1])
