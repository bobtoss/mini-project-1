from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('/get_user/<int:id>', get_user),
    path('/create_user', create_user),
    path('/update_user', update_user),
    path('/follow_user', follow_user),
    path('/unfollow_user/<int:user_id>/<int:follow_id>', unfollow_user),

]