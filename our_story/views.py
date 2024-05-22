from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponse
from .models import OurStory, ContactUs

# Create your views here.
class OurStoryListView(generic.ListView):
    queryset = OurStory.objects.all()
    template_name = 'our_story/our-story.html'

def contact_us(request):
    return render(request, 'our_story/contact-us.html',)