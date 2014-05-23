from django import forms
from django.contrib.auth.models import User
from models import *
from django.forms import ModelForm
 
 
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }
class CreateClient(ModelForm):
    class Meta:
        model = Client 
        fields = ['telefon', 'pais', 'direccio']


class CreateForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacio', 'data_ent', 'data_sort']


class EditForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacio', 'data_ent', 'data_sort', 'confirmada']

class QualifyForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['qualificacio', 'comentari_qualificacio']

        