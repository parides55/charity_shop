from django.contrib import admin
from .models import OurStory, ContactUs
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(OurStory)
class OurStoryAdmin(SummernoteModelAdmin):
    """
    Customizes the admin panel for the 'Our Story' model.
    Lists the fields to be displayed.
    """
    summernote_fields = ('content',)
    list_display = ('title', 'updated_on')


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    """
    Customizes the admin panel for the 'Contact Us' model.
    Lists the fields to be displayed, filters, search fields.
    """
    list_display = ('name', 'email', 'read')
    list_filter = ('read',)
    search_fields = ('name', 'email')
