# Generated by Django 5.0 on 2023-12-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Amk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "buli_id",
                    models.PositiveSmallIntegerField(db_comment="buli azonosító"),
                ),
                ("musz_id", models.SmallIntegerField(db_comment="muszak azonosító")),
            ],
            options={
                "verbose_name_plural": "amk-k",
                "db_table": "amk",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Aut",
            fields=[
                (
                    "sorsz",
                    models.SmallAutoField(
                        db_comment="sorszám", primary_key=True, serialize=False
                    ),
                ),
                ("datum", models.DateField(db_comment="datum")),
                ("ceg", models.CharField(db_comment="szervezo ceg", max_length=127)),
                ("kezd", models.CharField(db_comment="kezdés ideje", max_length=127)),
                ("hely", models.TextField(db_comment="helyszín")),
                (
                    "helykod",
                    models.SmallIntegerField(
                        db_comment="Helyszín kódja a helyszínek táblában."
                    ),
                ),
                ("musor", models.CharField(db_comment="előadás neve", max_length=200)),
                ("tev", models.CharField(db_comment="tevékenység", max_length=127)),
                (
                    "honv",
                    models.TextField(
                        blank=True, db_comment="közremukodok honvedos", null=True
                    ),
                ),
                (
                    "kulsos",
                    models.CharField(db_comment="Külsős résztvevő", max_length=254),
                ),
                (
                    "megjegyzes",
                    models.TextField(blank=True, db_comment="megjegyzes", null=True),
                ),
                (
                    "kontakt",
                    models.CharField(
                        blank=True, db_comment="kontakt", max_length=254, null=True
                    ),
                ),
                (
                    "muszak",
                    models.CharField(
                        blank=True, db_comment="muszak", max_length=254, null=True
                    ),
                ),
                (
                    "jelmezt",
                    models.CharField(
                        blank=True, db_comment="jelmeztár", max_length=254, null=True
                    ),
                ),
                (
                    "szallitas",
                    models.CharField(
                        blank=True, db_comment="szallitas", max_length=254, null=True
                    ),
                ),
                (
                    "kiallas",
                    models.CharField(
                        blank=True, db_comment="kiállás", max_length=254, null=True
                    ),
                ),
                (
                    "felelos",
                    models.CharField(
                        blank=True, db_comment="felelős", max_length=127, null=True
                    ),
                ),
                (
                    "alkjell",
                    models.CharField(
                        blank=True,
                        db_comment="alkalom jellege",
                        max_length=127,
                        null=True,
                    ),
                ),
                ("bevitel_time", models.DateTimeField(db_comment="Adatbevitel ideje.")),
            ],
            options={
                "verbose_name_plural": "autentikus",
                "db_table": "aut",
                "db_table_comment": "autentikus főtábla",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Ceglista",
            fields=[
                ("sorsz", models.AutoField(primary_key=True, serialize=False)),
                ("cegnev", models.CharField(max_length=127)),
                ("megjegy", models.CharField(max_length=256)),
                ("weboldal", models.CharField(db_comment="weboldal", max_length=254)),
            ],
            options={
                "db_table": "ceglista",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Headatok",
            fields=[
                ("sorsz", models.AutoField(primary_key=True, serialize=False)),
                ("nev", models.CharField(db_comment="név", max_length=127)),
                ("beosztas", models.CharField(max_length=127)),
                ("munkkezd", models.DateField(db_comment="Munkaviszony kezdete")),
                ("szuldat", models.DateField(db_comment="Születési dátum")),
                (
                    "szulhely",
                    models.CharField(db_comment="Születési hely", max_length=127),
                ),
                (
                    "allampolg",
                    models.CharField(db_comment="Állampolgársága", max_length=127),
                ),
                (
                    "utlevszam",
                    models.CharField(db_comment="Útlevélszáma", max_length=127),
                ),
                ("utleverv", models.DateField(db_comment="Útlevél érvényessége")),
                (
                    "szigszam",
                    models.CharField(
                        db_comment="Személyi igazolvány szám", max_length=10
                    ),
                ),
                ("szigerv", models.DateField(db_comment="Személyi érvényessége")),
                (
                    "eutaj",
                    models.CharField(db_comment="EU-s taj kártyaszám", max_length=32),
                ),
                ("eutajerv", models.DateField(db_comment="EU-s taj érvényesség")),
                ("cim", models.CharField(db_comment="Lakcím", max_length=127)),
                ("anyanev", models.CharField(db_comment="Anyja neve", max_length=127)),
                (
                    "tajsz",
                    models.CharField(
                        db_column="TAJsz", db_comment="TAJ száma", max_length=16
                    ),
                ),
                (
                    "adojel",
                    models.CharField(db_comment="Adóazonosító jel", max_length=32),
                ),
                (
                    "kar",
                    models.CharField(
                        db_comment="Melyik karnál dolgozik", max_length=40
                    ),
                ),
                (
                    "aktiv",
                    models.IntegerField(db_comment="Aktív tagja e az állománynak"),
                ),
            ],
            options={
                "db_table": "headatok",
                "db_table_comment": "Dolgozók adatai",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Helyszinek",
            fields=[
                (
                    "sorsz_helyid",
                    models.SmallAutoField(
                        db_comment="helyek sorszáma", primary_key=True, serialize=False
                    ),
                ),
                (
                    "hely",
                    models.CharField(
                        db_collation="utf8mb3_hungarian_ci",
                        db_comment="helyszín megnevezése",
                        max_length=255,
                    ),
                ),
                ("kord", models.CharField(max_length=39)),
            ],
            options={
                "verbose_name_plural": "helyszinek",
                "db_table": "helyszinek",
                "db_table_comment": "Helyszínek adatai",
                "ordering": ["hely"],
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Karok",
            fields=[
                (
                    "sorsz",
                    models.SmallAutoField(
                        db_comment="tábla sorszáma", primary_key=True, serialize=False
                    ),
                ),
                ("kar", models.CharField(db_comment="Kar megnevezése", max_length=255)),
            ],
            options={
                "db_table": "karok",
                "db_table_comment": "Karok és kódok illesztőtabella",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Muszak",
            fields=[
                ("sorszam", models.SmallAutoField(primary_key=True, serialize=False)),
                ("nev", models.CharField(max_length=127)),
                ("fullname", models.CharField(max_length=127)),
                ("telszam", models.CharField(max_length=16)),
                ("beosztas", models.CharField(max_length=128)),
                (
                    "aktiv",
                    models.IntegerField(db_comment="Itt dolgozike még az illető"),
                ),
            ],
            options={
                "db_table": "muszak",
                "db_table_comment": "muszak",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="musordarab",
            fields=[
                ("sorszam", models.SmallAutoField(primary_key=True, serialize=False)),
                ("musor", models.CharField(max_length=127)),
                ("db", models.IntegerField(max_length=6)),
            ],
            options={
                "db_table": "musordarabok",
                "db_table_comment": "Műsorok darabszám szerint",
                "managed": True,
            },
        ),
    ]