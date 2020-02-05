from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm

from user import form
from post.models import Post


class HelloDjango(TemplateView):
    template_name = 'index.html'

class AuthLogin(CreateView):
    form_class = UserCreationForm
    template = 'registration/login.html'
    success_url = reverse_lazy('posts')

class SignUp(CreateView):
    form_class = form.CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class ExploreView(LoginRequiredMixin, ListView):
    login_url = "login"

    model = Post
    template_name = "explore.html"

    def get_queryset(self):
        return Post.objects.all().order_by('-posted_on')[:20]

class View404(TemplateView):
    template_name = 'status/404.html'
