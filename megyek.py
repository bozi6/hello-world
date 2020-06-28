megyek = ['Bács-Kiskun', 'Baranya', 'Békés', 'Borsod-Abaúj-Zemplén', 'Csongrád-Csanád',
          'Fejér', 'Győr-Moson-Sopron', 'Hajdú-Bihar', 'Heves', 'Jász-Nagykun-Szolnok',
          'Komérom-Esztergom', 'Nógrád', 'Pest', 'Somogy', 'Szabolcs-Szatmár-Bereg',
          'Tolna', 'Vas', 'Veszprém', 'Zala', 'Budapest']

# print(states)  # prints all elements in a list
# print(states[0])  # print first element from a list


lista = [1, 3, 4, 6, 4, 7, 8, 2, 3]

for megye in megyek:
    print('Megye: {}'.format(megye))

print(sum(lista))
print(min(lista))
print(max(lista))
print(lista[0])
print(lista[-1])
