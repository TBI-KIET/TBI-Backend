from .models import *
from rest_framework import serializers

class NidhiEirSerializer(serializers.ModelSerializer):
    class Meta:
        model = NidhiEIR
        fields = '__all__'

class NidhiPrayasSerializer(serializers.ModelSerializer):
    class Meta:
        model = NidhiPrayas
        fields = '__all__'