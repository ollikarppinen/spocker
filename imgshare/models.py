import string
import random
from pyuploadcare.dj import ImageField
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Image(models.Model):
    slug = models.SlugField(max_length=10, primary_key=True, blank=True)
    image = ImageField(manual_crop="")
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('imgshare.views.image', args=[self.pk])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.sample(string.ascii_lowercase, 6))
        super(Image, self).save(*args, **kwargs)


class Comment(models.Model):
    # author = models.U
    image = models.ForeignKey('Image', on_delete=models.CASCADE,)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    # def save(self. *args, **kwargs):
