from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',

# Clase: Persona
## URLs genéricas

    url(
        regex = r'^persona/crear/$',
        view  = views.persona_crear.as_view(),
        name  = 'persona_crear'
    ),


    url(
        regex = r'^persona/(?P<pk>\d+)/editar/$',
        view  = views.persona_editar.as_view(),
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
        view  = views.domicilio_crear.as_view(),
        name  = 'domicilio_crear'
    ),


    url(
        regex = r'^domicilio/(?P<pk>\d+)/editar/$',
        view  = views.domicilio_editar.as_view(),
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
    