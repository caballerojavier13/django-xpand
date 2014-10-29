from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^app/', include('apps.gen.urls', namespace='gen', app_name='gen')),
    url(r'^admin/', include(admin.site.urls)),
)
