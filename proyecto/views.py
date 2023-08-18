from django.shortcuts import render
#from .models import Discografia


def home(request):
    return render(request, "aplicacion/home.html") #cuando llegue una solicitud la redirige a la pag
