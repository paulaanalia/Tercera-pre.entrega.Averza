from django.shortcuts import render
from .models import Discografia
from .models import Fecha
from .models import Integrante
from .forms import DiscoForms

from django.http import HttpResponse

def home(request):
   return render(request, "aplicacion/home.html") #cuando llegue una solicitud la redirige a la pag

def discos(request):
    contexto = {'discos': Discografia.objects.all()}
    return render(request, "aplicacion/discos.html", contexto)

def integrantes(request):
    contexto = {'integrantes': Integrante.objects.all()}
    return render(request, "aplicacion/integrantes.html", contexto)

def fechas(request):
    contexto = {'fechas': Fecha.objects.all()}
    return render(request, "aplicacion/fechas.html", contexto)

def contacto(request):
    return render(request, "aplicacion/contacto.html")


#Formularios
def discosForm2(request):
    if request.method == "POST":
       miForm = DiscoForms(request.POST)
       if miForm.is_valid():
           disco_nombre = miForm.cleaned_data.get('nombre')
           disco_anio =miForm.cleaned_data.get('anio')
           disco = Discografia(nombre=disco_nombre,
                               anio=disco_anio)
           disco.save()
           return render(request, "aplicacion/base.html")
    
    else:
        miForm = DiscoForms()

    return render(request, "aplicacion/discoForm2.html", {"form": miForm})


def buscarDisco(request):
    return render(request, "aplicacion/buscarDisco.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        discos = Discografia.objects.filter(nombre__icontains=patron)
        contexto ={"discos": discos }
        return render(request, "aplicacion/discos.html", contexto)
    return HttpResponse("No se ingresó una busqueda")