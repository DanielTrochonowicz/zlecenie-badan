
from django.urls import path
from .views import zlecenia_badan, nowe_zlecenie, edytuj_zlecenie, usun_zlecenie

urlpatterns = [
    path('zlecenia/', zlecenia_badan, name='zlecenia_badan'),
    path('nowy/', nowe_zlecenie, name='nowe_zlecenie'),
    path('edytuj/<int:id>/', edytuj_zlecenie, name='edytuj_zlecenie'),
    path('usun/<int:id>/', usun_zlecenie, name='usun_zlecenie'),
]
