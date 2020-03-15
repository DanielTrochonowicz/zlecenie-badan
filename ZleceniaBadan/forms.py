from django.forms import ModelForm
from .models import ZleceniaBadan

class ZlecenieForm(ModelForm):
    class Meta:
        model = ZleceniaBadan
        fields = ['imię', 'nazwisko', 'badanie', 'dodatkowe_badania', 'termin', 'opis', 'wynik', 'placówka', 'cena', 'data_wystawienia']