from . import views
from django.urls import path

urlpatterns = [
    path('', views.our_story, name='our_story'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('privacy/', views.privacy, name='privacy')
]