from django.db import models


class Persona(models.Model):
    # Atributos
    dni = Model.IntegerField()
    nombre = Model.CharField(max_length=50)
    apellido = Model.CharField(max_length=50)
    # Relaciones
    domicilio = Model.ForeignKey('Domicilio')

class Domicilio(models.Model):
    # Atributos
    calle = Model.CharField(max_length=50)
    numero = Model.IntegerField()
    localidad = Model.CharField(max_length=50)
    # Relaciones
    