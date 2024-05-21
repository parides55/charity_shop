from django.shortcuts import render, reverse
from django.http import HttpResponse

# Create your views here.
def events(request):
    return render(request, 'events/events.html',)