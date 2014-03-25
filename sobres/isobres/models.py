from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
	name = models.TextField(max_length=100)
	direction = models.TextField(max_length=100)
	tel = models.TextField(max_length=100)
	def __unicode__(self):
		return self.name


class Hostal(models.Model):
	nom =  models.TextField(max_length=100)
	carrer = models.TextField(max_length=100)
	telefon = models.TextField(max_length=9)
	def __unicode__(self):
		return self.nom	
	

class Habitacio(models.Model):
	hostal = models.ForeignKey(Hostal)
	pis = models.TextField(max_length=1)
	porta = models.TextField(max_length=2)
	preu_nit = models.TextField(max_length=4)
	def __unicode__(self):
		return self.hostal.name+" - "+self.pis+" - "+self.porta
			
	
class Reserva(models.Model):
	habitacio =  models.ForeignKey(Habitacio)
	client =  models.ForeignKey(Client)
	data_ent = models.DateTimeField()
	data_sort = models.DateTimeField()
	def __unicode__(self):
		return self.client.name+" - "+self.habitacio
		
		

		




#class Donor(models.Model):
#        name = models.CharField(max_length=40)
#        def __unicode__(self):
#                return self.name


#class Sobre(models.Model):
#	date = models.DateTimeField()
#	amount = models.IntegerField()
#	concept = models.TextField(max_length=100)
#	donor = models.ForeignKey(Donor)
#	user = models.ForeignKey(User)
#	def __unicode__(self):
#		return self.donor.name+" - "+self.concept


