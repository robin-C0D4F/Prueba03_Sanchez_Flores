from django.shortcuts import render
from django.http import HttpResponse
from app_gestion.models import Vacunado

# Create your views here.

def paginaprincipal(request):
    return render(request,"paginaprincipal.html")

def ingresar(request):
    return render(request,"ingresar.html")

def listar(request):
    return render(request,"listar.html")

def buscar1(request):
    return render(request,"buscar1.html")

def buscar(request):
    return render(request,"buscar.html")

def ingreso_vacunado(request):
    rut_aux = request.GET["txt_rut"]
    nombre_aux = request.GET["txt_nombre"]
    appaterno_aux = request.GET["txt_appaterno"]
    apmaterno_aux = request.GET["txt_apmaterno"]
    edad_aux = request.GET["txt_edad"]
    nom_vacuna_aux = request.GET["txt_nom_vacuna"]
    fecha_aux = request.GET["txt_fecha"]

    if len(rut_aux)>0 and len(nombre_aux)>0 and len(appaterno_aux)>0 and len(apmaterno_aux)>0 and len(edad_aux)>0 and len(nom_vacuna_aux)>0 and len(fecha_aux)>0:
        pro = Vacunado(rut=rut_aux,nombre=nombre_aux,appaterno=appaterno_aux,apmaterno=apmaterno_aux,edad=edad_aux,nom_vacuna=nom_vacuna_aux,fecha=fecha_aux)
        pro.save()
        mensaje = "vacunado ingresado"
        return HttpResponse(mensaje)
    else:
        mensaje = "Debe ingresar todos los datos"
    return HttpResponse(mensaje+"<a href='/paginaprincipal/'>Volver al inicio</a>")

def buscar_vacunado(request):
    if request.GET["txt_vacunado"]:
        vacunado = request.GET["txt_vacunado"]
        personas = Vacunado.objects.filter(rut__icontains=vacunado)
        return render(request,"buscar1.html",{"Vacunados":personas,"query":vacunado})
    else:
        mensaje = "Debe ingresar un nombre valido"
        return HttpResponse(mensaje+"<br><button type='button' class='btn btn-primary'><a href='/paginaprincipal/'>Volver al inicio</a></button>")

def listar_vacunado(request):
    datos = Vacunado.objects.all()
    return render(request,"listar.html",{'vacunados':datos})
