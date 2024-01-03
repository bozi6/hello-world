#  forms.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 30. 23:12
from django import forms
from django.forms import formset_factory
from .models import Aut
from django.utils.text import slugify


class AutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """

        Az adatbázisból jövő mezőket frissíti a form megjelenítéshez
        textarea méret meg ilyenek

        """
        super().__init__(*args, **kwargs)
        self.fields["datum"].widget.attrs.update({"class": "form-control"})
        self.fields["ceg"].widget.attrs.update({"class": "form-control"})
        self.fields["kezd"].widget.attrs.update({"class": "form-control"})
        self.fields["hely"].widget.attrs.update({"class": "form-control"})
        self.fields["helykod"].widget.attrs.update({"class": "form-control"})
        self.fields["musor"].widget.attrs.update({"class": "form-control"})
        self.fields["tev"].widget.attrs.update({"class": "form-control"})
        self.fields["honv"].widget.attrs.update({"class": "form-control"})
        self.fields["kulsos"].widget.attrs.update({"class": "form-control"})
        self.fields["megjegyzes"].widget.attrs.update({"class": "form-control"})
        self.fields["kontakt"].widget.attrs.update({"class": "form-control"})
        self.fields["muszak"].widget.attrs.update({"class": "form-control"})
        self.fields["jelmezt"].widget.attrs.update({"class": "form-control"})
        self.fields["szallitas"].widget.attrs.update({"class": "form-control"})
        self.fields["kiallas"].widget.attrs.update({"class": "form-control"})
        self.fields["felelos"].widget.attrs.update({"class": "form-control"})
        self.fields["alkjell"].widget.attrs.update({"class": "form-control"})
        self.fields["bevitel_time"].widget.attrs.update({"class": "form-control"})
        self.fields["slug"].widget.attrs.update({"class": "form-control"})
        self.fields["hely"].widget.attrs.update(rows="2")
        self.fields["honv"].widget.attrs.update(rows="2")
        self.fields["megjegyzes"].widget.attrs.update(cols="32", rows="2")

    class Meta:
        model = Aut
        fields = "__all__"
        localized_fields = "__all__"
        labels = {
            "datum": "Dátum",
            "ceg": "Cég kódja",
            "kezd": "Kezdési időpont",
            "HM": "Honvédségi rendezvény",
            "hely": "Előadás helyszíne",
            "helykod": "Előadás helyszín kódja",
            "musor": "Előadás neve",
            "tev": "Tevékenység",
            "honv": "Honvédos résztvevő(k)",
            "kulsos": "Külsős résztvevő(k)",
            "megjegyzes": "Megjegyzés",
            "kontakt": "Kapcsolattartó",
            "muszak": "Műszak részéről",
            "jelmezt": "Jelmeztár részéről",
            "szallitas": "Szállítás részéről",
            "kiallas": "Indulási időpont",
            "felelos": "Esemény felelős",
            "alkjell": "Alkalom jellege",
            "bevitel_time": "Rögzítés dátuma",
            "slug": "Barátságos név",
        }

    """

    datum = forms.DateField()
    ceg = forms.CharField(max_length=127)
    kezd = forms.CharField(max_length=127)
    HM = forms.BooleanField(required=False)
    hely = forms.Textarea()
    helykod = forms.IntegerField()
    musor = forms.CharField(max_length=200)
    tev = forms.CharField(max_length=127)
    honv = forms.Textarea()
    kulsos = forms.CharField(max_length=254)
    megjegyzes = forms.Textarea()
    kontakt = forms.CharField(max_length=254)
    muszak = forms.CharField(max_length=254)
    jelmezt = forms.CharField(max_length=254)
    szallitas = forms.CharField(max_length=254)
    kiallas = forms.CharField(max_length=254)
    felelos = forms.CharField(max_length=254)
    alkjell = forms.CharField(max_length=254)
    bevitel_time = forms.DateTimeField()
    slug = forms.SlugField(max_length=50)
"""
