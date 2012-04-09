from django.core.management.base import BaseCommand
from django.conf import settings
import sys, urllib, re
from fanfouapi import auth
import getpass

class Command(BaseCommand):
    help = "Make XAuth"
    def handle(self, username, **options):
        passwd = getpass.getpass('Password: ')
        m = auth.xauth(username, passwd)
        if m:
            print '# Put the following lines into settings.py'
            print '# User name: %s' % username
            print "PUBLISHER_OAUTH_TOKEN = '%s'" % m['key']
            print "PUBLISHER_OAUTH_SECRET = '%s'" % m['secret']
