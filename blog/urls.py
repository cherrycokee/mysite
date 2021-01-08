from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index),
    path('', views.PostList.as_view()),
    # path('blog/<int:pk>/', views.post_detail),
    path('<int:pk>/', views.PostDetail.as_view()),
]
