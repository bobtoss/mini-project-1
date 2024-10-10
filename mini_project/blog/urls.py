from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:post_id>/edit/', views.PostView.as_view(), name='post_edit'),
    path('post/<int:post_id>/delete/', views.PostView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comment/', views.comment.as_view()),
    path('post/<int:post_id>/comment/', views.comment.as_view()),
]