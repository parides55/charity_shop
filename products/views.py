from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect 
from .models import Product, Basket
from .forms import BasketForm

# Create your views here.

class Products(generic.ListView):
    queryset = Product.objects.all()
    template_name = "products/products.html"

def view_product(request, slug):

    queryset = Product.objects.all()
    product = get_object_or_404(queryset, slug=slug)
    basket = product.product.all()
    
    if request.method == 'POST':
        basket_form = BasketForm(data=request.POST)
        if basket_form.is_valid():
            order = basket_form.save(commit=False)
            order.user = request.user
            order.product = product
            order.amount = product.price
            order.quantity = 1
            order.save()
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

    items = Basket.objects.filter(user=request.user)
    total = sum(item.amount for item in items)

    return render(request, 'products/basket.html', {'items': items, 'total': total})


def remove_item(request, basket_id):

    basket_item = get_object_or_404(Basket, id=basket_id, user=request.user)
    print(basket_id)
    basket_item.delete()
    print("item deleted")
    messages.add_message(request, messages.SUCCESS, 'Item removed!')

    return HttpResponseRedirect(reverse('basket'))