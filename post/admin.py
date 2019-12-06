from django.contrib import admin

from post.models import Post, CustomUser, Like, Comment, UserConnection

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

class FollowingInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'follower'

class FollowerInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'following'

class UserAdmin(admin.ModelAdmin):
    inlines = [
        FollowingInline,
        FollowerInline,
    ]


# register the model in admin page
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(UserConnection)
