from django.contrib.auth.models import User
from django.db import models

from images.models import ImageModel


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    image = models.ForeignKey(ImageModel, related_name='comments', on_delete=models.CASCADE)
