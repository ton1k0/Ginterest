from django.shortcuts import render
from rest_framework import generics

from .models import Gin
from .serializers import GinSerializer


class GinCreateView(generics.ListCreateAPIView):
    queryset = Gin.objects.all()
    serializer_class = GinSerializer