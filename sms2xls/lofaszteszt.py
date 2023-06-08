
sor = 'kezd'
sorszam = 0
for i in range(50):
    if sorszam % 25 == 0:
        print(sor)
    else:
        print('nemkezd')
    sorszam += 1

szov = " ".join('l:EGYÉB ELÖFIZETÉSI DIJ       0020953162 UPC; UPC MAGY'.split())
print(szov)