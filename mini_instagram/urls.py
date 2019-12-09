"""mini_instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views
from post import views as views_post
from api import views as views_api


router = routers.DefaultRouter()
router.register(r'users', views_api.UserViewSet)
router.register(r'user_connections', views_api.UserConnectionViewSet)
router.register(r'posts', views_api.PostViewSet)
router.register(r'likes', views_api.LikeViewSet)
router.register(r'comments', views_api.CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # include urls from apps
    path('user/', include('user.urls')),
    path('posts/', include('post.urls')),
    # 'django.contrib.auth' provides the 'login' view to handle login operation
    # browse something like "localhost:8000/auth/demo" to see what path is provided
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', views.SignUp.as_view(), name='signup'),
    # set up RESTful API
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # set up general pages
    path('', views_post.PostListView.as_view(), name='index'),
    path('entry/', views.HelloDjango.as_view(), name='entry'),
    path('404/', views.View404.as_view(), name='page_not_found'),
]
