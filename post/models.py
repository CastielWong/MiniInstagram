from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField

class CustomUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        options={'quality': 100},
        null=True,
        blank=True,
    )

    def get_following(self):
        followings = UserConnection.objects.filter(follower=self)
        return followings

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers
    
    def is_followed_by(self, uers):
        return self.get_followers().filter(follower=user).exits()
    
    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(
        CustomUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='instagram_posts',
    )
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
    )
    posted_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    # return to its detail page when it's created
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

    def get_like_count(self):
        return self.likes.count()
    
    def get_comment_count(self):
        return self.comments.count()
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")
    
    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment

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

