from django.shortcuts import render, reverse
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'products/index.html',)

def products(request):
    return render(request, 'products/products.html',)

def basket(request):
    return render(request, 'products/basket.html',)