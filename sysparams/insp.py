#  insp.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 05. 26. 0:26
import os
from inspect import getmembers

for name, data in getmembers(os):
    if name == "__builtins__":
        continue
    print(f"{name}: {repr(data)}")
