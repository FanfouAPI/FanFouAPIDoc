from django.core.management.base import BaseCommand
from django.conf import settings
import sys, urllib, re
from fanfouapi import auth
from fanfouapi.auth import OAuthHandler
import getpass

class Command(BaseCommand):
    help = "Make OAuth with pin"
    def handle(self, **options):
        handler = OAuthHandler(settings.FF_API_KEY, settings.FF_API_SECRET)
        url = handler.get_authorization_url(callback='oob')
        request_token = handler.request_token
        print 'Open the url', url, 'to get pin code.'
        verifier = raw_input('PIN Code: ')
        handler = OAuthHandler(settings.FF_API_KEY, settings.FF_API_SECRET)
        handler.request_token = request_token
        access_token = handler.get_access_token(verifier=verifier)
        if access_token:
            print '# Put the following lines into settings.py'
            print "PUBLISHER_OAUTH_TOKEN = '%s'" % access_token.key
            print "PUBLISHER_OAUTH_SECRET = '%s'" % access_token.secret

        
        
        
