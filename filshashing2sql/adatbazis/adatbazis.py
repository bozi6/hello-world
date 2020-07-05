# MySQL csatlakozás modul.

import mysql.connector
from mysql.connector import Error

class MySQLstuffz():
    def __init__(self, host, user, pwd, port, db, tabla):
        """
        Connect to database
        :return: connection
        """
        self.host = host
        self.user = user
        self.pwd = pwd
        self.port = port
        self.db = db
        self.tabla = tabla
        self.connect()

    def connect(self):
        try:
            connection = mysql.connector.connect(self.host, self.user, self.pwd, self.port, self.db)
            return connection.cursor()
        except Error as e:
            print("Nem lehet csatalkozni valamiért:\n {},".format(e))


    def kezdotabla(self, tabla):
        """
        Initialize database and create table for it.
        :param tabla:
        :return:
        """
        con = self.connect()
        try:
            sql = "select * from {}".format(self.tabla)
            """        sql = '''
            CREATE DATABASE IF NOT EXISTS zfoto DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
            USE zfoto;
            DROP TABLE IF EXISTS {0}; CREATE TABLE {0} (sorsz int(4) NOT NULL,filenev varchar(254) NOT NULL,
            md5 char(32) COLLATE utf8mb4_hungarian_ci NOT NULL) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4
            COLLATE=utf8mb4_hungarian_ci COMMENT='Képek a Z: meghajtón';
            ALTER TABLE {0} ADD PRIMARY KEY(sorsz);
            ALTER TABLE {0} ADD FULLTEXT filenevIDX (filenev(32));
            ALTER TABLE {0} MODIFY sorsz int(4) NOT NULL AUTO_INCREMENT;
            COMMIT;'''.format(tabla)
            """
            con.execute(sql)

        finally:
            con.close()


if __name__ == "__main__":
    print("Connect to server if it's possible :-)")
