#  main.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 06. 20. 22:52

"""
Főprogram - xlsx fájl MySQL-re konvertálása (több munkalap -> egy tábla, fix mezőnevek)
"""

import logging
import sys
from pathlib import Path

from config import INPUT_FILE, OUTPUT_SQL_FILE, DATABASE_NAME, TABLE_NAME, FILTER_NULL_COLUMNS, FIXED_COLUMN_NAMES
from xlsx_reader import read_xlsx_file
from neoaut.sql_gereator import generate_mysql_file_multi_sheet


def setup_logging():
    """Logging beállítása"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('xlsx_to_mysql.log'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def main():
    """Főprogram futtatása"""
    setup_logging()
    logging.info("xlsx-ből MySQL konvertálás indítása (több munkalap -> egy tábla)...")

    try:
        # Bemeneti fájl ellenőrzése
        input_path = Path(INPUT_FILE)
        if not input_path.exists():
            logging.error(f"Bemeneti fájl nem található: {INPUT_FILE}")
            return False

        # Beállítások logolása
        logging.info(f"Cél tábla: {TABLE_NAME}")
        logging.info(f"Fix mezőnevek: {', '.join(FIXED_COLUMN_NAMES)}")
        
        if FILTER_NULL_COLUMNS:
            logging.info(f"NULL szűrés aktív a következő oszlopokra: {', '.join(FILTER_NULL_COLUMNS)}")
        else:
            logging.info("NULL szűrés nincs aktív")

        # Excel fájl beolvasása (minden munkalap szűréssel)
        logging.info(f"Excel fájl beolvasása: {INPUT_FILE}")
        all_sheets_data = read_xlsx_file(INPUT_FILE, FILTER_NULL_COLUMNS)

        # Statisztikák
        total_rows = sum(len(sheet_data['rows']) for sheet_data in all_sheets_data.values())
        total_sheets = len(all_sheets_data)
        
        logging.info(f"Összesen {total_sheets} munkalap, {total_rows} sor beolvasva (szűrés után)")
        
        # Részletes statisztikák minden munkalaphoz
        for sheet_name, sheet_data in all_sheets_data.items():
            logging.info(f"'{sheet_name}': {len(sheet_data['rows'])} sor, {len(sheet_data['headers'])} oszlop")

        # MySQL fájl generálása egyetlen táblába
        logging.info(f"MySQL fájl generálása: {OUTPUT_SQL_FILE}")
        logging.info(f"Minden adat a '{TABLE_NAME}' táblába kerül")
        
        generate_mysql_file_multi_sheet(
            all_sheets_data,
            OUTPUT_SQL_FILE,
            DATABASE_NAME
        )

        logging.info("Konvertálás sikeresen befejezve!")
        logging.info(f"Összes sor a '{TABLE_NAME}' táblában: {total_rows}")
        return True

    except Exception as e:
        logging.error(f"Hiba történt a konvertálás során: {str(e)}")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)