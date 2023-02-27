from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Comment
        fields = ('text', 'gin', 'author')