import itertools

"""
Megkeresi a megadott szó anagrammáit
olyan 8 betűsig még használható
utána nagyon belassul....
a szo változóba kell beírni a keresett szót, aztán
a for parancsnál összerakja annak változatait
minden lehetséges kombinációt,
majd kiekeresi, hogy szerepel-e a szotár.com ról letöltött 
szavak között valamelyik variációja.
Hasznos szavak pl. állat, csákós, alszik, drága, eresz stb...
"""

szo = 'eltesz'
x = []
for perm in itertools.permutations(szo):
    x.append("".join(perm))
print('Variációk száma: {}'.format(len(x)))
# print(x)
# print(*x, sep="\n ")
szolista = []

with open(r'./dicts/szotar.txt', 'r') as fp:
    # read all lines using readline()
    lines = fp.readlines()
    for sor in lines:
        if sor.strip():
            szolista.append(sor.split(maxsplit=1)[0])
fp.close()
print('Megtalált szavak:')
print('a sorszám a fájlban lévő szó sora.')
for row in szolista:
    if row in x:
        print('sorszám: {} - szó: {}'.format(szolista.index(row)+1, row))
    #  check if string present on a current line
    # word = 'Line'
    # print(row.find(word))
    # find() method returns -1 if the value is not found,
    # if found it returns index of the first occurrence of the substring
    """if row.find(word) != -1:
        print('string exists in file')
        print('line Number:', szolista.index(row))
    # lista kiírása fájlba ha számok vannak a szó után
    fajl = open('hu_full_stripped.txt', 'w')
    for items in szolista:
        fajl.writelines(items+'\n')
    fajl.close()
    """
