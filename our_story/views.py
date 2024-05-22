from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponse
from .models import OurStory, ContactUs
from .forms import ContactUsForm

# Create your views here.
class OurStoryListView(generic.ListView):
    queryset = OurStory.objects.all()
    template_name = 'our_story/our-story.html'

def contact_us(request):
    contact_us_form = ContactUsForm()
    return render(
        request,
        'our_story/contact-us.html',
        {"contact_us_form": contact_us_form},
        )