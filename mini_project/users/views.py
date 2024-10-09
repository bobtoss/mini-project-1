from django.shortcuts import render
from .models import Profile, Follow
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})


@login_required(login_url='users/login/')
def profile(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)
    return render(request, 'profile.html', {'profile': profile})


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


def base(request):
    return render(request, 'base.html', )


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('/users/')  # Redirect to a page after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid credentials.")

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
