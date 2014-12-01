from django.db import models
from django.db.models.base import Model


class Empresa(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    lema = models.CharField(max_length=250)
    descripcion = models.TextField()
    # Relaciones
    domicilio = models.ForeignKey('Domicilio')
    # String Representación
    def __str__( self ):
    	return "{0} ".format( self.nombre)

class Producto(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    # Relaciones
    categoria = models.ForeignKey('Categoria')
    # String Representación
    def __str__( self ):
    	return "{0} ".format( self.nombre)

class Almacen_producto(Model):
    # Atributos
    cantidad = models.IntegerField()
    # Relaciones
    producto = models.ForeignKey('Producto', null=True, blank=True, on_delete=models.SET_NULL)
    almacen = models.ForeignKey('Almacen', null=True, blank=True, on_delete=models.SET_NULL)
    # String Representación
    def __str__( self ):
    	return "Almacen_producto"

class Almacen(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    # Relaciones
    empresa = models.ForeignKey('Empresa')
    domicilio = models.ForeignKey('Domicilio', null=True, blank=True, on_delete=models.SET_NULL)
    # String Representación
    def __str__( self ):
    	return "{0} ".format( self.nombre)

class Domicilio(Model):
    # Atributos
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    piso = models.IntegerField()
    departamento = models.IntegerField()
    localidad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    # Relaciones
    # String Representación
    def __str__( self ):
    	return "{0} {1} {2} {3} ".format( self.calle,self.Número,self.Localidad,self.provincia)

class Cliente(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.DecimalField(max_digits=12, decimal_places=3)
    # Relaciones
    domicilio = models.ForeignKey('Domicilio')
    # String Representación
    def __str__( self ):
    	return "{0} {1} ".format( self.Nombre,self.Apellido)

class Categoria(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    # Relaciones
    # String Representación
    def __str__( self ):
    	return "{0} ".format( self.nombre)
    