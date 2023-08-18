from django.db import models

class Discografia(models.Model):
    nombre = models.CharField(max_length=50)
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Integrante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Fecha(models.Model):
    lugar = models.CharField(max_length=50)
    dia_mes = models.DateField(max_length=50)
    

    def __str__(self):
        return f"{self.lugar}, {self.dia_mes}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email= models.EmailField()
    mensaje = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.email}, {self.mensaje}"
