from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def connect():
    """Connect to MySQL database"""

    db_config = read_db_config(filename="..\\config.ini")
    conn = None
    try:
        print("Kapcsolódás a MySQL adatbázishoz...")
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print("Kapcsolat létrejött.")
        else:
            print("Kapcsolati hiba.")

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Kapcsolat lezárva.")


if __name__ == "__main__":
    connect()
