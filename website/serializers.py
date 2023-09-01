from .models import Events, ContactUs
from rest_framework import serializers

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'