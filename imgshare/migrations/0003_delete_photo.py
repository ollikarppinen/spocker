# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgshare', '0002_auto_20160108_0127'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
