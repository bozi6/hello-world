from django.contrib import admin
from .models import Aut, Muszak, Helyszinek, Ceglista


class AutAdmin(admin.ModelAdmin):
    list_display = ("sorsz", "musor", "datum")
    # prepopulated_fields = {"slug": ["musor", "datum"]}


# Register your models here.
admin.site.register(Aut, AutAdmin)
admin.site.register(Muszak)
admin.site.register(Helyszinek)
admin.site.register(Ceglista)
