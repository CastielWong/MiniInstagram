from django.views.generic import TemplateView, ListView, DetailView

from . import models

class PostIndex(ListView):
    model = models.Post
    template_name = 'index.html'

class PostListView(ListView):
    model = models.Post
    template_name = 'post/list.html'

class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post/detail.html'
