from django.urls import path, include

from .views import GinCreateView



urlpatterns = [
    path("create/", GinCreateView.as_view(), name='gins')
]