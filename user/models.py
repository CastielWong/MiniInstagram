from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField


class CustomUser(AbstractUser):
    user_alias = models.CharField(max_length=30)
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    def get_followings(self):
        followings = UserConnection.objects.filter(follower=self)
        return followings

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers
    
    def is_followed_by(self, uers):
        return self.get_followers().filter(follower=user).exits()

class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    follower = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="is_follower_set"
    )
    following = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name="is_following_by_set"
    )

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
