from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',

# Clase: Persona
## URLs genéricas

    url(
        regex = r'^persona/crear/$',
        view  = views.persona_crear,
        name  = 'persona_crear'
    ),


    url(
        regex = r'^persona/(?P<id>\d+)/editar/$',
        view  = views.persona_editar,
        name  = 'persona_editar'
    ),


    url(
        regex = r'^persona/(?P<id>\d+)/eliminar/$',
        view  = views.persona_eliminar,
        name  = 'persona_eliminar'
    ),


    url(
        regex = r'^persona/(?P<id>\d+)/$',
        view  = views.persona_detallar,
        name  = 'persona_detallar'
    ),


    url(
        regex = r'^persona/$',
        view  = views.persona_listar,
        name  = 'persona_listar'
    ),


## URLs JSON


    url(
        regex = r'^persona/json/crear/$',
        view  = views.persona_crear_json,
        name  = 'persona_crear_json'
    ),


    url(
        regex = r'^persona/json/(?P<id>\d+)/editar/$',
        view  = views.persona_editar_json,
        name  = 'persona_editar_json'
    ),


    url(
        regex = r'^persona/json/(?P<id>\d+)/eliminar/$',
        view  = views.persona_eliminar_json,
        name  = 'persona_eliminar_json'
    ),


    url(
        regex = r'^persona/json/(?P<id>\d+)/$',
        view  = views.persona_detallar_json,
        name  = 'persona_detallar_json'
    ),


    url(
        regex = r'^persona/json/$',
        view  = views.persona_listar_json,
        name  = 'persona_listar_json'
    ),



# Clase: Domicilio
## URLs genéricas

    url(
        regex = r'^domicilio/crear/$',
        view  = views.domicilio_crear,
        name  = 'domicilio_crear'
    ),


    url(
        regex = r'^domicilio/(?P<id>\d+)/editar/$',
        view  = views.domicilio_editar,
        name  = 'domicilio_editar'
    ),


    url(
        regex = r'^domicilio/(?P<id>\d+)/eliminar/$',
        view  = views.domicilio_eliminar,
        name  = 'domicilio_eliminar'
    ),


    url(
        regex = r'^domicilio/(?P<id>\d+)/$',
        view  = views.domicilio_detallar,
        name  = 'domicilio_detallar'
    ),


    url(
        regex = r'^domicilio/$',
        view  = views.domicilio_listar,
        name  = 'domicilio_listar'
    ),


## URLs JSON


    url(
        regex = r'^domicilio/json/crear/$',
        view  = views.domicilio_crear_json,
        name  = 'domicilio_crear_json'
    ),


    url(
        regex = r'^domicilio/json/(?P<id>\d+)/editar/$',
        view  = views.domicilio_editar_json,
        name  = 'domicilio_editar_json'
    ),


    url(
        regex = r'^domicilio/json/(?P<id>\d+)/eliminar/$',
        view  = views.domicilio_eliminar_json,
        name  = 'domicilio_eliminar_json'
    ),


    url(
        regex = r'^domicilio/json/(?P<id>\d+)/$',
        view  = views.domicilio_detallar_json,
        name  = 'domicilio_detallar_json'
    ),


    url(
        regex = r'^domicilio/json/$',
        view  = views.domicilio_listar_json,
        name  = 'domicilio_listar_json'
    ),


)
    