#  urls.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 24. 20:36
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="aut"),
    path("mindenki", views.mindenki, name="mindenki"),
    path("mindenki/nembuli", views.mindenmas, name="mindenki"),
    path("reszletek/<int:azonosito>", views.reszletek, name="reszletek"),
    # path("reszletek/<slug:slug>", views.reszletek, name="reszletek"),
    path("first/<int:evszam>", views.eveslista, name="eveslista"),
    path("kezdobetu/<str:buli>", views.get_kezdobetu, name="kezdobetu"),
    path("keres/", views.get_queryset, name="search_results"),
    path("musordb", views.get_musordb, name="musordb"),
    path("first/<str:musornev>", views.get_osszmus, name="osszmus"),
    path("osszmus/<str:musornev>", views.get_osszmus, name="osszmus"),
    path("szerkesztes/<int:sorszam>", views.szerkesztes, name="szerkesztes"),
    path("teszting/", views.teszting, name="teszt"),
]
