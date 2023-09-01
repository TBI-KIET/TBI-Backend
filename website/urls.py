from django.contrib import admin
from django.urls import path
from .views import EventsAPIView, ContactAPIView

urlpatterns = [
    path('events/',EventsAPIView.as_view(), name = 'events'),
    path('contact/', ContactAPIView.as_view(), name = 'contact')
]