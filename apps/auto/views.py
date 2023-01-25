from django.shortcuts import render, redirect
from apps.auto.models import Auto


def home(request):
    lista_autos = Auto.objects.all()
    context = {
        'autos': lista_autos,
        'actualiza':None
    }
    return render(request, 'auto/auto_admin.html', context)

def prueba():
    print("hola")