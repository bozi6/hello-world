#  main.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 06. 12. 23:46

from openpyxl import load_workbook
from typing import List

# Konstansok
INPUT_FILE = "./xlsx/tranzakciók.xlsx"
OUTPUT_FILE = "./sql/tranzakciok.sql"
SQL_TABLE_NAME = "otpxls"
HEADERS = ["sorsz", "transdate", "konydate", "tipus", "beki", "partnev", "partsz",
           "koltkat", "kozlem", "szamnev", "szamlaszam", "osszeg", "penznem"]


def read_excel_file() -> List[List]:
    """Excel fájl beolvasása"""
    workbook = load_workbook(filename=INPUT_FILE)
    sheet = workbook.active

    # Összes sor és oszlop beolvasása
    data = []
    for row in sheet.rows:
        row_data = [str(cell.value) if cell.value is not None else '' for cell in row]
        data.append(row_data)
    return data


def create_sql_values(data: List[List]) -> List[str]:
    """SQL értékek létrehozása a beolvasott adatokból"""
    headers = HEADERS
    values = []
    # Az első sor a fejléc, ezért a második sortól kezdjük
    for row in data[1:]:
        # Értékek megfelelő formázása
        formatted_values = ['NULL']
        for value in row:
            # String értékek idézőjelbe kerülnek
            if value.strip():
                removed_accent = value.replace("'", "")
                formatted_values.append(f"'{removed_accent}'")
            else:
                formatted_values.append('NULL')
        value_str = f"({', '.join(formatted_values)}),\n"
        values.append(value_str)
    return values, headers


def write_sql_file(values: List[str], headers: List[str]):
    """SQL fájl írása"""
    with open(OUTPUT_FILE, "w", encoding="utf8") as f:
        # Tábla létrehozása
        # create_table = f"CREATE TABLE IF NOT EXISTS {SQL_TABLE_NAME} (\n"
        # Oszlopok definiálása (minden mezőt VARCHAR(255)-ként kezelünk)
        # columns = [f"    {header} VARCHAR(255)" for header in headers]
        # create_table += ",\n".join(columns)
        # create_table += "\n);\n\n"
        #
        # f.write(create_table)
        # Tábla kiválasztása
        f.write(f"USE szamlatortenet;\n")
        # INSERT utasítás írása
        column_names = ", ".join(headers)
        f.write(f"INSERT INTO {SQL_TABLE_NAME} ({column_names}) VALUES\n")

        # Az utolsó elem kezelése (pontosvessző hozzáadása)
        last_value = values.pop().rstrip(",\n") + ";"
        values.append(last_value)

        # Értékek írása
        f.writelines(values)


def main():
    try:
        # Excel fájl beolvasása
        data = read_excel_file()
        # SQL értékek létrehozása
        values, headers = create_sql_values(data)
        # SQL fájl írása
        write_sql_file(values, headers)
        write_sql_file(values, headers)
        print(f"A konvertálás sikeres! Az eredmény a következő fájlban található: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Hiba történt: {str(e)}")


if __name__ == "__main__":
    main()
