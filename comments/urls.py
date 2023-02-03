from django.urls import path, include

from .views import CommentViewSet



urlpatterns = [
    path("create/", CommentViewSet.as_view(), name='comment')
]