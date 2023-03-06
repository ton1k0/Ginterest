from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
            )
    class Meta:
        model = Profile
        fields = ('user', 'first_name', 'surname', 'about', 'website', 'username')


class ProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'surname', 'about', 'website')