from rest_framework import serializers

from post.models import Post, Like, Comment

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'title', 'posted_on', 'likes']

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'user']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'comment', 'posted_on']
