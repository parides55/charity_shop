from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def our_story(request):
    return HttpResponse("Our Story")