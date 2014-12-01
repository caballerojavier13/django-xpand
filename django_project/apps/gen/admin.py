from django.contrib import admin

from .models import Empresa, Producto, Almacen_producto, Almacen, Domicilio, Cliente, Categoria

admin.site.register(Empresa)
admin.site.register(Producto)
admin.site.register(Almacen_producto)
admin.site.register(Almacen)
admin.site.register(Domicilio)
admin.site.register(Cliente)
admin.site.register(Categoria)
    