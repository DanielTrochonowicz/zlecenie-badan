from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import ZleceniaBadan
from .forms import ZlecenieForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def zlecenia_badan(request):
    lista_badan = "To jest lista zleconych badań"

    badania = ZleceniaBadan.objects.all()
    return render(request, 'zlecenie_badan.html',
                  {'lista': lista_badan, 'badania': badania})

@login_required(login_url='/login/')
def nowe_zlecenie(request):
    form = ZlecenieForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(zlecenia_badan)
    return  render(request, 'zlecenie_form.html', {'form': form})

@login_required(login_url='/login/')
def edytuj_zlecenie(request, id):
    zlecenie = get_object_or_404(ZleceniaBadan, pk=id)
    form = ZlecenieForm(request.POST or None, instance=zlecenie)

    if form.is_valid():
        form.save()
        return redirect(zlecenia_badan)
    return render(request, 'zlecenie_form.html', {'form': form})

@login_required(login_url='/login/')
def usun_zlecenie(request, id):
    zlecenie = get_object_or_404(ZleceniaBadan, pk=id)

    if request.method == 'POST':
        zlecenie.delete()
        return redirect(zlecenia_badan)
    return render(request, 'potwierdz.html', {'zlecenie': zlecenie})
