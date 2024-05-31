from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.Products.as_view(), name='products'),
    path("<slug:slug>/view_product/", views.view_product, name="view-product"),
    path('basket/', views.basket, name='basket'),
    path('basket/remove_item/<int:basket_id>', views.remove_item, name='remove_item'),
    path('after_payment/', views.after_payment, name='after_payment'),
]