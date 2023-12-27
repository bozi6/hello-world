from django.http import HttpResponse
from django.template import loader

from .models import Aut


# Create your views here.
def aut(request):
    """
    Kezdőoldal betöltése a first.html a templates mappában
    """
    template = loader.get_template("first.html")
    evek = Aut.objects.raw(
        "SELECT sorsz_id, YEAR(datum), count(*) as db FROM aut WHERE tev='előadás' GROUP BY YEAR(datum)"
    )
    # print(evek.query)
    # print(dir(evek))
    # print(evek.model)
    context = {
        "hol": 1,
        "evek": evek,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse(template.render())


def mindenki(request):
    """mindenki betöltése a mindeki.html a templateban
    és hozzáadjuk a mind változót a lekérdezésből."""
    mind = Aut.objects.all().order_by("-datum").filter(tev__exact="előadás").values()
    evek = Aut.objects.raw("SELECT sorsz_id, YEAR(datum) FROM aut GROUP BY YEAR(datum)")
    template = loader.get_template("mindenki.html")
    context = {"mindenki": mind, "hol": 2, "evek": evek, "esetszam": mind.count}
    return HttpResponse(template.render(context, request))


def reszletek(request, azonosito):
    egybuli = Aut.objects.get(sorsz_id=azonosito)
    template = loader.get_template("reszletek.html")
    evek = Aut.objects.raw("SELECT sorsz_id, YEAR(datum) FROM aut GROUP BY YEAR(datum)")
    context = {
        "valami": egybuli,
        "hol": 3,
        "evek": evek,
    }
    return HttpResponse(template.render(context, request))


def eveslista(request, evszam):
    template = loader.get_template("eveslista.html")
    evesbuli = Aut.objects.filter(datum__year=evszam).filter(tev__exact="előadás")
    evek = Aut.objects.raw("SELECT sorsz_id, YEAR(datum) FROM aut GROUP BY YEAR(datum)")
    context = {
        "ev": evszam,
        "bulik": evesbuli,
        "evek": evek,
        "hol": 4,
        "osszesen": evesbuli.count,
    }
    return HttpResponse(template.render(context))
