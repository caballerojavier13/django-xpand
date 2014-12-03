from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(
        regex = r'^$',
        view  = views.index,
        name  = 'index'
    ),
    url(r'^$', include('apps.home.urls', namespace='home', app_name='home')),
    url(r'^productos/', include('apps.home.urls', namespace='home', app_name='home')),
    url(r'^accounts/', include('apps.account.urls', namespace='account', app_name='account')),
    url(r'^configuracion/', include('apps.backend.urls', namespace='gen', app_name='gen')),
    url(r'^admin/', include(admin.site.urls)),
)
