#  models.py Copyright (C) 2023  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2023. 12. 24. 20:26

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime


class Amk(models.Model):
    buli_id = models.PositiveSmallIntegerField(db_comment="buli azonosító")
    musz_id = models.SmallIntegerField(db_comment="muszak azonosító")

    def __str__(self):
        return f"{self.buli_id} - {self.musz_id}"

    class Meta:
        managed = False
        db_table = "amk"
        verbose_name_plural = "amk-k"


class Helyszinek(models.Model):
    sorsz_helyid = models.SmallAutoField(primary_key=True, db_comment="helyek sorszáma")
    hely = models.CharField(
        max_length=255,
        db_collation="utf8mb3_hungarian_ci",
        db_comment="helyszín megnevezése",
    )
    kord = models.CharField(max_length=39)

    def __str__(self):
        return f"{self.hely} - {self.sorsz}"

    class Meta:
        managed = False
        db_table = "helyszinek"
        db_table_comment = "Helyszínek adatai"
        ordering = ["hely"]
        verbose_name_plural = "helyszinek"


class Aut(models.Model):
    sorsz = models.SmallAutoField(primary_key=True, db_comment="sorszám")
    datum = models.DateField(db_comment="datum", blank=False, null=False)
    ceg = models.CharField(max_length=127, db_comment="szervezo ceg", default=24)
    kezd = models.CharField(
        max_length=127,
        db_comment="kezdés ideje",
        default="Nincs megadva kezdés.",
        blank=True,
        null=True,
    )
    HM = models.BooleanField(db_comment="HM-esrendezvény")
    hely = models.TextField(db_comment="helyszín", blank=False)
    helykod = models.SmallIntegerField(
        db_comment="Helyszín kódja a helyszínek táblában.", default=995
    )
    # helykod = models.ForeignKey(Helyszinek, db_column=hely, on_delete=models.CASCADE)
    musor = models.CharField(max_length=200, db_comment="előadás neve", null=False)
    tev = models.CharField(max_length=127, db_comment="tevékenység", default="előadás")
    honv = models.TextField(blank=True, null=True)
    kulsos = models.CharField(
        max_length=254,
        db_comment="Külsős résztvevő",
        null=True,
        blank=True,
    )
    megjegyzes = models.TextField(blank=True, null=True, db_comment="megjegyzes")
    kontakt = models.CharField(
        max_length=254, blank=True, null=True, db_comment="kontakt"
    )
    muszak = models.CharField(
        max_length=254, blank=True, null=True, db_comment="muszak"
    )
    jelmezt = models.CharField(
        max_length=254, blank=True, null=True, db_comment="jelmeztár"
    )
    szallitas = models.CharField(
        max_length=254, blank=True, null=True, db_comment="szallitas"
    )
    kiallas = models.CharField(
        max_length=254, blank=True, null=True, db_comment="kiállás"
    )
    felelos = models.CharField(
        max_length=127, blank=True, null=True, db_comment="felelős"
    )
    alkjell = models.CharField(
        max_length=127, blank=True, null=True, db_comment="alkalom jellege"
    )
    bevitel_time = models.DateTimeField(
        db_comment="Adatbevitel ideje.", default=datetime.now(), null=True, blank=True
    )
    slug = models.SlugField(default="", null=True, blank=True)

    def __str__(self):
        return f"{self.datum} - {self.musor} - {self.hely}"

    class Meta:
        managed = False
        db_table = "aut"
        db_table_comment = "autentikus főtábla"
        indexes = [
            models.Index(
                fields=[
                    "datum",
                ]
            ),
        ]
        verbose_name_plural = "autentikus"


class Ceglista(models.Model):
    sorsz = models.AutoField(primary_key=True)
    cegnev = models.CharField(max_length=127)
    megjegy = models.CharField(max_length=256)
    weboldal = models.CharField(max_length=254, db_comment="weboldal")

    def __str__(self):
        return f"{self.sorsz} - {self.cegnev}"

    class Meta:
        managed = False
        db_table = "ceglista"


class Headatok(models.Model):
    sorsz = models.AutoField(primary_key=True)
    nev = models.CharField(max_length=127, db_comment="név")
    beosztas = models.CharField(max_length=127)
    munkkezd = models.DateField(db_comment="Munkaviszony kezdete")
    szuldat = models.DateField(db_comment="Születési dátum")
    szulhely = models.CharField(max_length=127, db_comment="Születési hely")
    allampolg = models.CharField(max_length=127, db_comment="Állampolgársága")
    utlevszam = models.CharField(max_length=127, db_comment="Útlevélszáma")
    utleverv = models.DateField(db_comment="Útlevél érvényessége")
    szigszam = models.CharField(max_length=10, db_comment="Személyi igazolvány szám")
    szigerv = models.DateField(db_comment="Személyi érvényessége")
    eutaj = models.CharField(max_length=32, db_comment="EU-s taj kártyaszám")
    eutajerv = models.DateField(db_comment="EU-s taj érvényesség")
    cim = models.CharField(max_length=127, db_comment="Lakcím")
    anyanev = models.CharField(max_length=127, db_comment="Anyja neve")
    tajsz = models.CharField(
        db_column="TAJsz", max_length=16, db_comment="TAJ száma"
    )  # Field name made lowercase.
    adojel = models.CharField(max_length=32, db_comment="Adóazonosító jel")
    kar = models.CharField(max_length=40, db_comment="Melyik karnál dolgozik")
    aktiv = models.IntegerField(db_comment="Aktív tagja e az állománynak")

    def __str__(self):
        return f"{self.nev} - {self.cim} - {self.szuldat}"

    class Meta:
        managed = False
        db_table = "headatok"
        db_table_comment = "Dolgozók adatai"


class Karok(models.Model):
    sorsz = models.SmallAutoField(primary_key=True, db_comment="tábla sorszáma")
    kar = models.CharField(max_length=255, db_comment="Kar megnevezése")

    def __str__(self):
        return f"{self.sorsz} - {self.kar}"

    class Meta:
        managed = False
        db_table = "karok"
        db_table_comment = "Karok és kódok illesztőtabella"


class Muszak(models.Model):
    sorszam = models.SmallAutoField(primary_key=True)
    nev = models.CharField(max_length=127)
    fullname = models.CharField(max_length=127)
    telszam = models.CharField(max_length=16)
    beosztas = models.CharField(max_length=128)
    aktiv = models.IntegerField(db_comment="Itt dolgozike még az illető")

    def __str__(self):
        return f"{self.sorszam} - {self.nev} - {self.aktiv}"

    class Meta:
        managed = False
        db_table = "muszak"
        db_table_comment = "muszak"
