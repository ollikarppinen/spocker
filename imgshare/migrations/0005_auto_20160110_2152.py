# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='photo',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='id',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(serialize=False, primary_key=True, blank=True, max_length=10),
        ),
    ]
