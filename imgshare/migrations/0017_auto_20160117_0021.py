# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0016_auto_20160117_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
    ]
