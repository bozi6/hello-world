from mysql.connector import MySQLConnection, Error


if __name__ == "__main__":
    from python_mysql_dbconfig import read_db_config

    """
    Main programs, inserts books list into MySQL database

    :return: print inserted books

    """
    books = [
        ("Harry Potter And The Order Of The Phoenix", "9780439358071"),
        ("Gone with the Wind", "9780446675536"),
        ("Pride and Prejudice (Modern Library Classics)", "9780679783268"),
    ]
    print(type(books))
    print(books)
    # insert_books(books)


def insert_books(books):
    """
    Könyvek beszúrása a táblázatba

    :param books: könyv object
    :return: None or Error

    """
    query = "INSERT INTO books(title,isbn) " "VALUES(%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.executemany(query, books)

        conn.commit()
    except Error as e:
        print("Error:", e, e.args[0])

    finally:
        cursor.close()
        conn.close()
