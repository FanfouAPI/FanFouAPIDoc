from django.conf.urls.defaults import patterns, include, url

from app.views import route, signout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apitest.views.home', name='home'),
    # url(r'^apitest/', include('apitest.foo.urls')),
    url(r'^logout$', signout, name='logout'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       
    url(r'^auth/', include('fanfouapi.urls')),
    url(r'^$', route, name='route'),
    url(r'^at/', include('app.urls')),
)
