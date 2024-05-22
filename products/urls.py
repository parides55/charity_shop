from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.Products.as_view(), name='products'),
    path('basket/', views.basket, name='basket'),
]