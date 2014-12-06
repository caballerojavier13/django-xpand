from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

import json

from .models import Empresa, Producto, Almacen_producto, Almacen, Domicilio, Cliente, Pedido, Detalle_pedido, Venta, Detalle_venta, Historico_precio
from .forms import empresa_form, producto_form, almacen_producto_form, almacen_form, domicilio_form, cliente_form, pedido_form, detalle_pedido_form, venta_form, detalle_venta_form, historico_precio_form
from .forms import EmpresaDomicilioFormset
from .forms import AlmacenDomicilioFormset
from .forms import ClienteDomicilioFormset


# Índice
@login_required(login_url='/accounts/login')
def index(request):
    return render_to_response('backend/index.html',
                              context_instance=RequestContext(request),
                              )
                              

# Índice Productos
@login_required(login_url='/accounts/login')
def index_modulo_productos(request):
    return render_to_response('module/index_productos.html',
                              context_instance=RequestContext(request),
                              )

# Índice Almacen
@login_required(login_url='/accounts/login')
def index_modulo_almacen(request):
    return render_to_response('module/index_almacen.html',
                              context_instance=RequestContext(request),
                              )

# Índice Ventas
@login_required(login_url='/accounts/login')
def index_modulo_ventas(request):
    return render_to_response('module/index_ventas.html',
                              context_instance=RequestContext(request),
                              )

# Índice Opciones
@login_required(login_url='/accounts/login')
def index_modulo_opciones(request):
    return render_to_response('module/index_opciones.html',
                              context_instance=RequestContext(request),
                              )


# Clase: Empresa
## Vistas genéricas

