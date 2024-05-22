from . import views
from django.urls import path

urlpatterns = [
    path('', views.Events.as_view(), name='events'),
    path('<slug:slug>/', views.event_info, name='event_info'),
]