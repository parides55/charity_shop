from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from .models import Product, Basket

# Create your views here.

class Products(generic.ListView):
    queryset = Product.objects.all()
    template_name = "products/products.html"

def home(request):
    return render(request, 'products/index.html',)

def basket(request):
    return render(request, 'products/basket.html',)