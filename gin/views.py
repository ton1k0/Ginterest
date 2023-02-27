from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Gin
from .serializers import GinSerializer


class GinCreateView(generics.ListCreateAPIView):
    queryset = Gin.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GinSerializer