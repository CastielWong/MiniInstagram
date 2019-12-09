from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from user.models import CustomUser, UserConnection
from user.serializers import UserSerializer, UserConnectionSerializer
from post.models import Post, Like, Comment
from post.serializers import PostSerializer, LikeSerializer, CommentSerializer

# ----------------------------------USER---------------------------------------
class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = CustomUser.objects.all().order_by('date_joined')
    serializer_class = UserSerializer

class UserConnectionViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    queryset = UserConnection.objects.all().order_by('created')
    serializer_class = UserConnectionSerializer

# -----------------------------------------------------------------------------

# ----------------------------------POST---------------------------------------
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('posted_on')
    serializer_class = PostSerializer

class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all().order_by('post')
    serializer_class = LikeSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('posted_on')
    serializer_class = CommentSerializer

# -----------------------------------------------------------------------------
