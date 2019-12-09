from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from annoying.decorators import ajax_request

from post.models import Post, Like, Comment


class PostIndex(ListView):
    model = Post
    template_name = "index.html"

class PostListView(ListView):
    model = Post
    template_name = "post/list.html"

# note that 'LoginRequiredMixin' should placed before other parent class
class PostDetailView(LoginRequiredMixin, DetailView):
    # jump to the url if not login
    login_url = "login"
    model = Post
    template_name = "post/detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "login"
    model = Post
    template_name = "post/create.html"
    # fields = "__all__"
    fields = ["title", "image"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView, LoginRequiredMixin):
    login_url = "login"
    model = Post
    fields = ["title"]
    template_name = "post/update.html"

class PostDeleteView(DeleteView, LoginRequiredMixin):
    login_url = "login"
    model = Post
    template_name = "post/delete.html"
    success_url = reverse_lazy("post_list")

@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
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
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        user_alias = request.user.user_alias

        commenter_info = {
            'username': user_alias,
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
