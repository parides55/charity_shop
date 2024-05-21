from . import views
from django.urls import path

urlpatterns = [
    path('', views.our_story, name='our_story')
]