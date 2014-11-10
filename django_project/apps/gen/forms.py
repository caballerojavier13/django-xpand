from django import forms
from django.forms.models import modelformset_factory

from .models import Persona, Domicilio


# Clase: Persona
class persona_form(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('dni', 'nombre', 'apellido')

# Clase: Domicilio
class domicilio_form(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ('calle', 'numero', 'localidad')

# Formsets generados por la clase: Persona
PersonaDomicilioFormset = modelformset_factory(Domicilio, extra=1, max_num=1)


    