from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

def index(request):
	return render_to_response('park/index.html', context_instance=RequestContext(request))

def gallery(request):
    return render_to_response('park/gallery.html', context_instance=RequestContext(request))


