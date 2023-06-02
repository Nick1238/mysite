from django.http import Http404
from django.shortcuts import render, get_object_or_404

from blog.models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'post/list.html',
                  {'posts': posts})

def post_detail(request, ind):
    post = get_object_or_404(Post,
                             id=ind)

    return render(request,
                  'post/detail.html',
                  {'post': post})
