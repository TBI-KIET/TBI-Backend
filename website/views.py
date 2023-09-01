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

        data = {
            'upcoming_events': upcoming_serializer.data,
            'past_events': past_serializer.data
        }

        return Response(data, status = status.HTTP_200_OK)
    
    
class ContactAPIView(APIView):
    def post (self ,request ):
        data = request.data
        serializer = ContactSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)