from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.views.generic import CreateView, UpdateView

import json

from .models import Persona, Domicilio
from .forms import persona_form, domicilio_form
from .forms import PersonaDomicilioFormset



# Índice
def index(request):
    return render_to_response('gen/index.html',
                              context_instance=RequestContext(request),
                              )


# Clase: Persona
## Vistas genéricas

class persona_crear(CreateView):
    model = Persona
    form_class = persona_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:persona_listar')
    
    
    def get_context_data(self, **kwargs):
        context = super(persona_crear, self).get_context_data(**kwargs)
        if self.request.POST:
            context['PersonaDomicilioFormset'] = PersonaDomicilioFormset(self.request.POST)
        else:
                context['PersonaDomicilioFormset'] = PersonaDomicilioFormset(
                  queryset=Domicilio.objects.none())
        return context
    def form_valid(self, form):
        context = self.get_context_data()
        domicilio_form = context['PersonaDomicilioFormset']
        if domicilio_form.is_valid():
            self.object = form.save()
            domicilio_form.instance = self.object
            domicilio_list = domicilio_form.save()
            self.object.domicilio = domicilio_list.pop()
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('gen:persona_listar'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
        


class persona_editar(UpdateView):
    model = Persona
    form_class = persona_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:persona_listar')
    
    
    def get_context_data(self, **kwargs):
        context = super(persona_editar, self).get_context_data(**kwargs)
        if self.request.POST:
            context['PersonaDomicilioFormset'] = PersonaDomicilioFormset(self.request.POST)
        else:
            if (self.object.domicilio):
                context['PersonaDomicilioFormset'] = PersonaDomicilioFormset(
                  queryset=Domicilio.objects.filter(pk=self.object.domicilio.pk))
            else:
                context['PersonaDomicilioFormset'] = PersonaDomicilioFormset(
                  queryset=Domicilio.objects.none())
        return context
    def form_valid(self, form):
        context = self.get_context_data()
        domicilio_form = context['PersonaDomicilioFormset']
        if domicilio_form.is_valid():
            self.object = form.save()
            domicilio_form.instance = self.object
            domicilio_list = domicilio_form.save()
            self.object.domicilio = domicilio_list.pop()
            self.object.save()
            return HttpResponseRedirect(reverse_lazy('gen:persona_listar'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
     


def persona_eliminar(request, pk):
    instancia = Persona.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:persona_listar'))


def persona_detallar(request):
    return render_to_response('gen/persona_detallar.html',
                              context_instance=RequestContext(request),
                              )


def persona_listar(request):
    return render_to_response('gen/persona_listar.html',
                              context_instance=RequestContext(request),
                              )


## Vistas JSON

def persona_detallar_json(request, pk):
    object = get_object_or_404(Persona, pk=pk)
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
    
     


def domicilio_eliminar(request, pk):
    instancia = Domicilio.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:domicilio_listar'))


def domicilio_detallar(request):
    return render_to_response('gen/domicilio_detallar.html',
                              context_instance=RequestContext(request),
                              )


def domicilio_listar(request):
    return render_to_response('gen/domicilio_listar.html',
                              context_instance=RequestContext(request),
                              )


## Vistas JSON

def domicilio_detallar_json(request, pk):
    object = get_object_or_404(Domicilio, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


def domicilio_listar_json(request):
    data = serializers.serialize('json', Domicilio.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')

    