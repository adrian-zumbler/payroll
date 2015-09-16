# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0002_auto_20150915_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='end_date',
        ),
    ]
