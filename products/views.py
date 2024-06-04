from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Product, Basket, Favorite
from .forms import BasketForm

# Create your views here.


class Products(generic.ListView):
    """
    Displays a list of approved products.

    ***Context***

    ``queryset``
        The queryset of approved products.

    ***Template***
    :template: products/products.html
    """

    queryset = Product.objects.filter(status=1)
    template_name = "products/products.html"


def view_product(request, slug):
    """
    Displays the details of a single product and
    handles adding the product to the basket.

    ***Context***

    ``product``
        The product object with the given slug.

    ``basket_items``
        The basket items for the product.

    ``basket_form``
        The form for adding the product to the basket.

    ***Template***
    :template: products/view_product.html
    """

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
        {
            'product': product, 'basket_items': basket_items,
            'basket_form': basket_form, },
        )


def home(request):
    """
    Displays the home page.

    ***Template***
    :template: products/index.html
    """

    return render(request, 'products/index.html',)


@login_required
def basket(request):
    """
    Displays the user's basket with items and the total amount.

    ***Context***

    ``items``
        The basket items for the user.

    ``total``
        The total amount of the basket items.

    ***Template***
    :template: products/basket.html
    """

    items = Basket.objects.filter(user=request.user)
    total = sum(item.amount*item.quantity for item in items)

    return render(request, 'products/basket.html', {
        'items': items, 'total': total})


@login_required
def remove_item(request, basket_id):
    """
    Removes an item from the user's basket.
    """

    basket_item = get_object_or_404(Basket, id=basket_id, user=request.user)
    basket_item.delete()
    messages.add_message(request, messages.SUCCESS, 'Item removed!')

    return HttpResponseRedirect(reverse('basket'))


def after_payment(request):
    """
    Clears the user's basket after payment and
    displays the after payment page.

    ***Template***
    :template: products/after_payment.html
    """

    basket_items = Basket.objects.filter(user=request.user)
    basket_items.delete()

    return render(
        request,
        'products/after_payment.html',
    )


@login_required
def add_to_favorites(request, product_id):
    """
    Adds a product to the user's favorites.
    """

    product = get_object_or_404(Product, id=product_id)
    favorite, created = Favorite.objects.get_or_create(
        user=request.user, product=product)

    if created:
        messages.success(
            request, f'{product.title} has been added to your favorites.')
    else:
        messages.info(
            request,
            f'{product.title} is already in your favorites.')

    return redirect('products')


@login_required
def favorites(request):
    """
    Displays the user's favorite products.
    ***Context***

    ``favorites``
        The favorite products for the user.

    ***Template***
    :template: products/favorites.html
    """

    favorites = Favorite.objects.filter(user=request.user)

    return render(
        request,
        'products/favorites.html',
        {'favorites': favorites, },
        )


@login_required
def remove_favorite(request, favorite_id):
    """
    Removes a product from the user's favorites.
    """

    favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
    favorite.delete()
    messages.add_message(request, messages.SUCCESS, 'Favorite removed!')

    return HttpResponseRedirect(reverse('favorites'))
