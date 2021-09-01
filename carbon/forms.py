from django.contrib.auth.models import User, auth
from django import forms
from django.forms import ModelForm , TextInput

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','email']

from django.forms import ModelForm , TextInput
from .models import Citys

class CityForm(ModelForm):
    class Meta:
        model = Citys
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input','placeholder' : 'City Name'})}