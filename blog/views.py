from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.
# [CBV : Class Based View] -----------------------------
class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post




# FBV : Function Based View ------------------------------
# def post_detail(request,pk):
#     blog_post = Post.objects.get(pk=pk)
#     context = {
#         'blog_post' : blog_post,
#     }
#     return render(request,'blog/post_detail.html',context)

# def index(request):
#     post = Post.objects.all()
#     context = {
#         'post' : post,
#     }
#     return render(request, 'blog/index.html', context)
#
#  -------------------------------------------------------
