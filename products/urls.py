from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.Products.as_view(), name='products'),
    path("<slug:slug>/view_product/", views.view_product, name="view-product"),
    path('basket/', views.basket, name='basket'),
]