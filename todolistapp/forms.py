from django import forms
from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 


# Created a Model form
class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
        model = Task #The model for which we are creating the form for
        fields = '__all__'#Fields that are allowed in that  form

#class UserRegistrationForm(UserCreationForm):
    #class Meta:
        #model = User
        #fields = ('username', 'password1', 'password2')