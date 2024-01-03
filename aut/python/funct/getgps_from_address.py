#  getgps_from_address.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 27. 17:50
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="autentika application")
sqfile = open("helyszinek_gps.sql", "a")
sql = "INSERT INTO helyszinek (sorsz_helyid, hely, kord) VALUES \n"
sqfile.write(sql)
with open("autcsakhely.csv", mode="r", encoding="utf-8") as f:
    for lines in f:
        sql = "(NULL, '"
        cim = lines.strip()
        location = geolocator.geocode(cim)
        try:
            print(f"Keresett cím: {cim}")
            print(f"Megtalált cím: {location.address}")
            sql += location.address
            sql += "','"
            sql += str(location.latitude)
            sql += ","
            sql += str(location.longitude)
            sql += "'),\n"
            print(f"szélesség: {location.latitude}, hosszúság:{location.longitude}")
            # print(sql)
            sqfile.write(sql)
            sql = ""
            time.sleep(6)
        except AttributeError:
            print("Nem találtam.")
            sqfile.write(f"(NULL, '{cim}',''),\n")
            time.sleep(3)
            pass

sqfile.close()
"""
cim = "Budapest, Somlói út 51."
location = geolocator.geocode(cim)
print(location.address)
print(location.raw)
print(location.latitude)
print(location.longitude)
time.sleep(1)
"""
