from django.urls import path, include

from .views import GinCreateView, GinSaveView



urlpatterns = [
    path("create/", GinCreateView.as_view(), name='gins'),
    path('<int:pk>/save/', GinSaveView.as_view(), name='post-save'),
]