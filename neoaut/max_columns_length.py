#  max_columns_length.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 06. 21. 13:14

import pandas as pd
from config import INPUT_FILE

# Konstansok
SEPARATOR_MAIN = "=" * 40
SEPARATOR_SUB = "-" * 40
SEPARATOR_HEADER = "-" * 50


def analyze_column(column_data):
    """
    Egy oszlop leghosszabb értékének meghatározása.
    
    Args:
        column_data: pandas Series - az oszlop adatai
        
    Returns:
        str or None: a leghosszabb érték vagy None ha üres
    """
    string_values = column_data.dropna().astype(str)
    if not string_values.empty:
        return max(string_values, key=len)
    return None


def process_worksheet(sheet_name):
    """
    Egy munkalap feldolgozása és eredmények visszaadása.
    
    Args:
        sheet_name (str): a munkalap neve
        
    Returns:
        dict: oszlop név -> leghosszabb érték megfeleltetés
    """
    df = pd.read_excel(INPUT_FILE, sheet_name=sheet_name)
    longest_values = {}

    for col in df.columns:
        longest_values[col] = analyze_column(df[col])

    return longest_values


def print_results(sheet_name, longest_values):
    """
    Egy munkalap eredményeinek kiírása.
    
    Args:
        sheet_name (str): a munkalap neve
        longest_values (dict): oszlop név -> leghosszabb érték
    """
    print(f"\nMUNKALAP: {sheet_name}")
    print(SEPARATOR_MAIN)

    if longest_values:
        for col, val in longest_values.items():
            if val is not None:
                print(f"Oszlop: {col}, Leghosszabb érték ({len(str(val))})")
            else:
                print(f"Oszlop: {col}, Üres oszlop")
    else:
        print("Nincsenek oszlopok ezen a munkalapon")

    print(SEPARATOR_SUB)


def main():
    """
    Főprogram - Excel fájl összes munkalapjának elemzése.
    """
    excel_file = pd.ExcelFile(INPUT_FILE)
    sheet_names = excel_file.sheet_names

    print(f"Talált munkalapok: {sheet_names}")
    print(SEPARATOR_HEADER)

    for sheet_name in sheet_names:
        longest_values = process_worksheet(sheet_name)
        print_results(sheet_name, longest_values)

    print("\nFeldolgozás befejezve!")


if __name__ == "__main__":
    main()
