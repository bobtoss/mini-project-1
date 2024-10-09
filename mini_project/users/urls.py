from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),

]