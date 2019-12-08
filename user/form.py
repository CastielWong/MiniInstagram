from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = models.CustomUser
        fields = ('username', 'user_alias', 'email', 'profile_pic')
