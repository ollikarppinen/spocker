# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imgshare', '0013_image_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedBy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'UploadedBy',
                'verbose_name_plural': 'UploadedBys',
            },
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AddField(
            model_name='uploadedby',
            name='image',
            field=models.ForeignKey(to='imgshare.Image'),
        ),
        migrations.AddField(
            model_name='uploadedby',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
