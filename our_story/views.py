from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from .models import OurStory, ContactUs
from .forms import ContactUsForm

# Create your views here.
def our_story(request):
    queryset = OurStory.objects.all()
    our_story = get_object_or_404(queryset)
    return render(
        request,
        'our_story/our-story.html',
        {"our_story": our_story},
        )

def contact_us(request):
    contact_us_form = ContactUsForm()
    return render(
        request,
        'our_story/contact-us.html',
        {"contact_us_form": contact_us_form},
        )