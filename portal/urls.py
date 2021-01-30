from . import views
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('post/<slug:slug>/', views.PostView, name='post_view'),
    path('resources/', views.ResourceView, name='resources'),
    path('tag/<slug:slug>/', views.TagView, name='tag_view'),
    path('posts/', views.PostListView, name='postlist'),
]