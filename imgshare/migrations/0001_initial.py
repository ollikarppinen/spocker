# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('slug', models.SlugField(blank=True, serialize=False, primary_key=True, max_length=10)),
                ('image', pyuploadcare.dj.models.ImageField()),
            ],
        ),
    ]
