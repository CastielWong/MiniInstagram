from django.contrib import admin

from post.models import Post, Like, Comment

# make models inline
class CommentInline(admin.StackedInline):
    model = Comment

class LikeInline(admin.StackedInline):
    model = Like

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        LikeInline,
    ]


# register the model in admin page
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
