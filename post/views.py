from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

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

class PostCreateView(CreateView):
    model = models.Post
    template_name = 'post/create.html'
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = models.Post
    template_name = 'post/update.html'
    fields = ['title']
    