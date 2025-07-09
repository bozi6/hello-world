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


class ExcelToSQLConfig:
    """Configuration constants for Excel to SQL conversion."""
    INPUT_FILE = "../xlsx/Aut_2025.xlsx"
    OUTPUT_FILE = "../sql/2025_aut.sql"
    XLSX_DIR = "../xlsx/"
    BACKUP_FILE = f"{XLSX_DIR}2025_Autentikus.bak"
    CELL_RANGE = "A2:I210"
    EXPECTED_COLUMNS = 9


class SQLGenerator:
    """Handles SQL file generation from Excel data."""

    def __init__(self, output_file: str):
        self.output_file = output_file
        self.sql_values = []

    def add_row_data(self, row_data):
        """Add processed row data to SQL values list."""
        processed_data = proc.Egysor(*row_data)
        self.sql_values.append(proc.sqlrak(processed_data))

    def write_to_file(self):
        """Write accumulated SQL values to output file."""
        with open(self.output_file, "w", encoding="utf8") as sql_file:
            sql_file.write(conf.SQLDEFAULT)
            sql_file.write(
                "\nINSERT INTO aut "
                "(sorsz,datum,ceg,kezd,hely,musor,kontakt,megjegyzes,helykod,szallitas,tev)"
                " VALUES \n")

            if self.sql_values:
                # Handle last element separately to add semicolon
                last_value = self.sql_values.pop().rstrip(",\n") + ";"
                self.sql_values.append(last_value)
                sql_file.writelines(self.sql_values)


def setup_logging():
    """Configure logging settings."""
    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s  - %(message)s")
    logging.disable(logging.DEBUG)


def validate_and_backup_file(filename: str, backup_file: str) -> str:
    """Validate input file and create backup if needed.
    
    Args:
        filename: Path to input file
        backup_file: Path to backup file
        
    Returns:
        Path to file to be processed
    """
    if os.path.exists(filename):
        shutil.copyfile(filename, backup_file)
        cprint.info("File backed up successfully.")
        return backup_file
    cprint.warn(f"File {filename} not found. Using backup file.")
    return backup_file


def extract_cell_values(row):
    """Extract values from Excel row cells."""
    return [cell.value for cell in row]


def is_valid_dance_company_row(cell_values: List) -> bool:
    """Check if row contains valid dance company data."""
    company_name, _, dance_name = cell_values[0], cell_values[1], cell_values[2]
    return company_name and dance_name and dance_name not in conf.TANCNEV


def is_valid_choir_row(cell_values: List) -> bool:
    """Check if row contains valid choir data."""
    company_name, _, _, _, choir_name = cell_values[0], cell_values[1], cell_values[2], cell_values[3], cell_values[4]
    return company_name and choir_name and choir_name not in conf.FERFIKARNEVEK


def process_worksheet_data(worksheet, sql_generator: SQLGenerator) -> int:
    """Process single worksheet and extract SQL values.
    
    Args:
        worksheet: Excel worksheet to process
        sql_generator: SQL generator instance
        
    Returns:
        Number of rows processed
    """
    cells = worksheet[ExcelToSQLConfig.CELL_RANGE]
    rows_processed = 0

    for row in cells:
        if len(row) != ExcelToSQLConfig.EXPECTED_COLUMNS:
            continue

        cell_values = extract_cell_values(row)

        if is_valid_dance_company_row(cell_values) or is_valid_choir_row(cell_values):
            sql_generator.add_row_data(cell_values)
            rows_processed += 1

    cprint.info(f"Processed {rows_processed} rows from {worksheet.title}")
    return rows_processed


def main():
    """Main function to process Excel file and generate SQL file."""
    setup_logging()
    start_time = time.time()

    config = ExcelToSQLConfig()
    input_file_path = validate_and_backup_file(config.INPUT_FILE, config.BACKUP_FILE)

    cprint.info(f"Processing input file: {config.INPUT_FILE}")

    workbook = openpyxl.load_workbook(filename=config.INPUT_FILE, read_only=True)
    sql_generator = SQLGenerator(config.OUTPUT_FILE)

    for worksheet in workbook.worksheets:
        process_worksheet_data(worksheet, sql_generator)

    sql_generator.write_to_file()

    execution_time = time.time() - start_time
    cprint.ok("File processing completed")
    cprint.info(f"Execution time: {execution_time:.2f} seconds")


if __name__ == "__main__":
    main()
