from django.shortcuts import render,get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponse
from .models import Event, Review

# Create your views here.
class Events(generic.ListView):
    queryset = Event.objects.all()
    template_name = "events/events.html"