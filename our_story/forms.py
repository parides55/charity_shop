from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """
    A form for users to submit contact us messages.
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = ContactUs
        fields = ('name', 'email', 'message',)
