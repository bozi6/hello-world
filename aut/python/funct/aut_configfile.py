#  aut_configfile.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 19. 22:40
SQLDEFAULT = """-- Honvédelmi adatok 2023-ra az autentikusból.
-- Készítette: Konta Boáz (kontab6@gmail.com)
-- Select current database
USE honved2;
-- Increase max allowed packets to 500MB from 1MB
SET GLOBAL max_allowed_packet=524288000;
DELETE FROM aut WHERE datum >= '2023-01-01';
    """

TANCNEV = ["Tánckar", "tánckar", "TÁNCKAR (és Zenekar)"]
FERFIKARNEVEK = ["FÉRFIKAR", "Férfikar"]
