from django.contrib import admin

from post.models import Post, CustomUser

# register the model in admin page
admin.site.register(CustomUser)
admin.site.register(Post)
