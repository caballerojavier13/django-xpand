from django.shortcuts import render_to_response
from django.template import RequestContext
from ..backend.models import Empresa, Producto

# Create your views here.

def index(request):
    empresa = Empresa.objects.filter().first()
    return render_to_response('home/index.html',
                              {'empresa':empresa},
                              context_instance=RequestContext(request),
                              )

def productos_index(request):
    empresa = Empresa.objects.filter().first()
    productos = Producto.objects.filter()
    return render_to_response('home/producto_index.html',
                              {'empresa':empresa,'productos':productos},
                              context_instance=RequestContext(request),
                              )
