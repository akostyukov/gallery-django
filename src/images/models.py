from django.contrib.auth.models import User
from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    signature = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
