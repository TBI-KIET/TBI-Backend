from django.urls import path
from .views import NidhiEirAPIView

urlpatterns = [
    path('nidhieir/',NidhiEirAPIView.as_view(), name = 'nidhieir'),
]