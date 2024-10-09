from django.shortcuts import render
from .models import Profile, Follow
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'templates/registration.html', {'form': form})


@login_required
def profile(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)
    return render(request, 'users/templates/profile.html', {'profile': profile})


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
