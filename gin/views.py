from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from .models import Gin, GinSave
from rest_framework.response import Response
from .serializers import GinSerializer, GinSaveSerializer


class GinCreateView(generics.ListCreateAPIView):
    queryset = Gin.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = GinSerializer


class GinSaveView(generics.ListCreateAPIView):
    serializer_class = GinSaveSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return GinSave.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        gin_id = self.kwargs.get('pk')
        if not Gin.objects.filter(pk=gin_id).exists():
            raise ValidationError({'gin_id': 'Invalid Gin ID'})

        saved_gin = GinSave(user=request.user, gin_id=gin_id)
        saved_gin.save()

        serializer = self.serializer_class(saved_gin)
        return Response(serializer.data, status=201)