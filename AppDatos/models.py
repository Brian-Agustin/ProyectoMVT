from django.db import models
class Datos(models.Model):
    parent = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField()