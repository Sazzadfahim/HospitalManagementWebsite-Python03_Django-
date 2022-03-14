from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import user_profile

class user_profile_form(ModelForm):
	class Meta:
		model = user_profile
		fields = '__all__'
		exclude = ['user']

