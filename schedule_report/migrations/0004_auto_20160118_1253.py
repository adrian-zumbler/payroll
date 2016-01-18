# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_report', '0003_auto_20160117_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedulereport',
            name='gab_time',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='schedulereport',
            name='vacation_time',
            field=models.FloatField(null=True),
        ),
    ]
