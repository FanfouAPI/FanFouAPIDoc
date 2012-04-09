from django.core.management.base import BaseCommand
from django.conf import settings
import sys, urllib, re
from fanfouapi import oauth, auth, api

from urllib2 import Request, urlopen
from urlparse import urljoin
import getpass

USER_AGENT = getattr(settings, 'USER_AGENT', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.109 Safari/535.1')

def get_api(oauth_token=settings.PUBLISHER_OAUTH_TOKEN,
            oauth_secret=settings.PUBLISHER_OAUTH_SECRET):
    handler = auth.OAuthHandler(settings.FF_API_KEY, settings.FF_API_SECRET)
    handler.set_access_token(oauth_token, oauth_secret)
    return api.API(handler)

class Command(BaseCommand):
    help = "Update URL"
    def handle(self, url, *args, **kw):
        print 'getting url', url, '...'
        req = Request(url, None, headers={'User-Agent': USER_AGENT})
        resp = urlopen(req, None, 30)
        info = resp.info()
        charset = info.getparam('charset')
        if charset is None:
            charset = 'utf-8'
        charset = charset.lower()
        ttype = info.gettype()
        if ttype in ('text/html', ):
            data = resp.read()
            m = re.search(r'<title>(.*?)</title>', data)
            if m:
                title = unicode(m.group(1), charset).encode('utf-8')
                api = get_api()
                content = '%s %s' % (title, url)
                print content
                #print api.update_status(content)
