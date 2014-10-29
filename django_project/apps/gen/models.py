from django.db import models
from django.db.models.base import Model


class Persona(Model):
    # Atributos
    dni = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    # Relaciones
    domicilio = models.ForeignKey('Domicilio')

class Domicilio(Model):
    # Atributos
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    localidad = models.CharField(max_length=50)
    # Relaciones
    