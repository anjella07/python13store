from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        field = ['product_name', 'category', 'description', 'price', 'have', 'image']