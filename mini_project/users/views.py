from django.shortcuts import render
from .models import *
from .serializers import *


# Create your views here.

def get_user(request, id):
    post = User.objects.get(id=id)
    return render(request, 'profile.html')


def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()


def update_user(request, id):
    post = User.objects.get(id=id)
    serializer = UserSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()


def follow_user(request):
    serializer = FollowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()


def unfollow_user(request, user_id, follow_id):
    follow = Follow.object.filter(user__id=user_id, follower__id=follow_id)
    follow.delete()
