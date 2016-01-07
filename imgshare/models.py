from django.db import models
from pyuploadcare.dj import ImageField
import string
import random
# Create your models here.


class Image(models.Model):
    slug = models.SlugField(max_length=10, primary_key=True, blank=True)
    image = ImageField(manual_crop="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = ''.join(random.sample(string.ascii_lowercase, 6))
        super(Image, self).save(*args, **kwargs)
