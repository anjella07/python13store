from django.shortcuts import render

from .forms import ProductForm
from .models import Product
from django.views.generic import ListView, DeleteView, CreateView
from .forms import ProductForm


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'



class ProductDetailView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'products'


    class ProductCreateView(CreateView):
        template_name = 'product create.html'
        form_class = ProductForm