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
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from datetime import *
from forms import *
 
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def client_sub(request,idres):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			client = Client.objects.get(nom=idres)
			client.direccio = form.cleaned_data["direccio"] 
			client.telefon = form.cleaned_data["telefon"]
			client.pais = form.cleaned_data["pais"]
			client.save()
	return HttpResponseRedirect('/')

def create(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = CreateForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
 
            # Process the data in form.cleaned_data
            habitacio = form.cleaned_data["habitacio"]
            data_ent = form.cleaned_data["data_ent"]
            data_sort = form.cleaned_data["data_sort"]
	    user = request.user
            cli = Client.objects.get(nom=user)
            reserva = Reserva(client=cli, habitacio=habitacio, data_ent=data_ent, data_sort=data_sort)
            reserva.save()

            return HttpResponseRedirect('/')  # Redirect after POST
    else:
        form = CreateForm()
 
    data = {
        'form': form,
    }
    return render_to_response('create.html', data, context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
 
            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
 
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
 
            # Save new user attributes
            user.save()

            cli = Client(nom=user)
            cli.save()
            template = get_template('signup.html')
            variables = Context({
                'user': user
            })
            output = template.render(variables)
            return HttpResponseRedirect(output)  # Redirect after POST
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('signup.html', data, context_instance=RequestContext(request))
    
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

def deleteone(request, idres):
    	try:
		reserva = Reserva.objects.get(pk=idres)
    	except:
		raise Http404('id Reserva not found.')
    	reserva.delete()
    	return HttpResponseRedirect('/delete')  

def delete(request):
	user = request.user
	cli = Client.objects.get(nom=user)
	r = Reserva.objects.all()
	reserves = []
	for res in r:
		if res.client == cli:
			reserves.append(res)
	template = get_template('delete.html')
	variables = Context({
		'username': user.username,
		'reserves': reserves
		})
	output = template.render(variables)

	return HttpResponse(output)


def qualify(request):
	user = request.user
	cli = Client.objects.get(nom=user)
	r = Reserva.objects.all()
	reserves = []
	for res in r:
		if res.client == cli and datetime.date(res.data_sort) < date.today():
			reserves.append(res)
	template = get_template('qualify.html')
	variables = Context({
		'username': user.username,
		'reserves': reserves
		})
	output = template.render(variables)
	return HttpResponse(output)

def view(request):
	user = request.user
	cli = Client.objects.get(nom=user)
	r = Reserva.objects.all()
	reserves = []
	for res in r:
		if res.confirmada == True  and res.qualificacio != 6 or res.comentari_qualificacio != "":
			reserves.append(res)
	template = get_template('view.html')
	variables = Context({
		'username': user.username,
		'reserves': reserves
		})
	output = template.render(variables)
	return HttpResponse(output)

def edit(request):
	user = request.user
	cli = Client.objects.get(nom=user)
	r = Reserva.objects.all()
	reserves = []
	for res in r:
		if res.client == cli:
			reserves.append(res)
	template = get_template('edit.html')
	variables = Context({
		'username': user.username,
		'reserves': reserves
		})
	output = template.render(variables)
	return HttpResponse(output)



def qualifyone(request, idres):
    if request.method == 'POST':  # If the form has been submitted...
	form = QualifyForm(request.POST)  # A form bound to the POST 
	if form.is_valid():
	    reserva = Reserva.objects.get(pk=idres)
            reserva.qualificacio = form.cleaned_data["qualificacio"]
            if reserva.qualificacio < 0:
            	reserva.qualificacio = 0
            elif reserva.qualificacio > 5:
            	reserva.qualificacio = 5 
            reserva.comentari_qualificacio = form.cleaned_data["comentari_qualificacio"]
            reserva.save()
    	return HttpResponseRedirect('/qualify')  
    else:
    	try:
		reserva = Reserva.objects.get(pk=idres)
    	except:
		raise Http404('id Reserva not found.')
    	form = QualifyForm(instance=reserva)
	data = {
		'form': form,
	}
	return render_to_response('qualifyone.html', data, context_instance=RequestContext(request))

def editone(request, idres):
    if request.method == 'POST':  # If the form has been submitted...
	form = EditForm(request.POST)  # A form bound to the POST 
	if form.is_valid():
	    reserva = Reserva.objects.get(pk=idres)
            reserva.habitacio = form.cleaned_data["habitacio"]
            reserva.data_ent = form.cleaned_data["data_ent"]
            reserva.data_sort = form.cleaned_data["data_sort"]
            reserva.confirmada = form.cleaned_data["confirmada"]
            reserva.save()
    	return HttpResponseRedirect('/edit')  
    else:
    	try:
		reserva = Reserva.objects.get(pk=idres)
    	except:
		raise Http404('id Reserva not found.')
    	form = EditForm(instance=reserva)
	data = {
		'form': form,
	}
	return render_to_response('editone.html', data, context_instance=RequestContext(request))
    	'''
	    if request.method == 'POST':  # If the form has been submitted...
	        form = EditForm(request.POST)  # A form bound to the POST 
            	reserva.habitacio = form.cleaned_data["habitacio"]
            	reserva.data_ent = form.cleaned_data["data_ent"]
            	reserva.data_sort = form.cleaned_data["data_sort"]
	        reserva.update()
    		return HttpResponseRedirect('/edit') 
	    else:
	        form = EditForm(instance=reserva)
	        data = {
	            'form': form,
	        }
	        return render_to_response('editone.html', data, context_instance=RequestContext(request))
	'''

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
		data = serializers.serialize('json', reserves)
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		data = serializers.serialize('xml', reserves)
		return HttpResponse(data, mimetype='application/xml')


def reserva(request, idres=1, format=None):
	reserva = Reserva.objects.get(id=1)
	if format is None or format == 'html':
		template = get_template('reserva.html')
		variables = Context({
			'reserva': reserva
		})
		output = template.render(variables)
		return HttpResponse(output)
	elif format == 'json':
		data = serializers.serialize('json', [reserva])
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		data = serializers.serialize('xml', [reserva])
		return HttpResponse(data, mimetype='application/xml')


def habitacions(request, format=None):
	habitacions = Habitacio.objects.all()
	if format is None or format == 'html':
		template = get_template('habitacions.html')
		variables = Context({
			'habitacions': habitacions
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif format == 'json':
		data = serializers.serialize('json', habitacions)
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		data = serializers.serialize('xml', habitacions)
		return HttpResponse(data, mimetype='application/xml')


def habitacio(request, idhab, format=None):
	habitacio = Habitacio.objects.get(id=idhab)
	if format is None or format == 'html':
		template = get_template('habitacio.html')
		variables = Context({
			'habitacio': habitacio
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif format == 'json':
		data = serializers.serialize('json', [habitacio])
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		data = serializers.serialize('xml', [habitacio])
		return HttpResponse(data, mimetype='application/xml')

def clients(request, format=None):
	clients = Client.objects.all()
	if format is None or format == 'html':
		template = get_template('clients.html')
		variables = Context({
			'clients': clients
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif format == 'json':
		data = serializers.serialize('json', clients)
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		data = serializers.serialize('xml', clients)
		return HttpResponse(data, mimetype='application/xml')


def client(request, idcli, format=None):
	client = Client.objects.get(id = idcli)
	if format is None or format == 'html':
		template = get_template('client.html')
		variables = Context({
			'client': client
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif format == 'json':
		data = serializers.serialize('json', [client])
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		data = serializers.serialize('xml', [client])
		return HttpResponse(data, mimetype='application/xml')


def hostals(request, format=None):
	hostals = Hostal.objects.all()
	if format is None or format == 'html':
		template = get_template('hostals.html')
		variables = Context({
			'hostals': hostals
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif format == 'json':
		data = serializers.serialize('json', hostals)
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		data = serializers.serialize('xml', hostals)
		return HttpResponse(data, mimetype='application/xml')

def hostal(request, idhos, format=None):
	hostal = Hostal.objects.get(id =idhos)
	if format is None or format == 'html':
		template = get_template('hostal.html')
		variables = Context({
			'hostal': hostal
			})
		output = template.render(variables)
		return HttpResponse(output)
	elif format == 'json':
		data = serializers.serialize('json', [hostal])
		return HttpResponse(data, mimetype='application/json')
	elif format == 'xml':
		data = serializers.serialize('xml', [hostal])
		return HttpResponse(data, mimetype='application/xml')
	
def nou_usuari(request):
	if request.method=='POST':
		formulari = UserCreationForm(request.POST)
		if formulari.is_valid:
			formulari.save()
			return HttpResponseRedirect('/')
	else:
		formulari = UserCreationForm()
	return render_to_response('nouusari.html', {'formulari':formulari},context_instance=RequestContext(request))