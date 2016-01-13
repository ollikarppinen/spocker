import string
import random
from pyuploadcare.dj import ImageField
from django.db import models
from django.core.urlresolvers import reverse


class Image(models.Model):
    slug = models.SlugField(max_length=10, primary_key=True, blank=True)
    image = ImageField(manual_crop="")

    def get_absolute_url(self):
        return reverse('imgshare.views.image', args=[self.pk])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.sample(string.ascii_lowercase, 6))
        super(Image, self).save(*args, **kwargs)


class Comment(models.Model):
    image = models.ForeignKey('Image', on_delete=models.CASCADE,)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
