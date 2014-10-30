from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from django.template import RequestContext

import json

from .models import Persona, Domicilio


# Clase: Persona
## Vistas genéricas

def persona_crear(request):
    return render_to_response('gen/persona_crear.html',
                              context_instance=RequestContext(request),
                              )


def persona_editar(request):
    return render_to_response('gen/persona_editar.html',
                              context_instance=RequestContext(request),
                              )


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

def persona_crear_json(request):
    pass


def persona_editar_json(request, id):
    pass


def persona_eliminar_json(request, id):
    pass


def persona_detallar_json(request, id):
    object = get_object_or_404(Persona, pk=id)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


def persona_listar_json(request):
    data = serializers.serialize('json', Persona.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Domicilio
## Vistas genéricas

def domicilio_crear(request):
    return render_to_response('gen/domicilio_crear.html',
                              context_instance=RequestContext(request),
                              )


def domicilio_editar(request):
    return render_to_response('gen/domicilio_editar.html',
                              context_instance=RequestContext(request),
                              )


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

def domicilio_crear_json(request):
    pass


def domicilio_editar_json(request, id):
    pass


def domicilio_eliminar_json(request, id):
    pass


def domicilio_detallar_json(request, id):
    object = get_object_or_404(Domicilio, pk=id)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


def domicilio_listar_json(request):
    data = serializers.serialize('json', Domicilio.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')

    