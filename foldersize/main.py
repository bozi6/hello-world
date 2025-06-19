#  main.py Copyright (C) 2025  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2025. 06. 19. 14:30

import os
import time
from pathlib import Path


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


def format_size(size_bytes):
    """Formázza a méretet olvasható formátumba"""
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

    directories = []

    # Csak a mappákat gyűjtjük össze
    try:
        for item in containers_path.iterdir():
            if item.is_dir():
                size = get_directory_size(item)
                last_access = get_last_access_time(item)
                directories.append((item.name, size, last_access))
    except PermissionError:
        print("Nincs jogosultság a Containers mappa olvasásához!")
        return

    if not directories:
        print("Nem található mappa a Containers mappában.")
        return

    # Méret szerint sorbarendezés (csökkenő sorrendben)
    # Itt a reverse True = Elöl van a legnagyobb méretű,
    # ha False akkor a list végén lesz a legnagyobb méretű mappa.
    directories.sort(key=lambda x: x[1], reverse=False)

    # Kilistázás
    print(f"{'Mappa neve':<50} {'Méret':<15} {'Utolsó hozzáférés'}")
    print("-" * 80)

    for name, size, last_access in directories:
        formatted_size = format_size(size)
        print(f"{name:<100} {formatted_size:<15} {last_access}")

    print(f"\nÖsszesen {len(directories)} mappa található.")


if __name__ == "__main__":
    main()
