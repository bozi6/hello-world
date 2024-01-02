#  urls.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 01. 01. 12:35
from django.urls import path
from . import views

urlpatterns = [
    path("contacts/", views.IndexView.as_view(), name="index"),
    path("contacts/<int:pk>/", views.ContactDetailView.as_view(), name="detail"),
    path("contacts/edit/<int:pk>/", views.edit, name="edit"),
    path("contacts/create/", views.create, name="create"),
    path("contacts/delete/<int:pk>/", views.delete, name="delete"),
]
