from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from blog.serializers import *


# Create your views herobjecte.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/templates/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/templates/post_detail.html', {'post': post})


def post_create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()


def post_edit(request, post_id):
    post = Post.objects.get(id=id)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()


def post_delete(request, post_id):
    post = Post.objects.get(id=id)
    post.delete()


def get_comments(request, post_id):
    comments = Comment.objects.filter(post__id=id)
    return JsonResponse(comments, safe=False)


def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
