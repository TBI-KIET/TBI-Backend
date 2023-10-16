from django.contrib import admin
from django.urls import path
from .views import EventsAPIView, ContactAPIView, PastEventDetailView

urlpatterns = [
    path('events/',EventsAPIView.as_view(), name = 'events'),
    path('past-events/<slug:slug>/', PastEventDetailView.as_view(), name='past-event-detail'),
    path('contact/', ContactAPIView.as_view(), name = 'contact')
]