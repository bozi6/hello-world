import hashlib
import os
from pathlib import Path


def main():
    """
    Main program
    deletes the files with same md5 hash value

    :TODO: order of deleted files do to create order, oldest stay intact.
    :returns: Message files deleted
    """
    file_path = "./"
    list_of_files = os.walk(file_path)
    unique_files = dict()
    for root, folders, files in list_of_files:
        for file in files:
            file_path = Path(os.path.join(root, file))
            Hash_file = hashlib.md5(open(file_path, "rb").read()).hexdigest()
            if Hash_file not in unique_files:
                unique_files[Hash_file] = file_path
            else:
                print("egyezés: ", " - ", file_path, " ezzel:", unique_files[Hash_file])
                os.remove(file_path)
                print(f"{file_path} törölve lett.")
    print("Kész is vogymuk.")


if __name__ == "__main__":
    main()
