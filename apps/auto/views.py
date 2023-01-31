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

def actualizar_form(request, id_auto):
    lista_autos = Auto.objects.all() # de obtener toda la informacion de la tabla
    auto_data = Auto.objects.get(idpbv=id_auto)
    context = {
        'autos': lista_autos,
        'actualiza':auto_data
    }
    return render(request, 'auto/auto_admin.html', context)

def actualizar(request):
    a_id_a = request.POST['idAuto']
    a_marca_a = request.POST['marca']
    a_modelo_a = request.POST['modelo']
    a_cc_a = request.POST['cc']
    a_des_a = request.POST['descripcion']

    act_auto = Auto.objects.get(idpbv=a_id_a)

    act_auto.marca = a_marca_a
    act_auto.modelo = a_modelo_a
    act_auto.cc = a_cc_a
    act_auto.especificaciones = a_des_a
    act_auto.save()
    return redirect('auto:index')