# Refactoring eredménye
import os
import time
from pathlib import Path

SEPARATOR_LINE = "-" * 80


def get_directory_size(directory):
    """Kiszámítja egy mappa teljes méretét bájtokban"""
    total_size = 0
    try:
        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(filepath)
                except (OSError, FileNotFoundError):
                    # Némely fájlok nem olvashatóak (pl. szimbolikus linkek)
                    continue
    except (OSError, PermissionError):
        # Ha nincs jogosultság a mappához
        pass
    return total_size


def format_size_human_readable(size_bytes):
    """Formázza a méretet ember által olvasható formátumba"""
    if size_bytes == 0:
        return "0 B"
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0
    size = float(size_bytes)
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


def get_last_access_time(directory):
    """Visszaadja a mappa utolsó hozzáférési idejét"""
    try:
        stat_info = os.stat(directory)
        return time.ctime(stat_info.st_atime)
    except (OSError, FileNotFoundError):
        return "Ismeretlen"


def list_directories(path):
    """Összegyűjti az adott könyvtár mappáit méret és hozzáférési adatokkal"""
    directories = []
    try:
        for item in path.iterdir():
            if item.is_dir():
                size = get_directory_size(item)
                last_access = get_last_access_time(item)
                directories.append((item.name, size, last_access))
    except PermissionError:
        print("Nincs jogosultság a mappák olvasásához!")
    return directories


def print_directories(directories):
    """Rendezve kilistázza a mappákat méret és hozzáférési adatokkal"""
    if not directories:
        print("Nem található mappa az adott mappában.")
        return
    directories.sort(key=lambda x: x[1], reverse=False)
    print(f"{'Mappa neve':<50} {'Méret':<15} {'Utolsó hozzáférés'}")
    print(SEPARATOR_LINE)
    for name, size, last_access in directories:
        formatted_size = format_size_human_readable(size)
        print(f"{name:<100} {formatted_size:<15} {last_access}")
    print(f"\nÖsszesen {len(directories)} mappa található.")


def main():
    containers_path = Path.home() / "Library" / "Containers"
    if not containers_path.exists():
        print(f"A {containers_path} mappa nem található!")
        return
    if not containers_path.is_dir():
        print(f"A {containers_path} nem mappa!")
        return
    print(f"Mappák listázása a {containers_path} mappából:\n")
    print("=" * 80)
    directories = list_directories(containers_path)
    print_directories(directories)


if __name__ == "__main__":
    main()
