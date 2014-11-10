from django import forms
from django.forms.models import inlineformset_factory

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

PersonaDomicilioFormset = inlineformset_factory(Persona, Domicilio)


    