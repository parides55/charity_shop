from django.contrib import admin
from .models import Event, Review
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    """
    Customizes the admin panel for the Event model.
    Lists the fields to be displayed, filters, search fields, 
    and prepopulated fields.
    """
    summernote_fields = ('content',)
    list_filter = ('status', 'created_on')
    list_display = ('title', 'author', 'created_on', 'status')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for the Review model.
    Lists the fields to be displayed, filters, search fields,
    """
    list_filter = ('approved', 'created_on')
    list_display = ('post', 'author', 'created_on', 'approved')
    search_fields = ('post', 'author')