from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from annoying.decorators import ajax_request

from user.models import CustomUser, UserConnection


class Profile(LoginRequiredMixin, DetailView):
    login_url = "login"

    model = CustomUser
    template_name = "user/profile.html"

class UpdateProfile(LoginRequiredMixin, UpdateView):
    login_url = "login"
    
    model = CustomUser
    fields = ['user_alias', 'profile_pic']
    template_name = "user/update.html"
    success_url = reverse_lazy("post_list")

@ajax_request
def toggleFollow(request):
    current_user = CustomUser.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get('follow_user_pk')
    follow_user = CustomUser.objects.get(pk=follow_user_pk)

    try:
        if current_user != follow_user:
            if request.POST.get('type') == 'follow':
                connection = UserConnection(follower=current_user, following=follow_user)
                connection.save()
            elif request.POST.get('type') == 'unfollow':
                UserConnection.objects.filter(follower=current_user, following=follow_user).delete()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_user_pk': follow_user_pk
    }
