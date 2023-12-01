# read_shopping_list.py

from pathlib import Path  # A Pathlib importálása

path = Path.cwd() / "shopping_list.md"
"""  Az aktuális munkakönyvtár megadása (cwd)
    És az olvasandó fájl hozzáadása:
    shopping_list.md
"""
with path.open(mode="r", encoding="utf-8") as md_file:
    """A path.open a beépített opent hívja meg
    Ezért lehet használni az olvasási
    és az enkódolási módokat.
    """
    content = md_file.read()
    groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))
