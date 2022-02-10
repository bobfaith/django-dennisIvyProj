from django.forms import ModelForm
from .models import Order

''' We are creating OrderForm by getting all the attributes from the Model Order
which saves our time as we don't need to write code again to ge the same thing 
To make it happen we import ModelForm from django.forms and make use of it.'''
class OrderForm(ModelForm):
    class Meta:
        model = Order
        # fields = ['customer', 'product']  # if you were to import specific fields as needed is specified in a list.
        fields = '__all__'
