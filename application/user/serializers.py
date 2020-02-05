from rest_framework import serializers

from user.models import CustomUser, UserConnection

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk', 'user_alias','email', 'url']
        read_only_fields = ['user_alias','email', 'url']

class UserConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConnection
        fields = ['pk', 'follower', 'following']
        read_only_fields = ['follower', 'following']

