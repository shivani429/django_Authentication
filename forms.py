from dataclasses import fields
from importlib.metadata import MetadataPathFinder
from django import forms
from demoapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

