from django import forms
from showProduct.models import User, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'password')
