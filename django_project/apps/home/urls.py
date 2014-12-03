from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',

    url(
        regex = r'^$',
        view  = views.productos_index,
        name  = 'productos_index'
    ),
)
