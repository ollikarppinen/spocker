# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', pyuploadcare.dj.models.ImageField()),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
