import hashlib
import os

from mysql.connector import MySQLConnection, Error

# from python_mysql_dbconfig import read_db_config
from sqlescapy import sqlescape
from tqdm import tqdm

__author__ = "Konta Boáz, kontab6@gmail.com @2020"


def insert_data(mit):
    """
    Adatbázisba a megérkezett adatok beillesztése insert metódussal

    :param mit: a bejövő mezők nevei és értékei
    :return: null

    """
    print(mit)
    query = "INSERT INTO {} (filenev, blake2, size) VALUES(%s,%s, %s)".format(tabla)
    try:
        db_config = read_db_config(filename="config.ini")
        conn = MySQLConnection(**db_config)
        if conn.is_connected():
            print("Kapcsolat létrejött...")
            conn.connect()
        else:
            print("Kapcsolati hiba.")
        cursor = conn.cursor()
        cursor.executemany(query, mit)
        conn.commit()
    except Error as e:
        print("Hiba:", e)
    finally:
        cursor.close()
        conn.close()


def hashfiles(source, buff):
    """
    Fájlok hashelése blake2b algioritmus szerint
    :param source: forrásfálj neve
    :param buff: bufferméret
    :return:

    """
    if not os.path.exists(source):
        print("nem létezik ilyen útvonal:" + source)
    else:
        i = 1  # a lista kiírásához a kezdőérték megadása
        file_count = sum(
            len(files) for _, _, files in os.walk(source)
        )  # mennyi az összes fájl lekérdezése
        with tqdm(total=file_count) as pbar:  # ezek megjelenítése progress barral
            for r, d, f in os.walk(
                source
            ):  # az r a kezdőkönyvtár a d a könyvtár a f pedig az aktuális file
                for file in f:
                    if file.lower().endswith(
                        extensions
                    ):  # ha a kiterjesztés megegyezik amit akarunk
                        filename = os.path.join("/", r, file)  # fájlnév kinyerése
                        size = os.path.getsize(filename)  # fájlméret lekérdezése
                        with open(filename, "rb") as afile:  # read file as byte (rb)
                            hasher = (
                                hashlib.blake2b()
                            )  # blake2b hash megadása a fájlokhoz. Jobb mint az md5 állítólag.
                            for chunk in iter(lambda: afile.read(buff), b""):
                                hasher.update(chunk)  # magic
                        sql = (
                            sqlescape(filename),
                            hasher.hexdigest(),
                            size,
                        )  # ezt egy sor sql
                        SqlInsert.append(sql)  # ezt meg hozzáadjuk a lekérdezéshez
                        # print('{};  -  filenév: {}. - hash: {}'.format(i, filename, sql[1]))
                        i += 1  # megtalált darabszám növelése
                        pbar.update()  # progressbar frissítése


if __name__ == "__main__":
    extensions = (
        ".jpg",
        ".JPG",
        ".png",
        ".PNG",
        ".bmp",
        ".BMP",
        ".gif",
        ".GIF",
        "jpeg",
        "JPEG",
    )
    src_dir = "Z://Nyilvános/"
    tabla: str = "fotok"  # a kitöltendő táblázat megadása az adatbázison belül.
    # extensions = ('.pdf', '.PDF')  # a fájlkiterjesztések listája
    # string helyett javasolt list használata, ami állítólag sokkal gyorsabb.
    SqlInsert = list()  # lista beállítása
    buf = 196608
    hashfiles(src_dir, buf)
    insert_data(SqlInsert)
