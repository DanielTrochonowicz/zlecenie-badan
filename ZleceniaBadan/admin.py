from django.contrib import admin

# Register your models here.

from .models import ZleceniaBadan, DodatkoweBadania


@admin.register(ZleceniaBadan)
class ZleceniaBadan(admin.ModelAdmin):
    # fields = ('nazwisko', 'badanie')
    list_display = ('imię', 'nazwisko', 'badanie', 'opis', 'wynik', 'termin')
    list_filter = ('imię', 'nazwisko', 'badanie')
    search_fields = ('wynik', 'opis')

admin.site.register(DodatkoweBadania)

