from . import views
from django.urls import path

urlpatterns = [
    path('', views.Events.as_view(), name='events'),
    path('<slug:slug>/', views.event_info, name='event_info'),
    path('<slug:slug>/write_review/', views.write_review, name='write_review'),
    path('<slug:slug>/edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('<slug:slug>/delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]