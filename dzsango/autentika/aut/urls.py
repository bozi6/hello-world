#  urls.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 24. 20:36
from django.urls import path
from . import views

urlpatterns = [
    path("", views.aut, name="aut"),
    path("mindenki", views.mindenki, name="mindenki"),
    path("reszletek/<int:azonosito>", views.reszletek, name="reszletek"),
    path("first/<int:evszam>", views.eveslista, name="eveslista"),
]
