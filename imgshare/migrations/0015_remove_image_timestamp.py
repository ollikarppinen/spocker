# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0014_auto_20160116_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='timestamp',
        ),
    ]
