from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class dataForm(forms.ModelForm):
    class Meta:
        model=Datamodel
        fields='__all__'
