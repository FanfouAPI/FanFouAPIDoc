from django.core.urlresolvers import reverse
from django.template.context import Context, RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import forms
from fanfouapi.models import FFUser
from django.conf import settings

def route(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        site_url = 'http://%s' % settings.FF_HOST
        return render_to_response('route.html',
                                  RequestContext(request,
                                                 locals()))

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('route'))

@login_required
def update_profile_image(request):
    ffuser = FFUser.objects.get_by_user(request.user)
    api = ffuser.get_api()


    class ProfileImageForm(forms.Form):
        image = forms.ImageField()
        def save(self):
            img = self.cleaned_data['image']
            content = img.read()
            filename = img.name
            if isinstance(filename, unicode):
                filename = filename.encode('utf-8')
            return api.update_profile_image(filename=filename,
                                     content = content,
                                     file_type=img.content_type)
    if request.method == 'POST':
        img = request.FILES.get('image')
        form = ProfileImageForm(request.POST,
                                request.FILES)
        if form.is_valid():
            print form.save()
            return HttpResponseRedirect(reverse('update_profile_image'))
        else:
            print form.errors

    else:
        form = ProfileImageForm()
    u = api.verify_credentials()
    return render_to_response('update_profile_image.html',
                              RequestContext(request, locals()))

@login_required
def dashboard(request):
    return render_to_response('dashboard.html',
                              RequestContext(request,
                                             locals()))
