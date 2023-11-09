from django import forms
from .models import Products,Order

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name','brand','model','category','quantity']

class OrderForm(forms.ModelForm):
    class Meta :
        model = Order
        fields = ['product','order_quantity']