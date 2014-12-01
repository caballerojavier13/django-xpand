from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('apps.home.urls', namespace='home', app_name='home')),
    url(r'^accounts/', include('apps.account.urls', namespace='account', app_name='account')),
    url(r'^configuracion/', include('apps.gen.urls', namespace='gen', app_name='gen')),
    url(r'^admin/', include(admin.site.urls)),
)
