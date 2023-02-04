from rest_framework import serializers

from .models import Gin


class GinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gin
        fields = ('id', 'description', 'created_at', 'author')
