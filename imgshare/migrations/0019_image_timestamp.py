# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0018_uploadeder'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
