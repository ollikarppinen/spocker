# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0006_auto_20160110_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('slug', models.SlugField(max_length=10, primary_key=True, serialize=False, blank=True)),
                ('image', pyuploadcare.dj.models.ImageField()),
            ],
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
    ]
