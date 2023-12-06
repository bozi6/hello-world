import os
import hashlib
from pathlib import Path

def main():
    file_path = './'
    list_of_files = os.walk(file_path)
    unique_files = dict()
    for root, folders, files in list_of_files:
        for file in files:
            file_path = Path(os.path.join(root, file))
            Hash_file = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
            if Hash_file not in unique_files:
                unique_files[Hash_file] = file_path
            else:
                print('egyezés: ', ' - ', file_path, ' ezzel:', unique_files[Hash_file])
                os.remove(file_path)
                print(f"{file_path} törölve lett.")
    print('Kész is vogymuk.')


if __name__ == "__main__":
    main()

