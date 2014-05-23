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
    url(r'^user/(\w+)', userpage),
    #url(r'^create/', create),
    url(r'^reserves/(?P<idres>(\w+))\.(?P<format>(json|xml))',reserva),
    url(r'^reserves/(\w+)',reserva),
    url(r'^reserves\.(?P<format>(json|xml))', reserves),
    url(r'^reserves', reserves),
    url(r'^habitacions/(?P<idhab>(\w+))\.(?P<format>(json|xml))', habitacio),
    url(r'^habitacions/(\w+)', habitacio),
    url(r'^habitacions\.(?P<format>(json|xml))', habitacions),
    url(r'^habitacions', habitacions),
    url(r'^clients/(?P<idcli>(\w+))\.(?P<format>(json|xml))', client),
    url(r'^clients/(\w+)', client),
    url(r'^clients\.(?P<format>(json|xml))', clients),
    url(r'^clients', clients),
    url(r'^hostals/(?P<idhos>(\w+))\.(?P<format>(json|xml))', hostal),
    url(r'^hostals/(\w+)', hostal),
    url(r'^hostals\.(?P<format>(json|xml))', hostals),
    url(r'^hostals', hostals),
    url(r'^login','django.contrib.auth.views.login'), 
    #url(r'^usuarinou/$','principal.views.nou_usuari'),
    url(r'^edit/(\w+)', 'isobres.views.editone', name='editone'),
    url(r'^edit', edit),
    url(r'^view', 'isobres.views.view', name='view'),
    url(r'^qualify/(\w+)', 'isobres.views.qualifyone', name='qualifyone'),
    url(r'^qualify', qualify),
    url(r'^signup/(\w+)', client_sub),
    url(r'^signup', 'isobres.views.signup', name='signup'),
    url(r'^create', 'isobres.views.create', name='create'),
    url(r'^delete/(\w+)', deleteone),
    url(r'^delete', 'isobres.views.delete', name='delete'),
    url(r'^logout', 'isobres.views.cerrar'),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework'))

)

#urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'xml'])