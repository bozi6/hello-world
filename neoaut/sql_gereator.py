"""
MySQL SQL fájl generálási funkciók - egy tábla, fix mezőnevekkel, dátum szűréssel
"""

from typing import List, Dict, Any
import logging
from config import FIXED_COLUMN_NAMES, FIXED_COLUMN_TYPES, TABLE_NAME


def generate_mysql_file_multi_sheet(all_sheets_data: Dict[str, Dict[str, Any]],
                                    output_file: str, database_name: str) -> None:
    """
    MySQL importálható fájl generálása több munkalapból egyetlen táblába fix mezőnevekkel
    Kiszűri az üres dátumú sorokat
    
    Args:
        all_sheets_data (Dict): Az összes munkalap adatai
        output_file (str): A kimeneti SQL fájl neve
        database_name (str): Az adatbázis neve
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # SQL fájl fejléc
            write_sql_header_single_table(f, database_name, list(all_sheets_data.keys()))

            # Egyetlen CREATE TABLE statement fix mezőnevekkel
            write_create_table_fixed(f, TABLE_NAME)

            # Összes munkalap adatának összegyűjtése és szűrése
            all_rows = []
            filtered_date_count = 0

            for sheet_name, sheet_data in all_sheets_data.items():
                logging.info(f"Adatok feldolgozása: '{sheet_name}' munkalapból ({len(sheet_data['rows'])} sor)")

                # Dátum alapú szűrés
                valid_rows = []
                for row in sheet_data['rows']:
                    if is_valid_date_row(row):
                        valid_rows.append(row)
                    else:
                        filtered_date_count += 1

                all_rows.extend(valid_rows)
                logging.info(f"'{sheet_name}': {len(valid_rows)} érvényes sor (dátum szűrés után)")

            # Összes INSERT statement egy táblába
            if all_rows:
                write_insert_statements_fixed(f, all_rows, TABLE_NAME)
                logging.info(f"Összesen {len(all_rows)} sor beszúrva a '{TABLE_NAME}' táblába")
                logging.info(f"Dátum szűrés miatt kihagyva: {filtered_date_count} sor")
            else:
                f.write("-- Nincs érvényes adat az Excel fájlban (dátum szűrés után)\n\n")

            # SQL fájl lábléc
            write_sql_footer(f)

        logging.info(f"MySQL fájl sikeresen generálva: {output_file}")

    except Exception as e:
        logging.error(f"Hiba a MySQL fájl generálása során: {str(e)}")
        raise


def is_valid_date_row(row: List[Any]) -> bool:
    """
    Ellenőrzi, hogy a sor első eleme (dátum mező) érvényes-e
    
    Args:
        row (List[Any]): Az adatsor
        
    Returns:
        bool: True, ha a dátum mező nem üres
    """
    if not row or len(row) == 0:
        return False

    # Az első oszlop a dátum (datum a FIXED_COLUMN_NAMES első eleme)
    date_value = row[1] if len(row) > 0 else None

    # Ellenőrizzük, hogy van-e érték és nem üres
    if date_value is None:
        return False

    # String esetén ellenőrizzük, hogy nem üres vagy csak whitespace
    # String esetén ellenőrizzük, hogy nem üres vagy csak whitespace
    if isinstance(date_value, str):
        # Üres string ('') vagy csak whitespace-ek esetén False
        stripped_value = date_value.strip()
        if stripped_value == '' or stripped_value.upper() == 'NULL':
            return False
        return True

    # Egyéb típusok esetén (datetime, stb.) elfogadjuk
    return True


def write_sql_header_single_table(file, database_name: str, sheet_names: List[str]) -> None:
    """SQL fájl fejléc írása egyetlen táblához"""
    file.write("-- MySQL adatbázis export (több munkalap -> egy tábla, fix mezőnevek)\n")
    file.write(f"-- Generálva adatbázis: {database_name}\n")
    file.write(f"-- Tábla: {TABLE_NAME}\n")
    file.write(f"-- Munkalapok: {', '.join(sheet_names)}\n")
    file.write(f"-- Fix mezőnevek: {', '.join(FIXED_COLUMN_NAMES)}\n")
    file.write("-- Szűrés: üres dátumú sorok kihagyva\n")
    file.write("-- --------------------------------------------------------\n\n")
    file.write("SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';\n")
    file.write("START TRANSACTION;\n")
    file.write("SET time_zone = '+02:00';\n")
    file.write("SET FOREIGN_KEY_CHECKS = 0;\n\n")
    file.write(
        f"CREATE DATABASE IF NOT EXISTS `{database_name}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;\n")
    file.write(f"USE `{database_name}`;\n\n")


def write_create_table_fixed(file, table_name: str) -> None:
    """CREATE TABLE statement írása fix mezőnevekkel és típusokkal a config-ból"""
    file.write(f"-- Tábla: {table_name}\n")
    file.write(f"-- Fix mezőnevek és típusok a config.py-ból\n")

    file.write(f"DROP TABLE IF EXISTS `{table_name}`;\n")
    file.write(f"CREATE TABLE `{table_name}` (\n")

    # Auto increment ID hozzáadása PRIMARY KEY-jel egy lépésben
    file.write("  `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,\n")

    # Fix oszlopok hozzáadása a config-ból
    for i, column_name in enumerate(FIXED_COLUMN_NAMES):
        col_type = FIXED_COLUMN_TYPES.get(column_name, 'VARCHAR(255)')

        # Az utolsó oszlop után nincs vessző
        comma = "," if i < len(FIXED_COLUMN_NAMES) - 1 else ""
        file.write(f"  `{column_name}` {col_type}{comma}\n")

    file.write(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;\n\n")


def write_insert_statements_fixed(file, rows: List[List[Any]], table_name: str) -> None:
    """INSERT statements írása fix mezőnevekkel"""
    if not rows:
        return

    # Fix mezőnevek használata a config-ból
    columns_str = "`, `".join(FIXED_COLUMN_NAMES)

    file.write(f"INSERT INTO `{table_name}` (`{columns_str}`) VALUES\n")

    for i, row in enumerate(rows):
        # Értékek feldolgozása - csak a szükséges számú oszlopot vesszük
        processed_values = []

        # Csak annyi értéket veszünk, amennyi fix oszlopunk van
        for j in range(len(FIXED_COLUMN_NAMES)):
            if j < len(row):
                value = row[j]
            else:
                value = None  # Ha nincs elég oszlop az Excel-ben, NULL-t használunk

            processed_values.append(escape_sql_value(value))

        values_str = ", ".join(processed_values)
        comma = "," if i < len(rows) - 1 else ";"
        file.write(f"({values_str}){comma}\n")

    file.write("\n")


def write_sql_footer(file) -> None:
    """SQL fájl lábléc írása"""
    file.write("SET FOREIGN_KEY_CHECKS = 1;\n")
    file.write("COMMIT;\n")


def escape_sql_value(value: Any) -> str:
    """SQL érték escape-elése"""
    if value is None or value == '' or str(value).strip() == '':
        return 'NULL'
    elif isinstance(value, str):
        # String értékek escape-elése
        escaped = str(value).replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')
        return f"'{escaped}'"
    elif isinstance(value, bool):
        return '1' if value else '0'
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        # Egyéb típusok string-ként kezelése
        escaped = str(value).replace("\\", "\\\\").replace("'", "\\'").replace('"', '\\"')
        return f"'{escaped}'"


# Visszafelé kompatibilitás érdekében megtartjuk a régi függvényeket is
def generate_mysql_file(data: Dict[str, Any], output_file: str,
                        database_name: str, table_name: str) -> None:
    """
    MySQL importálható fájl generálása (egyetlen tábla - visszafelé kompatibilitás)
    Most fix mezőnevekkel
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            # SQL fájl fejléc
            write_sql_header(f, database_name, table_name)

            # CREATE TABLE statement fix mezőnevekkel
            write_create_table_fixed(f, table_name)

            # INSERT statements fix mezőnevekkel  
            write_insert_statements_fixed(f, data['rows'], table_name)

            # SQL fájl lábléc
            write_sql_footer(f)

        logging.info(f"MySQL fájl sikeresen generálva: {output_file}")

    except Exception as e:
        logging.error(f"Hiba a MySQL fájl generálása során: {str(e)}")
        raise


def write_sql_header(file, database_name: str, table_name: str) -> None:
    """SQL fájl fejléc írása egyetlen táblához"""
    file.write("-- MySQL adatbázis export (fix mezőnevek)\n")
    file.write(f"-- Generálva: {database_name}.{table_name}\n")
    file.write(f"-- Fix mezőnevek: {', '.join(FIXED_COLUMN_NAMES)}\n")
    file.write("-- --------------------------------------------------------\n\n")
    file.write("SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';\n")
    file.write("START TRANSACTION;\n")
    file.write("SET time_zone = '+00:00';\n")
    file.write("SET FOREIGN_KEY_CHECKS = 0;\n\n")
    file.write(
        f"CREATE DATABASE IF NOT EXISTS `{database_name}` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;\n")
    file.write(f"USE `{database_name}`;\n\n")
