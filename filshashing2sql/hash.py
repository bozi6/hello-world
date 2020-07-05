import hashlib
import os
from sqlescapy import sqlescape

__author__ = "Konta Boáz, kontab6@gmail.com @2020"

src_dir = "z:\\boz\\fotok\\Családi\\maradek"
hasher = hashlib.md5()
# mentett = open('./mentett.sql', 'w', newline='\n')
tabla: str = 'fotok'


i = 1

extensions = ('.jpg', '.JPG', '.png', '.PNG', '.bmp', '.BMP', '.gif', '.GIF', 'jpeg', 'JPEG')
SqlInsert = list('INSERT INTO {} (sorsz,filenev,md5) VALUES '.format(tabla))
# string helyett javasolt list használata, ami állítólag sokkal gyorsabb.
for r, d, f in os.walk(src_dir):
    for file in f:
        if file.lower().endswith(extensions):
            filename = os.path.join("/", r, file)
            with open(filename, 'rb') as afile:
                buf = afile.read()
                hasher.update(buf)
            SqlInsert += ("(NULL,'{}', '{}'),\n".format(sqlescape(filename), hasher.hexdigest()))
            i += 1
# A szöveg végén az enter és a , lecserélése ;-re, mert az SQL azt szereti.
SqlInsert[-2:] = ';'

print(''.join(SqlInsert))

