# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payroll',
            old_name='padi_total',
            new_name='adjusted',
        ),
        migrations.AddField(
            model_name='payroll',
            name='aux',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payroll',
            name='avaya',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payroll',
            name='paid_total',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payroll',
            name='schedule_time',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payroll',
            name='softphone',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
