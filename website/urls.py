from django.contrib import admin
from django.urls import path
from .views import EventsAPIView

urlpatterns = [
    path('events/',EventsAPIView.as_view(), name = 'events')
]