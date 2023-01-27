from django.shortcuts import render, redirect
from apps.auto.models import Auto


def home(request):
    lista_autos = Auto.objects.all()
    context = {
        'autos': lista_autos,
        'actualiza':None
    }
    return render(request, 'auto/auto_admin.html', context)

def insertar_auto(request):
    marca_i = request.POST['marca']
    modelo_i = request.POST['modelo']
    cc_i = request.POST['cc']
    detalle_i = request.POST['descripcion']
    Auto_i = Auto(marca= marca_i, modelo = modelo_i, cc=cc_i, especificaciones=detalle_i)
    Auto_i.save()
    return redirect('auto:index')

def eliminar_auto(request, id_auto):
    Auto_del = Auto.objects.get(idpbv=id_auto)
    Auto_del.delete()
    return redirect('auto:index')