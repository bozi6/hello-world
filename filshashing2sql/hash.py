import hashlib
import os
from sqlescapy import sqlescape
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


__author__ = "Konta Boáz, kontab6@gmail.com @2020"

src_dir = "f:\\cuccbakk\\Dokumentumok\\Kepek\\Amerika"
tabla: str = 'pdfek'  # a kitöltendő táblázat megadása az adatbázison belül.


def insert_data(mit):
    """
    Adatbázisba a megérkezett adatok beillesztése insert metódussal
    :param mit: a bejövő mezők nevei és értékei
    :return: null
    """
    query = "INSERT INTO pdfek (filenev, blake2) VALUES(%s,%s)"
    try:
        db_config = read_db_config(filename='config.ini')
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print('Kapcsolat létrejött.')
        else:
            print('Kapcsolati hiba.')

        cursor = conn.cursor()
        cursor.executemany(query, mit)

        conn.connect()
    except Error as e:
        print('Hiba:', e)

    finally:
        cursor.close()
        conn.close()


extensions = ('.jpg', '.JPG', '.png', '.PNG', '.bmp', '.BMP', '.gif', '.GIF', 'jpeg', 'JPEG')
# extensions = ('.pdf', '.PDF')  # a fájlkiterjesztések listája
# string helyett javasolt list használata, ami állítólag sokkal gyorsabb.
SqlInsert = list()  # lista beállítása


def hashfiles(source, buff):
    i = 1  # a lista kiírásához a kezdőérték megadása
    for r, d, f in os.walk(source): # az r a kezdőkönyvtár a d a könyvtár a f pedig az aktuális file
        for file in f:
            if file.lower().endswith(extensions):
                filename = os.path.join("/", r, file)
                with open(filename, 'rb') as afile: # read file as byte (rb)
                    hasher = hashlib.blake2b()  # blake2b hash megadása a fájlokhoz. Jobb mint az md5 állítólag.
                    for chunk in iter(lambda: afile.read(buff), b""):
                        hasher.update(chunk)
                sql = (sqlescape(filename), hasher.hexdigest())
                SqlInsert.append(sql)
                # print('{};  -  filenév: {}.'.format(i, filename))
                i += 1


buf = 196608
hashfiles(src_dir, buf)

insert_data(SqlInsert)
