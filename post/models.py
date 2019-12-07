from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField

# the project directory is the root
from user import models as user


class Post(models.Model):
    author = models.ForeignKey(
        user.CustomUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts',
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
    user = models.ForeignKey(user.CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("post", "user")
    
    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(user.CustomUser, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment

