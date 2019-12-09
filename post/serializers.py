from rest_framework import serializers

from post.models import Post, Like, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['pk', 'author', 'title', 'posted_on', 'likes', 'comments']
        read_only_fields = ['author', 'title', 'posted_on', 'likes']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['pk', 'post', 'user']
        read_only_fields = ['post', 'user']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'post', 'user', 'comment', 'posted_on']
        read_only_fields = ['post', 'user', 'comment', 'posted_on']
