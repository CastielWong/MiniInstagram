from django.urls import path

from user import views


urlpatterns = [
    path('<int:pk>/', views.Profile.as_view(), name='profile'),
    path('update/<int:pk>/', views.UpdateProfile.as_view(), name='update_profile'),
    path('togglefollow', views.toggleFollow, name='togglefollow'),
]
