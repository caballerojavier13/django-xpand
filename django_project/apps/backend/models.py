import datetime
from django.db import models
from django.db.models.base import Model
from localflavor.us.models import PhoneNumberField


class Empresa(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    lema = models.CharField(max_length=250)
    descripcion = models.TextField()
    telefono = PhoneNumberField()
    email = models.EmailField(max_length=254
)
    # Relaciones
    domicilio = models.ForeignKey('Domicilio')
    # String Representación
    def __str__( self ):
    	return "{0} ".format( self.nombre
)

class Producto(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    # Relaciones
    # String Representación
    def __str__( self ):
    	return "{0} ".format( self.nombre
)

class Almacen_producto(Model):
    # Atributos
    cantidad = models.IntegerField()
    # Relaciones
    producto = models.ForeignKey('Producto', null=True, blank=True, on_delete=models.SET_NULL)
    almacen = models.ForeignKey('Almacen', null=True, blank=True, on_delete=models.SET_NULL)
    # String Representación
    def __str__( self ):
    	return "AlmacenProducto"

class Almacen(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    # Relaciones
    empresa = models.ForeignKey('Empresa')
    domicilio = models.ForeignKey('Domicilio', null=True, blank=True, on_delete=models.SET_NULL)
    # String Representación
    def __str__( self ):
    	return "{0} ".format( self.nombre
)

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
    	return "{0} {1} {2} {3} ".format( self.calle
,self.numero
,self.localidad
,self.provincia
)

class Cliente(Model):
    # Atributos
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = PhoneNumberField()
    # Relaciones
    domicilio = models.ForeignKey('Domicilio', null=True, blank=True, on_delete=models.SET_NULL)
    # String Representación
    def __str__( self ):
    	return "{0} {1} ".format( self.nombre
,self.apellido
)

class Pedido(Model):
    # Atributos
    fecha = models.DateField()
    # Relaciones
    # String Representación
    def __str__( self ):
    	return "Pedido de Venta"

class Detalle_pedido(Model):
    # Atributos
    # Relaciones
    # String Representación
    def __str__( self ):
    	return "Detalle de Pedido"

class Venta(Model):
    # Atributos
    fecha = models.DateField()
    # Relaciones
    cliente = models.ForeignKey('Cliente', null=True, blank=True, on_delete=models.SET_NULL)
    # String Representación
    def __str__( self ):
    	return "Venta"

class Detalle_venta(Model):
    # Atributos
    # Relaciones
    # String Representación
    def __str__( self ):
    	return "Detalle de Venta"
    