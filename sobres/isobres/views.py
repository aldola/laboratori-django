# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.db import models
from isobres.models import *
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
    
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


def reserves(request, format=None):
	reserves = Reserva.objects.all()
	if format is None or format == 'html':
		template = get_template('reserves.html')
		variables = Context({
			'reserves': reserves
		})
		output = template.render(variables)
		return HttpResponse(output)
	elif format == 'json':
		reserves.append(reserves[0])
		reserves.append(reserves[0])
		data = serializers.serialize('json', reserves)
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		reserves.append(reserves[1])
		reserves.append(reserves[1])
		data = serializers.serialize('xml', reserves)
		return HttpResponse(data, mimetype='application/xml')

def reserva(request, idres, format=None):
	reserva = Reserva.objects.get(id=idres)
	template = get_template('reserva.html')
	variables = Context({
		'reserva': reserva
		})
	output = template.render(variables)
	return HttpResponse(output)


def habitacions(request, format=None):
	habitacions = Habitacio.objects.all()
	template = get_template('habitacions.html')
	variables = Context({
		'habitacions': habitacions
		})
	output = template.render(variables)
	return HttpResponse(output)

def habitacio(request, idhab, format=None):
	habitacio = Habitacio.objects.get(id=idhab)
	template = get_template('habitacio.html')
	variables = Context({
		'habitacio': habitacio
		})
	output = template.render(variables)
	return HttpResponse(output)


def clients(request, format=None):
	clients = Client.objects.all()
	template = get_template('clients.html')
	variables = Context({
		'clients': clients
		})
	output = template.render(variables)
	return HttpResponse(output)


def client(request, idcli, format=None):
	client = Client.objects.get(id = idcli)
	template = get_template('client.html')
	variables = Context({
		'client': client
		})
	output = template.render(variables)
	return HttpResponse(output)


def hostals(request, format=None):
	hostals = Hostal.objects.all()
	template = get_template('hostals.html')
	variables = Context({
		'hostals': hostals
		})
	output = template.render(variables)
	return HttpResponse(output)

def hostal(request, idhos, format=None):
	hostal = Hostal.objects.get(id =idhos)
	template = get_template('hostal.html')
	variables = Context({
		'hostal': hostal
		})
	output = template.render(variables)
	return HttpResponse(output)
	
def nou_usuari(request):
	if request.method=='POST':
		formulari = UserCreationForm(request.POST)
		if formulari.is_valid:
			formulari.save()
			return HttpResponseRedirect('/')
	else:
		formulari = UserCreationForm()
		return render_to_response('nouusuari.html', RequestContext(request, {}))
