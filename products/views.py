from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from .models import Product, Basket, Favorite
from .forms import BasketForm

# Create your views here.

class Products(generic.ListView):
    queryset = Product.objects.filter(status=1)
    template_name = "products/products.html"

def view_product(request, slug):

    queryset = Product.objects.filter(status=1)
    product = get_object_or_404(queryset, slug=slug)
    basket_items = Basket.objects.filter(product=product)
    
    if request.method == 'POST':
        basket_form = BasketForm(data=request.POST)
        if basket_form.is_valid():
            order = basket_form.save(commit=False)
            order.user = request.user
            order.product = product
            order.amount = product.price
            order.save()
            messages.success(request, 'Product added to basket')
            return redirect('basket')
        else:
            messages.error(request, 'Error adding product to basket')

    basket_form = BasketForm()
    return render(
        request,
        'products/view_product.html',
        {'product': product,
        'basket_items': basket_items,
        'basket_form': basket_form,},
        )

def home(request):
    return render(request, 'products/index.html',)

@login_required
def basket(request):

    items = Basket.objects.filter(user=request.user)
    total = sum(item.amount*item.quantity for item in items)

    return render(request, 'products/basket.html', {'items': items, 'total': total})

@login_required
def remove_item(request, basket_id):

    basket_item = get_object_or_404(Basket, id=basket_id, user=request.user)
    basket_item.delete()
    messages.add_message(request, messages.SUCCESS, 'Item removed!')

    return HttpResponseRedirect(reverse('basket'))

def after_payment(request):

    return render(
        request,
        'products/after_payment.html',
    )

@login_required
def add_to_favorites(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if created:
        messages.success(request, f'{product.title} has been added to your favorites.')
    else:
        messages.info(request, f'{product.title} is already in your favorites.')
    
    return redirect('products')

@login_required
def favorites(request):

    favorites = Favorite.objects.filter(user=request.user)

    return render(
        request,
        'products/favorites.html',
        {'favorites': favorites,},
        )

@login_required
def remove_favorite(request, favorite_id):

    favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    favorite.delete()
    messages.add_message(request, messages.SUCCESS, 'Favorite removed!')

    return HttpResponseRedirect(reverse('favorites'))