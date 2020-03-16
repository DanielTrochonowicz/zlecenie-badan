from django.db import models

# Create your models here.

class Placowka(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Placowka"
        verbose_name_plural = "Placowki"

class Termin(models.Model):
    def __str__(self):
        return self.realizacja
    realizacja = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Termin"
        verbose_name_plural = "Terminy"

class DodatkoweBadania(models.Model):
    def __str__(self):
        return self.edycja
    edycja = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Dodatkowe Badanie"
        verbose_name_plural = "Dodatkowe Badania"

class Imię(models.Model):
    def __str__(self):
        return self.imię
    imię = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Imię"
        verbose_name_plural = "Imiona"

class Nazwisko(models.Model):
    def __str__(self):
        return self.nazwisko
    nazwisko = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Nazwisko"
        verbose_name_plural = "Nazwiska"

class WynikiBadań(models.Model):
    def __str__(self):
        return self.wynik
    wynik = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Wynik"
        verbose_name_plural = "Wyniki"


class ZleceniaBadan(models.Model):

    def __str__(self):
        return self.badanie

    imię = models.ForeignKey(Imię, on_delete=models.CASCADE, null=True, blank=True)
    nazwisko = models.ForeignKey(Nazwisko, on_delete=models.CASCADE, null=True, blank=True)
    badanie = models.CharField(max_length=100)
    dodatkowe_badania = models.ForeignKey(DodatkoweBadania, on_delete=models.CASCADE, null=True, blank=True)
    termin = models.ForeignKey(Termin, on_delete=models.CASCADE, null=True, blank=True)
    opis = models.TextField(blank=True)
    wynik = models.TextField(blank=True)
    placówka = models.ForeignKey(Placowka, on_delete=models.CASCADE, null=True)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    data_wystawienia = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Zlecenie Badania"
        verbose_name_plural = "Zlecenie Badań"

