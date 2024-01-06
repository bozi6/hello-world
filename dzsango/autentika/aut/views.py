from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q, Count, F
from django.db.models.functions import Left
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.utils.text import slugify

from .forms import AutForm
from .models import Aut


# Create your views here
def evek():
    # evszamok = Aut.objects.raw(
    #     "SELECT sorsz, YEAR(datum), count(*) as db FROM aut WHERE tev='előadás' GROUP BY YEAR(datum)"
    # )
    evszamok = (
        Aut.objects.filter(tev__exact="előadás")
        .annotate(db=Left("datum", 4))
        .values("db")
        .annotate(cnt_evek=Count("sorsz"))
        .order_by("db")
    )
    return evszamok


def muskezdbet():
    # object_list = Aut.objects.raw(
    #    "SELECT sorsz, LEFT(musor,1) AS abc FROM aut GROUP BY abc;"
    # )
    # object_list = (
    #     Aut.objects.all().annotate(kezdobetu=Left("musor", 1)).order_by()
    # )
    object_list = (
        Aut.objects.filter(tev__exact="előadás")
        .annotate(buli=Left("musor", 1))
        .values("buli")
        .annotate(cnt_musor=Count("sorsz"))
        .order_by("buli")
    )
    return object_list


def index(request):
    """
    Kezdőoldal betöltése a first.html a templates mappában
    """
    template = loader.get_template("first.html")
    context = {
        "hol": 1,
        "evek": evek(),
        "kb": muskezdbet(),
    }
    return HttpResponse(template.render(context, request))


def mindenki(request):
    """mindenki betöltése a mindeki.html a templateban
    és hozzáadjuk a mind változót a lekérdezésből."""
    mind = Aut.objects.all().order_by("-datum").filter(tev__exact="előadás").values()
    paginator = Paginator(mind, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    template = loader.get_template("mindenki.html")
    context = {
        # "mindenki": mind,
        "hol": 2,
        "evek": evek(),
        "esetszam": mind.count,
        "kb": muskezdbet(),
        "page_obj": page_obj,
    }
    return HttpResponse(template.render(context, request))


def reszletek(request, azonosito):
    egybuli = Aut.objects.get(sorsz=azonosito)
    template = loader.get_template("reszletek.html")
    context = {
        "valami": egybuli,
        "hol": 3,
        "evek": evek(),
        "kb": muskezdbet(),
    }
    return HttpResponse(template.render(context, request))


def eveslista(request, evszam):
    """Egyben ez a first/<évszám> kezellője is!"""
    template = loader.get_template("eveslista.html")
    evesbuli = Aut.objects.filter(datum__year=evszam).filter(tev__exact="előadás")
    context = {
        "ev": evszam,
        "bulik": evesbuli,
        "evek": evek(),
        "hol": 4,
        "osszesen": evesbuli.count,
        "kb": muskezdbet(),
    }
    return HttpResponse(template.render(context))


def get_queryset(request):
    template = loader.get_template("search_results.html")

    query = request.GET.get("q")
    object_list = Aut.objects.filter(
        Q(musor__icontains=query) | Q(hely__icontains=query), Q(tev__exact="Előadás")
    ).order_by("datum")
    context = {
        "evek": evek(),
        "object_list": object_list,
        "elemsz": object_list.count(),
        "hol": 5,
        "kb": muskezdbet(),
    }
    return HttpResponse(template.render(context, request))


def get_kezdobetu(request, buli):
    """Ha egy karaktert adtunk meg a kezdobetű után
    akkor az ilyen betűvel kezdődőelket írjuk ki."""
    template = loader.get_template("muskezdbet.html")
    object_list = (
        Aut.objects.filter(musor__istartswith=buli)
        .filter(tev__exact="előadás")
        .order_by("musor")
    )
    context = {
        "evek": evek(),
        "hol": 9,
        "kb": muskezdbet(),
        "kezdbet": buli,
        "bulik": object_list,
        "bdb": object_list.count(),
    }
    return HttpResponse(template.render(context, request))


def get_musordb(request):
    object_list = (
        Aut.objects.alias(db=Count("musor"))
        .values("musor")
        .annotate(db=F("db"))
        .filter(tev__exact="előadás")
        .order_by("-db", "musor")
    )
    # print(object_list.query)
    template = loader.get_template("musordb.html")
    context = {
        "evek": evek(),
        "hol": 6,
        "musdb": object_list,
        "kb": muskezdbet(),
    }
    return HttpResponse(template.render(context, request))


def get_osszmus(request, musornev):
    template = loader.get_template("osszmus.html")
    object_list = (
        Aut.objects.all().filter(musor__exact=musornev).filter(tev__exact="előadás")
    )
    musor = Aut.objects.filter(musor__exact=musornev).filter(tev__exact="előadás")
    context = {
        "object_list": object_list,
        "hol": 7,
        "musdb": object_list.count(),
        "musor": musor,
        "kb": muskezdbet(),
    }
    return HttpResponse(template.render(context, request))


def szerkesztes(request, sorszam, template_name="szerkesztes.html"):
    szerkesztendo = get_object_or_404(Aut, pk=sorszam)
    form = AutForm(request.POST or None, instance=szerkesztendo)
    rendered_form = form.render("form_sablon.html")
    if form.is_valid():
        szerkesztendo.bevitel_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        szerkesztendo.slug = slugify(
            f"{datetime.now().strftime('%Y-%m-%d')}-{szerkesztendo.musor}"
        )
        form.save()
        return redirect("szerkesztes", sorszam)
    context = {
        "form": rendered_form,
        "hol": 8,
        "evek": evek(),
        "kb": muskezdbet(),
    }
    return render(request, template_name, context)


def mindenmas(request):
    """mindenki ami nem előadás betöltése a mindeki.html a templateban
    és hozzáadjuk a mind változót a lekérdezésből."""
    mind = (
        Aut.objects.all()
        .order_by("-datum")
        .exclude(tev__exact="előadás")
        .order_by("tev", "datum")
        .values()
    )
    paginator = Paginator(mind, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    template = loader.get_template("mindenki.html")
    context = {
        "hol": 2,
        "evek": evek(),
        "esetszam": mind.count,
        "kb": muskezdbet(),
        "m": 1,
        "page_obj": page_obj,
    }
    return HttpResponse(template.render(context, request))


def teszting(request):
    object_list = (
        Aut.objects.alias(db=Count("hely"))
        .values("hely")
        .annotate(db=F("db"))
        .annotate(musor=F("hely"))
        .filter(tev__exact="előadás")
        .order_by("-db", "hely")
    )

    # print(object_list.query)
    template = loader.get_template("musordb.html")
    context = {
        "evek": evek(),
        "hol": 6,
        "musdb": object_list,
        "kb": muskezdbet(),
    }
    return HttpResponse(template.render(context, request))
