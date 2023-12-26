#  urls.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 23. 12:52
from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("members/", views.members, name="members"),
    path("members/details/<slug:slug>", views.details, name="details"),
    path("testing/", views.testing, name="testing"),
]
