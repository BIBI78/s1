from . import views
from django.urls import path
from .views import create_post


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', create_post, name='create_post'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('update/<slug:slug>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete/<slug:slug>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('get_paginated_posts/<int:page_number>/', views.get_paginated_posts, name='get_paginated_posts'),
    





]