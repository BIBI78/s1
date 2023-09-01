from . import views
from django.urls import path
from .views import create_post


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', create_post, name='create_post'),
    #path('create/', views.CreatePost.as_view(), name='create-post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    
]