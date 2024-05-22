from django.shortcuts import render,get_object_or_404, reverse
from django.http import HttpResponse

# Create your views here.
def events(request):
    return render(request, 'events/events.html',)