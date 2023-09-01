from django.shortcuts import render
from .serializers import EventSerializer
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone


class EventsAPIView(APIView):

    def get_object(self, slug):
        try:
            return Events.objects.get(slug = slug)
        except Events.DoesNotExist:
            return None
        
        
    def get(self, request):
        upcoming_events = Events.objects.filter(eventDate__gte=timezone.now())
        past_events = Events.objects.filter(eventDate__lt=timezone.now())

        upcoming_serializer = EventSerializer(upcoming_events, many = True)
        past_serializer = EventSerializer(past_events, many = True)


        print("Upcoming Events Data:")
        print(upcoming_serializer.data)
        print("Past Events Data:")
        print(past_serializer.data)


        data = {
            'upcoming_events': upcoming_serializer.data,
            'past_events': past_serializer.data
        }

        return Response(data, status = status.HTTP_200_OK)
    
    
    

