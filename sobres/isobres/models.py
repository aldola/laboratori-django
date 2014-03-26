from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
	nom = models.CharField(max_length=100)
	direccio = models.TextField(max_length=100)
	telefon = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nom


class Hostal(models.Model):
	nom =  models.TextField(max_length=100)
	direccio = models.TextField(max_length=100)
	telefon = models.CharField(max_length=12)
	def __unicode__(self):
		return self.nom	
	

class Habitacio(models.Model):
	hostal = models.ForeignKey(Hostal)
	numero_habitacio = models.CharField(max_length=3)
	preu_nit = models.CharField(max_length=6)
	def __unicode__(self):
		return self.hostal.nom+" - "+self.numero_habitacio+" - "+self.preu_nit
			
	
class Reserva(models.Model):
	habitacio =  models.ForeignKey(Habitacio)
	client =  models.ForeignKey(Client)
	data_ent = models.DateTimeField()
	data_sort = models.DateTimeField()
	def __unicode__(self):
		return self.client.nom+" - "+self.habitacio.numero_habitacio+" - "+self.habitacio.hostal.nom
		
		

		




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


