from django.shortcuts import render
from users.models import Profile, Follow
from django.shortcuts import render, redirect, get_object_or_404
from .serializers import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm, ProfileForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Save the user form and create the user
            user = user_form.save()

            login(request, user)
            messages.success(request, f"Account created for {user.username}!")
            return redirect('/users/')  # Redirect to some page after registration
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration.html', {'user_form': user_form})

def create_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile_form.save()  # Now save the profile
            return redirect('/users/')  # Redirect to some page after registration
    else:
        profile_form = ProfileForm()
    return render(request, 'create_profile.html', {'profile_form': profile_form})

@login_required(login_url='users/login/')
def profile(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    return render(request, 'profile.html', {'profile': profile})


def update_user(request, id):
    post = User.objects.get(id=id)
    serializer = UserSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()


def follow_user(request, user_id):
    following_id = request.GET.get('following_id', None)
    Follow.objects.create(follower__id=user_id, following__id=following_id)


def unfollow_user(request, user_id, follow_id):
    follow = Follow.object.filter(follower_id=user_id, following__id=follow_id)
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
