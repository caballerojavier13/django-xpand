from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(
        regex = r'^login/$',
        view  = views.user_login,
        name  = 'login'
    ),
    url(
        regex = r'^logout/$',
        view  = views.user_logout,
        name  = 'logout'
    ),
)
