from django.shortcuts import render, reverse
from django.http import HttpResponse

# Create your views here.
def our_story(request):
    return render(request, 'our_story/our-story.html',)

def contact_us(request):
    return render(request, 'our_story/contact-us.html',)