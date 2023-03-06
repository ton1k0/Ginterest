from django.urls import path, include

from .views import ProfileCreate, ProfileView



urlpatterns = [
    path("create/", ProfileCreate.as_view(), name='profiles'),
    path("", ProfileView.as_view(), name='profiles')
]