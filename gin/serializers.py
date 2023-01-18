from rest_framework import serializers

from .models import Gin


class GinSerializer(serializers.ModelSerializer):

    #author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())

    class Meta:
        model = Gin
        fields = ('gin_id', 'gin_description', 'gin_created_at')
