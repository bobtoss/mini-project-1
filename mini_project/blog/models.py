from django.db import models

from users.models import User


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_of_post')


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_to_post')
    author = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='author_of_comment')
