from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic
from django.views.generic import FormView
from django.http import HttpResponse
from .models import Product, Basket
from .forms import BasketForm

# Create your views here.

class Products(generic.ListView):
    queryset = Product.objects.all()
    template_name = "products/products.html"

def view_product(request, slug):

    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    print(product)
    basket = product.product.all()
    print(basket)
    
    if request.method == 'POST':
        basket_form = BasketForm(request.POST)
        print(basket_form)
        if basket_form.is_valid():
            order = basket_form.save()
            order.product = product
            order.amount = product.price
            order.quantity = 1
            order.save()
            print(order)
            messages.success(request, 'Product added to basket')
        else:
            messages.error(request, 'Error adding product to basket')

    basket_form = BasketForm()
    return render(
        request,
        'products/view_product.html',
        {'product': product,
        'basket': basket,
        'basket_from': basket_form,},
        )

def home(request):
    return render(request, 'products/index.html',)

def basket(request):
    return render(request, 'products/basket.html',)