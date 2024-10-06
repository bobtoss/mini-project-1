from django.db import models

from mini_project.users.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(100)
    content = models.TextField()
    created_at = models.DateTimeField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Post, on_delete=models.CASCADE)
