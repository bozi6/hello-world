"""
Database utility module for OTP transaction history.
Copyright (C) 2025 Konta Boáz
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions.
Last Modified: 2025. 06. 09. 14:43
"""
#  main.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 06. 12. 23:46

from tabulate import tabulate
import mysql.connector
from mysql.connector import Error

# Database connection constants
DB_CONFIG = {
    'host'    : 'ds718.lan',
    'port'    : 3307,
    'user'    : 'root',
    'password': 'qwe',
    'database': 'szamlatortenet'
}


def get_database_connection():
    """Create and return a database connection using predefined configuration."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        raise ConnectionError(f"Nem sikerült kapcsolódni az adatbázishoz: {e}")


def fetch_otp_transactions():
    """Fetch all transactions from OTP transaction history."""
    try:
        with get_database_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM otpxls")
                return cursor.fetchall()
    except Error as e:
        raise RuntimeError(f"Hiba történt az adatok lekérdezése során: {e}")


def execute_query(query: str, params: tuple = None) -> list:
    """
    MySQL lekérdezés végrahajtása

    Args:
        query (str): A lekérdezés leghosszabb szövege.
        params (tuple): A lekérdezés paramétereinek listája.

    Returns:
        list: A lekérdezés eredménye.

    Raises:
        RuntimeError: Hiba térni től a lekérdezés végéig.
    """
    try:
        with get_database_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()

    except Error as e:
        raise RuntimeError(f"Hiba történt lekérdezés végéig: {e}")


def main():
    """Main function database query functionality."""
    try:
        all_records = execute_query("SELECT * FROM otpxls")
        filtered_records = execute_query(
            "SELECT * FROM otpxls WHERE transdate >= %s AND transdate <= %s LIMIT 63", ("2020-01-01", "2020-12-31"))

        # print(all_records)
        # print(filtered_records[10]['osszeg'])
        tablazat = []
        for rekord in filtered_records:
            # print(rekord)
            tablazat.append([str(rekord['transdate']), str(rekord['osszeg']), rekord['kozlem']])
        print(tabulate(tablazat, headers=["Tranzakció ideje", "Összeg"], tablefmt="fancy_grid"))
        print("Összes rekord: ", len(all_records), "db.")
        print("Szűrt rekord: ", len(filtered_records), "db.")
    except Exception as e:
        print(f"Hiba történt a lekérdezés végéig: {e}")


if __name__ == "__main__":
    main()
