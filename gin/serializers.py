from rest_framework import serializers

from .models import Gin, GinSave


class GinSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
            )
    class Meta:
        model = Gin
        fields = ('id', 'description', 'created_at', 'author')


class GinSaveSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
            )
    class Meta:
        model = GinSave
        fields = '__all__'
