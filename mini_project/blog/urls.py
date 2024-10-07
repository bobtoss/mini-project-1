from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('/list_post', list_post),
    path('/get_post/<int:id>', get_post),
    path('/create_post', update_post),
    path('/update_post/<int:id>', update_post),
    path('/delete_post/<int:id>', delete_post),
    path('/get_comments/<int:id>', get_comments),
    path('/create_comment', create_comment),

]