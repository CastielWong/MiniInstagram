from rest_framework import serializers

from user.models import CustomUser, UserConnection

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_alias','email', 'url']

class UserConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserConnection
        fields =['follower', 'following']

