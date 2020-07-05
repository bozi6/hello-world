from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def insert_data(miket, hova):
    query = hova

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**)

        cursor = conn.cursor()
        cursor.executemany(query, miket)

        conn.connect()