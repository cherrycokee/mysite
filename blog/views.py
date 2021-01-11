from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView


# Create your views here.
# [CBV : Class Based View] -----------------------------
class PostList(ListView):
    model = Post

    # 작성일 기준으로 내림차순 정렬
    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        print('context 1) : **kwargs >> ', context)

        context['category_list'] = Category.objects.all()
        context['post_without_category'] = Post.objects.filter(category=None).count()
        print('context 2) >> ', context)

        return context


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
