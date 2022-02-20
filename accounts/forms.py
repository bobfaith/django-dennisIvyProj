from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


''' We are creating OrderForm by getting all the attributes from the Model Order
which saves our time as we don't need to write code again to ge the same thing 
To make it happen we import ModelForm from django.forms and make use of it.'''

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']



class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = ['customer', 'product']  # if you were to import specific fields as needed is specified in a list.
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


