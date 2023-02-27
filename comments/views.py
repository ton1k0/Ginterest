from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import CommentSerializer
from rest_framework import generics
from .models import Comment


class CommentViewSet(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()