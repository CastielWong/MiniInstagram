from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class Profile(LoginRequiredMixin, DetailView):
    login_url = "login"
    model = models.CustomUser
    template_name = "user/profile.html"

class UpdateProfile(LoginRequiredMixin, UpdateView):
    login_url = "login"
    model = models.CustomUser
    fields = ['username', 'profile_pic']
    template_name = "user/update.html"
