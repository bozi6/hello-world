#!/usr/bin/env python3
"""
Transform authentic Excel table to mySQL SQL file.
Created 2025.06.06.
"""
import logging
import os.path
import shutil
import time
from typing import List

import openpyxl
from cprint import cprint

import aut.python.funct.aut_configfile as conf
import aut.python.funct.process as proc

__author__ = "Konta Boáz"
__author_email__ = "kontab6@gmail.com"
__copyright__ = "Konta Boáz 2025"

# Constans
INPUT_FILE = "../xlsx/Aut_2025.xlsx"
OUTPUT_FILE = "../sql/2025_aut.sql"
XLSX_DIR = "../xlsx/"
BACKUP_FILE = f"{XLSX_DIR}2025_Autentikus.bak"
CELL_RANGE = "A2:I210"


def setup_logging():
    """Configure logging settings."""
    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s  - %(message)s")
    logging.disable(logging.DEBUG)


def validate_input_file(filename):
    """Validate and copy input file if needed

    Args:
        filename: PAth to input file
    Returns:
        Path to file to be processed
    """

    if os.path.exists(filename):
        shutil.copyfile(filename, BACKUP_FILE)
        cprint.info("File backed up successfully.")
        return BACKUP_FILE
    cprint.warn(f"File {filename} not found. Using backup file.")
    return BACKUP_FILE


def process_worksheet(sheet, sql_values: List[str]):
    """Process single worksheet and extract SQL values"""
    cells = sheet[CELL_RANGE]
    rows_processed = 0

    for row in cells:
        c1, c2, c3, c4, c5, c6, c7, c8, c9 = row

        # Process dance company rows
        if c1.value and c3.value and c3.value not in conf.TANCNEV:
            process_data = proc.Egysor(c1.value, c2.value, c3.value, c4.value,
                                       c5.value, c6.value, c7.value, c8.value, c9.value)
            sql_values.append(proc.sqlrak(process_data))
            rows_processed += 1

        # Process choir rows
        elif c1.value and c5.value and c5.value not in conf.FERFIKARNEVEK:
            process_data = proc.Egysor(c1.value, c2.value, c3.value, c4.value,
                                       c5.value, c6.value, c7.value, c8.value, c9.value)
            sql_values.append(proc.sqlrak(process_data))
            rows_processed += 1
    cprint.info(f"Processed {rows_processed} rows from {sheet.title}")
    return rows_processed


def write_sql_file(sql_values: List[str]):
    """Write SQL values to output file"""
    with open(OUTPUT_FILE, "w", encoding="utf8") as f:
        f.write(conf.SQLDEFAULT)
        f.write("\nINSERT INTO aut (sorsz,datum,ceg,kezd,hely,musor,kontakt,megjegyzes,helykod,szallitas,tev) VALUES \n")

        # Handle last element separately to add semicolon
        last_value = sql_values.pop().rstrip(",\n") + ";"
        sql_values.append(last_value)
        f.writelines(sql_values)


def main():
    """Main functions to process Excel file and generate SQL file"""
    setup_logging()
    start_time = time.time()
    input_file = validate_input_file(INPUT_FILE)
    cprint.info(f"Processing input file: {INPUT_FILE}")

    workbook = openpyxl.load_workbook(filename=INPUT_FILE, read_only=True)
    sql_values = []

    for sheet in workbook.worksheets:
        process_worksheet(sheet, sql_values)

    write_sql_file(sql_values)

    execution_time = time.time() - start_time
    cprint.ok("File processing completed")
    cprint.info(f"Execution time: {execution_time:.2f} seconds")


if __name__ == "__main__":
    main()
