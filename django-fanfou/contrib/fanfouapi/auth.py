# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.
import sys
import re
from urllib2 import Request, urlopen
import base64

from django.conf import settings

from fanfouapi import oauth
from fanfouapi.error import WeibopError
from fanfouapi.api import API

API_HOST = getattr(settings, 'API_HOST', 'api.fanfou.com')
SEARCH_HOST = getattr(settings, 'SEARCH_HOST', 'api.fanfou.com')
FF_HOST = getattr(settings, 'FF_HOST', 'fanfou.com')
OAUTH_HOST = getattr(settings, 'OAUTH_HOST', FF_HOST)
OAUTH_ROOT = getattr(settings, 'OAUTH_ROOT', '/oauth/')

class AuthHandler(object):
    def apply_auth(self, url, method, headers, parameters):
        """Apply authentication headers to request"""
        raise NotImplementedError

    def get_username(self):
        """Return the username of the authenticated user"""
        raise NotImplementedError

class BasicAuthHandler(AuthHandler):
    def __init__(self, username, password):
        self.username = username
        self._b64up = base64.b64encode('%s:%s' % (username, password))

    def apply_auth(self, url, method, headers, parameters):
        headers['Authorization'] = 'Basic %s' % self._b64up
        
    def get_username(self):
        return self.username


class OAuthHandler(AuthHandler):
    """OAuth authentication handler"""

    def __init__(self, consumer_key, consumer_secret, callback=None, secure=False):
        self._consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)
        self._sigmethod = oauth.OAuthSignatureMethod_HMAC_SHA1()
        self.request_token = None
        self.access_token = None
        self.callback = callback
        self.username = None
        self.secure = secure

    def _get_oauth_url(self, endpoint):
        if self.secure:
            prefix = 'https://'
        else:
            prefix = 'http://'

        return prefix + OAUTH_HOST + OAUTH_ROOT + endpoint

    def apply_auth(self, url, method, headers, parameters):
        request = oauth.OAuthRequest.from_consumer_and_token(
            self._consumer, http_url=url, http_method=method,
            token=self.access_token, parameters=parameters
        )
        request.sign_request(self._sigmethod, self._consumer, self.access_token)
        headers.update(request.to_header())

    def _get_request_token(self):
        try:
            url = self._get_oauth_url('request_token')
            request = oauth.OAuthRequest.from_consumer_and_token(
                self._consumer, http_url=url, callback=self.callback
            )
            request.sign_request(self._sigmethod, self._consumer, None)
            resp = urlopen(Request(url, headers=request.to_header()))
            data = resp.read()
            return oauth.OAuthToken.from_string(data)
        except Exception, e:
            import traceback
            traceback.print_exc()
            print >>sys.stderr, url
            raise WeibopError(e)

    def set_request_token(self, key, secret):
        self.request_token = oauth.OAuthToken(key, secret)

    def set_access_token(self, key, secret):
        self.access_token = oauth.OAuthToken(key, secret)

    def get_authorization_url(self, signin_with_twitter=False, callback=None):
        """Get the authorization URL to redirect the user"""
        try:
            # get the request token
            self.request_token = self._get_request_token()
            # build auth request and return as url
            if signin_with_twitter:
                url = self._get_oauth_url('authenticate')
            else:
                url = self._get_oauth_url('authorize')
            request = oauth.OAuthRequest.from_token_and_callback(
                token=self.request_token, http_url=url,
                callback=callback
            )

            return request.to_url()
        except Exception, e:
            import traceback
            traceback.print_exc()
            raise WeibopError(e)

    def get_access_token(self, verifier=None):
        """
        After user has authorized the request token, get access token
        with user supplied verifier.
        """
        try:
            url = self._get_oauth_url('access_token')

            # build request
            request = oauth.OAuthRequest.from_consumer_and_token(
                self._consumer,
                token=self.request_token, http_url=url,
                verifier=str(verifier)
            )
            request.sign_request(self._sigmethod, self._consumer, self.request_token)
            # send request                        
            resp = urlopen(Request(url, headers=request.to_header()))
            data = resp.read()
            self.access_token = oauth.OAuthToken.from_string(data)
            return self.access_token
        except Exception, e:
            import traceback
            traceback.print_exc()
            raise WeibopError(e)
        
    def setToken(self, token, tokenSecret):
        self.access_token = oauth.OAuthToken(token, tokenSecret)
        
    def get_username(self):
        if self.username is None:
            api = API(self)
            user = api.verify_credentials()
            if user:
                self.username = user.screen_name
            else:
                raise WeibopError("Unable to get username, invalid oauth token!")
        return self.username

def xauth_request_to_header(request, realm=''):
    """Serialize as a header for an HTTPAuth request."""
    auth_header = 'OAuth realm="%s"' % realm
    # Add the oauth parameters.
    if request.parameters:
        for k, v in request.parameters.iteritems():
            if k.startswith('oauth_') or k.startswith('x_auth_'):
                auth_header += ', %s="%s"' % (k, oauth.escape(str(v)))
    if settings.DEBUG:
        print '[DEBUG]', 'OAuth header:', auth_header
    return {'Authorization': auth_header}

def xauth(username, passwd):
    """
    returns {'key': ..., 'secret': '...'} if successed
    or 
    None if xauth failed 
    """
    access_token_url = 'http://' + FF_HOST + '/oauth/access_token'
    verify_url = 'http://' + API_HOST+ '/account/verify_credentials.xml'

    consumer = oauth.OAuthConsumer(settings.FF_API_KEY,
                                   settings.FF_API_SECRET)
    params = {}
    params["x_auth_username"] = username
    params["x_auth_password"] = passwd
    params["x_auth_mode"] = 'client_auth'
    request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                                                         http_url=access_token_url,
                                                         parameters=params)
    signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
    request.sign_request(signature_method, consumer, None)
    headers=xauth_request_to_header(request)
    resp = urlopen(Request(access_token_url, headers=headers))
    token = resp.read()
    m = re.match(r'oauth_token=(?P<key>.+?)&oauth_token_secret=(?P<secret>.+)', token)
    if m:
        return m.groupdict()
