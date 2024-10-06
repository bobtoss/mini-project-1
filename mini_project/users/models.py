from django.db import models


# Create your models here.
def user_directory_path(instance):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}'.format(instance.user.id)


class User(models.Model):
    username = models.TextField(100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    picture = models.ImageField(upload_to=user_directory_path)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE(), primary_key=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(User, on_delete=models.CASCADE)
