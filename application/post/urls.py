from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('new/', views.PostCreateView.as_view(), name='make_post'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('like', views.addLike, name='addLike'),
    path('comment', views.addComment, name='addComment'),
]

