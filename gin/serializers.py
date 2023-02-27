from rest_framework import serializers

from .models import Gin


class GinSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
            )
    class Meta:
        model = Gin
        fields = ('id', 'description', 'created_at', 'author')
