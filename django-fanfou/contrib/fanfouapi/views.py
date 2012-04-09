import urllib
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from fanfouapi.auth import OAuthHandler
from fanfouapi.api import API
from fanfouapi.models import FFUser

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

def api_auth(request):
    handler = OAuthHandler(settings.FF_API_KEY, settings.FF_API_SECRET)
    callback_url = request.GET.get('oauth_callback')
    if not callback_url:
        callback_url = request.build_absolute_uri(reverse('fanfou_oauth_callback'))
    url = handler.get_authorization_url(callback=callback_url)
    request.session['reqtoken'] = handler.request_token
    print handler.request_token
    return HttpResponseRedirect(url)

def get_user(api, **token_dict):
    ffuser = FFUser.objects.get_or_create_from_api(api)
    user = ffuser.get_or_create_user(**token_dict)
    return user

def api_authcb(request):
    try:
        handler = OAuthHandler(settings.FF_API_KEY, settings.FF_API_SECRET)
        request_token = request.session.get('reqtoken', '')
        print 'request token', request_token
        handler.request_token = request_token
        token = handler.get_access_token(verifier=request.GET.get('verifier'))
        api = API(handler)
        u = get_user(api, oauth_token=token.key, oauth_token_secret=token.secret)
        u = authenticate(username=u.username, password='1111')
        login(request, u)
        request.user = u
    except Exception, e:
        print 'got error ', e
        import traceback
        traceback.print_exc()
        logout(request)
    #return HttpResponse('%s' % req_token)
    return HttpResponseRedirect(reverse('route'))
