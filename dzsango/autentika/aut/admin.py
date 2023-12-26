from django.contrib import admin
from .models import Aut, Muszak, Amk, Karok, Headatok, Helyszinek, Ceglista


class AutAdmin(admin.ModelAdmin):
    list_display = ("sorsz", "musor", "datum")


# Register your models here.
admin.site.register(Aut, AutAdmin)
admin.site.register(Muszak)
admin.site.register(Amk)
admin.site.register(Karok)
admin.site.register(Headatok)
admin.site.register(Helyszinek)
admin.site.register(Ceglista)
