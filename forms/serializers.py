from .models import *
from rest_framework import serializers

class NidhiEirSerializer(serializers.ModelSerializer):
    class Meta:
        model = NidhiEIR
        fields = '__all__'