from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    signature = models.CharField(max_length=100, blank=True, null=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    comments = models.ManyToManyField(User, blank=True, related_name='comments', through='Comment')


class Comment(models.Model):
    text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
