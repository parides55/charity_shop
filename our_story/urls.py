from . import views
from django.urls import path

urlpatterns = [
    path('', views.OurStoryListView.as_view(), name='our_story'),
    path('contact-us/', views.contact_us, name='contact_us'),
]