class empresa_editar(UpdateView):
    model = Empresa
    form_class = empresa_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:empresa_detallar')
    
    
    
    def get_context_data(self, **kwargs):
        context = super(empresa_editar, self).get_context_data(**kwargs)
        if self.request.POST:
            context['EmpresaDomicilioFormset'] = EmpresaDomicilioFormset(self.request.POST)

        else:
            if (self.object.domicilio):
                context['EmpresaDomicilioFormset'] = EmpresaDomicilioFormset(
                  queryset=Domicilio.objects.filter(pk=self.object.domicilio.pk))
            else:
                context['EmpresaDomicilioFormset'] = EmpresaDomicilioFormset(
                  queryset=Domicilio.objects.none())

        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        domicilio_form = context['EmpresaDomicilioFormset']

        if domicilio_form.is_valid():
            self.object = form.save()
            domicilio_form.instance = self.object

			
            domicilio_list = domicilio_form.save()
            

            if (domicilio_list):
                self.object.domicilio = domicilio_list.pop()

            self.object.save()
            return HttpResponseRedirect(reverse_lazy('gen:empresa_detallar'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
     


@login_required(login_url='/accounts/login')
def empresa_detallar(request):
    model = Empresa.objects.filter().first()
    return render_to_response('backend/empresa_detallar.html',
                              {'object':model},
                              context_instance=RequestContext(request),
                              )

## Vistas JSON

@login_required(login_url='/accounts/login')
def empresa_detallar_json(request, pk):
    object = get_object_or_404(Empresa, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def empresa_listar_json(request):
    data = serializers.serialize('json', Empresa.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Producto
## Vistas genéricas

class producto_crear(CreateView):
    model = Producto
    form_class = producto_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:producto_listar')
    
    
        


class producto_editar(UpdateView):
    model = Producto
    form_class = producto_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:producto_listar')
    
    
     


@login_required(login_url='/accounts/login')
def producto_eliminar(request, pk):
    instancia = Producto.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:producto_listar'))


class producto_detallar(DetailView):
    model = Producto
    template_name_suffix = '_detallar'
    
    


@login_required(login_url='/accounts/login')
def producto_listar(request):
    return render_to_response('backend/producto_listar.html',
                              context_instance=RequestContext(request),
                              )

## Vistas JSON

@login_required(login_url='/accounts/login')
def producto_detallar_json(request, pk):
    object = get_object_or_404(Producto, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def producto_listar_json(request):
    data = serializers.serialize('json', Producto.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Almacen_producto
## Vistas genéricas
## Vistas JSON

@login_required(login_url='/accounts/login')
def almacen_producto_detallar_json(request, pk):
    object = get_object_or_404(Almacen_producto, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def almacen_producto_listar_json(request):
    data = serializers.serialize('json', Almacen_producto.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Almacen
## Vistas genéricas

class almacen_crear(CreateView):
    model = Almacen
    form_class = almacen_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:almacen_listar')
    
    
    
    def get_context_data(self, **kwargs):
        context = super(almacen_crear, self).get_context_data(**kwargs)
        if self.request.POST:
            context['AlmacenDomicilioFormset'] = AlmacenDomicilioFormset(self.request.POST)

        else:
                context['AlmacenDomicilioFormset'] = AlmacenDomicilioFormset(
                  queryset=Domicilio.objects.none())

        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        domicilio_form = context['AlmacenDomicilioFormset']

        if domicilio_form.is_valid():
            self.object = form.save()
            domicilio_form.instance = self.object

			
            domicilio_list = domicilio_form.save()
            

            if (domicilio_list):
                self.object.domicilio = domicilio_list.pop()

            self.object.save()
            return HttpResponseRedirect(reverse_lazy('gen:almacen_listar'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
        


class almacen_editar(UpdateView):
    model = Almacen
    form_class = almacen_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:almacen_listar')
    
    
    
    def get_context_data(self, **kwargs):
        context = super(almacen_editar, self).get_context_data(**kwargs)
        if self.request.POST:
            context['AlmacenDomicilioFormset'] = AlmacenDomicilioFormset(self.request.POST)

        else:
            if (self.object.domicilio):
                context['AlmacenDomicilioFormset'] = AlmacenDomicilioFormset(
                  queryset=Domicilio.objects.filter(pk=self.object.domicilio.pk))
            else:
                context['AlmacenDomicilioFormset'] = AlmacenDomicilioFormset(
                  queryset=Domicilio.objects.none())

        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        domicilio_form = context['AlmacenDomicilioFormset']

        if domicilio_form.is_valid():
            self.object = form.save()
            domicilio_form.instance = self.object

			
            domicilio_list = domicilio_form.save()
            

            if (domicilio_list):
                self.object.domicilio = domicilio_list.pop()

            self.object.save()
            return HttpResponseRedirect(reverse_lazy('gen:almacen_listar'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
     


@login_required(login_url='/accounts/login')
def almacen_eliminar(request, pk):
    instancia = Almacen.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:almacen_listar'))


class almacen_detallar(DetailView):
    model = Almacen
    template_name_suffix = '_detallar'
    
    


@login_required(login_url='/accounts/login')
def almacen_listar(request):
    return render_to_response('backend/almacen_listar.html',
                              context_instance=RequestContext(request),
                              )

## Vistas JSON

@login_required(login_url='/accounts/login')
def almacen_detallar_json(request, pk):
    object = get_object_or_404(Almacen, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def almacen_listar_json(request):
    data = serializers.serialize('json', Almacen.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Domicilio
## Vistas genéricas
## Vistas JSON

@login_required(login_url='/accounts/login')
def domicilio_detallar_json(request, pk):
    object = get_object_or_404(Domicilio, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def domicilio_listar_json(request):
    data = serializers.serialize('json', Domicilio.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Cliente
## Vistas genéricas

class cliente_crear(CreateView):
    model = Cliente
    form_class = cliente_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:cliente_listar')
    
    
    
    def get_context_data(self, **kwargs):
        context = super(cliente_crear, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ClienteDomicilioFormset'] = ClienteDomicilioFormset(self.request.POST)

        else:
                context['ClienteDomicilioFormset'] = ClienteDomicilioFormset(
                  queryset=Domicilio.objects.none())

        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        domicilio_form = context['ClienteDomicilioFormset']

        if domicilio_form.is_valid():
            self.object = form.save()
            domicilio_form.instance = self.object

			
            domicilio_list = domicilio_form.save()
            

            if (domicilio_list):
                self.object.domicilio = domicilio_list.pop()

            self.object.save()
            return HttpResponseRedirect(reverse_lazy('gen:cliente_listar'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
        


class cliente_editar(UpdateView):
    model = Cliente
    form_class = cliente_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:cliente_listar')
    
    
    
    def get_context_data(self, **kwargs):
        context = super(cliente_editar, self).get_context_data(**kwargs)
        if self.request.POST:
            context['ClienteDomicilioFormset'] = ClienteDomicilioFormset(self.request.POST)

        else:
            if (self.object.domicilio):
                context['ClienteDomicilioFormset'] = ClienteDomicilioFormset(
                  queryset=Domicilio.objects.filter(pk=self.object.domicilio.pk))
            else:
                context['ClienteDomicilioFormset'] = ClienteDomicilioFormset(
                  queryset=Domicilio.objects.none())

        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        domicilio_form = context['ClienteDomicilioFormset']

        if domicilio_form.is_valid():
            self.object = form.save()
            domicilio_form.instance = self.object

			
            domicilio_list = domicilio_form.save()
            

            if (domicilio_list):
                self.object.domicilio = domicilio_list.pop()

            self.object.save()
            return HttpResponseRedirect(reverse_lazy('gen:cliente_listar'))
        else:
            return self.render_to_response(self.get_context_data(form=form))
     


@login_required(login_url='/accounts/login')
def cliente_eliminar(request, pk):
    instancia = Cliente.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:cliente_listar'))


class cliente_detallar(DetailView):
    model = Cliente
    template_name_suffix = '_detallar'
    
    


@login_required(login_url='/accounts/login')
def cliente_listar(request):
    return render_to_response('backend/cliente_listar.html',
                              context_instance=RequestContext(request),
                              )

## Vistas JSON

@login_required(login_url='/accounts/login')
def cliente_detallar_json(request, pk):
    object = get_object_or_404(Cliente, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def cliente_listar_json(request):
    data = serializers.serialize('json', Cliente.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Pedido
## Vistas genéricas

class pedido_crear(CreateView):
    model = Pedido
    form_class = pedido_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:pedido_listar')
    
    def get_context_data(self, **kwargs):
        context = super(pedido_crear, self).get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.filter().first()
        return context
    
        


class pedido_editar(UpdateView):
    model = Pedido
    form_class = pedido_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:pedido_listar')
    
    def get_context_data(self, **kwargs):
        context = super(pedido_editar, self).get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.filter().first()
        context['detalles'] = Detalle_pedido.objects.filter(pedido = self.object)
        return context
    
     


@login_required(login_url='/accounts/login')
def pedido_eliminar(request, pk):
    instancia = Pedido.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:pedido_listar'))


class pedido_detallar(DetailView):
    model = Pedido
    template_name_suffix = '_detallar'
    
    def get_context_data(self, **kwargs):
        context = super(pedido_detallar, self).get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.filter().first()
        context['detalles'] = Detalle_pedido.objects.filter(pedido = self.object)
        return context
    


@login_required(login_url='/accounts/login')
def pedido_listar(request):
    return render_to_response('backend/pedido_listar.html',
                              context_instance=RequestContext(request),
                              )

## Vistas JSON

@login_required(login_url='/accounts/login')
def pedido_detallar_json(request, pk):
    object = get_object_or_404(Pedido, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def pedido_listar_json(request):
    data = serializers.serialize('json', Pedido.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Detalle_pedido
## Vistas genéricas

class detalle_pedido_crear(CreateView):
    model = Detalle_pedido
    form_class = detalle_pedido_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:detalle_pedido_listar')
    
    
        


@login_required(login_url='/accounts/login')
def detalle_pedido_eliminar(request, pk):
    instancia = Detalle_pedido.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:detalle_pedido_listar'))


@login_required(login_url='/accounts/login')
def detalle_pedido_listar(request):
    return render_to_response('backend/detalle_pedido_listar.html',
                              context_instance=RequestContext(request),
                              )

## Vistas JSON

@login_required(login_url='/accounts/login')
def detalle_pedido_detallar_json(request, pk):
    object = get_object_or_404(Detalle_pedido, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def detalle_pedido_listar_json(request):
    data = serializers.serialize('json', Detalle_pedido.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Venta
## Vistas genéricas

class venta_crear(CreateView):
    model = Venta
    form_class = venta_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:venta_listar')
    
    def get_context_data(self, **kwargs):
        context = super(venta_crear, self).get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.filter().first()
        return context
    
        


class venta_editar(UpdateView):
    model = Venta
    form_class = venta_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:venta_listar')
    
    def get_context_data(self, **kwargs):
        context = super(venta_editar, self).get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.filter().first()
        context['detalles'] = Detalle_venta.objects.filter(venta = self.object)
        return context
    
     


@login_required(login_url='/accounts/login')
def venta_eliminar(request, pk):
    instancia = Venta.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:venta_listar'))


class venta_detallar(DetailView):
    model = Venta
    template_name_suffix = '_detallar'
    
    def get_context_data(self, **kwargs):
        context = super(venta_detallar, self).get_context_data(**kwargs)
        context['empresa'] = Empresa.objects.filter().first()
        context['detalles'] = Detalle_venta.objects.filter(venta = self.object)
        return context
    


@login_required(login_url='/accounts/login')
def venta_listar(request):
    return render_to_response('backend/venta_listar.html',
                              context_instance=RequestContext(request),
                              )

## Vistas JSON

@login_required(login_url='/accounts/login')
def venta_detallar_json(request, pk):
    object = get_object_or_404(Venta, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def venta_listar_json(request):
    data = serializers.serialize('json', Venta.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Detalle_venta
## Vistas genéricas

class detalle_venta_crear(CreateView):
    model = Detalle_venta
    form_class = detalle_venta_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:detalle_venta_listar')
    
    
        


class detalle_venta_editar(UpdateView):
    model = Detalle_venta
    form_class = detalle_venta_form
    template_name_suffix = '_form'
    success_url = reverse_lazy('gen:detalle_venta_listar')
    
    
     


@login_required(login_url='/accounts/login')
def detalle_venta_eliminar(request, pk):
    instancia = Detalle_venta.objects.get(pk=pk)
    instancia.delete()
    return HttpResponseRedirect(reverse_lazy('gen:detalle_venta_listar'))


@login_required(login_url='/accounts/login')
def detalle_venta_listar(request):
    return render_to_response('backend/detalle_venta_listar.html',
                              context_instance=RequestContext(request),
                              )

## Vistas JSON

@login_required(login_url='/accounts/login')
def detalle_venta_detallar_json(request, pk):
    object = get_object_or_404(Detalle_venta, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def detalle_venta_listar_json(request):
    data = serializers.serialize('json', Detalle_venta.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')


# Clase: Historico_precio
## Vistas genéricas
## Vistas JSON

@login_required(login_url='/accounts/login')
def historico_precio_detallar_json(request, pk):
    object = get_object_or_404(Historico_precio, pk=pk)
    data = serializers.serialize('json', [object])
    return HttpResponse(data, content_type='application/json; charset=utf-8')


@login_required(login_url='/accounts/login')
def historico_precio_listar_json(request):
    data = serializers.serialize('json', Historico_precio.objects.all())
    return HttpResponse(data, content_type='application/json; charset=utf-8')

    