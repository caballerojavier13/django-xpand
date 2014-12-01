from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = patterns('',

# Índice
    url(
        regex = r'^$',
        view  = views.index,
        name  = 'index'
    ),


# Índice Productos 
    url(
        regex = r'^productos/$',
        view  = views.index_modulo_productos,
        name  = 'index_productos'
    ),


# Índice Almacen 
    url(
        regex = r'^almacen/$',
        view  = views.index_modulo_almacen,
        name  = 'index_almacen'
    ),


# Índice Ventas 
    url(
        regex = r'^ventas/$',
        view  = views.index_modulo_ventas,
        name  = 'index_ventas'
    ),


# Índice Opciones 
    url(
        regex = r'^opciones/$',
        view  = views.index_modulo_opciones,
        name  = 'index_opciones'
    ),


# Clase: Empresa
## URLs genéricas

    url(
        regex = r'^opciones/empresa/(?P<pk>\d+)/editar/$',
        view  = login_required(views.empresa_editar.as_view()),
        name  = 'empresa_editar'
    ),


	url(
        regex = r'^opciones/empresa/$',
        view  = views.empresa_detallar,
        name  = 'empresa_detallar'
    ),


## URLs JSON

    url(
        regex = r'^opciones/empresa/json/(?P<pk>\d+)/$',
        view  = views.empresa_detallar_json,
        name  = 'empresa_detallar_json'
    ),


    url(
        regex = r'^opciones/empresa/json/$',
        view  = views.empresa_listar_json,
        name  = 'empresa_listar_json'
    ),



# Clase: Producto
## URLs genéricas

    url(
        regex = r'^productos/producto/crear/$',
        view  = login_required(views.producto_crear.as_view()),
        name  = 'producto_crear'
    ),


    url(
        regex = r'^productos/producto/(?P<pk>\d+)/editar/$',
        view  = login_required(views.producto_editar.as_view()),
        name  = 'producto_editar'
    ),


    url(
        regex = r'^productos/producto/(?P<pk>\d+)/eliminar/$',
        view  = views.producto_eliminar,
        name  = 'producto_eliminar'
    ),


    url(
        regex = r'^productos/producto/(?P<pk>\d+)/$',
        view  = login_required(views.producto_detallar.as_view()),
        name  = 'producto_detallar'
    ),


    url(
        regex = r'^productos/producto/$',
        view  = views.producto_listar,
        name  = 'producto_listar'
    ),


## URLs JSON

    url(
        regex = r'^productos/producto/json/(?P<pk>\d+)/$',
        view  = views.producto_detallar_json,
        name  = 'producto_detallar_json'
    ),


    url(
        regex = r'^productos/producto/json/$',
        view  = views.producto_listar_json,
        name  = 'producto_listar_json'
    ),



# Clase: Almacen_producto
## URLs genéricas

## URLs JSON

    url(
        regex = r'^/almacen_producto/json/(?P<pk>\d+)/$',
        view  = views.almacen_producto_detallar_json,
        name  = 'almacen_producto_detallar_json'
    ),


    url(
        regex = r'^/almacen_producto/json/$',
        view  = views.almacen_producto_listar_json,
        name  = 'almacen_producto_listar_json'
    ),



# Clase: Almacen
## URLs genéricas

    url(
        regex = r'^almacen/almacen/crear/$',
        view  = login_required(views.almacen_crear.as_view()),
        name  = 'almacen_crear'
    ),


    url(
        regex = r'^almacen/almacen/(?P<pk>\d+)/editar/$',
        view  = login_required(views.almacen_editar.as_view()),
        name  = 'almacen_editar'
    ),


    url(
        regex = r'^almacen/almacen/(?P<pk>\d+)/eliminar/$',
        view  = views.almacen_eliminar,
        name  = 'almacen_eliminar'
    ),


    url(
        regex = r'^almacen/almacen/(?P<pk>\d+)/$',
        view  = login_required(views.almacen_detallar.as_view()),
        name  = 'almacen_detallar'
    ),


    url(
        regex = r'^almacen/almacen/$',
        view  = views.almacen_listar,
        name  = 'almacen_listar'
    ),


## URLs JSON

    url(
        regex = r'^almacen/almacen/json/(?P<pk>\d+)/$',
        view  = views.almacen_detallar_json,
        name  = 'almacen_detallar_json'
    ),


    url(
        regex = r'^almacen/almacen/json/$',
        view  = views.almacen_listar_json,
        name  = 'almacen_listar_json'
    ),



# Clase: Domicilio
## URLs genéricas

## URLs JSON

    url(
        regex = r'^/domicilio/json/(?P<pk>\d+)/$',
        view  = views.domicilio_detallar_json,
        name  = 'domicilio_detallar_json'
    ),


    url(
        regex = r'^/domicilio/json/$',
        view  = views.domicilio_listar_json,
        name  = 'domicilio_listar_json'
    ),



# Clase: Cliente
## URLs genéricas

    url(
        regex = r'^ventas/cliente/crear/$',
        view  = login_required(views.cliente_crear.as_view()),
        name  = 'cliente_crear'
    ),


    url(
        regex = r'^ventas/cliente/(?P<pk>\d+)/editar/$',
        view  = login_required(views.cliente_editar.as_view()),
        name  = 'cliente_editar'
    ),


    url(
        regex = r'^ventas/cliente/(?P<pk>\d+)/eliminar/$',
        view  = views.cliente_eliminar,
        name  = 'cliente_eliminar'
    ),


    url(
        regex = r'^ventas/cliente/(?P<pk>\d+)/$',
        view  = login_required(views.cliente_detallar.as_view()),
        name  = 'cliente_detallar'
    ),


    url(
        regex = r'^ventas/cliente/$',
        view  = views.cliente_listar,
        name  = 'cliente_listar'
    ),


## URLs JSON

    url(
        regex = r'^ventas/cliente/json/(?P<pk>\d+)/$',
        view  = views.cliente_detallar_json,
        name  = 'cliente_detallar_json'
    ),


    url(
        regex = r'^ventas/cliente/json/$',
        view  = views.cliente_listar_json,
        name  = 'cliente_listar_json'
    ),



# Clase: Categoria
## URLs genéricas

    url(
        regex = r'^productos/categoria/crear/$',
        view  = login_required(views.categoria_crear.as_view()),
        name  = 'categoria_crear'
    ),


    url(
        regex = r'^productos/categoria/(?P<pk>\d+)/editar/$',
        view  = login_required(views.categoria_editar.as_view()),
        name  = 'categoria_editar'
    ),


    url(
        regex = r'^productos/categoria/(?P<pk>\d+)/eliminar/$',
        view  = views.categoria_eliminar,
        name  = 'categoria_eliminar'
    ),


    url(
        regex = r'^productos/categoria/(?P<pk>\d+)/$',
        view  = login_required(views.categoria_detallar.as_view()),
        name  = 'categoria_detallar'
    ),


    url(
        regex = r'^productos/categoria/$',
        view  = views.categoria_listar,
        name  = 'categoria_listar'
    ),


## URLs JSON

    url(
        regex = r'^productos/categoria/json/(?P<pk>\d+)/$',
        view  = views.categoria_detallar_json,
        name  = 'categoria_detallar_json'
    ),


    url(
        regex = r'^productos/categoria/json/$',
        view  = views.categoria_listar_json,
        name  = 'categoria_listar_json'
    ),


)
    