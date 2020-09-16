from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *


# Create your views here.

class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 3


# class PostDetail(DetailView):
#     model = Post
#     template_name = "post_detail.html"


def post_detail(request, pk):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, id=pk)

    comments = post.comments.filter(active=True)
    new_comment = None

    # if comment is posted

    if request.method == 'POST':
        comment_form = CommentForms(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForms()

    content = {"post": post, "comments": comments, "new_comment": new_comment, "comment_form": comment_form}
    return render(request, template_name, content)
