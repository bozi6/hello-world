#  config.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 06. 20. 22:56

"""
Konfigurációs fájl az xlsx-ből MySQL fájl generálásához
"""

# Fájl útvonalak
INPUT_FILE = "xlsx/Aut_2025.xlsx"
OUTPUT_SQL_FILE = "sql/aut2025_data.sql"

# Adatbázis beállítások
DATABASE_NAME = "aut_database"
TABLE_NAME = "aut_events"  # Egyetlen tábla az összes munkalap adatának

# Fix mezőnevek az SQL táblákhoz (az Excel fejlécek helyett)
FIXED_COLUMN_NAMES = [
    "datum",
    "nap",
    "tanckar",
    "zkr",
    "ffkar",
    "kulsos",
    "kontakt",
    "status",
    "megjegyzes"
]

# Fix oszlop típusok a mezőnevekhez
FIXED_COLUMN_TYPES = {
    "datum"     : "DATE",
    "nap"       : "VARCHAR(19)",
    "tanckar"   : "VARCHAR(180)",
    "zkr"       : "VARCHAR(255)",
    "ffkar"     : "VARCHAR(255)",
    "kulsos"    : "VARCHAR(200)",
    "kontakt"   : "VARCHAR(150)",
    "status"    : "VARCHAR(160)",
    "megjegyzes": "TEXT"
}

# Oszlopok, ahol NULL értékek esetén kiszűrjük a sort (Excel fejléc nevekkel)
FILTER_NULL_COLUMNS = [
    "TÁNCKAR (és Zenekar)",
    "Zenekar önálló",
    "FÉRFIKAR",
    "KÖZREMŰK. EGY. ALATT/ KÜLSŐS",
    "tánckar_és_zenekar",
    "férfikar",
    "zenekar_önálló",
    "közreműk_egy_alatt_külsős"
]

# Oszlop típus megfeleltetések (általános)
COLUMN_TYPE_MAPPING = {
    'string'  : 'VARCHAR(255)',
    'int'     : 'INT',
    'float'   : 'DECIMAL(10,2)',
    'datetime': 'DATETIME',
    'date'    : 'DATE',
    'bool'    : 'BOOLEAN'
}

# Alapértelmezett oszlop típus
DEFAULT_COLUMN_TYPE = 'VARCHAR(255)'
