from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from annoying.decorators import ajax_request

from . import models


class PostIndex(ListView):
    model = models.Post
    template_name = "index.html"

class PostListView(ListView):
    model = models.Post
    template_name = "post/list.html"

# note that 'LoginRequiredMixin' should placed before other parent class
class PostDetailView(LoginRequiredMixin, DetailView):
    # jump to the url if not login
    login_url = "login"
    model = models.Post
    template_name = "post/detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = models.Post
    template_name = "post/create.html"
    fields = "__all__"

class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = "login"
    model = models.Post
    fields = ["title"]
    template_name = "post/update.html"

class PostDeleteView(DeleteView, LoginRequiredMixin):
    login_url = "login"
    model = models.Post
    template_name = "post/delete.html"
    success_url = reverse_lazy("post_list")

@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = models.Post.objects.get(pk=post_pk)
    try:
        like = models.Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = models.Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0
    
    return {
        'result': result,
        'post_pk': post_pk
    }

@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = models.Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = models.Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }
