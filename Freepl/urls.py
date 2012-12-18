from django.conf.urls import patterns, include, url
from simulator.views import *
from simulator.models import users

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Freepl.views.home', name='home'),
    # url(r'^Freepl/', include('Freepl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^freepl/admin/', include(admin.site.urls)),
     url(r'^freepl/$',landing),
     url(r'^freepl/extract/$',extract),
     url(r'^freepl/myteam/$',team),
    
)
