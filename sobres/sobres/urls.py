from django.conf.urls import patterns, include, url
from isobres.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sobres.views.home', name='home'),
    # url(r'^sobres/', include('sobres.foo.urls')),
   
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage, name='home'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^reserves/(\w+)/$', reserva),
    url(r'^reserves', reserves),
    url(r'^habitacions/(\w+)/$', habitacio),
    url(r'^habitacions', habitacions),
    url(r'^clients/(\w+)/$', client),
    url(r'^clients', clients),
    url(r'^hostals/(\w+)/$', hostal),
    url(r'^hostals', hostals),
    url(r'^login/$','django.contrib.auth.views.login'), 
    #url(r'^usuarinou/$','principal.views.nou_usuari'),
    url(r'^usuarinou/$',nou_usuari), 
    url(r'^signup$', 'myapp.views.signup', name='signup'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'xml'])
