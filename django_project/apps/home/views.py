from django.shortcuts import render_to_response
from django.template import RequestContext
from ..gen.models import Empresa, Producto, Almacen_producto, Almacen, Domicilio, Cliente, Categoria

# Create your views here.

def index(request):
    empresa = Empresa.objects.filter().first()
    return render_to_response('home/index.html',
                              {'empresa':empresa},
                              context_instance=RequestContext(request),
                              )
