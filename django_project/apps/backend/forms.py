from django import forms
from django.forms.models import modelformset_factory

from .models import Empresa, Producto, Almacen_producto, Almacen, Domicilio, Cliente, Pedido, Detalle_pedido, Venta, Detalle_venta, Historico_precio


# Clase: Empresa
class empresa_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(empresa_form, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre"
        self.fields['lema'].label = "Lema"
        self.fields['descripcion'].label = "Descripción"
        self.fields['telefono'].label = "Teléfono"
        self.fields['email'].label = "E-mail"
        self.fields['nombre'].widget.attrs['class'] = "form-control"
        self.fields['lema'].widget.attrs['class'] = "form-control"
        self.fields['descripcion'].widget.attrs['class'] = "form-control"
        self.fields['telefono'].widget.attrs['class'] = "form-control"
        self.fields['email'].widget.attrs['class'] = "form-control"
    class Meta:
        model = Empresa
        fields = ['nombre', 'lema', 'descripcion', 'telefono', 'email']

# Clase: Producto
class producto_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(producto_form, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre"
        self.fields['descripcion'].label = "Descripción"
        self.fields['nombre'].widget.attrs['class'] = "form-control"
        self.fields['descripcion'].widget.attrs['class'] = "form-control"
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion']

# Clase: Almacen_producto
class almacen_producto_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(almacen_producto_form, self).__init__(*args, **kwargs)
        self.fields['cantidad'].label = "Cantidad"
        self.fields['cantidad'].widget.attrs['class'] = "form-control"
    class Meta:
        model = Almacen_producto
        fields = ['cantidad','producto', 'almacen']

# Clase: Almacen
class almacen_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(almacen_form, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nombre"
        self.fields['nombre'].widget.attrs['class'] = "form-control"
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
        self.fields['calle'].widget.attrs['class'] = "form-control"
        self.fields['numero'].widget.attrs['class'] = "form-control"
        self.fields['piso'].widget.attrs['class'] = "form-control"
        self.fields['departamento'].widget.attrs['class'] = "form-control"
        self.fields['localidad'].widget.attrs['class'] = "form-control"
        self.fields['provincia'].widget.attrs['class'] = "form-control"
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
        self.fields['nombre'].widget.attrs['class'] = "form-control"
        self.fields['apellido'].widget.attrs['class'] = "form-control"
        self.fields['telefono'].widget.attrs['class'] = "form-control"
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono']

# Clase: Pedido
class pedido_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(pedido_form, self).__init__(*args, **kwargs)
        self.fields['fecha'].label = "Fecha"
        self.fields['total'].label = "Total"
        self.fields['fecha'].widget.attrs['class'] = "form-control datepicker"
        self.fields['total'].widget.attrs['class'] = "form-control"
    class Meta:
        model = Pedido
        fields = ['fecha', 'total','cliente', 'domicilio']

# Clase: Detalle_pedido
class detalle_pedido_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(detalle_pedido_form, self).__init__(*args, **kwargs)
    class Meta:
        model = Detalle_pedido
        fields = []

# Clase: Venta
class venta_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(venta_form, self).__init__(*args, **kwargs)
        self.fields['fecha'].label = "Fecha"
        self.fields['total'].label = "Total"
        self.fields['fecha'].widget.attrs['class'] = "form-control datepicker"
        self.fields['total'].widget.attrs['class'] = "form-control"
    class Meta:
        model = Venta
        fields = ['fecha', 'total','cliente', 'domicilio']

# Clase: Detalle_venta
class detalle_venta_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(detalle_venta_form, self).__init__(*args, **kwargs)
        self.fields['cantidad'].label = "Cantidad"
        self.fields['cantidad'].widget.attrs['class'] = "form-control"
    class Meta:
        model = Detalle_venta
        fields = ['cantidad','producto', 'venta', 'precio']

# Clase: Historico_precio
class historico_precio_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(historico_precio_form, self).__init__(*args, **kwargs)
        self.fields['fecha'].label = "Fecha Desde"
        self.fields['precio'].label = "Precio"
        self.fields['fecha'].widget.attrs['class'] = "form-control datepicker"
        self.fields['precio'].widget.attrs['class'] = "form-control"
    class Meta:
        model = Historico_precio
        fields = ['fecha', 'precio','producto']

# Formsets generados por la clase: Empresa
EmpresaDomicilioFormset = modelformset_factory(Domicilio, extra=1, max_num=1)


# Formsets generados por la clase: Almacen_producto

# Formsets generados por la clase: Almacen
AlmacenDomicilioFormset = modelformset_factory(Domicilio, extra=1, max_num=1)


# Formsets generados por la clase: Cliente
ClienteDomicilioFormset = modelformset_factory(Domicilio, extra=1, max_num=1)

# Formsets generados por la clase: Pedido


# Formsets generados por la clase: Venta

# Formsets generados por la clase: Detalle_venta

# Formsets generados por la clase: Historico_precio

    