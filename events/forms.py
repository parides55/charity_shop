from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """"
    A form for users to submit reviews.
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = Review
        fields = ('body',)