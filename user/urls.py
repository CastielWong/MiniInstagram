from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.UserProfile.as_view(), name='profile'),
]
