from multiprocessing.sharedctypes import Value
from urllib import request
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class pastel2(forms.ModelForm):
	class Meta:
		model=pastel
		fields= ['id','tamano','sabores','cantidad','costo']