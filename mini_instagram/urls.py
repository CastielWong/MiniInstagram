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

from . import views
import post

urlpatterns = [
    path('admin/', admin.site.urls),
    # 'django.contrib.auth' provides the 'login' view to handle login operation
    # browse something like "localhost:8000/auth/demo" to see what path is provided
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', views.SignUp.as_view(), name='signup'),
    path('posts/', include('post.urls')),
    path('entry/', views.HelloDjango.as_view(), name='entry'),
    path('', post.views.PostListView.as_view(), name='index'),
]
