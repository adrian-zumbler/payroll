# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulereport',
            name='break_time',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
