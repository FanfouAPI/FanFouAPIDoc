from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.encoding import smart_str
import sys, urllib, re
from fanfouapi import oauth, auth, api

from urllib2 import Request, urlopen
from urlparse import urljoin
import getpass

def get_api(oauth_token=settings.PUBLISHER_OAUTH_TOKEN,
            oauth_secret=settings.PUBLISHER_OAUTH_SECRET):
    handler = auth.OAuthHandler(settings.FF_API_KEY, settings.FF_API_SECRET)
    handler.set_access_token(oauth_token, oauth_secret)
    return api.API(handler)
                                            
class Command(BaseCommand):
    help = "Call API"
    def handle(self, action, *args, **options):
        a = get_api()
        if action == 'statuses/update':
            if len(args) > 0:
                print a.update_status(status=args[0])
            else:
                print >>sys.stderr, 'statuses/update <status>'
        elif action == 'statuses/repost':
            if len(args) == 0:
                print >>sys.stderr, 'statuses/repost <statusid> <status>'
            else:
                repost_status_id = args[0]
                repost_status = a.get_status(repost_status_id)
                print repost_status.get_text()
                if len(args) > 1:
                    status = args[1]
                else:
                    status = '\xe8\xbd\xac@' + smart_str(repost_status.user.screen_name + ' ' + repost_status.get_text())
                    #status = prefix + msg.sendFromRealName
                a.update_status(status=status, repost_status_id=repost_status_id)                
        elif action == 'friendships/exists':
            if len(args) >= 2:
                v = a.exists_friendship(user_a=args[0], user_b=args[1])
                print v.value
            else:
                print >>sys.stderr, 'friendships/exists <user_a> <user_b>'
        elif action == 'photos/upload':
            if len(args) > 1:
                print a.upload(args[0], args[1])
            else:
                print >>sys.stderr, 'photos/upload <imgfile> <status>'
        elif action in ('statuses/friends_timeline',
                        'statuses/home_timeline'):
            print a.friends_timeline()
        elif action == 'statuses/public_timeline':
            print a.public_timeline()
        elif action in ('statuses/user_timeline',):
            if len(args) > 0:
                print a.user_timeline(user_id=args[0])
            else:
                print >>sys.stderr, 'statuses/user_timeline <user_id>'
        else:
            print >>sys.stderr, 'Unknown action', action
