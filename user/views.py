from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class UserProfile(LoginRequiredMixin, DetailView):
    model = models.CustomUser
    template_name = "user/profile.html"
    login_url = 'login'

