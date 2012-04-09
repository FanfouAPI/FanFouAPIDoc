# -*- encoding: utf-8 -*-
import re
import urllib
import urlparse
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from fanfouapi import oauth, auth, api
from django.utils.encoding import smart_str, force_unicode
from django.conf import settings

class FFUserManager(models.Manager):
    def get_or_create_from_api(self, api):
        objuser = api.verify_credentials()
        uname = self.model.unquote_name(objuser.id)
        u, c = self.get_or_create(loginname=uname)
        u.objuser = objuser
        u.screen_name = objuser.name
        u.profile_image = objuser.profile_image_url
        try:
            u.created_at = objuser.created_at
        except Exception, e:
            print e
        u.save()
        return u

    def get_from_api(self, api):
        objuser = api.verify_credentials()
        uname = self.model.unquote_name(objuser.id)
        u = self.get(loginname=uname)
        u.objuser = objuser
        u.screen_name = objuser.name
        u.profile_image = objuser.profile_image_url
        u.save()
        return u

    def get_by_user(self, user):
        uname = self.model.unquote_name(user.username)
        return self.get(loginname=force_unicode(uname))

class FFUser(models.Model):
    loginname = models.CharField(max_length=100,  unique=True)
    screen_name = models.CharField(max_length=100,  db_index=True)
    profile_image = models.CharField(max_length=100, db_index=False)

    oauth_token_secret = models.CharField(max_length=60, null=True, blank=True)
    oauth_token = models.CharField(max_length=60, db_index=True, null=True, blank=True)

    login_time = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now=False, null=True)

    objects = FFUserManager()

    class Meta:
        ordering=['-login_time']
        verbose_name = u'饭否用户'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.loginname

    def get_absolute_url(self):
        return urlparse.urljoin('http://%s' % settings.FF_HOST, self.loginname)

    def get_invite_token(self):
        if self.invite_token:
            return self.invite_token

        while True:
            token_str = ''.join(random.choice(string.letters + string.digits) for i in xrange(10))

            #check if exists in email/sms express
            if FFUser.objects.filter(invite_token=token_str).count():
                continue
            else:
                self.invite_token = token_str
                self.save()
                return token_str
    @classmethod
    def quote_name(cls, username):
        username = force_unicode(username)
        s = ''
        for c in username:
            d = ord(c)
            if c == '~':
                s += '-%02x' % d
            elif d < 128:
                s += c
            else:
                s += '+%04x' % d
        return s

    @classmethod
    def unquote_name(cls, username):
        def to_unicode(m):
            a = int(m.group(1), 16)
            return unichr(a)
        username = re.sub(r'\+([a-zA-Z0-9]{4})', to_unicode, username)
        username = re.sub(r'\-([a-zA-A0-9]{2})', to_unicode, username)
        return username

    def get_or_create_user(self, oauth_token=None, oauth_token_secret=None):
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret
        self.save()
        
        u, c = User.objects.get_or_create(username=self.quote_name(self.loginname))
        if c:
            u.email = '%s@fanfou.cc' % u.username
            u.set_password('1111')
            u.save()
        return u

    def get_api(self):
        handler = auth.OAuthHandler(settings.FF_API_KEY, settings.FF_API_SECRET)
        handler.set_access_token(self.oauth_token, self.oauth_token_secret)
        return api.API(handler)
        
