# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0005_auto_20160110_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('photo', pyuploadcare.dj.models.ImageField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
