from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.
# [CBV : Class Based View] -----------------------------
class PostList(ListView):
    model = Post



# FBV : Function Based View ------------------------------
# def index(request):
#     post = Post.objects.all()
#     context = {
#         'post' : post,
#     }
#     return render(request, 'blog/index.html', context)
#
#  -------------------------------------------------------

