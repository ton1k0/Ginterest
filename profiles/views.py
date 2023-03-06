from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer, ProfileViewSerializer


class ProfileCreate(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()


class ProfileView(generics.GenericAPIView):
    serializer_class = ProfileViewSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({
            'profile': ProfileViewSerializer(request.user.profile, context=self.get_serializer_context()).data,
        })