from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm

from user import form

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
