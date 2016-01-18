# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_report', '0002_schedulereport_break_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulereport',
            old_name='dayly_hours',
            new_name='daily_hours',
        ),
        migrations.AddField(
            model_name='schedulereport',
            name='absence_time',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='schedulereport',
            name='addtional_time',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='schedulereport',
            name='green_time',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='schedulereport',
            name='lunch_time',
            field=models.FloatField(null=True),
        ),
    ]
