from django import forms
from django.forms.models import modelformset_factory

from .models import Empresa, Producto, Almacen_producto, Almacen, Domicilio, Cliente, Categoria


# Clase: Empresa
class empresa_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(empresa_form, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre"
        self.fields['lema'].label = "Lema"
        self.fields['descripcion'].label = "Descripción"
    class Meta:
        model = Empresa
        fields = ['nombre', 'lema', 'descripcion']

# Clase: Producto
class producto_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(producto_form, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre"
        self.fields['descripcion'].label = "Descripción"
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion','categoria']

# Clase: Almacen_producto
class almacen_producto_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(almacen_producto_form, self).__init__(*args, **kwargs)
        self.fields['cantidad'].label = "Cantidad"
    class Meta:
        model = Almacen_producto
        fields = ['cantidad','producto', 'almacen']

# Clase: Almacen
class almacen_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(almacen_form, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre"
    class Meta:
        model = Almacen
        fields = ['nombre','empresa']

# Clase: Domicilio
class domicilio_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(domicilio_form, self).__init__(*args, **kwargs)
        self.fields['calle'].label = "Calle"
        self.fields['numero'].label = "Número"
        self.fields['piso'].label = "Piso"
        self.fields['departamento'].label = "Departamento"
        self.fields['localidad'].label = "Localidad"
        self.fields['provincia'].label = "Provincia"
    class Meta:
        model = Domicilio
        fields = ['calle', 'numero', 'piso', 'departamento', 'localidad', 'provincia']

# Clase: Cliente
class cliente_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(cliente_form, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre"
        self.fields['apellido'].label = "Apellido"
        self.fields['telefono'].label = "Teléfono"
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono']

# Clase: Categoria
class categoria_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(categoria_form, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre"
    class Meta:
        model = Categoria
        fields = ['nombre']

# Formsets generados por la clase: Empresa
EmpresaDomicilioFormset = modelformset_factory(Domicilio, extra=1, max_num=1)

# Formsets generados por la clase: Producto

# Formsets generados por la clase: Almacen_producto

# Formsets generados por la clase: Almacen
AlmacenDomicilioFormset = modelformset_factory(Domicilio, extra=1, max_num=1)


# Formsets generados por la clase: Cliente
ClienteDomicilioFormset = modelformset_factory(Domicilio, extra=1, max_num=1)


    