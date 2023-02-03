from rest_framework.permissions import AllowAny
from .serializers import CommentSerializer
from rest_framework import generics
from .models import Comment


class CommentViewSet(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()