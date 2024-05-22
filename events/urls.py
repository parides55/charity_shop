from . import views
from django.urls import path

urlpatterns = [
    path('', views.Events.as_view(), name='events')
]