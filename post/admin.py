from django.contrib import admin

from post.models import Post

# register the model in admin page
admin.site.register(Post)
