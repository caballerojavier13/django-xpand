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


    url(
        regex = r'^opciones/empresa/json/crear/$',
        view  = views.empresa_crear_json,
        name  = 'empresa_crear_json'
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


    url(
        regex = r'^productos/producto/json/crear/$',
        view  = views.producto_crear_json,
        name  = 'producto_crear_json'
    ),


# Clase: Almacen_producto
## URLs genéricas

## URLs JSON

    url(
        regex = r'^almacen_producto/json/(?P<pk>\d+)/$',
        view  = views.almacen_producto_detallar_json,
        name  = 'almacen_producto_detallar_json'
    ),


    url(
        regex = r'^almacen_producto/json/$',
        view  = views.almacen_producto_listar_json,
        name  = 'almacen_producto_listar_json'
    ),


    url(
        regex = r'^almacen_producto/json/crear/$',
        view  = views.almacen_producto_crear_json,
        name  = 'almacen_producto_crear_json'
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


    url(
        regex = r'^almacen/almacen/json/crear/$',
        view  = views.almacen_crear_json,
        name  = 'almacen_crear_json'
    ),


# Clase: Domicilio
## URLs genéricas

## URLs JSON

    url(
        regex = r'^domicilio/json/(?P<pk>\d+)/$',
        view  = views.domicilio_detallar_json,
        name  = 'domicilio_detallar_json'
    ),


    url(
        regex = r'^domicilio/json/$',
        view  = views.domicilio_listar_json,
        name  = 'domicilio_listar_json'
    ),


    url(
        regex = r'^domicilio/json/crear/$',
        view  = views.domicilio_crear_json,
        name  = 'domicilio_crear_json'
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


    url(
        regex = r'^ventas/cliente/json/crear/$',
        view  = views.cliente_crear_json,
        name  = 'cliente_crear_json'
    ),


# Clase: Pedido
## URLs genéricas

    url(
        regex = r'^ventas/pedido/crear/$',
        view  = login_required(views.pedido_crear.as_view()),
        name  = 'pedido_crear'
    ),


    url(
        regex = r'^ventas/pedido/(?P<pk>\d+)/editar/$',
        view  = login_required(views.pedido_editar.as_view()),
        name  = 'pedido_editar'
    ),


    url(
        regex = r'^ventas/pedido/(?P<pk>\d+)/eliminar/$',
        view  = views.pedido_eliminar,
        name  = 'pedido_eliminar'
    ),


    url(
        regex = r'^ventas/pedido/(?P<pk>\d+)/$',
        view  = login_required(views.pedido_detallar.as_view()),
        name  = 'pedido_detallar'
    ),


    url(
        regex = r'^ventas/pedido/$',
        view  = views.pedido_listar,
        name  = 'pedido_listar'
    ),


## URLs JSON

    url(
        regex = r'^ventas/pedido/json/(?P<pk>\d+)/$',
        view  = views.pedido_detallar_json,
        name  = 'pedido_detallar_json'
    ),


    url(
        regex = r'^ventas/pedido/json/$',
        view  = views.pedido_listar_json,
        name  = 'pedido_listar_json'
    ),


    url(
        regex = r'^ventas/pedido/json/crear/$',
        view  = views.pedido_crear_json,
        name  = 'pedido_crear_json'
    ),


# Clase: Detalle_pedido
## URLs genéricas

    url(
        regex = r'^/detalle_pedido/crear/$',
        view  = login_required(views.detalle_pedido_crear.as_view()),
        name  = 'detalle_pedido_crear'
    ),


    url(
        regex = r'^/detalle_pedido/(?P<pk>\d+)/eliminar/$',
        view  = views.detalle_pedido_eliminar,
        name  = 'detalle_pedido_eliminar'
    ),


    url(
        regex = r'^/detalle_pedido/$',
        view  = views.detalle_pedido_listar,
        name  = 'detalle_pedido_listar'
    ),


## URLs JSON

    url(
        regex = r'^detalle_pedido/json/(?P<pk>\d+)/$',
        view  = views.detalle_pedido_detallar_json,
        name  = 'detalle_pedido_detallar_json'
    ),


    url(
        regex = r'^detalle_pedido/json/$',
        view  = views.detalle_pedido_listar_json,
        name  = 'detalle_pedido_listar_json'
    ),


    url(
        regex = r'^detalle_pedido/json/crear/$',
        view  = views.detalle_pedido_crear_json,
        name  = 'detalle_pedido_crear_json'
    ),


# Clase: Venta
## URLs genéricas

    url(
        regex = r'^ventas/venta/crear/$',
        view  = login_required(views.venta_crear.as_view()),
        name  = 'venta_crear'
    ),


    url(
        regex = r'^ventas/venta/(?P<pk>\d+)/editar/$',
        view  = login_required(views.venta_editar.as_view()),
        name  = 'venta_editar'
    ),


    url(
        regex = r'^ventas/venta/(?P<pk>\d+)/eliminar/$',
        view  = views.venta_eliminar,
        name  = 'venta_eliminar'
    ),


    url(
        regex = r'^ventas/venta/(?P<pk>\d+)/$',
        view  = login_required(views.venta_detallar.as_view()),
        name  = 'venta_detallar'
    ),


    url(
        regex = r'^ventas/venta/$',
        view  = views.venta_listar,
        name  = 'venta_listar'
    ),


## URLs JSON

    url(
        regex = r'^ventas/venta/json/(?P<pk>\d+)/$',
        view  = views.venta_detallar_json,
        name  = 'venta_detallar_json'
    ),


    url(
        regex = r'^ventas/venta/json/$',
        view  = views.venta_listar_json,
        name  = 'venta_listar_json'
    ),


    url(
        regex = r'^ventas/venta/json/crear/$',
        view  = views.venta_crear_json,
        name  = 'venta_crear_json'
    ),


# Clase: Detalle_venta
## URLs genéricas

    url(
        regex = r'^ventas/detalle_venta/crear/$',
        view  = login_required(views.detalle_venta_crear.as_view()),
        name  = 'detalle_venta_crear'
    ),


    url(
        regex = r'^ventas/detalle_venta/(?P<pk>\d+)/editar/$',
        view  = login_required(views.detalle_venta_editar.as_view()),
        name  = 'detalle_venta_editar'
    ),


    url(
        regex = r'^ventas/detalle_venta/(?P<pk>\d+)/eliminar/$',
        view  = views.detalle_venta_eliminar,
        name  = 'detalle_venta_eliminar'
    ),


    url(
        regex = r'^ventas/detalle_venta/$',
        view  = views.detalle_venta_listar,
        name  = 'detalle_venta_listar'
    ),


## URLs JSON

    url(
        regex = r'^ventas/detalle_venta/json/(?P<pk>\d+)/$',
        view  = views.detalle_venta_detallar_json,
        name  = 'detalle_venta_detallar_json'
    ),


    url(
        regex = r'^ventas/detalle_venta/json/$',
        view  = views.detalle_venta_listar_json,
        name  = 'detalle_venta_listar_json'
    ),


    url(
        regex = r'^ventas/detalle_venta/json/crear/$',
        view  = views.detalle_venta_crear_json,
        name  = 'detalle_venta_crear_json'
    ),


# Clase: Historico_precio
## URLs genéricas

## URLs JSON

    url(
        regex = r'^historico_precio/json/(?P<pk>\d+)/$',
        view  = views.historico_precio_detallar_json,
        name  = 'historico_precio_detallar_json'
    ),


    url(
        regex = r'^historico_precio/json/$',
        view  = views.historico_precio_listar_json,
        name  = 'historico_precio_listar_json'
    ),


    url(
        regex = r'^historico_precio/json/crear/$',
        view  = views.historico_precio_crear_json,
        name  = 'historico_precio_crear_json'
    ),

)
    