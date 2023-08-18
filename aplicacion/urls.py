
from django.urls import path, include
from .views import *


urlpatterns = [
   path('', home, name="home"),
   path('discos',discos, name="discos"),
   path('integrantes',integrantes, name="integrantes"),
   path('fechas',fechas, name="fechas"),
   path('contacto',contacto, name="contacto"),
   
   path('discosform2',discosForm2, name="discosform2"),
   
   path('buscardisco',buscarDisco, name="buscardisco"),
   path('buscar2',buscar2, name="buscar2")

   
]