from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.views.generic import CreateView, UpdateView

import json

from .models import Persona, Domicilio
from .forms import persona_form, domicilio_form


# Clase: Persona
## Vistas genéricas

class persona_crear(CreateView):
    model = Persona
    form_class = persona_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:persona_listar')


class persona_editar(UpdateView):
    model = Persona
    form_class = persona_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:persona_listar')


def persona_eliminar(request):
    return render_to_response('gen/persona_eliminar.html',
                              context_instance=RequestContext(request),
                              )


def persona_detallar(request):
    return render_to_response('gen/persona_detallar.html',
                              context_instance=RequestContext(request),
                              )


def persona_listar(request):
    return render_to_response('gen/persona_listar.html',
                              context_instance=RequestContext(request),
                              )


## Vistas JSON

def persona_detallar_json(request, id):
    object = get_object_or_404(Persona, pk=id)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


def persona_listar_json(request):
    data = serializers.serialize('json', Persona.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Domicilio
## Vistas genéricas

class domicilio_crear(CreateView):
    model = Domicilio
    form_class = domicilio_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:domicilio_listar')


class domicilio_editar(UpdateView):
    model = Domicilio
    form_class = domicilio_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:domicilio_listar')


def domicilio_eliminar(request):
    return render_to_response('gen/domicilio_eliminar.html',
                              context_instance=RequestContext(request),
                              )


def domicilio_detallar(request):
    return render_to_response('gen/domicilio_detallar.html',
                              context_instance=RequestContext(request),
                              )


def domicilio_listar(request):
    return render_to_response('gen/domicilio_listar.html',
                              context_instance=RequestContext(request),
                              )


## Vistas JSON

def domicilio_detallar_json(request, id):
    object = get_object_or_404(Domicilio, pk=id)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


def domicilio_listar_json(request):
    data = serializers.serialize('json', Domicilio.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')

    