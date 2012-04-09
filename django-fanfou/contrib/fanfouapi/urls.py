from django.conf.urls.defaults import patterns, include, url
from fanfouapi.views import api_auth, api_authcb

urlpatterns = patterns('',
                       url(r'^$', api_auth, name='fanfou_oauth'),
                       url(r'^cb$', api_authcb, name='fanfou_oauth_callback'),
)
