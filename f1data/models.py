from django.db import models

class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.CharField(max_length=50)
    puntos = models.IntegerField()
    
    class Meta:
        app_label = 'f1data'

class Circuito(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    longitud = models.FloatField()

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)