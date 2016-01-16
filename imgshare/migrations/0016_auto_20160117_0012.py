# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imgshare', '0015_remove_image_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedby',
            name='image',
        ),
        migrations.RemoveField(
            model_name='uploadedby',
            name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
        ),
        migrations.DeleteModel(
            name='UploadedBy',
        ),
    ]
