from django.http import JsonResponse
from django.shortcuts import render

from blog.models import Post, Comment
from blog.serializers import *


# Create your views herobjecte.
def list_post(request):
    post = Post.objects.all()
    return render(request, 'post_list.html')


def get_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html')


def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()


def update_post(request, id):
    post = Post.objects.get(id=id)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()


def get_comments(request, id):
    comments = Comment.objects.filter(post__id=id)
    return JsonResponse(comments, safe=False)


def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
