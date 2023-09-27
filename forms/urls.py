from django.urls import path
from .views import NidhiEirAPIView, NidhiPrayasAPIView

urlpatterns = [
    path('nidhieir/',NidhiEirAPIView.as_view(), name = 'nidhieir'),
    path('nidhiprayas/',NidhiPrayasAPIView.as_view(), name = 'nidhiprayas'),
]