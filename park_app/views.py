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
	works = [	
	{
		'title': 		'The Clouds',
		'artist': 		'Niko Princen',
		'artistURL': 	'http://www.nikoprincen.com/',
		'workURL': 		'animation.gif'
	},
	{
		'title': 		'Parked Domain Girl RIP',
		'artist': 		'Emilie Gervais',
		'artistURL': 	'http://www.emiliegervais.com/',
		'workURL': 		'parkeddomaingirlrip.gif'
	},
	{
		'title': 		'Glyph Garland',
		'artist': 		'Brenna Murphy',
		'artistURL': 	'http://bmruernpnhay.com/',
		'workURL': 		'glyph_garland.png'
	},
	{
		'title': 		'Parked Domain Girl RIP',
		'artist': 		'Emilie Gervais',
		'artistURL': 	'http://www.emiliegervais.com/',
		'workURL': 		'parkeddomaingirlrip.gif'
	},
	{
		'title': 		'Recyclism',
		'artist': 		'Benjamin Gaulon',
		'artistURL': 	'http://www.recyclism.com/',
		'workURL': 		'recyclism.jpg'
	},
	{
		'title': 		'No shake',
		'artist': 		'Justin Blinder',
		'artistURL': 	'http://www.justinblinder.com/',
		'workURL': 		'no_shake.gif'
	},
	{
		'title': 		'Parked Domain Gallery',
		'artist': 		'Olof, Paul, Thiago',
		'artistURL': 	'http://www.arthackday.net/',
		'workURL': 		'parkeddomaingallery_art.png'
	},
	{
		'title': 		'Bought a new bin',
		'artist': 		'Bernhard Garnicnig',
		'artistURL':	'http://www.bernhardgustavanton.com/',
		'workURL': 		'garnicnig-bought-a-new-bin.jpg'
	}]

	return render_to_response('park/gallery.html', {'works': works}, context_instance=RequestContext(request))


