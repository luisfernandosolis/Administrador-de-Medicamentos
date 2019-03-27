from django.contrib.auth.forms import UserCreationForm # formulario pos defecto para crear usuarios
from django.contrib.auth.models import User # modelo que contiene los campos de User 

from django import forms


class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['username', 'email', 'password1', 'password2']