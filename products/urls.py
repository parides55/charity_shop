from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('basket/', views.basket, name='basket'),
]