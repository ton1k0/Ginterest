from django.urls import path, include

from .views import ProfileCreate



urlpatterns = [
    path("create/", ProfileCreate.as_view(), name='profiles')
]