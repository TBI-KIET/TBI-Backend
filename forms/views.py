from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

class NidhiEirAPIView(APIView):
    def post(self, request):
        serializer = NidhiEirSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NidhiPrayasAPIView(APIView):
    def post(self, request):
        serializer = NidhiPrayasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
