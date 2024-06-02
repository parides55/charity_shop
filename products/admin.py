from django.contrib import admin
from .models import Product, Basket, Favorite
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = ('title', 'price', 'status', 'created_on')
    list_filter = ('title', 'created_on')
    search_fields = ('title', 'condition')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'created_on')
    list_filter = ('product', 'user', 'created_on')
    search_fields = ('product', 'user')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'added_at')
    list_filter = ('product', 'user', 'added_at')
    search_fields = ('product', 'user')