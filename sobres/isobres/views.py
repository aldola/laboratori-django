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
	cli = Client.objects.get(nom=user)
	r = Reserva.objects.all()
	reserves = []
	for res in r:
		if res.client == cli:
			reserves.append(res)
	template = get_template('userpage.html')
	variables = Context({
		'username': username,
		'reserves': reserves
		})
	output = template.render(variables)
	return HttpResponse(output)


def reserves(request):
	reserves = Reserva.objects.all()
	template = get_template('reserves.html')
	variables = Context({
		'reserves': reserves
		})
	output = template.render(variables)
	return HttpResponse(output)


def habitacions(request):
	habitacions = Habitacio.objects.all()
	template = get_template('habitacions.html')
	variables = Context({
		'habitacions': habitacions
		})
	output = template.render(variables)
	return HttpResponse(output)


def clients(request):
	clients = Client.objects.all()
	template = get_template('clients.html')
	variables = Context({
		'clients': clients
		})
	output = template.render(variables)
	return HttpResponse(output)


def hostals(request):
	hostals = Hostal.objects.all()
	template = get_template('hostals.html')
	variables = Context({
		'hostals': hostals
		})
	output = template.render(variables)
	return HttpResponse(output)