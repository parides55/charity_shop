from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
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

    try:
        queryset = Product.objects.filter(status=1)
        product = get_object_or_404(queryset, slug=slug)
        basket_items = Basket.objects.filter(product=product)

        if request.method == 'POST':
            basket_form = BasketForm(data=request.POST)
            if basket_form.is_valid():
                order_quantity = basket_form.cleaned_data['quantity']
                # Check if product is already in the user's basket
                existing_basket_item = Basket.objects.filter(product=product, user=request.user).first()

                if existing_basket_item:
                    # Increase the quantity of the existing item
                    existing_basket_item.quantity += order_quantity
                    existing_basket_item.save()
                    messages.success(request, f'The quantity of {product.title} has been updated in your basket!')
                else:
                    # Add a new item to the basket
                    order = basket_form.save(commit=False)
                    order.user = request.user
                    order.product = product
                    order.amount = product.price
                    order.save()
                    messages.success(request, f'{product.title} added successfully to your basket!')

                return redirect('basket')
            else:
                messages.error(request, 'There was an error adding the product to Your basket. Please try again.')

        basket_form = BasketForm()

        return render(
            request,
            'products/view_product.html',
            {
                'product': product, 'basket_items': basket_items,
                'basket_form': basket_form, },
            )
    except Exception as e:
        messages.error(request, f'The following error occurred:\n{str(e)}.')
        return render(request, '500.html', status=500)


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

    try:
        items = Basket.objects.filter(user=request.user)
        total = sum(item.amount*item.quantity for item in items)

        context = {
        'items': items,
        'total': total,
        'paypal_client_id': settings.PAYPAL_CLIENT_ID,
    }

        return render(request, 'products/basket.html', context)

    except Exception as e:
        messages.error(request, f'The following error occurred:\n{str(e)}.')
        return render(request, '500.html', status=500)


@login_required
def remove_item(request, basket_id):
    """
    Removes an item from the user's basket.
    """

    try:
        basket_item = get_object_or_404(Basket, id=basket_id, user=request.user)
        basket_item.delete()
        messages.add_message(request, messages.ERROR, 'Item removed from your basket!')

        return HttpResponseRedirect(reverse('basket'))
    except Exception as e:
        messages.error(request, f'Failed to remove item because of the following error:\n{str(e)}')
        return redirect('basket')


def after_payment(request):
    """
    Clears the user's basket after payment and
    displays the after payment page.

    ***Template***
    :template: products/after_payment.html
    """

    try:
        basket_items = Basket.objects.filter(user=request.user)
        basket_items.delete()

        return render(
            request,
            'products/after_payment.html',
        )
    except Exception as e:
        messages.error(request, f'Payment processing failed because of the following error:\n{str(e)}')
        return render(request, '500.html', status=500)


@login_required
def add_to_favorites(request, product_id):
    """
    Adds a product to the user's favorites.
    """

    try:
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
    except IntegrityError:
        messages.error(request, 'Database error. Please try again.')
        return redirect('products')
    except Exception as e:
        messages.error(request, f'The following unexpected error occurred:\n{str(e)}')
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

    try:
        favorites = Favorite.objects.filter(user=request.user)

        return render(
            request,
            'products/favorites.html',
            {'favorites': favorites, },
            )
    except Exception as e:
        messages.error(request, f'The following unexpected error occurred:\n{str(e)}')
        return render(request, '500.html', status=500)


@login_required
def remove_favorite(request, favorite_id):
    """
    Removes a product from the user's favorites.
    """

    try:
        favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
        favorite.delete()
        messages.add_message(request, messages.ERROR, 'Item removed from favorites!')

        return HttpResponseRedirect(reverse('favorites'))
    except Exception as e:
        messages.error(request, f'Failed to remove item because of the following error:\n{str(e)}')
        return redirect('favorites')
