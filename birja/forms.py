from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User, Task
from django.db import models

class SignUpForm(UserCreationForm):
    balance = forms.IntegerField(required=True)
    username = forms.CharField()


    class Meta:
        model = User
        fields = ('username', 'balance', 'role', 'password1', 'password2', )

class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        
        fields = ('name', 'description', 'cost')
