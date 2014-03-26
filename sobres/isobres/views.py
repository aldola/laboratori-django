# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.db import models
from isobres.models import *
    
def mainpage(request):
	template = get_template('mainpage.html')
	variables = Context({
		'titlehead': 'Reserves app',
		'pagetitle': 'Welcome to the reserves application',
		'contentbody': 'Managing non legal funding since 2013',
		'user' : request.user
	})
	output = template.render(variables)
	return HttpResponse(output)


def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	reserves = Reserva.objects.get(username=nom)
	#reserves = user.reserva_set.all()
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'reserves': reserves
		})
	output = template.render(variables)
	return HttpResponse(output)