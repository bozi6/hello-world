import hashlib
import os
from pathlib import Path

# Constants
BASE_DIRECTORY = "./"


def calculate_file_hash(file_path):
    """
    Calculate the MD5 hash of a given file.

    :param file_path: Path to the file
    :return: MD5 hash as a string
    """
    with open(file_path, "rb") as file:
        return hashlib.md5(file.read()).hexdigest()


def delete_duplicate_files(base_path):
    """
    Identify and delete files with duplicate MD5 hashes in a directory.

    :param base_path: Path to the base directory to scan
    """
    unique_files = {}
    for root, _, files in os.walk(base_path):
        for file in files:
            file_path = Path(root) / file
            file_hash = calculate_file_hash(file_path)

            if file_hash not in unique_files:
                unique_files[file_hash] = file_path
            else:
                print(f"Duplicate found: {file_path} - Original: {unique_files[file_hash]}")
                os.remove(file_path)
                print(f"{file_path} has been deleted.")
    print("Process completed.")


def main():
    """
    Main program to delete duplicate files based on MD5 hash values in a given directory.
    """
    delete_duplicate_files(BASE_DIRECTORY)


if __name__ == "__main__":
    main()
