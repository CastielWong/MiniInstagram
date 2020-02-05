from django.contrib import admin

from user.models import CustomUser, UserConnection

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
admin.site.register(UserConnection)
