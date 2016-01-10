from django.db import models

from pyuploadcare.dj import ImageField


class Image(models.Model):
    title = models.CharField(max_length=255)
    photo = ImageField()
